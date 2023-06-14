"""Module for NationalInstruments.VeriStand.DAQPlugin."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.XMLReader")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.DAQPlugin  # type: ignore
import System  # type: ignore

from .. import *


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.daqplugin.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.daqplugin.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

    def __str__(self) -> str:
        return f"{type(self).__qualname__}.{self._py_field_name}"

    def __int__(self) -> int:
        return int(self._dotnet_instance)


def _is_iterable(arg: Any) -> bool:
    return not isinstance(arg, str) and isinstance(arg, Iterable)


def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]:
    insertion_index = -1
    if out_params:
        use_out_param = False
        for signature, out_param in out_params.items():
            if not signature:
                use_out_param = True
            elif len(args) == len(signature):
                use_out_param = True
                for arg, sig_type in zip(args, signature):
                    if not isinstance(arg, sig_type):
                        use_out_param = False
                        break
            if use_out_param:
                insertion_index, insertion_value = out_param
                break

    for index, arg in enumerate(args):
        # insert the extra value then continue
        if index == insertion_index:
            yield insertion_value

        if hasattr(arg, "_dotnet_instance"):
            yield arg._dotnet_instance
        elif arg and _is_iterable(arg) and hasattr(next(iter(arg)), "_dotnet_instance"):
            yield [item._dotnet_instance for item in arg]
        else:
            yield arg
    # insert the extra value if at the end
    if len(args) == insertion_index:
        yield insertion_value


_wrap_sentinel_value = object()

def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]:
    def _is_ni_type(item: Any):
        return type(item).__module__.startswith("NationalInstruments.")

    def _wrap_dotnet_instance(dotnetitem: Any):
        if type(dotnetitem) != NationalInstruments.VeriStand.Error:
            pytype = eval(type(dotnetitem).__name__)
            return pytype(dotnetitem)
        elif dotnetitem.IsError:
            raise VeriStandSdfError(dotnetitem)
        else:
            return _wrap_sentinel_value

    def _wrap_core(arg: Any) -> Any:
        if _is_iterable(arg):
            first = next(iter(arg), _wrap_sentinel_value)
            if first is _wrap_sentinel_value:
                return []  # empty Python list preferable to an empty .NET list or enumerable
            elif _is_ni_type(first):
                return [_wrap_dotnet_instance(item) for item in arg]
            else:
                return [item for item in arg]
        elif _is_ni_type(arg):
            return _wrap_dotnet_instance(arg)
        elif str(type(arg)) == "<class 'System.Version'>":
            # System.Version uses `Build` as the third element, not the fourth
            return (arg.Major, arg.Minor, arg.Build, arg.Revision)
        return arg

    if isinstance(one_or_many_args, Tuple):
        wrapped = [_wrap_core(x) for x in one_or_many_args]
        result = [x for x in wrapped if x is not _wrap_sentinel_value]
        # if we have two parameters, and one is Error, only return the non-error one
        return result[0] if len(result) == 1 and len(wrapped) == 2 else tuple(result)
    else:
        result = _wrap_core(one_or_many_args)
        return result if result is not _wrap_sentinel_value else None


class ValueDataType(_DotNetEnum):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.DAQPlugin.ValueDataType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ValueDataType")

    @_staticproperty
    def STRING() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "String")
        return ValueDataType(dotnet_result, "STRING")

    @_staticproperty
    def ENUM() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "Enum")
        return ValueDataType(dotnet_result, "ENUM")

    @_staticproperty
    def DOUBLE() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "Double")
        return ValueDataType(dotnet_result, "DOUBLE")

    @_staticproperty
    def U64() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "U64")
        return ValueDataType(dotnet_result, "U64")

    @_staticproperty
    def U32() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "U32")
        return ValueDataType(dotnet_result, "U32")

    @_staticproperty
    def U16() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "U16")
        return ValueDataType(dotnet_result, "U16")

    @_staticproperty
    def I64() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "I64")
        return ValueDataType(dotnet_result, "I64")

    @_staticproperty
    def I32() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "I32")
        return ValueDataType(dotnet_result, "I32")

    @_staticproperty
    def I16() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "I16")
        return ValueDataType(dotnet_result, "I16")

    @_staticproperty
    def BOOLEAN() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "Boolean")
        return ValueDataType(dotnet_result, "BOOLEAN")
