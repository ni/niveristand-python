"""Update niveristand imports to the new package layout.

The following modules moved from ``niveristand`` to ``niveristand.realtimesequenceapi``:
clientapi, library, errors, realtimesequencetools, _decorators, _errormessages, _translation

For every Python file under the supplied path, this script updates these forms:

    # A module import.
    import niveristand.clientapi
    import niveristand.realtimesequenceapi.clientapi

    # A module import with an alias.
    import niveristand.library.primitives as primitives
    import niveristand.realtimesequenceapi.library.primitives as primitives

    # Multiple module imports.
    import niveristand.clientapi, niveristand.errors
    import niveristand.realtimesequenceapi.clientapi, niveristand.realtimesequenceapi.errors

    # Private import.
    import niveristand.clientapi._datatypes.rtprimitives as rt
    import niveristand.realtimesequenceapi.clientapi._datatypes.rtprimitives as rt

    # A from import, including aliases and star imports.
    from niveristand.clientapi import DoubleValue as Value
    from niveristand.realtimesequenceapi.clientapi import DoubleValue as Value

    from niveristand.clientapi import *
    from niveristand.realtimesequenceapi.clientapi import *

    # Parenthesized, multi-line from imports keep their existing layout.
    from niveristand.clientapi import (
        BooleanValue,
        DoubleValue,
    )
    from niveristand.realtimesequenceapi.clientapi import (
        BooleanValue,
        DoubleValue,
    )

    # Moved members imported directly from the niveristand package.
    from niveristand import clientapi, library
    from niveristand.realtimesequenceapi import clientapi, library

If a direct niveristand import mixes moved and unmoved names, it is split:

    from niveristand import nivs_rt_sequence, errors

becomes:

    from niveristand import nivs_rt_sequence
    from niveristand.realtimesequenceapi import errors

The script does not modify strings, comments or cases like:

    import niveristand
    value = niveristand.clientapi.DoubleValue()

Usage:
    python migrate_niveristand_imports.py <one or more file or directory paths, separated by spaces>
"""

import ast
import os
import re
import sys
import tokenize
from pathlib import Path

# Members that moved from ``niveristand.<name>`` to
# ``niveristand.realtimesequenceapi.<name>``.
MOVED_MEMBERS = frozenset(
    {
        "clientapi",
        "library",
        "errors",
        "realtimesequencetools",
        "_decorators",
        "_errormessages",
        "_translation",
    }
)

_ROOT = "niveristand"
_NEW_ROOT = "niveristand.realtimesequenceapi"


def _rewrite_module(module):
    if not module:
        return None
    parts = module.split(".")
    if len(parts) >= 2 and parts[0] == _ROOT and parts[1] in MOVED_MEMBERS:
        return _NEW_ROOT + "." + ".".join(parts[1:])
    return None


def _render_from(module, aliases):
    names = ", ".join(a.name + (f" as {a.asname}" if a.asname else "") for a in aliases)
    return f"from {module} import {names}"


def _new_text_for_node(node, orig, indent):
    if isinstance(node, ast.ImportFrom):
        if node.level:  # relative import; not customer-facing
            return None
        module = node.module or ""
        new_module = _rewrite_module(module)
        if new_module is not None:
            # Swap only the module token; keep the rest of the statement verbatim.
            return re.sub(
                r"(^from\s+)" + re.escape(module) + r"\b",
                lambda m: m.group(1) + new_module,
                orig,
                count=1,
            )
        # Bare ``from niveristand import <names>`` where some names moved.
        if module == _ROOT:
            moved = [a for a in node.names if a.name in MOVED_MEMBERS]
            if not moved:
                return None
            stay = [a for a in node.names if a.name not in MOVED_MEMBERS]
            lines = []
            if stay:
                lines.append(_render_from(_ROOT, stay))
            lines.append(_render_from(_NEW_ROOT, moved))
            return ("\n" + indent).join(lines)
        return None

    if isinstance(node, ast.Import):
        new_text = orig
        changed = False
        for a in node.names:
            new_name = _rewrite_module(a.name)
            if new_name is not None:
                changed = True
                new_text = re.sub(re.escape(a.name) + r"(?![\w.])", new_name, new_text, count=1)
        return new_text if changed else None

    return None


def _update_imports(source):
    tree = ast.parse(source)
    # AST columns are UTF-8 byte offsets, so locate statements in the encoded bytes.
    data = source.encode("utf-8")
    line_starts = [0] + [i + 1 for i, byte in enumerate(data) if byte == 0x0A]

    edits = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Import, ast.ImportFrom)):
            continue
        start = line_starts[node.lineno - 1] + node.col_offset
        end = line_starts[node.end_lineno - 1] + node.end_col_offset
        orig = data[start:end].decode("utf-8")
        new_text = _new_text_for_node(node, orig, " " * node.col_offset)
        if new_text is None or new_text == orig:
            continue
        edits.append((start, end, new_text.encode("utf-8")))

    # Apply from the bottom up so earlier offsets stay valid.
    edits.sort(key=lambda e: e[0], reverse=True)
    for start, end, text in edits:
        data = data[:start] + text + data[end:]
    return data.decode("utf-8"), len(edits)


def _read_source(path):
    with path.open("rb") as file:
        encoding, _ = tokenize.detect_encoding(file.readline)
        file.seek(0)
        return file.read().decode(encoding), encoding


def _process_file(path):
    original, encoding = _read_source(path)
    updated, count = _update_imports(original)
    if count and updated != original:
        path.write_bytes(updated.encode(encoding))
        print(f"UPDATED  {path}  ({count} import statement(s))")
        return count
    return 0


def _collect_files(roots, errors):
    files = []
    for root in roots:
        try:
            if root.is_file():
                files.append(root)
                continue
        except Exception as exc:
            errors.append(f"Error collecting files from {root}: {exc}")
            continue

        def record_error(exc):
            errors.append(f"Error collecting files from {exc.filename or root}: {exc}")

        for directory, directory_names, file_names in os.walk(
            root, topdown=True, onerror=record_error, followlinks=False
        ):
            traversable_directories = []
            for name in directory_names:
                path = Path(directory) / name
                try:
                    if name != "__pycache__" and not path.is_symlink():
                        traversable_directories.append(name)
                except Exception as exc:
                    errors.append(f"Error collecting directory {path}: {exc}")
            directory_names[:] = traversable_directories
            for name in sorted(file_names):
                if not name.endswith(".py"):
                    continue
                path = Path(directory) / name
                try:
                    if path.is_file() and not path.is_symlink():
                        files.append(path)
                except Exception as exc:
                    errors.append(f"Error collecting file {path}: {exc}")
    return files


def main():
    """Main entry of the script."""
    if len(sys.argv) < 2:
        print(
            r"python migrate_niveristand_imports.py <one or more file or directory paths, separated by spaces>"
        )
        return 1

    errors = []
    roots = set()
    for arg in sys.argv[1:]:
        root = Path(arg)
        try:
            if not root.exists():
                errors.append(f"Path does not exist: {root}")
            elif root.is_symlink():
                errors.append(f"Symbolic links are not supported: {root}")
            elif root.is_file() and root.suffix != ".py":
                errors.append(f"Not a Python file: {root}")
            else:
                roots.add(root)
        except Exception as exc:
            errors.append(f"Error inspecting {root}: {exc}")

    files = _collect_files(roots, errors)

    total = 0
    for path in files:
        try:
            total += _process_file(path)
        except Exception as exc:
            errors.append(f"Error updating imports for {path}: {exc}")
    print(f"\nUpdated {total} import statement(s) across {len(files)} file(s).")
    if errors:
        print(f"Encountered {len(errors)} error(s):")
        for error in errors:
            print(error)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
