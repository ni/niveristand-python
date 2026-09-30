"""Shared utilities for auto-generated NI VeriStand Python wrappers."""

from __future__ import annotations

import datetime
import re
import sys
import uuid
from typing import (
    Any,
    Dict,
    Iterable,
    Optional,
    Tuple,
    Union,
    get_origin,
)

import System  # type: ignore

__all__ = [
    "_staticproperty",
    "_DotNetBase",
    "_DotNetEnum",
    "_DOTNET_EXCEPTION_MAP",
    "_wrap_exception",
    "_is_iterable",
    "_type_matches",
    "_select_matching_overload",
    "_unwrap_single_arg",
    "_unwrap",
    "_convert_tdms_property_value",
    "_wrap_sentinel_value",
    "_wrap",
    "_init_dotnet_wrapper",
    "_DOTNET_FULLNAME_REGISTRY",
    "_register_dotnet_type",
    "_raise_veristand_error",
    "_raise_veristand_sdf_error",
    "_dotnet_type_for",
    "_subscribe_event_handler",
    "_pop_event_handler_from_cache",
]


_VERISTAND_NAMESPACE = "NationalInstruments.VeriStand."
_DOTNET_FULLNAME_REGISTRY: Dict[str, type] = {}
_DOTNET_CTOR_TYPE_REGISTRY: Dict[type, type] = {}
_DOTNET_CONSTRUCTABLE_REGISTRY: Dict[type, bool] = {}
_VERISTAND_EXCEPTION_ERROR_CODES: Dict[str, str] = {}


def _dotnet_type_for(wrapper_cls: Any) -> Any:
    """Resolve a Python wrapper class to its underlying .NET constructor type.

    Used by generated generic method wrappers so that a caller can pass the
    Python class (e.g. ``Target``) as the type argument and the correct C#
    type is substituted.
    """
    return _DOTNET_CTOR_TYPE_REGISTRY.get(wrapper_cls, wrapper_cls)


def _register_dotnet_type(
    dotnet_ctor_type: Optional[type] = None,
    constructable: bool = True,
    error_code: Optional[str] = None,
):
    """Register generated wrapper metadata used by _wrap and _init_dotnet_wrapper."""

    def _decorate(wrapper_cls):
        if dotnet_ctor_type is not None:
            _DOTNET_CTOR_TYPE_REGISTRY[wrapper_cls] = dotnet_ctor_type
            full_name = f"{dotnet_ctor_type.__module__}.{wrapper_cls.__name__}"
            _DOTNET_FULLNAME_REGISTRY[full_name] = wrapper_cls
            if error_code is not None:
                _VERISTAND_EXCEPTION_ERROR_CODES[error_code] = full_name
        _DOTNET_CONSTRUCTABLE_REGISTRY[wrapper_cls] = constructable
        return wrapper_cls

    return _decorate


def _init_dotnet_wrapper(self, *args, unwrap_spec=None) -> None:
    """Initialize a .NET wrapper instance."""
    wrapper_type = type(self)
    dotnet_type = _DOTNET_CTOR_TYPE_REGISTRY.get(wrapper_type)
    if dotnet_type is None:
        raise RuntimeError(
            f"No .NET constructor type registered for "
            f"{wrapper_type.__module__}.{wrapper_type.__qualname__}"
        )
    if len(args) == 1 and type(args[0]) is dotnet_type:
        self._dotnet_instance = args[0]
        return
    constructable = _DOTNET_CONSTRUCTABLE_REGISTRY.get(wrapper_type, True)
    if not constructable:
        raise ValueError(f"No instance constructor for {wrapper_type.__name__}")
    unwrapped = _unwrap(unwrap_spec, *args)
    try:
        self._dotnet_instance = dotnet_type(*unwrapped)
    except System.Exception as e:
        _wrap_exception(e)


class _staticproperty(staticmethod):  # noqa: N801
    """Descriptor that makes a static method accessible as a property (without parentheses)."""

    def __get__(self, *_):
        """Return the result of calling the wrapped static function."""
        return self.__func__()


class _DotNetBase:
    """Base class for all auto-generated .NET wrapper types."""

    def __eq__(self, other) -> bool:
        """Check equality by comparing the underlying .NET instances."""
        return (
            self._dotnet_instance == other._dotnet_instance
            if isinstance(other, _DotNetBase)
            else False
        )

    def __hash__(self) -> int:
        """Return a hash consistent with __eq__, derived from the underlying .NET instance."""
        return hash(self._dotnet_instance)

    def __repr__(self) -> str:
        """Return a developer-friendly string representation of this wrapper."""
        qualname = type(self).__qualname__
        _mod = type(self).__module__.rsplit("._auto_generated_classes", 1)[0]
        return f"<{_mod}.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    """Base class for auto-generated .NET enum wrapper types."""

    def __repr__(self) -> str:
        """Return a developer-friendly string representation of this enum value."""
        _mod = type(self).__module__.rsplit("._auto_generated_classes", 1)[0]
        return f"<{_mod}.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

    def __str__(self) -> str:
        """Return the qualified name of this enum value."""
        return f"{type(self).__qualname__}.{self._py_field_name}"

    def __int__(self) -> int:
        """Return the integer value of this enum."""
        return int(self._dotnet_instance)


_DOTNET_EXCEPTION_MAP = {
    # Argument / value errors
    "System.ArgumentNullException": ValueError,
    "System.ArgumentException": ValueError,
    "System.ArgumentOutOfRangeException": ValueError,
    "System.FormatException": ValueError,
    # Type / cast errors
    "System.InvalidCastException": TypeError,
    # Runtime / state errors
    "System.InvalidOperationException": RuntimeError,
    "System.ObjectDisposedException": RuntimeError,
    # Arithmetic errors
    "System.DivideByZeroException": ZeroDivisionError,
    "System.OverflowException": OverflowError,
    # Collection errors
    "System.Collections.Generic.KeyNotFoundException": KeyError,
    "System.IndexOutOfRangeException": IndexError,
    # Not implemented
    "System.NotImplementedException": NotImplementedError,
    "System.NotSupportedException": NotImplementedError,
    # IO / file system errors
    "System.IO.FileNotFoundException": FileNotFoundError,
    "System.IO.DirectoryNotFoundException": FileNotFoundError,
    "System.IO.IOException": OSError,
    # Permission / access errors
    "System.UnauthorizedAccessException": PermissionError,
    # Timeout errors
    "System.TimeoutException": TimeoutError,
}


def _wrap_exception(e: "System.Exception") -> Exception:
    """Translate a .NET exception into an equivalent Python exception and raise it.

    A .NET exception that has a generated wrapper (for example
    ``NationalInstruments.VeriStand.SequenceNotFoundException``) is re-raised as that
    wrapper so callers can catch the specific type; otherwise it is mapped to a built-in
    Python exception via ``_DOTNET_EXCEPTION_MAP`` (default ``Exception``).
    """
    _exc_key = f"{type(e).__module__}.{type(e).__name__}"
    pytype = _DOTNET_FULLNAME_REGISTRY.get(_exc_key)
    if isinstance(pytype, type) and issubclass(pytype, BaseException):
        raise pytype(e) from None
    _exc_class = _DOTNET_EXCEPTION_MAP.get(_exc_key, Exception)
    raise _exc_class(e.ToString()) from None


def _raise_veristand_error(error: Any) -> None:
    """Raises VeriStandException for non sdf apis."""
    error_code = str(error.ErrorCode)
    exception_name = _VERISTAND_EXCEPTION_ERROR_CODES.get(
        error_code, _VERISTAND_NAMESPACE + "UnexpectedErrorException"
    )
    exception_type = _DOTNET_FULLNAME_REGISTRY[exception_name]
    base_exception_type = _DOTNET_FULLNAME_REGISTRY[_VERISTAND_NAMESPACE + "VeriStandException"]

    base_exception = base_exception_type(error)
    exception = exception_type.__new__(exception_type)
    # initializes the built-in Python Exception state. In particular,
    # it sets exception.args, so normal exception display and logging have a message.
    Exception.__init__(exception, str(base_exception))
    exception._dotnet_instance = base_exception._dotnet_instance
    raise exception from None


def _raise_veristand_sdf_error(error: Any) -> None:
    """Raises VeriStandSdfError for sdf apis."""
    raise _DOTNET_FULLNAME_REGISTRY[_VERISTAND_NAMESPACE + "VeriStandSdfError"](error) from None


def _is_sdf_api_module(module_name: str) -> bool:
    """Return whether *module_name* identifies a System Definition API wrapper module."""
    return module_name.startswith("niveristand.systemdefinitionapi")


def _is_iterable(arg: Any) -> bool:
    """Return True if arg is iterable but not a string."""
    return not isinstance(arg, str) and isinstance(arg, Iterable)


def _type_matches(arg: Any, sig_type: Any) -> bool:
    """Return True if ``arg`` satisfies ``sig_type``.

    ``isinstance`` rejects subscripted generics such as ``Iterable[BaseNode]`` or
    ``Callable[[IChannel], bool]`` with "Subscripted generics cannot be used with
    class and instance checks". ``typing.get_origin`` strips the type parameters and
    returns the runtime-checkable origin (``Iterable``, ``Callable``, ``list`` ...),
    which is enough to select the intended .NET overload. Plain classes have no
    origin, so they are checked directly.
    """
    check_type = get_origin(sig_type) or sig_type
    try:
        return isinstance(arg, check_type)
    except TypeError:
        return False


def _select_matching_overload(
    spec: Dict[Optional[Tuple[type, ...]], Tuple[Tuple[int, ...], Tuple[Any, ...]]],
    args: Tuple[Any, ...],
) -> Optional[Tuple[Tuple[int, ...], Tuple[Any, ...]]]:
    """Select the (out_positions, dotnet_types) entry whose Python signature matches args.

    Keys are Python input-type signatures used to pick the intended .NET overload;
    a ``None`` key is the fallback used when the overload is already unambiguous.
    """
    for signature, value in spec.items():
        if signature is None:
            continue

        if len(args) != len(signature):
            continue

        all_types_match = True
        for arg, sig_type in zip(args, signature):
            if not _type_matches(arg, sig_type):
                all_types_match = False
                break

        if all_types_match:
            return value

    if None in spec:
        return spec[None]

    return None


def _to_dotnet_datetime(arg: datetime.datetime) -> Any:
    """Convert a Python datetime.datetime to System.DateTime."""
    kind = (
        System.DateTimeKind.Utc
        if arg.utcoffset() == datetime.timedelta(0)
        else System.DateTimeKind.Local
    )

    return System.DateTime(
        arg.year,
        arg.month,
        arg.day,
        arg.hour,
        arg.minute,
        arg.second,
        kind,
    ).AddTicks(arg.microsecond * 10)


def _from_dotnet_datetime(arg: Any) -> datetime.datetime:
    """Convert a System.DateTime to Python datetime.datetime."""
    result = datetime.datetime(
        arg.Year,
        arg.Month,
        arg.Day,
        arg.Hour,
        arg.Minute,
        arg.Second,
        (arg.Ticks % System.TimeSpan.TicksPerSecond) // 10,
    )

    if arg.Kind == System.DateTimeKind.Utc:
        return result.replace(tzinfo=datetime.timezone.utc)

    return result


def _to_dotnet_guid(arg: uuid.UUID) -> Any:
    """Convert a Python uuid.UUID to System.Guid."""
    return System.Guid(str(arg))


def _to_dotnet_version(value: Any) -> Any:
    """Convert a four-element (major, minor, build, revision) sequence to System.Version."""
    major, minor, build, revision = value
    return System.Version(major, minor, build, revision)


_TDMS_PROPERTY_CLR_TYPES = {
    "Boolean": System.Boolean,
    "DateTime": System.DateTime,
    "Double": System.Double,
    "Float": System.Single,
    "Int8": System.SByte,
    "Int16": System.Int16,
    "Int32": System.Int32,
    "Int64": System.Int64,
    "String": System.String,
    "UInt8": System.Byte,
    "UInt16": System.UInt16,
    "UInt32": System.UInt32,
    "UInt64": System.UInt64,
}


def _convert_tdms_property_value(data_type: Any, value: Any) -> Any:
    """Convert a Python value to the .NET type required by a TDMS property."""
    dotnet_data_type = getattr(data_type, "_dotnet_instance", data_type)
    clr_type = _TDMS_PROPERTY_CLR_TYPES.get(str(dotnet_data_type))
    if clr_type is None:
        return value
    if clr_type is System.DateTime and isinstance(value, datetime.datetime):
        return _to_dotnet_datetime(value)
    return clr_type(value)


def _unwrap_untyped_iterable(arg: Any) -> Any:
    """Unwrap an iterable when no target .NET element type is known.

    Each element that is a wrapper object is replaced by its .NET instance; everything else
    is passed through so pythonnet converts it. Used for .NET arrays (whose element type
    maps to None) and as the fallback for generic shapes we do not build explicitly.
    """
    return [item._dotnet_instance if hasattr(item, "_dotnet_instance") else item for item in arg]


# Open generic collection definitions used to build strongly typed collections at runtime.
_DOTNET_LIST_TYPE_DEF = System.Type.GetType("System.Collections.Generic.List`1")
_DOTNET_DICT_TYPE_DEF = System.Type.GetType("System.Collections.Generic.Dictionary`2")
# Cache of resolved .NET types keyed by their (assembly-qualified) fullname.
_dotnet_type_cache: Dict[str, Any] = {}
# Cache of successfully closed generic types keyed by their structured descriptor.
_resolved_descriptor_cache: Dict[Any, Any] = {}


def _resolve_dotnet_type(fullname: str) -> Any:
    """Resolve (and cache) a .NET Type from its fullname, or None if it cannot be found."""
    if fullname not in _dotnet_type_cache:
        _dotnet_type_cache[fullname] = System.Type.GetType(fullname)
    return _dotnet_type_cache[fullname]


def _resolve_leaf_type(token: str) -> Any:
    """Resolve a descriptor leaf token to a .NET Type.

    System leaves are emitted as their fullname ('System.Int32', 'System.String') and
    resolve directly through System.Type.GetType. NI leaves are emitted as their full .NET
    name ('NationalInstruments.VeriStand.ClientAPI.IChannel') and resolve through the
    generated-type registry keyed by full name. Returns None when the token names a type
    that has not been generated/loaded.
    """
    dotnet_type = _resolve_dotnet_type(token)
    if dotnet_type is not None:
        return dotnet_type
    wrapper = _DOTNET_FULLNAME_REGISTRY.get(token)
    if wrapper is not None:
        return _DOTNET_CTOR_TYPE_REGISTRY.get(wrapper)
    return None


def _resolve_descriptor(descriptor: Any) -> Any:
    """Rebuild the exact closed .NET Type from a compact marshaling descriptor.

    A descriptor is None, a leaf token string, or a nested tuple
    (open_generic_def_fullname, element_descriptor, ...). The open definition is resolved
    with System.Type.GetType and closed over its recursively resolved element types via
    MakeGenericType, so arbitrarily nested collections/tuples/delegates are reconstructed
    from parts. Returns None if any piece cannot be resolved, so the caller can fall back.
    """
    if descriptor is None:
        return None
    if descriptor in _resolved_descriptor_cache:
        return _resolved_descriptor_cache[descriptor]
    if isinstance(descriptor, str):
        return _resolve_leaf_type(descriptor)
    # Special case: rank-2 array descriptor emitted by the code generator for types
    # like double[,].  Resolve the element type then call MakeArrayType(2) so that
    # _build_dotnet_value receives the exact .NET array type it needs.
    if descriptor[0] == "__array2d__":
        element_type = _resolve_descriptor(descriptor[1])
        if element_type is None:
            return None
        try:
            resolved = element_type.MakeArrayType(2)
        except System.Exception:
            return None
        _resolved_descriptor_cache[descriptor] = resolved
        return resolved
    generic_def = _resolve_dotnet_type(descriptor[0])
    if generic_def is None:
        return None
    element_types = [_resolve_descriptor(element) for element in descriptor[1:]]
    if any(element_type is None for element_type in element_types):
        return None
    try:
        resolved = generic_def.MakeGenericType(*element_types)
    except System.Exception:
        return None
    _resolved_descriptor_cache[descriptor] = resolved
    return resolved


def _dotnet_generic_def_name(dotnet_type: Any) -> str:
    """Return the fullname of the open generic type definition (e.g. 'System.Tuple`2')."""
    return dotnet_type.GetGenericTypeDefinition().FullName if dotnet_type.IsGenericType else ""


def _build_dotnet_value(value: Any, dotnet_type: Any) -> Any:
    """Recursively marshal a Python value into the exact .NET ``dotnet_type``.

    The value is returned unchanged when no explicit construction applies (pythonnet then
    performs the conversion). This is shape-based rather than type-by-type: any sequence,
    map, or tuple is handled generically by inspecting the resolved .NET type, and every
    element/key/value is marshaled by this same recursion, so nested combinations work and
    new collection types need no new code.
    """
    if value is None:
        return None
    if hasattr(value, "_dotnet_instance"):
        return value._dotnet_instance
    if isinstance(value, datetime.datetime):
        return _to_dotnet_datetime(value)
    if isinstance(value, uuid.UUID):
        return _to_dotnet_guid(value)
    if dotnet_type is not None and dotnet_type.FullName == "System.Version":
        return _to_dotnet_version(value)
    if dotnet_type is not None and dotnet_type.IsArray and dotnet_type.GetArrayRank() > 1:
        # Multi-dimensional .NET array (e.g. double[,]): build from a nested Python sequence.
        element_type = dotnet_type.GetElementType()
        rows = list(value)
        if not rows:
            return System.Array.CreateInstance(element_type, 0, 0)
        row0 = list(rows[0])
        arr = System.Array.CreateInstance(element_type, len(rows), len(row0))
        for r, row in enumerate(rows):
            for c, item in enumerate(row):
                arr[r, c] = _build_dotnet_value(item, element_type)
        return arr
    if dotnet_type is None or not dotnet_type.IsGenericType:
        # Scalars, primitives and arrays are converted by pythonnet.
        return value
    return _build_dotnet_generic(value, dotnet_type)


def _build_dotnet_generic(value: Any, dotnet_type: Any) -> Any:
    """Build a value for a closed generic .NET type (tuple / map / sequence).

    Returns ``value`` unchanged when the shape is not one we construct explicitly, so the
    caller (or pythonnet) can fall back and surface a clear error rather than corrupting it.
    """
    generic_args = dotnet_type.GetGenericArguments()

    # Tuple: built through the static factory, which closes the tuple over its elements.
    if _dotnet_generic_def_name(dotnet_type).startswith("System.Tuple`") and _is_iterable(value):
        items = list(value)
        if len(items) == len(generic_args):
            marshaled = [_build_dotnet_value(item, t) for item, t in zip(items, generic_args)]
            return System.Tuple.Create(*marshaled)
        return value

    # Map: any 2-argument type a Dictionary<K, V> satisfies (Dictionary, IDictionary,
    # IReadOnlyDictionary, ...).
    if len(generic_args) == 2 and _DOTNET_DICT_TYPE_DEF is not None:
        dict_type = _DOTNET_DICT_TYPE_DEF.MakeGenericType(generic_args[0], generic_args[1])
        if dotnet_type.IsAssignableFrom(dict_type):
            instance = System.Activator.CreateInstance(dict_type)
            pairs = value.items() if isinstance(value, dict) else value
            for key, val in pairs:
                instance[_build_dotnet_value(key, generic_args[0])] = _build_dotnet_value(
                    val, generic_args[1]
                )
            return instance

    # Sequence: any single-argument type a List<T> satisfies (List, IList, ICollection,
    # IEnumerable, IReadOnlyList, ...).
    if len(generic_args) == 1 and _is_iterable(value):
        element_type = generic_args[0]
        list_type = _DOTNET_LIST_TYPE_DEF.MakeGenericType(element_type)
        if dotnet_type.IsAssignableFrom(list_type):
            instance = System.Activator.CreateInstance(list_type)
            for item in value:
                instance.Add(_build_dotnet_value(item, element_type))
            return instance

    # Unknown/unsupported generic shape: let pythonnet attempt the conversion.
    return value


def _to_dotnet_collection(arg: Any, descriptor: Any) -> Any:
    """Marshal a Python value into the real .NET generic type described by descriptor.

    Falls back to a plain unwrapped iterable when the type cannot be resolved or is not a
    shape we build explicitly.
    """
    collection_type = _resolve_descriptor(descriptor)
    if collection_type is not None:
        built = _build_dotnet_value(arg, collection_type)
        if built is not arg:
            return built
    return _unwrap_untyped_iterable(arg)


_DOTNET_DELEGATE_CLASSES = {
    "System.Predicate`1": System.Predicate,
    "System.EventHandler`1": System.EventHandler,
}
_closed_dotnet_delegate_cache: Dict[Any, Any] = {}
# EventHandler registration and unregistration must receive the same delegate instance.
_dotnet_event_handler_cache: Dict[Any, Any] = {}


def _callable_cache_key(callable_arg: Any, descriptor: Any) -> Any:
    """Return a stable cache key for functions, bound methods, and unhashable callables."""
    try:
        hash(callable_arg)
    except TypeError:
        return ("id", id(callable_arg), descriptor)
    return ("callable", callable_arg, descriptor)


def _to_dotnet_delegate(callable_arg: Any, descriptor: Any) -> Any:
    """Adapt a Python callable to a supported .NET generic delegate.

    For ``('System.Predicate`1', 'IChannel')``, this constructs the equivalent of
    ``System.Predicate[VSAPI.IChannel](bridge)``. When .NET invokes ``bridge``, each raw
    argument is passed through ``_wrap`` before the user's callable runs, so its channel
    argument exposes Python properties such as ``channel.is_writable``. The callback result
    is unwrapped before returning to .NET.

    Only ``Predicate<T>`` and ``EventHandler<TEventArgs>`` are supported because they are the
    only delegate parameter families in the generated API surface. Other descriptors are
    returned unchanged for pythonnet to reject normally.
    """
    if not isinstance(descriptor, tuple) or len(descriptor) != 2:
        return callable_arg

    delegate_name, argument_descriptor = descriptor
    delegate_class = _DOTNET_DELEGATE_CLASSES.get(delegate_name)
    if delegate_class is None:
        return callable_arg

    # System.Predicate[IChannel] is closed generic class and System.Predicate is open generic class
    closed_delegate_class = _closed_dotnet_delegate_cache.get(descriptor)
    if closed_delegate_class is None:
        argument_type = _resolve_descriptor(argument_descriptor)
        if argument_type is None:
            return callable_arg
        closed_delegate_class = delegate_class[argument_type]
        _closed_dotnet_delegate_cache[descriptor] = closed_delegate_class

    cache_key = None
    if delegate_name == "System.EventHandler`1":
        cache_key = _callable_cache_key(callable_arg, descriptor)
        cached = _dotnet_event_handler_cache.get(cache_key)
        if cached is not None:
            return cached

    def _bridge(*delegate_args: Any):
        wrapped_args = tuple(_wrap(arg) for arg in delegate_args)
        result = callable_arg(*wrapped_args)
        return _unwrap_single_arg(result)

    delegate = closed_delegate_class(_bridge)
    if cache_key is not None:
        _dotnet_event_handler_cache[cache_key] = delegate
    return delegate


def _subscribe_event_handler(
    callable_arg: Any, dotnet_instance: Any, event_name: str, delegate_type: Any
) -> Any:
    """Create a new .NET delegate for an event subscription (+=)."""
    cache_descriptor = (id(dotnet_instance), event_name)
    full_key = _callable_cache_key(callable_arg, cache_descriptor)

    def _bridge(*delegate_args: Any) -> Any:
        if callable_arg is None:
            # A None handler mirrors C# ``event += null``: registered but a no-op when raised.
            return None
        wrapped_args = tuple(_wrap(arg) for arg in delegate_args)
        result = callable_arg(*wrapped_args)
        return _unwrap_single_arg(result)

    delegate = delegate_type(_bridge)
    _dotnet_event_handler_cache.setdefault(full_key, []).append(delegate)
    return delegate


def _pop_event_handler_from_cache(
    callable_arg: Any, dotnet_instance: Any, event_name: str
) -> Optional[Any]:
    """Remove and return one cached .NET delegate for a single event unsubscription (-=)."""
    cache_descriptor = (id(dotnet_instance), event_name)
    full_key = _callable_cache_key(callable_arg, cache_descriptor)
    delegates = _dotnet_event_handler_cache.get(full_key)
    if not delegates:
        return None
    delegate = delegates.pop()
    if not delegates:
        del _dotnet_event_handler_cache[full_key]
    return delegate


def _unwrap_single_arg(arg: Any, dotnet_type: Any = None) -> Any:
    """Marshal a single Python argument into its target .NET type."""
    if hasattr(arg, "_dotnet_instance"):
        return arg._dotnet_instance
    if isinstance(arg, datetime.datetime):
        return _to_dotnet_datetime(arg)
    if isinstance(arg, uuid.UUID):
        return _to_dotnet_guid(arg)

    # Predicate<T> or EventHandler<T>.
    if dotnet_type is not None and callable(arg) and not _is_iterable(arg):
        return _to_dotnet_delegate(arg, dotnet_type)

    # An iterable argument targets a generic collection (List/IList/IEnumerable/Dictionary/
    # Tuple/...): build the real closed .NET collection so pythonnet is not left to guess the
    # element type. Everything else (scalars, primitive/wrapper arrays) is converted by
    # pythonnet, so it is passed through unchanged.
    if dotnet_type is not None and _is_iterable(arg):
        return _to_dotnet_collection(arg, dotnet_type)

    if _is_iterable(arg):
        return _unwrap_untyped_iterable(arg)
    return arg


def _unwrap(
    spec: Optional[Dict[Optional[Tuple[type, ...]], Tuple[Tuple[int, ...], Tuple[Any, ...]]]],
    *args: Any,
) -> Iterable[Any]:
    """Yield .NET-ready positional arguments for a wrapped .NET call.

    ``spec`` is either ``None`` (legacy callers with no out params) or a dict mapping
    an optional Python input-type signature to a ``(out_positions, dotnet_types)`` tuple:

      * ``out_positions``: indices where a placeholder is inserted for a .NET out/ref
        parameter. The real value is produced by the .NET call and surfaced through the
        returned tuple. Only *interior* out params (those followed by a normal input
        param) appear here; *trailing* out params are left off the call entirely and
        filled in by pythonnet, so they never need a placeholder.
      * ``dotnet_types``: a compact marshaling descriptor per position -- None, a leaf token
        ('System.Int32', 'IChannel'), or a nested (generic_def, element, ...) tuple -- naming
        the exact target .NET type so a generic collection or delegate argument can be built
        manually (_resolve_descriptor rebuilds the closed type). It is empty when no argument
        needs manual marshaling, and any position past its end is treated as None.
    """
    out_positions: Tuple[int, ...] = ()
    dotnet_types: Tuple[Any, ...] = ()
    if spec:
        selected = _select_matching_overload(spec, args)
        if selected is not None:
            out_positions, dotnet_types = selected

    # First layer: rebuild the full .NET argument list by inserting a None placeholder at
    # each out/ref parameter position, so the arguments line up with the .NET parameter
    # list (and, when present, with ``dotnet_types``).
    reformed_args = list(args)
    for position in sorted(out_positions):
        reformed_args.insert(position, None)

    # Second layer: manually marshal each argument into its target .NET type. A None entry
    # is an out/ref placeholder (or an explicit null); it is yielded as-is without calling
    # _unwrap_single_arg, since the .NET side supplies the real value.
    for i, arg in enumerate(reformed_args):
        if arg is None:
            yield None
            continue
        target_dotnet_type = dotnet_types[i] if i < len(dotnet_types) else None
        yield _unwrap_single_arg(arg, target_dotnet_type)


_wrap_sentinel_value = object()


_ENUM_NAME_BASIC_REGEX = re.compile(r"(.)([A-Z][a-z]+)")
_ENUM_NAME_ADVANCED_REGEX = re.compile(r"([a-z0-9])([A-Z])")
_ENUM_NAME_COMPOUND_WORDS = ("VeriStand", "VIs", "UInt", "MHz")


def _dotnet_name_to_py_field(name: str) -> str:
    """Convert a .NET enum field name to its generated Python field name."""
    name_with_underscores = _ENUM_NAME_BASIC_REGEX.sub(r"\1_\2", name)
    result = _ENUM_NAME_ADVANCED_REGEX.sub(r"\1_\2", name_with_underscores)

    for compound in _ENUM_NAME_COMPOUND_WORDS:
        split_compound = _ENUM_NAME_BASIC_REGEX.sub(r"\1_\2", compound)
        split_compound = _ENUM_NAME_ADVANCED_REGEX.sub(r"\1_\2", split_compound)
        result = result.replace(split_compound, compound)

    result = re.sub(r"_I_([A-Z][a-z0-9]*)", r"_I\1", result)
    return result.upper()


def _wrap(
    one_or_many_args: Union[Any, Tuple[Any]], error_as_data: bool = False
) -> Union[Any, Tuple[Any]]:
    """Wrap one or many .NET values into their Python wrapper equivalents."""
    caller_module = sys._getframe(1).f_globals.get("__name__", "")
    is_sdf_api = _is_sdf_api_module(caller_module)

    def _is_ni_type(item: Any):
        return type(item).__module__.startswith("NationalInstruments.")

    def _is_key_value_pair(item: Any) -> bool:
        return type(item).__name__.startswith("KeyValuePair")

    def _is_dotnet_tuple(item: Any) -> bool:
        return type(item).__module__ == "System" and type(item).__name__.startswith("Tuple")

    def _wrap_dotnet_tuple(item: Any) -> Tuple[Any, ...]:
        arity = len(item.GetType().GetGenericArguments())
        return tuple(_wrap_core(getattr(item, f"Item{index}")) for index in range(1, arity + 1))

    def _wrap_dotnet_instance(dotnetitem: Any):
        full_name = f"{type(dotnetitem).__module__}.{type(dotnetitem).__name__}"
        if full_name != "NationalInstruments.VeriStand.Error":
            pytype = _DOTNET_FULLNAME_REGISTRY.get(full_name)
            if pytype is None:
                return dotnetitem
            # For enums, derive the Python field name from the dotnet ToString()
            # so that _py_field_name is always populated (not left as "").
            if issubclass(pytype, _DotNetEnum):
                return pytype(dotnetitem, _dotnet_name_to_py_field(str(dotnetitem)))
            return pytype(dotnetitem)
        elif error_as_data:
            # The Error is returned as data (e.g. an item in an Iterable[VeriStandError]),
            # so expose it as a wrapper instead of treating it as a status to raise.
            return _DOTNET_FULLNAME_REGISTRY[_VERISTAND_NAMESPACE + "VeriStandError"](dotnetitem)
        elif dotnetitem.IsError:
            if is_sdf_api:
                _raise_veristand_sdf_error(dotnetitem)
            _raise_veristand_error(dotnetitem)
        else:
            return _wrap_sentinel_value

    def _wrap_core(arg: Any) -> Any:
        if _is_iterable(arg) and getattr(arg, "Rank", 1) > 1:
            # Multi-dimensional .NET array (e.g. double[,]) — pythonnet iterates flat,
            # so rebuild the shape manually.
            rows, cols = arg.GetLength(0), arg.GetLength(1)
            return [[_wrap_core(arg[r, c]) for c in range(cols)] for r in range(rows)]
        elif _is_dotnet_tuple(arg):
            return _wrap_dotnet_tuple(arg)
        elif _is_iterable(arg) and type(arg).__name__.startswith(("HashSet")):
            # .NET set types: preserve set semantics. _DotNetBase defines __hash__ so
            # wrapper objects are safely hashable.
            return {_wrap_core(item) for item in arg}
        elif _is_iterable(arg) and hasattr(arg, "Keys"):
            # .NET map types (Dictionary<K,V>, IReadOnlyDictionary<K,V>,
            # ...): any type exposing .Keys is a dictionary — wrap as a Python dict.
            # This is distinct from iterables that merely *contain* KeyValuePair elements
            # (e.g. IEnumerable<KeyValuePair<IChannel,IChannel>>) which become lists of tuples.
            return {_wrap_core(item.Key): _wrap_core(item.Value) for item in arg}
        elif _is_iterable(arg):
            return [_wrap_core(item) for item in arg]
        elif _is_key_value_pair(arg):
            return (_wrap_core(arg.Key), _wrap_core(arg.Value))
        elif _is_ni_type(arg):
            return _wrap_dotnet_instance(arg)
        elif str(type(arg)) == "<class 'System.Version'>":
            # System.Version uses `Build` as the third element, not the fourth
            return (arg.Major, arg.Minor, arg.Build, arg.Revision)
        elif str(type(arg)) == "<class 'System.DateTime'>":
            return _from_dotnet_datetime(arg)
        elif str(type(arg)) == "<class 'System.Guid'>":
            return uuid.UUID(str(arg))
        return arg

    def _is_sentinel_result(value: Any) -> bool:
        return value is _wrap_sentinel_value or (
            isinstance(value, list)
            and value
            and all(item is _wrap_sentinel_value for item in value)
        )

    if isinstance(one_or_many_args, Tuple):
        wrapped = [_wrap_core(x) for x in one_or_many_args]
        result = [value for value in wrapped if not _is_sentinel_result(value)]
        if not result:
            return None
        # if we have two parameters, and one is Error, only return the non-error one
        return result[0] if len(result) == 1 and len(wrapped) == 2 else tuple(result)
    else:
        result = _wrap_core(one_or_many_args)
        return result if result is not _wrap_sentinel_value else None
