"""Module for NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.SystemDefinitionAPI")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport  # type: ignore
import System  # type: ignore

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

    @_staticproperty
    def can_standard() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.Constants.CanStandard
        return _wrap(dotnet_result)

    @_staticproperty
    def can_fd() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.Constants.CanFd
        return _wrap(dotnet_result)

    @_staticproperty
    def can_fd_brs() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.Constants.CanFdBrs
        return _wrap(dotnet_result)


class IECUNetworkClusterConfiguration(_DotNetBase):
    """Interface class for serializing and de-serializing ECU network cluster configuration."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.IECUNetworkClusterConfiguration:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IECUNetworkClusterConfiguration")

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
    def cluster_name(self) -> str:
        """Name of the cluster used in database."""
        dotnet_result = self._dotnet_instance.ClusterName
        return _wrap(dotnet_result)

    @cluster_name.setter
    def cluster_name(self, value: str):
        """Name of the cluster used in database."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ClusterName = next(unwrapped)

    @property
    def time_step(self) -> float:
        """Time step of cluster."""
        dotnet_result = self._dotnet_instance.TimeStep
        return _wrap(dotnet_result)

    @time_step.setter
    def time_step(self, value: float):
        """Time step of cluster."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TimeStep = next(unwrapped)

    @property
    def protocol(self) -> str:
        """The communication type of the cluster."""
        dotnet_result = self._dotnet_instance.Protocol
        return _wrap(dotnet_result)

    @protocol.setter
    def protocol(self, value: str):
        """The communication type of the cluster."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Protocol = next(unwrapped)

    @property
    def toolchain(self) -> str:
        """Toolchain name."""
        dotnet_result = self._dotnet_instance.Toolchain
        return _wrap(dotnet_result)

    @toolchain.setter
    def toolchain(self, value: str):
        """Toolchain name."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Toolchain = next(unwrapped)

    @property
    def virtual_ecu_list(self) -> Iterable[str]:
        """Virtual ECUs that have been added to the cluster."""
        dotnet_result = self._dotnet_instance.VirtualECUList
        return _wrap(dotnet_result)

    @virtual_ecu_list.setter
    def virtual_ecu_list(self, value: Iterable[str]):
        """Virtual ECUs that have been added to the cluster."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.VirtualECUList = next(unwrapped)

    @property
    def io_mode(self) -> str:
        """I/O Mode if protocol is CAN."""
        dotnet_result = self._dotnet_instance.IOMode
        return _wrap(dotnet_result)

    @io_mode.setter
    def io_mode(self, value: str):
        """I/O Mode if protocol is CAN."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IOMode = next(unwrapped)

    @property
    def lin_master_model_linux_path(self) -> str:
        """LIN Master Model path."""
        dotnet_result = self._dotnet_instance.LinMasterModelLinuxPath
        return _wrap(dotnet_result)

    @lin_master_model_linux_path.setter
    def lin_master_model_linux_path(self, value: str):
        """LIN Master Model path."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LinMasterModelLinuxPath = next(unwrapped)

    @property
    def xnet_can_configuration(self) -> IXnetCanConfiguration:
        """Protocol specific configuration for CAN."""
        dotnet_result = self._dotnet_instance.XnetCanConfiguration
        return _wrap(dotnet_result)

    @xnet_can_configuration.setter
    def xnet_can_configuration(self, value: IXnetCanConfiguration):
        """Protocol specific configuration for CAN."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.XnetCanConfiguration = next(unwrapped)

    @property
    def xnet_lin_configuration(self) -> IXnetLinConfiguration:
        """Protocol specific configuration for LIN."""
        dotnet_result = self._dotnet_instance.XnetLinConfiguration
        return _wrap(dotnet_result)

    @xnet_lin_configuration.setter
    def xnet_lin_configuration(self, value: IXnetLinConfiguration):
        """Protocol specific configuration for LIN."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.XnetLinConfiguration = next(unwrapped)

    @property
    def xnet_ethernet_configuration(self) -> IXnetEthernetConfiguration:
        """Protocol specific configuration for Ethernet."""
        dotnet_result = self._dotnet_instance.XnetEthernetConfiguration
        return _wrap(dotnet_result)

    @xnet_ethernet_configuration.setter
    def xnet_ethernet_configuration(self, value: IXnetEthernetConfiguration):
        """Protocol specific configuration for Ethernet."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.XnetEthernetConfiguration = next(unwrapped)

    @property
    def svb_configuration(self) -> ISvbConfiguration:
        """Configuration required to initialize Synopsys Virtual Bus (SVB)."""
        dotnet_result = self._dotnet_instance.SvbConfiguration
        return _wrap(dotnet_result)

    @svb_configuration.setter
    def svb_configuration(self, value: ISvbConfiguration):
        """Configuration required to initialize Synopsys Virtual Bus (SVB)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SvbConfiguration = next(unwrapped)

    @overload
    def serialize_to(self, cluster_configuration_file_path: str):
        ...

    def serialize_to(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SerializeTo(*unwrapped)
        return _wrap(dotnet_result)


class ISvbConfiguration(_DotNetBase):
    """Represents the configuration for Synopsys Virtual Bus (SVB)."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ISvbConfiguration:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ISvbConfiguration")

    @property
    def rx_fifo_capacity(self) -> int:
        """Number of frames that can be buffered by the controller's Rx FIFO."""
        dotnet_result = self._dotnet_instance.RxFifoCapacity
        return _wrap(dotnet_result)

    @rx_fifo_capacity.setter
    def rx_fifo_capacity(self, value: int):
        """Number of frames that can be buffered by the controller's Rx FIFO."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.RxFifoCapacity = next(unwrapped)


class IXnetCanConfiguration(_DotNetBase):
    """Represents the configuration for an XNET interface for CAN communication."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.IXnetCanConfiguration:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IXnetCanConfiguration")

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
    def xnet_interface(self) -> str:
        """Interface port of XNET device to be used."""
        dotnet_result = self._dotnet_instance.XnetInterface
        return _wrap(dotnet_result)

    @xnet_interface.setter
    def xnet_interface(self, value: str):
        """Interface port of XNET device to be used."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.XnetInterface = next(unwrapped)

    @property
    def baud_rate(self) -> int:
        """Baudrate for CAN message transfer."""
        dotnet_result = self._dotnet_instance.BaudRate
        return _wrap(dotnet_result)

    @baud_rate.setter
    def baud_rate(self, value: int):
        """Baudrate for CAN message transfer."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BaudRate = next(unwrapped)

    @property
    def brs_baud_rate(self) -> int:
        """Baudrate for CAN-BRS message transfer."""
        dotnet_result = self._dotnet_instance.BrsBaudRate
        return _wrap(dotnet_result)

    @brs_baud_rate.setter
    def brs_baud_rate(self, value: int):
        """Baudrate for CAN-BRS message transfer."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BrsBaudRate = next(unwrapped)

    @property
    def transceiver_type(self) -> int:
        """The transceiver type value."""
        dotnet_result = self._dotnet_instance.TransceiverType
        return _wrap(dotnet_result)

    @transceiver_type.setter
    def transceiver_type(self, value: int):
        """The transceiver type value."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TransceiverType = next(unwrapped)

    @property
    def can_fd_iso_mode(self) -> int:
        """Can fd iso mode value."""
        dotnet_result = self._dotnet_instance.CanFdIsoMode
        return _wrap(dotnet_result)

    @can_fd_iso_mode.setter
    def can_fd_iso_mode(self, value: int):
        """Can fd iso mode value."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.CanFdIsoMode = next(unwrapped)


class IXnetEthernetConfiguration(_DotNetBase):
    """Represents the configuration for an XNET interface for Ethernet communication"""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.IXnetEthernetConfiguration:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IXnetEthernetConfiguration")

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
    def xnet_interface(self) -> str:
        """Interface port of XNET device to be used."""
        dotnet_result = self._dotnet_instance.XnetInterface
        return _wrap(dotnet_result)

    @xnet_interface.setter
    def xnet_interface(self, value: str):
        """Interface port of XNET device to be used."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.XnetInterface = next(unwrapped)


class IXnetLinConfiguration(_DotNetBase):
    """Represents the configuration for an XNET interface for LIN communication."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.IXnetLinConfiguration:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IXnetLinConfiguration")

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
    def xnet_interface(self) -> str:
        """Interface port of XNET device to be used."""
        dotnet_result = self._dotnet_instance.XnetInterface
        return _wrap(dotnet_result)

    @xnet_interface.setter
    def xnet_interface(self, value: str):
        """Interface port of XNET device to be used."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.XnetInterface = next(unwrapped)

    @property
    def virtual_tx_frame_i_ds(self) -> Iterable[int]:
        """Virtual transmission frame IDs."""
        dotnet_result = self._dotnet_instance.VirtualTxFrameIDs
        return _wrap(dotnet_result)

    @virtual_tx_frame_i_ds.setter
    def virtual_tx_frame_i_ds(self, value: Iterable[int]):
        """Virtual transmission frame IDs."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.VirtualTxFrameIDs = next(unwrapped)

    @property
    def baud_rate(self) -> int:
        """Baudrate for LIN communication."""
        dotnet_result = self._dotnet_instance.BaudRate
        return _wrap(dotnet_result)

    @baud_rate.setter
    def baud_rate(self, value: int):
        """Baudrate for LIN communication."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BaudRate = next(unwrapped)


class SvbConfiguration(ISvbConfiguration):
    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.SvbConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.SvbConfiguration(*unwrapped)


class XnetCanConfiguration(IXnetCanConfiguration):
    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.XnetCanConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.XnetCanConfiguration(*unwrapped)


class XnetEthernetConfiguration(IXnetEthernetConfiguration):
    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.XnetEthernetConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.XnetEthernetConfiguration(*unwrapped)


class XnetLinConfiguration(IXnetLinConfiguration):
    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.XnetLinConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.XnetLinConfiguration(*unwrapped)


class ECUNetworkClusterConfiguration(IECUNetworkClusterConfiguration):
    """Class for serializing and de-serializing ECU network cluster configuration."""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration(*unwrapped)

    @staticmethod
    @overload
    def try_deserialize_from(model_path: str) -> Tuple[bool, ECUNetworkClusterConfiguration]:
        ...

    def try_deserialize_from(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration.TryDeserializeFrom(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def deserialize_from(file_path: str) -> ECUNetworkClusterConfiguration:
        ...

    def deserialize_from(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration.DeserializeFrom(*unwrapped)
        return _wrap(dotnet_result)
