"""Module for NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.SystemDefinitionAPI")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport  # type: ignore
import System  # type: ignore

from ... import *
from .... import *


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.systemdefinitionapi.modelsupport.virtualecusupport.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.systemdefinitionapi.modelsupport.virtualecusupport.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

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


class CANConfiguration(ICANConfiguration):
    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, other: ICANConfiguration):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.CANConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.CANConfiguration(*unwrapped)

    @property
    def connect_to_real_network(self) -> bool:
        """Value indicating whether to connect to the real network."""
        dotnet_result = self._dotnet_instance.ConnectToRealNetwork
        return _wrap(dotnet_result)

    @connect_to_real_network.setter
    def connect_to_real_network(self, value: bool):
        """Value indicating whether to connect to the real network."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ConnectToRealNetwork = next(unwrapped)

    @property
    def use_database(self) -> bool:
        """Value indicating whether to use a database."""
        dotnet_result = self._dotnet_instance.UseDatabase
        return _wrap(dotnet_result)

    @use_database.setter
    def use_database(self, value: bool):
        """Value indicating whether to use a database."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.UseDatabase = next(unwrapped)

    @property
    def database_alias(self) -> str:
        """Database alias value."""
        dotnet_result = self._dotnet_instance.DatabaseAlias
        return _wrap(dotnet_result)

    @database_alias.setter
    def database_alias(self, value: str):
        """Database alias value."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DatabaseAlias = next(unwrapped)


class Constants(_DotNetBase):
    """Contains constants for VirtualECU"""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.Constants:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Constants")

    @_staticproperty
    def ecu_network_cluster_file_extension() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.Constants.ECUNetworkClusterFileExtension
        return _wrap(dotnet_result)


class ECUNetworkClusterConfiguration(IECUNetworkClusterConfiguration):
    """Class for serializing and de-serializing ECU network cluster configuration."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, other: IECUNetworkClusterConfiguration):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration(*unwrapped)

    @property
    def version(self) -> str:
        """Version of the json file."""
        dotnet_result = self._dotnet_instance.Version
        return _wrap(dotnet_result)

    @version.setter
    def version(self, value: str):
        """Version of the json file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Version = next(unwrapped)

    @property
    def database_path(self) -> str:
        """Database path."""
        dotnet_result = self._dotnet_instance.DatabasePath
        return _wrap(dotnet_result)

    @database_path.setter
    def database_path(self, value: str):
        """Database path."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DatabasePath = next(unwrapped)

    @property
    def virtual_ecu_list(self) -> Sequence[str]:
        """Virtual ECUs that have been added to the cluster."""
        dotnet_result = self._dotnet_instance.VirtualECUList
        return _wrap(dotnet_result)

    @virtual_ecu_list.setter
    def virtual_ecu_list(self, value: Sequence[str]):
        """Virtual ECUs that have been added to the cluster."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.VirtualECUList = next(unwrapped)

    @property
    def lin_master_model_linux_path(self) -> str:
        """LIN Master Model path."""
        dotnet_result = self._dotnet_instance.LINMasterModelLinuxPath
        return _wrap(dotnet_result)

    @lin_master_model_linux_path.setter
    def lin_master_model_linux_path(self, value: str):
        """LIN Master Model path."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LINMasterModelLinuxPath = next(unwrapped)

    @property
    def svb_configuration(self) -> SVBConfiguration:
        """Represents the configuration for Synopsys Virtual Bus (SVB)."""
        dotnet_result = self._dotnet_instance.SVBConfiguration
        return _wrap(dotnet_result)

    @svb_configuration.setter
    def svb_configuration(self, value: SVBConfiguration):
        """Represents the configuration for Synopsys Virtual Bus (SVB)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SVBConfiguration = next(unwrapped)

    @overload
    def serialize_to(self, cluster_configuration_file_path: str):
        ...

    def serialize_to(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SerializeTo(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def try_deserialize_from(model_path: str) -> Tuple[bool, IECUNetworkClusterConfiguration]:
        ...

    def try_deserialize_from(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration.TryDeserializeFrom(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def deserialize_from(file_path: str) -> IECUNetworkClusterConfiguration:
        ...

    def deserialize_from(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration.DeserializeFrom(*unwrapped)
        return _wrap(dotnet_result)


class EthernetConfiguration(IEthernetConfiguration):
    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, other: IEthernetConfiguration):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.EthernetConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.EthernetConfiguration(*unwrapped)

    @property
    def connect_to_real_network(self) -> bool:
        """Value indicating whether to connect to the real network."""
        dotnet_result = self._dotnet_instance.ConnectToRealNetwork
        return _wrap(dotnet_result)

    @connect_to_real_network.setter
    def connect_to_real_network(self, value: bool):
        """Value indicating whether to connect to the real network."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ConnectToRealNetwork = next(unwrapped)

    @property
    def virtual_ecumac_addresses(self) -> Sequence[str]:
        """Virtual ECU MAC Addresses."""
        dotnet_result = self._dotnet_instance.VirtualECUMACAddresses
        return _wrap(dotnet_result)

    @virtual_ecumac_addresses.setter
    def virtual_ecumac_addresses(self, value: Sequence[str]):
        """Virtual ECU MAC Addresses."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.VirtualECUMACAddresses = next(unwrapped)


class LINConfiguration(ILINConfiguration):
    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, other: ILINConfiguration):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.LINConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.LINConfiguration(*unwrapped)

    @property
    def connect_to_real_network(self) -> bool:
        """Value indicating whether to connect to the real network."""
        dotnet_result = self._dotnet_instance.ConnectToRealNetwork
        return _wrap(dotnet_result)

    @connect_to_real_network.setter
    def connect_to_real_network(self, value: bool):
        """Value indicating whether to connect to the real network."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ConnectToRealNetwork = next(unwrapped)

    @property
    def use_database(self) -> bool:
        """Value indicating whether to use a database."""
        dotnet_result = self._dotnet_instance.UseDatabase
        return _wrap(dotnet_result)

    @use_database.setter
    def use_database(self, value: bool):
        """Value indicating whether to use a database."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.UseDatabase = next(unwrapped)

    @property
    def database_alias(self) -> str:
        """Database alias value."""
        dotnet_result = self._dotnet_instance.DatabaseAlias
        return _wrap(dotnet_result)

    @database_alias.setter
    def database_alias(self, value: str):
        """Database alias value."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DatabaseAlias = next(unwrapped)

    @property
    def virtual_tx_frame_i_ds(self) -> Sequence[int]:
        """Virtual transmission frame IDs."""
        dotnet_result = self._dotnet_instance.VirtualTxFrameIDs
        return _wrap(dotnet_result)

    @virtual_tx_frame_i_ds.setter
    def virtual_tx_frame_i_ds(self, value: Sequence[int]):
        """Virtual transmission frame IDs."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.VirtualTxFrameIDs = next(unwrapped)


class SVBConfiguration(_DotNetBase):
    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.SVBConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.SVBConfiguration(*unwrapped)

    @property
    def rx_fifo_capacity(self) -> int:
        dotnet_result = self._dotnet_instance.RxFifoCapacity
        return _wrap(dotnet_result)

    @rx_fifo_capacity.setter
    def rx_fifo_capacity(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.RxFifoCapacity = next(unwrapped)
