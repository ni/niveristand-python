"""Module for NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA_Support."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.SystemDefinitionAPI")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA_Support  # type: ignore
import System  # type: ignore

from ... import *


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.systemdefinitionapi.fpga_support.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.systemdefinitionapi.fpga_support.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

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


class FPGACategory(_DotNetBase):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA_Support.FPGACategory:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGACategory")

    @property
    def name(self) -> str:
        dotnet_result = self._dotnet_instance.Name
        return _wrap(dotnet_result)

    @property
    def description(self) -> str:
        dotnet_result = self._dotnet_instance.Description
        return _wrap(dotnet_result)

    @property
    def symbol(self) -> str:
        dotnet_result = self._dotnet_instance.Symbol
        return _wrap(dotnet_result)

    @property
    def categories(self) -> Sequence[FPGACategory]:
        dotnet_result = self._dotnet_instance.Categories
        return _wrap(dotnet_result)

    @property
    def channels(self) -> Sequence[FPGAChannel]:
        dotnet_result = self._dotnet_instance.Channels
        return _wrap(dotnet_result)

    @overload
    def to_string(self) -> str:
        ...

    def to_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ToString(*unwrapped)
        return _wrap(dotnet_result)

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class FPGAChannel(_DotNetBase):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA_Support.FPGAChannel:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGAChannel")

    @property
    def name(self) -> str:
        dotnet_result = self._dotnet_instance.Name
        return _wrap(dotnet_result)

    @property
    def category(self) -> str:
        dotnet_result = self._dotnet_instance.Category
        return _wrap(dotnet_result)

    @property
    def symbol(self) -> str:
        dotnet_result = self._dotnet_instance.Symbol
        return _wrap(dotnet_result)

    @property
    def description(self) -> str:
        dotnet_result = self._dotnet_instance.Description
        return _wrap(dotnet_result)

    @property
    def unit(self) -> str:
        dotnet_result = self._dotnet_instance.Unit
        return _wrap(dotnet_result)

    @property
    def initial_value(self) -> float:
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @property
    def packet_index(self) -> int:
        dotnet_result = self._dotnet_instance.PacketIndex
        return _wrap(dotnet_result)

    @property
    def bit_offset(self) -> int:
        dotnet_result = self._dotnet_instance.BitOffset
        return _wrap(dotnet_result)

    @property
    def representation(self) -> int:
        dotnet_result = self._dotnet_instance.Representation
        return _wrap(dotnet_result)

    @property
    def scaling(self) -> float:
        dotnet_result = self._dotnet_instance.Scaling
        return _wrap(dotnet_result)

    @property
    def scaling_offset(self) -> float:
        dotnet_result = self._dotnet_instance.ScalingOffset
        return _wrap(dotnet_result)

    @property
    def fxpwl(self) -> int:
        dotnet_result = self._dotnet_instance.FXPWL
        return _wrap(dotnet_result)

    @property
    def fxpiwl(self) -> int:
        dotnet_result = self._dotnet_instance.FXPIWL
        return _wrap(dotnet_result)

    @property
    def period_pwm(self) -> int:
        dotnet_result = self._dotnet_instance.PeriodPWM
        return _wrap(dotnet_result)

    @property
    def data_offset(self) -> int:
        dotnet_result = self._dotnet_instance.DataOffset
        return _wrap(dotnet_result)

    @property
    def is_write(self) -> bool:
        dotnet_result = self._dotnet_instance.IsWrite
        return _wrap(dotnet_result)

    @overload
    def to_string(self) -> str:
        ...

    def to_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ToString(*unwrapped)
        return _wrap(dotnet_result)

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class FPGALoader(_DotNetBase):
    @overload
    def __init__(self, file_path: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA_Support.FPGALoader:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA_Support.FPGALoader(*unwrapped)

    @property
    def version(self) -> float:
        dotnet_result = self._dotnet_instance.Version
        return _wrap(dotnet_result)

    @property
    def bit_file(self) -> str:
        dotnet_result = self._dotnet_instance.BitFile
        return _wrap(dotnet_result)

    @property
    def read_packets(self) -> int:
        dotnet_result = self._dotnet_instance.ReadPackets
        return _wrap(dotnet_result)

    @property
    def write_packets(self) -> int:
        dotnet_result = self._dotnet_instance.WritePackets
        return _wrap(dotnet_result)

    @property
    def categories(self) -> Sequence[FPGACategory]:
        dotnet_result = self._dotnet_instance.Categories
        return _wrap(dotnet_result)

    @overload
    def to_string(self) -> str:
        ...

    def to_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ToString(*unwrapped)
        return _wrap(dotnet_result)
