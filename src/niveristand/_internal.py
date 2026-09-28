import os
import sys
import tempfile

# VeriStand 2027 and newer ship .NET (Core) assemblies; older versions ship
# .NET Framework assemblies. This drives which runtime pythonnet loads on Windows.
# Linux only ships .NET (Core), so it always loads coreclr.
_CORE_MIN_VERSION = 2027

# Linux VeriStand installs live directly under this root, one folder per year named
# ``<prefix><year>``, e.g. ``/usr/local/niveristand2027``.
_LINUX_INSTALL_ROOT = "/usr/local"
_LINUX_INSTALL_PREFIX = "niveristand"


def base_assembly_path():
    """Directory that contains the VeriStand assemblies.

    Public: also used by ``niveristand.legacy.NIVeriStand`` to locate the install.
    """
    path, _ = _resolve_binaries()
    return path


def _resolve_binaries():
    """Return ``(assembly_dir, use_coreclr)``.

    The VeriStand version comes from the ``NIVERISTAND_VERSION`` env var (a year such
    as ``2027``); when it is unset the newest installed version is used. The assembly
    directory is that version's install location. On Windows, versions 2027 or newer
    load .NET (Core) and older versions load .NET Framework; Linux always loads
    .NET (Core).
    """
    year = _requested_version()
    if year:
        install_dir = _install_path_for_version(year)
    else:
        install_dir, year = _latest_install()

    use_coreclr = sys.platform != "win32" or year >= _CORE_MIN_VERSION
    return install_dir, use_coreclr


def _requested_version():
    """The VeriStand year from ``NIVERISTAND_VERSION``, or ``0`` when unset."""
    value = os.environ.get("NIVERISTAND_VERSION", "").strip()
    if not value:
        return 0
    try:
        return int(value)
    except ValueError:
        raise ValueError(
            "Invalid NIVERISTAND_VERSION %r; expected a VeriStand year such as 2027." % value
        )


def _install_path_for_version(year):
    """Install directory for a specific VeriStand ``year``; raises if not installed."""
    if sys.platform == "win32":
        install_dir = _windows_install_path(year)
    else:
        install_dir = os.path.join(_LINUX_INSTALL_ROOT, "%s%d" % (_LINUX_INSTALL_PREFIX, year))

    if not install_dir or not os.path.isdir(install_dir):
        raise IOError(
            "VeriStand %d is not installed (expected assemblies at %r)." % (year, install_dir)
        )
    return install_dir


def _latest_install():
    """Return ``(install_dir, year)`` of the newest installed VeriStand, else ('', 0)."""
    if sys.platform == "win32":
        return _latest_windows_install()
    return _latest_linux_install()


def _windows_install_path(year):
    """Registry ``InstallDir`` for a specific VeriStand ``year``, or '' when absent."""
    import winreg

    try:
        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SOFTWARE\\Wow6432Node\\National Instruments\\VeriStand\\%d" % year,
        ) as key:
            return winreg.QueryValueEx(key, "InstallDir")[0]
    except OSError:
        return ""


def _latest_windows_install():
    """Return ``(install_dir, year)`` of the newest registered VeriStand, else ('', 0)."""
    import winreg

    latest_dir = ""
    latest_year = 0
    try:
        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Wow6432Node\\National Instruments\\VeriStand\\"
        ) as vskey:
            count = winreg.QueryInfoKey(vskey)[0]
            for k in range(count):
                subkey = winreg.EnumKey(vskey, k)  # e.g. "2026"
                try:
                    year = int(subkey)
                except ValueError:
                    continue
                if year > latest_year:
                    try:
                        with winreg.OpenKey(vskey, subkey) as this_key:
                            install_dir = winreg.QueryValueEx(this_key, "InstallDir")[0]
                    except OSError:
                        # Skip a corrupt/incomplete subkey rather than aborting the whole scan.
                        continue
                    latest_dir = install_dir
                    latest_year = year
    except OSError:
        return "", 0
    return latest_dir, latest_year


def _latest_linux_install():
    """Return ``(install_dir, year)`` of the newest ``<prefix><year>`` install, else ('', 0)."""
    latest_dir = ""
    latest_year = 0
    try:
        entries = os.listdir(_LINUX_INSTALL_ROOT)
    except OSError:
        return "", 0
    for name in entries:
        if not name.startswith(_LINUX_INSTALL_PREFIX):
            continue
        try:
            year = int(name[len(_LINUX_INSTALL_PREFIX) :])
        except ValueError:
            continue
        install_dir = os.path.join(_LINUX_INSTALL_ROOT, name)
        if year > latest_year and os.path.isdir(install_dir):
            latest_dir = install_dir
            latest_year = year
    return latest_dir, latest_year


# Resolve the assembly directory and select the runtime BEFORE importing clr,
# because pythonnet can only load one runtime per process.
_asm_search_path, _run_coreclr = _resolve_binaries()

if _run_coreclr:
    from pythonnet import load

    load("coreclr")

import clr  # noqa: E402


_CORE_ASSEMBLIES = [
    "NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi",
    "NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities",
    "NationalInstruments.VeriStand.DataTypes",
    "NationalInstruments.VeriStand.ClientAPI",
    "NationalInstruments.VeriStand",
    "NationalInstruments.VeriStand.Internal",
    "NationalInstruments.VeriStand.SystemDefinitionAPI",
    "NationalInstruments.VeriStand.SystemStorage",
    "NationalInstruments.VeriStand.XMLReader",
    "NationalInstruments.VeriStand.APIInterface",
    "NationalInstruments.VeriStand.WorkspaceMacro",
]

if sys.platform == "win32":
    clr.AddReference("System")
    clr.AddReference("System.IO")
    from System.IO import (  # noqa: E402, I202 .net imports can't be at top of file.
        FileNotFoundException,
    )

    _load_exception = FileNotFoundException


# Register an assembly resolver so dependencies load from our assembly directory.
# Required on .NET Core (no GAC, and clr.AddReference("Name") does not probe
# sys.path) and harmless on .NET Framework.
if _asm_search_path:
    import System  # noqa: E402
    import System.Reflection  # noqa: E402

    def _resolve_assembly(sender, args):
        name = args.Name.split(",")[0]
        dll_path = os.path.join(_asm_search_path, name + ".dll")
        if os.path.isfile(dll_path):
            return System.Reflection.Assembly.LoadFrom(dll_path)
        return None

    _resolve_assembly_handler = System.ResolveEventHandler(_resolve_assembly)
    System.AppDomain.CurrentDomain.add_AssemblyResolve(_resolve_assembly_handler)


def _load_assemblies():
    if _asm_search_path:
        # Load by full path; works on both .NET Core and .NET Framework, and the
        # AssemblyResolve handler above pulls dependencies from the same folder.
        for asm in _CORE_ASSEMBLIES:
            dll_path = os.path.join(_asm_search_path, asm + ".dll")
            if not os.path.isfile(dll_path):
                raise IOError("Assembly not found: %s" % dll_path)
            clr.AddReference(os.path.abspath(dll_path))
    elif sys.platform == "win32":
        # No path resolved (e.g. no install found): last-resort GAC lookup by name.
        try:
            for asm in _CORE_ASSEMBLIES:
                clr.AddReference(asm)
        except _load_exception as e:
            raise IOError(
                "No VeriStand installation found. Install VeriStand or set the "
                "'NIVERISTAND_VERSION' env var to an installed year such as 2027. "
                "(%s)" % e
            )
    else:
        raise IOError(
            "No VeriStand installation found under %r (expected a %r<year> folder). "
            "Install VeriStand or set the 'NIVERISTAND_VERSION' env var to an installed "
            "year such as 2027." % (_LINUX_INSTALL_ROOT, _LINUX_INSTALL_PREFIX)
        )


_load_assemblies()


def dummy():
    """Do nothing because you're just a dummy.

    This dummy can be used by any module that imports internal to get rid of PEP8 errors about
    an import not being used. This internal module takes care of loading C# references, so most
    times it will only be imported but not actually used.
    """
    pass


# set the temporary folder to C:\Users\$USER\AppData\Local\Temp\python_rt_sequences
tempfile.tempdir = os.path.join(tempfile.gettempdir(), "python_rt_sequences")
if not os.path.exists(tempfile.tempdir):
    os.makedirs(tempfile.tempdir)
