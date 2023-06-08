"""Module for NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.SystemDefinitionAPI")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport  # type: ignore
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
        return f"<niveristand.systemdefinitionapi.modelsupport.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.systemdefinitionapi.modelsupport.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

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


class IModelDescriptor(_DotNetBase):
    """Holds information from the model descriptor"""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.IModelDescriptor:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IModelDescriptor")

    @property
    def model_name(self) -> str:
        """Name of the model"""
        return _wrap(self._dotnet_instance.ModelName)

    @property
    def model_generation_toolchain_version(self) -> Tuple[int, int, int, int]:
        """Version of the tool that was used to generate the model"""
        return _wrap(self._dotnet_instance.ModelGenerationToolchainVersion)

    @property
    def model_version(self) -> Tuple[int, int, int, int]:
        """Version of the model"""
        return _wrap(self._dotnet_instance.ModelVersion)

    @property
    def author(self) -> str:
        """Model author"""
        return _wrap(self._dotnet_instance.Author)

    @property
    def model_description(self) -> str:
        """Description of the model"""
        return _wrap(self._dotnet_instance.ModelDescription)

    @property
    def target_platforms(self) -> Iterable[str]:
        """Target platforms supported by the model"""
        return _wrap(self._dotnet_instance.TargetPlatforms)


class ModelParamType(_DotNetBase):
    """RESERVED FOR INTERNAL USE. Wraps model parameter information."""

    @overload
    def __init__(self, idx: int, id: str, name: str, type: int, dims: Sequence[int], value: Sequence[float]):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelParamType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelParamType(*_unwrap(None, *args))

    @property
    def idx(self) -> int:
        return _wrap(self._dotnet_instance.Idx)

    @property
    def id(self) -> str:
        return _wrap(self._dotnet_instance.ID)

    @property
    def name(self) -> str:
        return _wrap(self._dotnet_instance.Name)

    @property
    def data_type(self) -> int:
        return _wrap(self._dotnet_instance.DataType)

    @property
    def dims(self) -> Sequence[int]:
        """RESERVED FOR INTERNAL USE."""
        return _wrap(self._dotnet_instance.Dims)

    @property
    def value(self) -> Sequence[float]:
        """RESERVED FOR INTERNAL USE."""
        return _wrap(self._dotnet_instance.Value)

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class ModelPortType(_DotNetBase):
    """RESERVED FOR INTERNAL USE. Wraps model port information."""

    @overload
    def __init__(self, name: str, index: int, task_id: int, is_input: bool, dims: Sequence[int]):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelPortType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelPortType(*_unwrap(None, *args))

    @property
    def name(self) -> str:
        return _wrap(self._dotnet_instance.Name)

    @property
    def index(self) -> int:
        return _wrap(self._dotnet_instance.Index)

    @property
    def task_id(self) -> int:
        return _wrap(self._dotnet_instance.TaskID)

    @property
    def is_input(self) -> bool:
        return _wrap(self._dotnet_instance.IsInput)

    @property
    def dims(self) -> Sequence[int]:
        """RESERVED FOR INTERNAL USE."""
        return _wrap(self._dotnet_instance.Dims)

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class ModelSignalType(_DotNetBase):
    """RESERVED FOR INTERNAL USE. Wraps signal info from a model."""

    @overload
    def __init__(self, idx: int, id: str, name: str, block_name: str, port_number: int, datatype: int, dims: Sequence[int]):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelSignalType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelSignalType(*_unwrap(None, *args))

    @property
    def idx(self) -> int:
        return _wrap(self._dotnet_instance.Idx)

    @property
    def id(self) -> str:
        return _wrap(self._dotnet_instance.ID)

    @property
    def name(self) -> str:
        return _wrap(self._dotnet_instance.Name)

    @property
    def block_name(self) -> str:
        return _wrap(self._dotnet_instance.BlockName)

    @property
    def data_type(self) -> int:
        return _wrap(self._dotnet_instance.DataType)

    @property
    def port_number(self) -> int:
        return _wrap(self._dotnet_instance.PortNumber)

    @property
    def dims(self) -> Sequence[int]:
        """RESERVED FOR INTERNAL USE."""
        return _wrap(self._dotnet_instance.Dims)

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class VsModelFeatureSet(_DotNetBase):
    """Provides information about supported features of a specific version of .vsmodel"""

    @overload
    def __init__(self, vsmodel_version: str):
        ...

    @overload
    def __init__(self, vsmodel_version: System.Version):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelFeatureSet:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelFeatureSet(*_unwrap(None, *args))

    @_staticproperty
    def first_released_vs_model_addon_version_string() -> str:
        """The first released VsModel addon version as string"""
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelFeatureSet.FirstReleasedVsModelAddonVersionString)

    @_staticproperty
    def highest_supported_vs_model_addon_version_string() -> str:
        """Highest supported VsModel addon version as string"""
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelFeatureSet.HighestSupportedVsModelAddonVersionString)

    @property
    def supports_non_virtual_bus(self) -> bool:
        """Indicates whether the vsmodel has support for non virtual buses"""
        return _wrap(self._dotnet_instance.SupportsNonVirtualBus)

    @property
    def generated_using_latest_addon_version(self) -> bool:
        """Indicates whether the vsmodel was built with the latest VsModel addon"""
        return _wrap(self._dotnet_instance.GeneratedUsingLatestAddonVersion)

    @property
    def supports_signals(self) -> bool:
        """Indicates whether the vsmodel has support for signals"""
        return _wrap(self._dotnet_instance.SupportsSignals)


class VsModelItemBaseType(_DotNetBase):
    """Class containing information about a model item type. The item can be input, output or parameter"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelItemBaseType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelItemBaseType(*_unwrap(None, *args))

    @property
    def name(self) -> str:
        """Name of the element"""
        return _wrap(self._dotnet_instance.Name)

    @name.setter
    def name(self, value: str):
        """Name of the element"""
        self._dotnet_instance.Name = next(_unwrap(None, value))

    @property
    def data_type(self) -> str:
        """Model item data type"""
        return _wrap(self._dotnet_instance.DataType)

    @data_type.setter
    def data_type(self, value: str):
        """Model item data type"""
        self._dotnet_instance.DataType = next(_unwrap(None, value))

    @property
    def c_api_type(self) -> str:
        """Type used by Simulink in the generated C code"""
        return _wrap(self._dotnet_instance.CApiType)

    @c_api_type.setter
    def c_api_type(self, value: str):
        """Type used by Simulink in the generated C code"""
        self._dotnet_instance.CApiType = next(_unwrap(None, value))

    @property
    def dimensions(self) -> Any:
        """Model item dimensions"""
        return _wrap(self._dotnet_instance.Dimensions)

    @dimensions.setter
    def dimensions(self, value: Any):
        """Model item dimensions"""
        self._dotnet_instance.Dimensions = next(_unwrap(None, value))

    @property
    def elements(self) -> Sequence[VsModelElement]:
        """Model item elements - has content when the item is Bus"""
        return _wrap(self._dotnet_instance.Elements)

    @elements.setter
    def elements(self, value: Sequence[VsModelElement]):
        """Model item elements - has content when the item is Bus"""
        self._dotnet_instance.Elements = next(_unwrap(None, value))

    @overload
    def is_valid(self) -> bool:
        ...

    def is_valid(self, *args):
        return _wrap(self._dotnet_instance.IsValid(*_unwrap(None, *args)))

    @overload
    def is_supported_fixed_point_type(self) -> bool:
        ...

    def is_supported_fixed_point_type(self, *args):
        return _wrap(self._dotnet_instance.IsSupportedFixedPointType(*_unwrap(None, *args)))

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class VsModelItemType(VsModelItemBaseType):
    """Model item type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelItemType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelItemType(*_unwrap(None, *args))

    @property
    def unit(self) -> str:
        """Model item unit"""
        return _wrap(self._dotnet_instance.Unit)

    @unit.setter
    def unit(self, value: str):
        """Model item unit"""
        self._dotnet_instance.Unit = next(_unwrap(None, value))


class VsModelJsonFileDescriptor(_DotNetBase):
    """Class containing information for deserializing the VsModel descriptor JSON file"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelJsonFileDescriptor:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelJsonFileDescriptor(*_unwrap(None, *args))

    @property
    def version(self) -> str:
        """Model version"""
        return _wrap(self._dotnet_instance.Version)

    @version.setter
    def version(self, value: str):
        """Model version"""
        self._dotnet_instance.Version = next(_unwrap(None, value))

    @property
    def model_name(self) -> str:
        """Model name"""
        return _wrap(self._dotnet_instance.ModelName)

    @model_name.setter
    def model_name(self, value: str):
        """Model name"""
        self._dotnet_instance.ModelName = next(_unwrap(None, value))

    @property
    def metadata(self) -> VsModelMetadata:
        """Model metadata"""
        return _wrap(self._dotnet_instance.Metadata)

    @metadata.setter
    def metadata(self, value: VsModelMetadata):
        """Model metadata"""
        self._dotnet_instance.Metadata = next(_unwrap(None, value))

    @property
    def inports(self) -> Sequence[VsModelInport]:
        """Inport list"""
        return _wrap(self._dotnet_instance.Inports)

    @inports.setter
    def inports(self, value: Sequence[VsModelInport]):
        """Inport list"""
        self._dotnet_instance.Inports = next(_unwrap(None, value))

    @property
    def outports(self) -> Sequence[VsModelOutport]:
        """Outport list"""
        return _wrap(self._dotnet_instance.Outports)

    @outports.setter
    def outports(self, value: Sequence[VsModelOutport]):
        """Outport list"""
        self._dotnet_instance.Outports = next(_unwrap(None, value))

    @property
    def parameters(self) -> Sequence[VsModelParameter]:
        """Parameter list"""
        return _wrap(self._dotnet_instance.Parameters)

    @parameters.setter
    def parameters(self, value: Sequence[VsModelParameter]):
        """Parameter list"""
        self._dotnet_instance.Parameters = next(_unwrap(None, value))

    @property
    def signals(self) -> Sequence[VsModelSignal]:
        """Signals list"""
        return _wrap(self._dotnet_instance.Signals)

    @signals.setter
    def signals(self, value: Sequence[VsModelSignal]):
        """Signals list"""
        self._dotnet_instance.Signals = next(_unwrap(None, value))


class VsModelJsonFileDescriptorUtilities(_DotNetBase):
    """Utility methods for VsModelJsonFileDescriptor"""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelJsonFileDescriptorUtilities:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for VsModelJsonFileDescriptorUtilities")

    @staticmethod
    @overload
    def get_dimensions(dimensions: Any) -> Sequence[int]:
        ...

    def get_dimensions(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelJsonFileDescriptorUtilities.GetDimensions(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def is_scalar(dimensions: Any) -> bool:
        ...

    def is_scalar(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelJsonFileDescriptorUtilities.IsScalar(*_unwrap(None, *args)))


class VsModelMetadata(_DotNetBase):
    """VsModel metadata"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelMetadata:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelMetadata(*_unwrap(None, *args))

    @property
    def slx_file_path(self) -> str:
        """.slx file path"""
        return _wrap(self._dotnet_instance.SLXFilePath)

    @slx_file_path.setter
    def slx_file_path(self, value: str):
        """.slx file path"""
        self._dotnet_instance.SLXFilePath = next(_unwrap(None, value))

    @property
    def simulink_release(self) -> str:
        """Simulink release"""
        return _wrap(self._dotnet_instance.SimulinkRelease)

    @simulink_release.setter
    def simulink_release(self, value: str):
        """Simulink release"""
        self._dotnet_instance.SimulinkRelease = next(_unwrap(None, value))

    @property
    def simulink_version(self) -> str:
        """Simulink version"""
        return _wrap(self._dotnet_instance.SimulinkVersion)

    @simulink_version.setter
    def simulink_version(self, value: str):
        """Simulink version"""
        self._dotnet_instance.SimulinkVersion = next(_unwrap(None, value))

    @property
    def release_description(self) -> str:
        """Simulink release descripton"""
        return _wrap(self._dotnet_instance.ReleaseDescription)

    @release_description.setter
    def release_description(self, value: str):
        """Simulink release descripton"""
        self._dotnet_instance.ReleaseDescription = next(_unwrap(None, value))

    @property
    def author(self) -> str:
        """Model file author"""
        return _wrap(self._dotnet_instance.Author)

    @author.setter
    def author(self, value: str):
        """Model file author"""
        self._dotnet_instance.Author = next(_unwrap(None, value))

    @property
    def description(self) -> str:
        """Model description"""
        return _wrap(self._dotnet_instance.Description)

    @description.setter
    def description(self, value: str):
        """Model description"""
        self._dotnet_instance.Description = next(_unwrap(None, value))

    @property
    def model_version(self) -> str:
        """Model version"""
        return _wrap(self._dotnet_instance.ModelVersion)

    @model_version.setter
    def model_version(self, value: str):
        """Model version"""
        self._dotnet_instance.ModelVersion = next(_unwrap(None, value))

    @property
    def time_step(self) -> str:
        """Model time step"""
        return _wrap(self._dotnet_instance.TimeStep)

    @time_step.setter
    def time_step(self, value: str):
        """Model time step"""
        self._dotnet_instance.TimeStep = next(_unwrap(None, value))

    @property
    def target_platforms(self) -> Sequence[str]:
        """Target platform the model was compiled for"""
        return _wrap(self._dotnet_instance.TargetPlatforms)

    @target_platforms.setter
    def target_platforms(self, value: Sequence[str]):
        """Target platform the model was compiled for"""
        self._dotnet_instance.TargetPlatforms = next(_unwrap(None, value))

    @property
    def bitness(self) -> int:
        """Model bitness"""
        return _wrap(self._dotnet_instance.Bitness)

    @bitness.setter
    def bitness(self, value: int):
        """Model bitness"""
        self._dotnet_instance.Bitness = next(_unwrap(None, value))

    @property
    def number_of_sample_times(self) -> int:
        """Number of sample times"""
        return _wrap(self._dotnet_instance.NumberOfSampleTimes)

    @number_of_sample_times.setter
    def number_of_sample_times(self, value: int):
        """Number of sample times"""
        self._dotnet_instance.NumberOfSampleTimes = next(_unwrap(None, value))

    @property
    def external_mode(self) -> str:
        """External mode setting: on or off"""
        return _wrap(self._dotnet_instance.ExternalMode)

    @external_mode.setter
    def external_mode(self, value: str):
        """External mode setting: on or off"""
        self._dotnet_instance.ExternalMode = next(_unwrap(None, value))


class VsModelParameter(VsModelItemType):
    """Parameter type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelParameter:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelParameter(*_unwrap(None, *args))

    @property
    def default_value(self) -> Any:
        """Default value"""
        return _wrap(self._dotnet_instance.DefaultValue)

    @default_value.setter
    def default_value(self, value: Any):
        """Default value"""
        self._dotnet_instance.DefaultValue = next(_unwrap(None, value))


class VsModelSignal(VsModelItemBaseType):
    """Signal type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelSignal:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelSignal(*_unwrap(None, *args))

    @property
    def block_path(self) -> str:
        """Name of the source block for the signal."""
        return _wrap(self._dotnet_instance.BlockPath)

    @block_path.setter
    def block_path(self, value: str):
        """Name of the source block for the signal."""
        self._dotnet_instance.BlockPath = next(_unwrap(None, value))

    @property
    def port_number(self) -> int:
        """Port number of the block that is the source of the signal."""
        return _wrap(self._dotnet_instance.PortNumber)

    @port_number.setter
    def port_number(self, value: int):
        """Port number of the block that is the source of the signal."""
        self._dotnet_instance.PortNumber = next(_unwrap(None, value))

    @property
    def signal_label(self) -> str:
        """Name of the signal"""
        return _wrap(self._dotnet_instance.SignalLabel)

    @signal_label.setter
    def signal_label(self, value: str):
        """Name of the signal"""
        self._dotnet_instance.SignalLabel = next(_unwrap(None, value))

    @property
    def is_connected_to_virtual_bus(self) -> bool:
        """Whether the signal is connected to a virtual bus."""
        return _wrap(self._dotnet_instance.IsConnectedToVirtualBus)

    @is_connected_to_virtual_bus.setter
    def is_connected_to_virtual_bus(self, value: bool):
        """Whether the signal is connected to a virtual bus."""
        self._dotnet_instance.IsConnectedToVirtualBus = next(_unwrap(None, value))


class VsModelDescriptorExtended(VsModelJsonFileDescriptor, IModelDescriptor):
    """VsModel descriptor containing both information needed for deserialization and other vsmodel properties"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelDescriptorExtended:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelDescriptorExtended(*_unwrap(None, *args))

    @staticmethod
    @overload
    def deserialize_from(stream_reader: System.IO.StreamReader) -> VsModelDescriptorExtended:
        ...

    def deserialize_from(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelDescriptorExtended.DeserializeFrom(*_unwrap(None, *args)))


class VsModelElement(VsModelItemBaseType):
    """Element type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelElement:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelElement(*_unwrap(None, *args))


class VsModelInportOutportType(VsModelItemType):
    """Inport and Outports type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelInportOutportType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelInportOutportType(*_unwrap(None, *args))


class VsModelOutport(VsModelInportOutportType):
    """Outport type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelOutport:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelOutport(*_unwrap(None, *args))

    @property
    def is_connected_to_virtual_bus(self) -> bool:
        """Whether the outport is connected to a virtual bus."""
        return _wrap(self._dotnet_instance.IsConnectedToVirtualBus)

    @is_connected_to_virtual_bus.setter
    def is_connected_to_virtual_bus(self, value: bool):
        """Whether the outport is connected to a virtual bus."""
        self._dotnet_instance.IsConnectedToVirtualBus = next(_unwrap(None, value))


class VsModelInport(VsModelInportOutportType):
    """Inport type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelInport:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelInport(*_unwrap(None, *args))
