"""Module for NationalInstruments.VeriStand.SystemDefinitionAPI."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.SystemDefinitionAPI")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.SystemDefinitionAPI  # type: ignore
import System  # type: ignore

from .. import *
from ..customdevice import *
from ..daqplugin import *
from ..systemstorage import *
from .modelsupport import *


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.systemdefinitionapi.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.systemdefinitionapi.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

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


class AcquisitionMode(_DotNetEnum):
    """Defines the acquisition mode of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.AcquisitionMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for AcquisitionMode")

    @_staticproperty
    def FINITE() -> AcquisitionMode:
        return AcquisitionMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AcquisitionMode, "Finite"), "FINITE")

    @_staticproperty
    def CONTINUOUS() -> AcquisitionMode:
        return AcquisitionMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AcquisitionMode, "Continuous"), "CONTINUOUS")


class AcquisitionUnits(_DotNetEnum):
    """Defines whether the size of acquisitions is represented as samples per channel or time, in seconds."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.AcquisitionUnits:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for AcquisitionUnits")

    @_staticproperty
    def SAMPLES() -> AcquisitionUnits:
        return AcquisitionUnits(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AcquisitionUnits, "Samples"), "SAMPLES")

    @_staticproperty
    def SECONDS() -> AcquisitionUnits:
        return AcquisitionUnits(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AcquisitionUnits, "Seconds"), "SECONDS")


class ActionOnNew(_DotNetEnum):
    """Defines the location to which to log data when a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> begins a new acquisition."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ActionOnNew:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ActionOnNew")

    @_staticproperty
    def NEW_GROUP() -> ActionOnNew:
        return ActionOnNew(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ActionOnNew, "NewGroup"), "NEW_GROUP")

    @_staticproperty
    def NEW_FILE() -> ActionOnNew:
        return ActionOnNew(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ActionOnNew, "NewFile"), "NEW_FILE")


class AlarmMode(_DotNetEnum):
    """The action that occurs when the alarm is triggered on the target."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for AlarmMode")

    @_staticproperty
    def NORMAL() -> AlarmMode:
        return AlarmMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmMode, "Normal"), "NORMAL")

    @_staticproperty
    def INDICATE_ONLY() -> AlarmMode:
        return AlarmMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmMode, "IndicateOnly"), "INDICATE_ONLY")


class AlarmPriority(_DotNetEnum):
    """This enumeration is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this enumeration to Low, Medium, or High automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>"""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmPriority:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for AlarmPriority")

    @_staticproperty
    def LOW() -> AlarmPriority:
        return AlarmPriority(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmPriority, "Low"), "LOW")

    @_staticproperty
    def MEDIUM() -> AlarmPriority:
        return AlarmPriority(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmPriority, "Medium"), "MEDIUM")

    @_staticproperty
    def HIGH() -> AlarmPriority:
        return AlarmPriority(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmPriority, "High"), "HIGH")


class AlarmState(_DotNetEnum):
    """The state of an alarm on the target."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmState:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for AlarmState")

    @_staticproperty
    def DISABLED() -> AlarmState:
        return AlarmState(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmState, "Disabled"), "DISABLED")

    @_staticproperty
    def ENABLED() -> AlarmState:
        return AlarmState(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmState, "Enabled"), "ENABLED")


class AlarmingStepFunction(_DotNetEnum):
    """The function of an alarm running on the target."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for AlarmingStepFunction")

    @_staticproperty
    def ADJUST_SETTINGS() -> AlarmingStepFunction:
        return AlarmingStepFunction(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "AdjustSettings"), "ADJUST_SETTINGS")

    @_staticproperty
    def ENABLE_ALARM() -> AlarmingStepFunction:
        return AlarmingStepFunction(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "EnableAlarm"), "ENABLE_ALARM")

    @_staticproperty
    def DISABLE_ALARM() -> AlarmingStepFunction:
        return AlarmingStepFunction(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "DisableAlarm"), "DISABLE_ALARM")

    @_staticproperty
    def RESET_ALARM_EXIT_SUBROUTINE() -> AlarmingStepFunction:
        return AlarmingStepFunction(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "ResetAlarmExitSubroutine"), "RESET_ALARM_EXIT_SUBROUTINE")

    @_staticproperty
    def DISABLE_ALARM_EXIT_SUBROUTINE() -> AlarmingStepFunction:
        return AlarmingStepFunction(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "DisableAlarmExitSubroutine"), "DISABLE_ALARM_EXIT_SUBROUTINE")

    @_staticproperty
    def RESET_ALARM() -> AlarmingStepFunction:
        return AlarmingStepFunction(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "ResetAlarm"), "RESET_ALARM")


class BaseNode(_DotNetBase):
    """Represents generic nodes in the system definition and provides access to options and configuration settings that all nodes support."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for BaseNode")

    @property
    def base_node_type(self) -> BaseNodeType:
        """Gets a reference to the internal representation of this node."""
        return _wrap(self._dotnet_instance.BaseNodeType)

    @property
    def name(self) -> str:
        """Gets the name of this node. To rename a node, use the <see cref="M:NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode.RenameNode(System.String)" crefType="Unqualified" /> method."""
        return _wrap(self._dotnet_instance.Name)

    @property
    def node_path(self) -> str:
        """Gets the path to the node within the system definition file."""
        return _wrap(self._dotnet_instance.NodePath)

    @property
    def node_id(self) -> int:
        """Gets the ID of this node."""
        return _wrap(self._dotnet_instance.NodeID)

    @property
    def log_file_producer(self) -> bool:
        """Gets a value indicating whether the node is a log file producer"""
        return _wrap(self._dotnet_instance.LogFileProducer)

    @property
    def description(self) -> str:
        """Gets or sets the description of this node."""
        return _wrap(self._dotnet_instance.Description)

    @description.setter
    def description(self, value: str):
        """Gets or sets the description of this node."""
        self._dotnet_instance.Description = next(_unwrap(None, value))

    @property
    def type_guid(self) -> str:
        """Gets the GUID associated with the node.
            Attempts to set the GUID of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode" crefType="Unqualified" /> will generate an exception."""
        return _wrap(self._dotnet_instance.TypeGUID)

    @type_guid.setter
    def type_guid(self, value: str):
        """Gets the GUID associated with the node.
            Attempts to set the GUID of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode" crefType="Unqualified" /> will generate an exception."""
        self._dotnet_instance.TypeGUID = next(_unwrap(None, value))

    @overload
    def get_parent(self) -> Tuple[bool, BaseNode]:
        ...

    def get_parent(self, *args):
        return _wrap(self._dotnet_instance.GetParent(*_unwrap(None, *args)))

    @overload
    def get_children(self) -> Sequence[BaseNode]:
        ...

    def get_children(self, *args):
        return _wrap(self._dotnet_instance.GetChildren(*_unwrap(None, *args)))

    @overload
    def find_children_by_guid(self, type_guid: str) -> Sequence[BaseNode]:
        ...

    def find_children_by_guid(self, *args):
        return _wrap(self._dotnet_instance.FindChildrenByGUID(*_unwrap(None, *args)))

    @overload
    def find_first_child_with_name(self, name: str, deep_hierarchy: bool) -> Tuple[bool, BaseNode]:
        ...

    def find_first_child_with_name(self, *args):
        return _wrap(self._dotnet_instance.FindFirstChildWithName(*_unwrap({None: (1, None)}, *args)))

    @overload
    def find_node_by_path(self, nodepath: str) -> Tuple[bool, BaseNode]:
        ...

    def find_node_by_path(self, *args):
        return _wrap(self._dotnet_instance.FindNodeByPath(*_unwrap(None, *args)))

    @overload
    def get_document_root(self) -> Root:
        ...

    def get_document_root(self, *args):
        return _wrap(self._dotnet_instance.GetDocumentRoot(*_unwrap(None, *args)))

    @overload
    def get_document_path(self) -> str:
        ...

    def get_document_path(self, *args):
        return _wrap(self._dotnet_instance.GetDocumentPath(*_unwrap(None, *args)))

    @overload
    def remove_node(self) -> bool:
        ...

    def remove_node(self, *args):
        return _wrap(self._dotnet_instance.RemoveNode(*_unwrap(None, *args)))

    @overload
    def rename_node(self, new_name: str) -> bool:
        ...

    def rename_node(self, *args):
        return _wrap(self._dotnet_instance.RenameNode(*_unwrap(None, *args)))

    @overload
    def get_node_errors(self):
        ...

    def get_node_errors(self, *args):
        return _wrap(self._dotnet_instance.GetNodeErrors(*_unwrap(None, *args)))

    @overload
    def equals(self, obj: Any) -> bool:
        ...

    def equals(self, *args):
        return _wrap(self._dotnet_instance.Equals(*_unwrap(None, *args)))

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_hash_code(self, *args):
        return _wrap(self._dotnet_instance.GetHashCode(*_unwrap(None, *args)))

    def _custom_repr(self) -> str:
        return f"(name={self.name}, node_path={self.node_path})"


class CANTransceiverType(_DotNetEnum):
    """The transceiver type of an NI-XNET CAN port."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for CANTransceiverType")

    @_staticproperty
    def HS() -> CANTransceiverType:
        return CANTransceiverType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType, "HS"), "HS")

    @_staticproperty
    def LS() -> CANTransceiverType:
        return CANTransceiverType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType, "LS"), "LS")

    @_staticproperty
    def SW() -> CANTransceiverType:
        return CANTransceiverType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType, "SW"), "SW")


class CANTransmitOrderType(_DotNetEnum):
    """The order in which the CAN interface transmits frames from the internal queue."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransmitOrderType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for CANTransmitOrderType")

    @_staticproperty
    def AS_SUBMITTED() -> CANTransmitOrderType:
        return CANTransmitOrderType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransmitOrderType, "AsSubmitted"), "AS_SUBMITTED")

    @_staticproperty
    def BY_IDENTIFIER() -> CANTransmitOrderType:
        return CANTransmitOrderType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransmitOrderType, "ByIdentifier"), "BY_IDENTIFIER")


class CDChannel_Type(_DotNetEnum):
    """Specifies the type (<format type="monospace">Input</format> or <format type="monospace">Output</format>) of a custom device channel."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CDChannel_Type:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for CDChannel_Type")

    @_staticproperty
    def INPUT() -> CDChannel_Type:
        return CDChannel_Type(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDChannel_Type, "Input"), "INPUT")

    @_staticproperty
    def OUTPUT() -> CDChannel_Type:
        return CDChannel_Type(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDChannel_Type, "Output"), "OUTPUT")


class CDDriverExecMode(_DotNetEnum):
    """Specifies the execution mode, or device type, of a custom device. The execution mode defines how the device interacts with the VeriStand Engine."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CDDriverExecMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for CDDriverExecMode")

    @_staticproperty
    def ASYNCHRONOUS() -> CDDriverExecMode:
        return CDDriverExecMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDDriverExecMode, "Asynchronous"), "ASYNCHRONOUS")

    @_staticproperty
    def INLINE_HW_INTERFACE() -> CDDriverExecMode:
        return CDDriverExecMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDDriverExecMode, "InlineHWInterface"), "INLINE_HW_INTERFACE")

    @_staticproperty
    def INLINE_MODEL_INTERFACE() -> CDDriverExecMode:
        return CDDriverExecMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDDriverExecMode, "InlineModelInterface"), "INLINE_MODEL_INTERFACE")

    @_staticproperty
    def INLINE_TIMING_AND_SYNC() -> CDDriverExecMode:
        return CDDriverExecMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDDriverExecMode, "InlineTimingAndSync"), "INLINE_TIMING_AND_SYNC")

    @_staticproperty
    def ASYNCHRONOUS_TIMING_AND_SYNC() -> CDDriverExecMode:
        return CDDriverExecMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDDriverExecMode, "AsynchronousTimingAndSync"), "ASYNCHRONOUS_TIMING_AND_SYNC")


class CDLoopType(_DotNetEnum):
    """Specifies the type of loop in which an asynchronous custom device executes."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CDLoopType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for CDLoopType")

    @_staticproperty
    def WHILE_LOOP() -> CDLoopType:
        return CDLoopType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDLoopType, "WhileLoop"), "WHILE_LOOP")

    @_staticproperty
    def TIMED_LOOP() -> CDLoopType:
        return CDLoopType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDLoopType, "TimedLoop"), "TIMED_LOOP")


class CDTimeLoopPriority(_DotNetEnum):
    """Specifies the priority of the Timed Loop that an asynchronous custom device with a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CDLoopType" crefType="Unqualified" /> of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.CDLoopType.TimedLoop" crefType="Unqualified" /> executes in. If you want to wire this value to the input terminal of a Timed Loop in LabVIEW, you must first convert it to a positive integer between 1 and 65,535."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CDTimeLoopPriority:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for CDTimeLoopPriority")

    @_staticproperty
    def LOW() -> CDTimeLoopPriority:
        return CDTimeLoopPriority(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDTimeLoopPriority, "Low"), "LOW")

    @_staticproperty
    def MEDIUM() -> CDTimeLoopPriority:
        return CDTimeLoopPriority(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDTimeLoopPriority, "Medium"), "MEDIUM")

    @_staticproperty
    def HIGH() -> CDTimeLoopPriority:
        return CDTimeLoopPriority(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDTimeLoopPriority, "High"), "HIGH")


class ChannelNames(_DotNetEnum):
    """Specifies how the names of DAQ channels appear in log files this task creates and in the list of available triggers."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ChannelNames:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ChannelNames")

    @_staticproperty
    def PHYSICAL_CHANNEL() -> ChannelNames:
        return ChannelNames(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ChannelNames, "PhysicalChannel"), "PHYSICAL_CHANNEL")

    @_staticproperty
    def SYSTEM_DEFINITION() -> ChannelNames:
        return ChannelNames(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ChannelNames, "SystemDefinition"), "SYSTEM_DEFINITION")


class ConditionStepComparison(_DotNetEnum):
    """The condition to use when comparing <format type="italics">Variable</format> and <format type="italics">Value</format> in a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Condition" crefType="Unqualified" /> step."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ConditionStepComparison")

    @_staticproperty
    def GREATER() -> ConditionStepComparison:
        return ConditionStepComparison(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "Greater"), "GREATER")

    @_staticproperty
    def LESS() -> ConditionStepComparison:
        return ConditionStepComparison(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "Less"), "LESS")

    @_staticproperty
    def EQUAL() -> ConditionStepComparison:
        return ConditionStepComparison(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "Equal"), "EQUAL")

    @_staticproperty
    def NOT_EQUAL() -> ConditionStepComparison:
        return ConditionStepComparison(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "NotEqual"), "NOT_EQUAL")

    @_staticproperty
    def GREATER_OR_EQUAL() -> ConditionStepComparison:
        return ConditionStepComparison(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "GreaterOrEqual"), "GREATER_OR_EQUAL")

    @_staticproperty
    def LESS_OR_EQUAL() -> ConditionStepComparison:
        return ConditionStepComparison(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "LessOrEqual"), "LESS_OR_EQUAL")


class CustomDeviceBase(BaseNode):
    """Defines a base class for NI VeriStand custom devices."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceBase:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for CustomDeviceBase")

    @overload
    def rename_node(self, new_name: str, force_rename: bool) -> bool:
        ...

    def rename_node(self, *args):
        return _wrap(self._dotnet_instance.RenameNode(*_unwrap(None, *args)))

    @overload
    def get_boolean_property(self, name: str) -> Tuple[bool, bool]:
        ...

    def get_boolean_property(self, *args):
        return _wrap(self._dotnet_instance.GetBooleanProperty(*_unwrap(None, *args)))

    @overload
    def get_u16_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u16_property(self, *args):
        return _wrap(self._dotnet_instance.GetU16Property(*_unwrap(None, *args)))

    @overload
    def get_u32_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u32_property(self, *args):
        return _wrap(self._dotnet_instance.GetU32Property(*_unwrap(None, *args)))

    @overload
    def get_u32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u32_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetU32ArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_u64_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u64_property(self, *args):
        return _wrap(self._dotnet_instance.GetU64Property(*_unwrap(None, *args)))

    @overload
    def get_i32_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i32_property(self, *args):
        return _wrap(self._dotnet_instance.GetI32Property(*_unwrap(None, *args)))

    @overload
    def get_i32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i32_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetI32ArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_double_property(self, name: str) -> Tuple[bool, float]:
        ...

    def get_double_property(self, *args):
        return _wrap(self._dotnet_instance.GetDoubleProperty(*_unwrap(None, *args)))

    @overload
    def get_double_array_property(self, name: str) -> Tuple[bool, Sequence[float]]:
        ...

    def get_double_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetDoubleArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_string_property(self, name: str) -> Tuple[bool, str]:
        ...

    def get_string_property(self, *args):
        return _wrap(self._dotnet_instance.GetStringProperty(*_unwrap(None, *args)))

    @overload
    def get_binary_string_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_binary_string_property(self, *args):
        return _wrap(self._dotnet_instance.GetBinaryStringProperty(*_unwrap(None, *args)))

    @overload
    def get_string_array_property(self, name: str) -> Tuple[bool, Sequence[str]]:
        ...

    def get_string_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetStringArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_dependent_node_property_basenode(self, name: str) -> Tuple[bool, BaseNode]:
        ...

    def get_dependent_node_property_basenode(self, *args):
        for method in NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceBase().GetType().GetMethods():
            if str(method) == 'Boolean GetDependentNodeProperty(System.String, NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode ByRef)':
                params_tuple = tuple(_unwrap({None: (1, None)}, *args))
                # Object[] needed to get out parameters
                params_array = System.Array[System.Object](len(params_tuple))
                for i, param in enumerate(params_tuple):
                    params_array[i] = param
                result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((result, params_array[1]))

    @overload
    def get_dependent_node_property_str(self, name: str) -> Tuple[bool, str]:
        ...

    def get_dependent_node_property_str(self, *args):
        for method in NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceBase().GetType().GetMethods():
            if str(method) == 'Boolean GetDependentNodeProperty(System.String, System.String ByRef)':
                params_tuple = tuple(_unwrap({None: (1, "")}, *args))
                # Object[] needed to get out parameters
                params_array = System.Array[System.Object](len(params_tuple))
                for i, param in enumerate(params_tuple):
                    params_array[i] = param
                result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((result, params_array[1]))

    @overload
    def get_dependent_file_property(self, name: str) -> Tuple[bool, DependentFile]:
        ...

    def get_dependent_file_property(self, *args):
        return _wrap(self._dotnet_instance.GetDependentFileProperty(*_unwrap(None, *args)))

    @overload
    def get_dictionary_property(self, name: str) -> Tuple[bool, Dictionary]:
        ...

    def get_dictionary_property(self, *args):
        return _wrap(self._dotnet_instance.GetDictionaryProperty(*_unwrap(None, *args)))

    @overload
    def get_dictionary_array_property(self, name: str) -> Tuple[bool, Sequence[Dictionary]]:
        ...

    def get_dictionary_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetDictionaryArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_variant_property(self, name: str) -> Tuple[bool, Sequence[int], Sequence[int]]:
        ...

    def get_variant_property(self, *args):
        return _wrap(self._dotnet_instance.GetVariantProperty(*_unwrap(None, *args)))

    @overload
    def set_boolean_property(self, name: str, value: bool) -> bool:
        ...

    def set_boolean_property(self, *args):
        return _wrap(self._dotnet_instance.SetBooleanProperty(*_unwrap(None, *args)))

    @overload
    def set_u16_property(self, name: str, value: int) -> bool:
        ...

    def set_u16_property(self, *args):
        return _wrap(self._dotnet_instance.SetU16Property(*_unwrap(None, *args)))

    @overload
    def set_u32_property(self, name: str, value: int) -> bool:
        ...

    def set_u32_property(self, *args):
        return _wrap(self._dotnet_instance.SetU32Property(*_unwrap(None, *args)))

    @overload
    def set_u32_array_property(self, name: str, value: Sequence[int]) -> bool:
        ...

    def set_u32_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetU32ArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_u64_property(self, name: str, value: int) -> bool:
        ...

    def set_u64_property(self, *args):
        return _wrap(self._dotnet_instance.SetU64Property(*_unwrap(None, *args)))

    @overload
    def set_i32_property(self, name: str, value: int) -> bool:
        ...

    def set_i32_property(self, *args):
        return _wrap(self._dotnet_instance.SetI32Property(*_unwrap(None, *args)))

    @overload
    def set_i32_array_property(self, name: str, value: Sequence[int]) -> bool:
        ...

    def set_i32_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetI32ArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_double_property(self, name: str, value: float) -> bool:
        ...

    def set_double_property(self, *args):
        return _wrap(self._dotnet_instance.SetDoubleProperty(*_unwrap(None, *args)))

    @overload
    def set_double_array_property(self, name: str, value: Sequence[float]) -> bool:
        ...

    def set_double_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetDoubleArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_string_property(self, name: str, value: str) -> bool:
        ...

    def set_string_property(self, *args):
        return _wrap(self._dotnet_instance.SetStringProperty(*_unwrap(None, *args)))

    @overload
    def set_binary_string_property(self, name: str, value: Sequence[int]) -> bool:
        ...

    def set_binary_string_property(self, *args):
        return _wrap(self._dotnet_instance.SetBinaryStringProperty(*_unwrap(None, *args)))

    @overload
    def set_string_array_property(self, name: str, value: Sequence[str]) -> bool:
        ...

    def set_string_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetStringArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_dependent_node_property(self, name: str, value: BaseNode) -> bool:
        ...

    @overload
    def set_dependent_node_property(self, name: str, dep_node_path: str) -> bool:
        ...

    def set_dependent_node_property(self, *args):
        return _wrap(self._dotnet_instance.SetDependentNodeProperty(*_unwrap(None, *args)))

    @overload
    def set_dependent_file_property(self, name: str, value: DependentFile) -> bool:
        ...

    def set_dependent_file_property(self, *args):
        return _wrap(self._dotnet_instance.SetDependentFileProperty(*_unwrap(None, *args)))

    @overload
    def set_dictionary_property(self, name: str, value: Dictionary) -> bool:
        ...

    def set_dictionary_property(self, *args):
        return _wrap(self._dotnet_instance.SetDictionaryProperty(*_unwrap(None, *args)))

    @overload
    def set_dictionary_array_property(self, name: str, value: Sequence[Dictionary]) -> bool:
        ...

    def set_dictionary_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetDictionaryArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_variant_property(self, name: str, type: Sequence[int], value: Sequence[int]) -> bool:
        ...

    def set_variant_property(self, *args):
        return _wrap(self._dotnet_instance.SetVariantProperty(*_unwrap(None, *args)))

    @overload
    def get_property_names(self) -> Sequence[str]:
        ...

    def get_property_names(self, *args):
        return _wrap(self._dotnet_instance.GetPropertyNames(*_unwrap(None, *args)))

    @overload
    def get_property_type(self, property_name: str) -> Tuple[bool, PropertyContent]:
        ...

    def get_property_type(self, *args):
        return _wrap(self._dotnet_instance.GetPropertyType(*_unwrap(None, *args)))

    @overload
    def remove_property(self, name: str) -> bool:
        ...

    def remove_property(self, *args):
        return _wrap(self._dotnet_instance.RemoveProperty(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def move_node_to(self, parent_type: CustomDeviceBase) -> bool:
        ...

    def move_node_to(self, *args):
        return _wrap(self._dotnet_instance.MoveNodeTo(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def remove_error(self, error_id: str):
        ...

    def remove_error(self, *args):
        return _wrap(self._dotnet_instance.RemoveError(*_unwrap(None, *args)))

    @overload
    def report_error(self, error_id: str, is_error: bool, err_code: int, message: str):
        ...

    def report_error(self, *args):
        return _wrap(self._dotnet_instance.ReportError(*_unwrap(None, *args)))

    @overload
    def set_log_file_producer_flag(self, is_log_file_producer: bool):
        ...

    def set_log_file_producer_flag(self, *args):
        return _wrap(self._dotnet_instance.SetLogFileProducerFlag(*_unwrap(None, *args)))


class CustomDeviceSection(CustomDeviceBase):
    """Represents a section under a custom device. Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy."""

    @overload
    def __init__(self, name: str, guid: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceSection:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceSection(*_unwrap(None, *args))

    @overload
    def add_custom_device_section_if_not_found(self, name: str, guid: str) -> Tuple[CustomDeviceSection, bool]:
        ...

    def add_custom_device_section_if_not_found(self, *args):
        return _wrap(self._dotnet_instance.AddCustomDeviceSectionIfNotFound(*_unwrap(None, *args)))

    @overload
    def add_custom_device_channel_if_not_found(self, name: str, guid: str) -> Tuple[CustomDeviceChannel, bool]:
        ...

    def add_custom_device_channel_if_not_found(self, *args):
        return _wrap(self._dotnet_instance.AddCustomDeviceChannelIfNotFound(*_unwrap(None, *args)))

    @overload
    def add_custom_device_waveform_if_not_found(self, name: str, guid: str, data_type: WaveformTypeDataType) -> Tuple[CustomDeviceWaveform, bool]:
        ...

    def add_custom_device_waveform_if_not_found(self, *args):
        return _wrap(self._dotnet_instance.AddCustomDeviceWaveformIfNotFound(*_unwrap(None, *args)))

    @overload
    def add_output_underflow_count_channel(self, name: str) -> CustomDeviceChannel:
        ...

    def add_output_underflow_count_channel(self, *args):
        return _wrap(self._dotnet_instance.AddOutputUnderflowCountChannel(*_unwrap(None, *args)))

    @overload
    def add_input_overflow_count_channel(self, name: str) -> CustomDeviceChannel:
        ...

    def add_input_overflow_count_channel(self, *args):
        return _wrap(self._dotnet_instance.AddInputOverflowCountChannel(*_unwrap(None, *args)))

    @overload
    def add_error_channel(self, name: str) -> CustomDeviceChannel:
        ...

    def add_error_channel(self, *args):
        return _wrap(self._dotnet_instance.AddErrorChannel(*_unwrap(None, *args)))


class CustomDeviceWaveform(CustomDeviceBase):
    """Represents a waveform in a custom device."""

    @overload
    def __init__(self, name: str, guid: str, data_type: WaveformTypeDataType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceWaveform:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceWaveform(*_unwrap(None, *args))

    @property
    def units(self) -> str:
        """Gets or sets the units associated with a CustomDeviceWaveform. Units can be any string that makes sense for your custom device."""
        return _wrap(self._dotnet_instance.Units)

    @units.setter
    def units(self, value: str):
        """Gets or sets the units associated with a CustomDeviceWaveform. Units can be any string that makes sense for your custom device."""
        self._dotnet_instance.Units = next(_unwrap(None, value))

    @property
    def data_type(self) -> WaveformTypeDataType:
        """Gets or sets the data type associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceWaveform" /> class."""
        return _wrap(self._dotnet_instance.DataType)

    @data_type.setter
    def data_type(self, value: WaveformTypeDataType):
        """Gets or sets the data type associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceWaveform" /> class."""
        self._dotnet_instance.DataType = next(_unwrap(None, value))


class DAQAnalogChannelType(_DotNetEnum):
    """Specifies the measurement type of an analog DAQ channel."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogChannelType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQAnalogChannelType")

    @_staticproperty
    def VOLTAGE() -> DAQAnalogChannelType:
        return DAQAnalogChannelType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogChannelType, "Voltage"), "VOLTAGE")

    @_staticproperty
    def CURRENT() -> DAQAnalogChannelType:
        return DAQAnalogChannelType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogChannelType, "Current"), "CURRENT")

    @_staticproperty
    def OTHER() -> DAQAnalogChannelType:
        return DAQAnalogChannelType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogChannelType, "Other"), "OTHER")


class DAQCM_Active_Edge(_DotNetEnum):
    """Specifies the edge on which the sample clock pulses to acquire or generate samples."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Active_Edge:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCM_Active_Edge")

    @_staticproperty
    def RISING() -> DAQCM_Active_Edge:
        return DAQCM_Active_Edge(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Active_Edge, "Rising"), "RISING")

    @_staticproperty
    def FALLING() -> DAQCM_Active_Edge:
        return DAQCM_Active_Edge(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Active_Edge, "Falling"), "FALLING")


class DAQCM_Clock_Source(_DotNetEnum):
    """Specifies the source of the sample clock."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCM_Clock_Source")

    @_staticproperty
    def ONBOARD10_M_HZ_CLOCK() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "Onboard10MHzClock"), "ONBOARD10_M_HZ_CLOCK")

    @_staticproperty
    def PFI_0() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_0"), "PFI_0")

    @_staticproperty
    def PFI_1() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_1"), "PFI_1")

    @_staticproperty
    def PFI_2() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_2"), "PFI_2")

    @_staticproperty
    def PFI_3() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_3"), "PFI_3")

    @_staticproperty
    def PFI_4() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_4"), "PFI_4")

    @_staticproperty
    def PFI_5() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_5"), "PFI_5")

    @_staticproperty
    def PFI_6() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_6"), "PFI_6")

    @_staticproperty
    def PFI_7() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_7"), "PFI_7")

    @_staticproperty
    def PFI_8() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_8"), "PFI_8")

    @_staticproperty
    def PFI_9() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_9"), "PFI_9")

    @_staticproperty
    def PFI_10() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_10"), "PFI_10")

    @_staticproperty
    def PFI_11() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_11"), "PFI_11")

    @_staticproperty
    def PFI_12() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_12"), "PFI_12")

    @_staticproperty
    def PFI_13() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_13"), "PFI_13")

    @_staticproperty
    def PFI_14() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_14"), "PFI_14")

    @_staticproperty
    def PFI_15() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_15"), "PFI_15")

    @_staticproperty
    def RTSI_PXI_TRIG_0() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_0"), "RTSI_PXI_TRIG_0")

    @_staticproperty
    def RTSI_PXI_TRIG_1() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_1"), "RTSI_PXI_TRIG_1")

    @_staticproperty
    def RTSI_PXI_TRIG_2() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_2"), "RTSI_PXI_TRIG_2")

    @_staticproperty
    def RTSI_PXI_TRIG_3() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_3"), "RTSI_PXI_TRIG_3")

    @_staticproperty
    def RTSI_PXI_TRIG_4() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_4"), "RTSI_PXI_TRIG_4")

    @_staticproperty
    def RTSI_PXI_TRIG_5() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_5"), "RTSI_PXI_TRIG_5")

    @_staticproperty
    def RTSI_PXI_TRIG_6() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_6"), "RTSI_PXI_TRIG_6")

    @_staticproperty
    def RTSI_PXI_TRIG_7() -> DAQCM_Clock_Source:
        return DAQCM_Clock_Source(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_7"), "RTSI_PXI_TRIG_7")


class DAQCM_Export_Clk_On_Line(_DotNetEnum):
    """Specifies the line that receives the pulse from the sample clock."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCM_Export_Clk_On_Line")

    @_staticproperty
    def DEFAULT_RTSI_PXI_TRIG_0() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "Default_RTSI_PXI_TRIG_0"), "DEFAULT_RTSI_PXI_TRIG_0")

    @_staticproperty
    def PFI_0() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_0"), "PFI_0")

    @_staticproperty
    def PFI_1() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_1"), "PFI_1")

    @_staticproperty
    def PFI_2() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_2"), "PFI_2")

    @_staticproperty
    def PFI_3() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_3"), "PFI_3")

    @_staticproperty
    def PFI_4() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_4"), "PFI_4")

    @_staticproperty
    def PFI_5() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_5"), "PFI_5")

    @_staticproperty
    def PFI_6() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_6"), "PFI_6")

    @_staticproperty
    def PFI_7() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_7"), "PFI_7")

    @_staticproperty
    def PFI_8() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_8"), "PFI_8")

    @_staticproperty
    def PFI_9() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_9"), "PFI_9")

    @_staticproperty
    def PFI_10() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_10"), "PFI_10")

    @_staticproperty
    def PFI_11() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_11"), "PFI_11")

    @_staticproperty
    def PFI_12() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_12"), "PFI_12")

    @_staticproperty
    def PFI_13() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_13"), "PFI_13")

    @_staticproperty
    def PFI_14() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_14"), "PFI_14")

    @_staticproperty
    def PFI_15() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_15"), "PFI_15")

    @_staticproperty
    def RTSI_PXI_TRIG_0() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_0"), "RTSI_PXI_TRIG_0")

    @_staticproperty
    def RTSI_PXI_TRIG_1() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_1"), "RTSI_PXI_TRIG_1")

    @_staticproperty
    def RTSI_PXI_TRIG_2() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_2"), "RTSI_PXI_TRIG_2")

    @_staticproperty
    def RTSI_PXI_TRIG_3() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_3"), "RTSI_PXI_TRIG_3")

    @_staticproperty
    def RTSI_PXI_TRIG_4() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_4"), "RTSI_PXI_TRIG_4")

    @_staticproperty
    def RTSI_PXI_TRIG_5() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_5"), "RTSI_PXI_TRIG_5")

    @_staticproperty
    def RTSI_PXI_TRIG_6() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_6"), "RTSI_PXI_TRIG_6")

    @_staticproperty
    def RTSI_PXI_TRIG_7() -> DAQCM_Export_Clk_On_Line:
        return DAQCM_Export_Clk_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_7"), "RTSI_PXI_TRIG_7")


class DAQCM_Export_Sample_Clock(_DotNetEnum):
    """Specifies the sample clock to export."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Sample_Clock:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCM_Export_Sample_Clock")

    @_staticproperty
    def AI_SAMPLE_CLOCK() -> DAQCM_Export_Sample_Clock:
        return DAQCM_Export_Sample_Clock(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Sample_Clock, "aiSampleClock"), "AI_SAMPLE_CLOCK")

    @_staticproperty
    def AO_SAMPLE_CLOCK() -> DAQCM_Export_Sample_Clock:
        return DAQCM_Export_Sample_Clock(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Sample_Clock, "aoSampleClock"), "AO_SAMPLE_CLOCK")


class DAQCM_Export_StartTrigger_On_Line(_DotNetEnum):
    """Specifies the line that exports the Start Trigger."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCM_Export_StartTrigger_On_Line")

    @_staticproperty
    def NONE() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "None"), "NONE")

    @_staticproperty
    def PFI_0() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_0"), "PFI_0")

    @_staticproperty
    def PFI_1() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_1"), "PFI_1")

    @_staticproperty
    def PFI_2() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_2"), "PFI_2")

    @_staticproperty
    def PFI_3() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_3"), "PFI_3")

    @_staticproperty
    def PFI_4() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_4"), "PFI_4")

    @_staticproperty
    def PFI_5() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_5"), "PFI_5")

    @_staticproperty
    def PFI_6() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_6"), "PFI_6")

    @_staticproperty
    def PFI_7() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_7"), "PFI_7")

    @_staticproperty
    def PFI_8() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_8"), "PFI_8")

    @_staticproperty
    def PFI_9() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_9"), "PFI_9")

    @_staticproperty
    def PFI_10() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_10"), "PFI_10")

    @_staticproperty
    def PFI_11() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_11"), "PFI_11")

    @_staticproperty
    def PFI_12() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_12"), "PFI_12")

    @_staticproperty
    def PFI_13() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_13"), "PFI_13")

    @_staticproperty
    def PFI_14() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_14"), "PFI_14")

    @_staticproperty
    def PFI_15() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_15"), "PFI_15")

    @_staticproperty
    def RTSI_PXI_TRIG_0() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_0"), "RTSI_PXI_TRIG_0")

    @_staticproperty
    def RTSI_PXI_TRIG_1() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_1"), "RTSI_PXI_TRIG_1")

    @_staticproperty
    def RTSI_PXI_TRIG_2() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_2"), "RTSI_PXI_TRIG_2")

    @_staticproperty
    def RTSI_PXI_TRIG_3() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_3"), "RTSI_PXI_TRIG_3")

    @_staticproperty
    def RTSI_PXI_TRIG_4() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_4"), "RTSI_PXI_TRIG_4")

    @_staticproperty
    def RTSI_PXI_TRIG_5() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_5"), "RTSI_PXI_TRIG_5")

    @_staticproperty
    def RTSI_PXI_TRIG_6() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_6"), "RTSI_PXI_TRIG_6")

    @_staticproperty
    def RTSI_PXI_TRIG_7() -> DAQCM_Export_StartTrigger_On_Line:
        return DAQCM_Export_StartTrigger_On_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_7"), "RTSI_PXI_TRIG_7")


class DAQCM_Export_Start_Trigger(_DotNetEnum):
    """Specifies the start trigger to export."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Start_Trigger:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCM_Export_Start_Trigger")

    @_staticproperty
    def AI_START_TRIGGER() -> DAQCM_Export_Start_Trigger:
        return DAQCM_Export_Start_Trigger(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Start_Trigger, "aiStartTrigger"), "AI_START_TRIGGER")

    @_staticproperty
    def AO_START_TRIGGER() -> DAQCM_Export_Start_Trigger:
        return DAQCM_Export_Start_Trigger(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Start_Trigger, "aoStartTrigger"), "AO_START_TRIGGER")


class DAQCM_Slope(_DotNetEnum):
    """Specifies the edge on which to trigger the device."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Slope:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCM_Slope")

    @_staticproperty
    def RISING() -> DAQCM_Slope:
        return DAQCM_Slope(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Slope, "Rising"), "RISING")

    @_staticproperty
    def FALLING() -> DAQCM_Slope:
        return DAQCM_Slope(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Slope, "Falling"), "FALLING")


class DAQCM_Trigger_Line(_DotNetEnum):
    """Specifies the line that triggers the acquisition or generation of samples."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCM_Trigger_Line")

    @_staticproperty
    def NONE() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "None"), "NONE")

    @_staticproperty
    def PFI_0() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_0"), "PFI_0")

    @_staticproperty
    def PFI_1() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_1"), "PFI_1")

    @_staticproperty
    def PFI_2() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_2"), "PFI_2")

    @_staticproperty
    def PFI_3() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_3"), "PFI_3")

    @_staticproperty
    def PFI_4() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_4"), "PFI_4")

    @_staticproperty
    def PFI_5() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_5"), "PFI_5")

    @_staticproperty
    def PFI_6() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_6"), "PFI_6")

    @_staticproperty
    def PFI_7() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_7"), "PFI_7")

    @_staticproperty
    def PFI_8() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_8"), "PFI_8")

    @_staticproperty
    def PFI_9() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_9"), "PFI_9")

    @_staticproperty
    def PFI_10() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_10"), "PFI_10")

    @_staticproperty
    def PFI_11() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_11"), "PFI_11")

    @_staticproperty
    def PFI_12() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_12"), "PFI_12")

    @_staticproperty
    def PFI_13() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_13"), "PFI_13")

    @_staticproperty
    def PFI_14() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_14"), "PFI_14")

    @_staticproperty
    def PFI_15() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_15"), "PFI_15")

    @_staticproperty
    def RTSI_PXI_TRIG_0() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_0"), "RTSI_PXI_TRIG_0")

    @_staticproperty
    def RTSI_PXI_TRIG_1() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_1"), "RTSI_PXI_TRIG_1")

    @_staticproperty
    def RTSI_PXI_TRIG_2() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_2"), "RTSI_PXI_TRIG_2")

    @_staticproperty
    def RTSI_PXI_TRIG_3() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_3"), "RTSI_PXI_TRIG_3")

    @_staticproperty
    def RTSI_PXI_TRIG_4() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_4"), "RTSI_PXI_TRIG_4")

    @_staticproperty
    def RTSI_PXI_TRIG_5() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_5"), "RTSI_PXI_TRIG_5")

    @_staticproperty
    def RTSI_PXI_TRIG_6() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_6"), "RTSI_PXI_TRIG_6")

    @_staticproperty
    def RTSI_PXI_TRIG_7() -> DAQCM_Trigger_Line:
        return DAQCM_Trigger_Line(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_7"), "RTSI_PXI_TRIG_7")


class DAQConversionRate(_DotNetEnum):
    """Specifies the rate used to run the analog-digital converters (ADCs) on a DAQ device."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQConversionRate:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQConversionRate")

    @_staticproperty
    def DEFAULT() -> DAQConversionRate:
        return DAQConversionRate(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQConversionRate, "Default"), "DEFAULT")

    @_staticproperty
    def MAXIMUM() -> DAQConversionRate:
        return DAQConversionRate(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQConversionRate, "Maximum"), "MAXIMUM")


class DAQCounterCountMode(_DotNetEnum):
    """Specifies the mode of the count direction."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterCountMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCounterCountMode")

    @_staticproperty
    def UP() -> DAQCounterCountMode:
        return DAQCounterCountMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterCountMode, "Up"), "UP")

    @_staticproperty
    def DOWN() -> DAQCounterCountMode:
        return DAQCounterCountMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterCountMode, "Down"), "DOWN")

    @_staticproperty
    def EXTERNALLY_CONTROLLED() -> DAQCounterCountMode:
        return DAQCounterCountMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterCountMode, "ExternallyControlled"), "EXTERNALLY_CONTROLLED")


class DAQCounterDecoding(_DotNetEnum):
    """Specifies the method used to count and interpret the pulses the encoder generates on signal A and signal B. <format type="bold">Decoding1X</format>, <format type="bold">Decoding2X</format>, and <format type="bold">Decoding4X</format> are valid for quadrature encoders only."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterDecoding:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCounterDecoding")

    @_staticproperty
    def DECODING1_X() -> DAQCounterDecoding:
        return DAQCounterDecoding(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterDecoding, "Decoding1X"), "DECODING1_X")

    @_staticproperty
    def DECODING2_X() -> DAQCounterDecoding:
        return DAQCounterDecoding(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterDecoding, "Decoding2X"), "DECODING2_X")

    @_staticproperty
    def DECODING4_X() -> DAQCounterDecoding:
        return DAQCounterDecoding(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterDecoding, "Decoding4X"), "DECODING4_X")

    @_staticproperty
    def DECODING_PULSE_COUNTING() -> DAQCounterDecoding:
        return DAQCounterDecoding(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterDecoding, "DecodingPulseCounting"), "DECODING_PULSE_COUNTING")


class DAQCounterEdge(_DotNetEnum):
    """Specifies the mode the counter uses to count the edge."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterEdge:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCounterEdge")

    @_staticproperty
    def FALLING() -> DAQCounterEdge:
        return DAQCounterEdge(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterEdge, "Falling"), "FALLING")

    @_staticproperty
    def RISING() -> DAQCounterEdge:
        return DAQCounterEdge(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterEdge, "Rising"), "RISING")


class DAQCounterType(_DotNetEnum):
    """Specifies the type of task the DAQ counter performs."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCounterType")

    @_staticproperty
    def FREQUENCY_MEASUREMENT() -> DAQCounterType:
        return DAQCounterType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterType, "FrequencyMeasurement"), "FREQUENCY_MEASUREMENT")

    @_staticproperty
    def PERIOD_MEASUREMENT() -> DAQCounterType:
        return DAQCounterType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterType, "PeriodMeasurement"), "PERIOD_MEASUREMENT")

    @_staticproperty
    def COUNT_UP_DOWN() -> DAQCounterType:
        return DAQCounterType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterType, "CountUpDown"), "COUNT_UP_DOWN")

    @_staticproperty
    def POSITION_MEASUREMENT() -> DAQCounterType:
        return DAQCounterType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterType, "PositionMeasurement"), "POSITION_MEASUREMENT")

    @_staticproperty
    def OTHER() -> DAQCounterType:
        return DAQCounterType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterType, "Other"), "OTHER")


class DAQCounterZIndexMode(_DotNetEnum):
    """Specifies the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than <format type="bold">AHighBHigh</format>. When signal Z transitions to high and how long it stays high varies from encoder to encoder. Refer to the documentation for the encoder to determine the timing of signal Z with respect to signal A and signal B."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterZIndexMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQCounterZIndexMode")

    @_staticproperty
    def A_HIGH_B_HIGH() -> DAQCounterZIndexMode:
        return DAQCounterZIndexMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterZIndexMode, "AHighBHigh"), "A_HIGH_B_HIGH")

    @_staticproperty
    def A_HIGH_B_LOW() -> DAQCounterZIndexMode:
        return DAQCounterZIndexMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterZIndexMode, "AHighBLow"), "A_HIGH_B_LOW")

    @_staticproperty
    def A_LOW_B_HIGH() -> DAQCounterZIndexMode:
        return DAQCounterZIndexMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterZIndexMode, "ALowBHigh"), "A_LOW_B_HIGH")

    @_staticproperty
    def A_LOW_B_LOW() -> DAQCounterZIndexMode:
        return DAQCounterZIndexMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterZIndexMode, "ALowBLow"), "A_LOW_B_LOW")


class DAQDataChannelType(_DotNetEnum):
    """Specifies the type of data channel in a DAQ measurement <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQSectionType" /> section."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDataChannelType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQDataChannelType")

    @_staticproperty
    def FREQUENCY() -> DAQDataChannelType:
        return DAQDataChannelType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDataChannelType, "Frequency"), "FREQUENCY")

    @_staticproperty
    def DUTY_CYCLE() -> DAQDataChannelType:
        return DAQDataChannelType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDataChannelType, "DutyCycle"), "DUTY_CYCLE")


class DAQDeviceInputConfiguration(_DotNetEnum):
    """Specifies the input terminal configuration to apply to the device channels."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfiguration:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQDeviceInputConfiguration")

    @_staticproperty
    def DEFAULT() -> DAQDeviceInputConfiguration:
        return DAQDeviceInputConfiguration(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfiguration, "Default"), "DEFAULT")

    @_staticproperty
    def RSE() -> DAQDeviceInputConfiguration:
        return DAQDeviceInputConfiguration(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfiguration, "RSE"), "RSE")

    @_staticproperty
    def NRSE() -> DAQDeviceInputConfiguration:
        return DAQDeviceInputConfiguration(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfiguration, "NRSE"), "NRSE")

    @_staticproperty
    def DIFFERENTIAL() -> DAQDeviceInputConfiguration:
        return DAQDeviceInputConfiguration(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfiguration, "Differential"), "DIFFERENTIAL")

    @_staticproperty
    def PSEUDODIFFERENTIAL() -> DAQDeviceInputConfiguration:
        return DAQDeviceInputConfiguration(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfiguration, "Pseudodifferential"), "PSEUDODIFFERENTIAL")


class DAQMeasurementType(_DotNetEnum):
    """Specifies the measurement type of a DAQ channel."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DAQMeasurementType")

    @_staticproperty
    def ANALOG_INPUT_VOLTAGE() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputVoltage"), "ANALOG_INPUT_VOLTAGE")

    @_staticproperty
    def ANALOG_INPUT_CURRENT() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputCurrent"), "ANALOG_INPUT_CURRENT")

    @_staticproperty
    def ANALOG_INPUT_TEMPERATURE_THERMOCOUPLE() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputTemperatureThermocouple"), "ANALOG_INPUT_TEMPERATURE_THERMOCOUPLE")

    @_staticproperty
    def ANALOG_INPUT_TEMPERATURE_THERMISTOR_VEX() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputTemperatureThermistorVex"), "ANALOG_INPUT_TEMPERATURE_THERMISTOR_VEX")

    @_staticproperty
    def ANALOG_INPUT_TEMPERATURE_THERMISTOR_IEX() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputTemperatureThermistorIex"), "ANALOG_INPUT_TEMPERATURE_THERMISTOR_IEX")

    @_staticproperty
    def ANALOG_INPUT_TEMPERATURE_RTD() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputTemperatureRTD"), "ANALOG_INPUT_TEMPERATURE_RTD")

    @_staticproperty
    def ANALOG_INPUT_STRAIN_GAGE() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputStrainGage"), "ANALOG_INPUT_STRAIN_GAGE")

    @_staticproperty
    def ANALOG_INPUT_ACCELEROMETER() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputAccelerometer"), "ANALOG_INPUT_ACCELEROMETER")

    @_staticproperty
    def ANALOG_INPUT_BRIDGE() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputBridge"), "ANALOG_INPUT_BRIDGE")

    @_staticproperty
    def ANALOG_INPUT_FORCE() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputForce"), "ANALOG_INPUT_FORCE")

    @_staticproperty
    def ANALOG_INPUT_PRESSURE() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputPressure"), "ANALOG_INPUT_PRESSURE")

    @_staticproperty
    def ANALOG_INPUT_TORQUE() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputTorque"), "ANALOG_INPUT_TORQUE")

    @_staticproperty
    def ANALOG_INPUT_POSITION_LVDT() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputPositionLVDT"), "ANALOG_INPUT_POSITION_LVDT")

    @_staticproperty
    def ANALOG_INPUT_POSITION_RVDT() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputPositionRVDT"), "ANALOG_INPUT_POSITION_RVDT")

    @_staticproperty
    def ANALOG_OUTPUT_VOLTAGE() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogOutputVoltage"), "ANALOG_OUTPUT_VOLTAGE")

    @_staticproperty
    def ANALOG_OUTPUT_CURRENT() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogOutputCurrent"), "ANALOG_OUTPUT_CURRENT")

    @_staticproperty
    def DIGITAL_INPUT() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "DigitalInput"), "DIGITAL_INPUT")

    @_staticproperty
    def DIGITAL_OUTPUT() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "DigitalOutput"), "DIGITAL_OUTPUT")

    @_staticproperty
    def COUNTER_INPUT_COUNT_EDGES() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterInputCountEdges"), "COUNTER_INPUT_COUNT_EDGES")

    @_staticproperty
    def COUNTER_INPUT_FREQUENCY() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterInputFrequency"), "COUNTER_INPUT_FREQUENCY")

    @_staticproperty
    def COUNTER_INPUT_PERIOD() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterInputPeriod"), "COUNTER_INPUT_PERIOD")

    @_staticproperty
    def COUNTER_INPUT_POSITION_LINEAR_ENCODER() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterInputPositionLinearEncoder"), "COUNTER_INPUT_POSITION_LINEAR_ENCODER")

    @_staticproperty
    def COUNTER_INPUT_PULSE_MEASUREMENT() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterInputPulseMeasurement"), "COUNTER_INPUT_PULSE_MEASUREMENT")

    @_staticproperty
    def COUNTER_OUTPUT_PULSE_GENERATION() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterOutputPulseGeneration"), "COUNTER_OUTPUT_PULSE_GENERATION")

    @_staticproperty
    def USER_DEFINED() -> DAQMeasurementType:
        return DAQMeasurementType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "UserDefined"), "USER_DEFINED")


class DAQTrigger(_DotNetBase):
    """Provides an <see langword="abstract" /> base class for different types of triggers you can use to configure a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> to start acquiring under certain conditions."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQTrigger")

    @property
    def trigger_type(self) -> TriggerType:
        """Gets the type of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" />."""
        return _wrap(self._dotnet_instance.TriggerType)


class DAQTriggerAnalogEdge(DAQTrigger):
    """Represents an analog edge trigger that can configure a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> to start acquiring under certain conditions."""

    @overload
    def __init__(self, source: str, slope: DirectionType, level: float):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge(*_unwrap(None, *args))

    @property
    def source(self) -> str:
        """Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger."""
        return _wrap(self._dotnet_instance.Source)

    @source.setter
    def source(self, value: str):
        """Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger."""
        self._dotnet_instance.Source = next(_unwrap(None, value))

    @property
    def slope(self) -> DirectionType:
        """Gets or sets the direction of a signal slope that causes a trigger when the signal crosses the threshold <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Level" />."""
        return _wrap(self._dotnet_instance.Slope)

    @slope.setter
    def slope(self, value: DirectionType):
        """Gets or sets the direction of a signal slope that causes a trigger when the signal crosses the threshold <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Level" />."""
        self._dotnet_instance.Slope = next(_unwrap(None, value))

    @property
    def level(self) -> float:
        """Gets or sets the threshold value, in the units of the measurement, at which to start acquiring samples. Set the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Slope" /> to specify on which type of slope this level causes the task to start acquiring data."""
        return _wrap(self._dotnet_instance.Level)

    @level.setter
    def level(self, value: float):
        """Gets or sets the threshold value, in the units of the measurement, at which to start acquiring samples. Set the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Slope" /> to specify on which type of slope this level causes the task to start acquiring data."""
        self._dotnet_instance.Level = next(_unwrap(None, value))


class DAQTriggerAnalogWindow(DAQTrigger):
    """Represents an analog window trigger that can configure a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> to start acquiring under certain conditions."""

    @overload
    def __init__(self, source: str, window_top: float, window_bottom: float, window_condition: WindowConditionType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow(*_unwrap(None, *args))

    @property
    def source(self) -> str:
        """Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger."""
        return _wrap(self._dotnet_instance.Source)

    @source.setter
    def source(self, value: str):
        """Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger."""
        self._dotnet_instance.Source = next(_unwrap(None, value))

    @property
    def window_condition(self) -> WindowConditionType:
        """Gets or sets whether the task starts acquiring samples when the signal enters the window between <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowBottom" /> and <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowTop" /> or when it leaves the window."""
        return _wrap(self._dotnet_instance.WindowCondition)

    @window_condition.setter
    def window_condition(self, value: WindowConditionType):
        """Gets or sets whether the task starts acquiring samples when the signal enters the window between <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowBottom" /> and <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowTop" /> or when it leaves the window."""
        self._dotnet_instance.WindowCondition = next(_unwrap(None, value))

    @property
    def window_top(self) -> float:
        """Gets or sets the upper limit of the window, in the units of the measurement."""
        return _wrap(self._dotnet_instance.WindowTop)

    @window_top.setter
    def window_top(self, value: float):
        """Gets or sets the upper limit of the window, in the units of the measurement."""
        self._dotnet_instance.WindowTop = next(_unwrap(None, value))

    @property
    def window_bottom(self) -> float:
        """Gets or sets the lower limit of the window, in the units of the measurement."""
        return _wrap(self._dotnet_instance.WindowBottom)

    @window_bottom.setter
    def window_bottom(self, value: float):
        """Gets or sets the lower limit of the window, in the units of the measurement."""
        self._dotnet_instance.WindowBottom = next(_unwrap(None, value))


class DAQTriggerDigitalEdge(DAQTrigger):
    """Represents a digital edge trigger that can configure a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> to start acquiring under certain conditions."""

    @overload
    def __init__(self, source: str, edge: DirectionType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerDigitalEdge:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerDigitalEdge(*_unwrap(None, *args))

    @property
    def source(self) -> str:
        """Gets or sets the name of a terminal that is the source of the digital signal used as the trigger."""
        return _wrap(self._dotnet_instance.Source)

    @source.setter
    def source(self, value: str):
        """Gets or sets the name of a terminal that is the source of the digital signal used as the trigger."""
        self._dotnet_instance.Source = next(_unwrap(None, value))

    @property
    def edge(self) -> DirectionType:
        """Gets or sets on which type of edge of the digital signal to start acquiring samples."""
        return _wrap(self._dotnet_instance.Edge)

    @edge.setter
    def edge(self, value: DirectionType):
        """Gets or sets on which type of edge of the digital signal to start acquiring samples."""
        self._dotnet_instance.Edge = next(_unwrap(None, value))


class DAQTriggerNone(DAQTrigger):
    """Represents a disabled <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" />."""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerNone:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerNone(*_unwrap(None, *args))


class DAQTriggerSoftware(DAQTrigger):
    """Represents a software trigger that can configure a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> to start acquiring under certain conditions."""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerSoftware:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerSoftware(*_unwrap(None, *args))


class DataLoggingFilterType(_DotNetEnum):
    """Specifies the type of filtering applied to a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" /> under an NI-XNET port."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFilterType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DataLoggingFilterType")

    @_staticproperty
    def LOG_ENTIRE_BUS_TRAFFIC() -> DataLoggingFilterType:
        return DataLoggingFilterType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFilterType, "LogEntireBusTraffic"), "LOG_ENTIRE_BUS_TRAFFIC")

    @_staticproperty
    def EXCLUDE_FRAME_I_DS() -> DataLoggingFilterType:
        return DataLoggingFilterType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFilterType, "ExcludeFrameIDs"), "EXCLUDE_FRAME_I_DS")

    @_staticproperty
    def INCLUDE_FRAME_I_DS() -> DataLoggingFilterType:
        return DataLoggingFilterType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFilterType, "IncludeFrameIDs"), "INCLUDE_FRAME_I_DS")


class DataLoggingOperationType(_DotNetEnum):
    """Specifies the action taken when a trigger condition is met."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingOperationType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DataLoggingOperationType")

    @_staticproperty
    def CONTINUE_LOGGING_IN_NEW_FILE() -> DataLoggingOperationType:
        return DataLoggingOperationType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingOperationType, "ContinueLoggingInNewFile"), "CONTINUE_LOGGING_IN_NEW_FILE")

    @_staticproperty
    def STOP_LOGGING() -> DataLoggingOperationType:
        return DataLoggingOperationType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingOperationType, "StopLogging"), "STOP_LOGGING")


class DataLoggingTriggerType(_DotNetEnum):
    """Specifies the type of trigger used to start or stop logging data to a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingTriggerType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DataLoggingTriggerType")

    @_staticproperty
    def START_LOGGING_ON_NON_ZERO() -> DataLoggingTriggerType:
        return DataLoggingTriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingTriggerType, "StartLoggingOnNonZero"), "START_LOGGING_ON_NON_ZERO")

    @_staticproperty
    def START_LOGGING_ON_ZERO() -> DataLoggingTriggerType:
        return DataLoggingTriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingTriggerType, "StartLoggingOnZero"), "START_LOGGING_ON_ZERO")

    @_staticproperty
    def ENABLE_LOGGING_WHEN_TRIGGER_IS_ZERO() -> DataLoggingTriggerType:
        return DataLoggingTriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingTriggerType, "EnableLoggingWhenTriggerIsZero"), "ENABLE_LOGGING_WHEN_TRIGGER_IS_ZERO")

    @_staticproperty
    def ENABLE_LOGGING_WHEN_TRIGGER_IS_NON_ZERO() -> DataLoggingTriggerType:
        return DataLoggingTriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingTriggerType, "EnableLoggingWhenTriggerIsNonZero"), "ENABLE_LOGGING_WHEN_TRIGGER_IS_NON_ZERO")


class Delimiter(_DotNetEnum):
    """Defines the delimiter of the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" crefType="PartiallyQualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Delimiter:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for Delimiter")

    @_staticproperty
    def TAB() -> Delimiter:
        return Delimiter(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.Delimiter, "Tab"), "TAB")

    @_staticproperty
    def EQUALS() -> Delimiter:
        return Delimiter(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.Delimiter, "Equals"), "EQUALS")

    @_staticproperty
    def COMMA() -> Delimiter:
        return Delimiter(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.Delimiter, "Comma"), "COMMA")


class DependentFile(_DotNetBase):
    """Represents a dependent file, which can be any file that another node requires. For example, model files, bitfiles, and VIs that make up custom devices can all be dependent files."""

    @overload
    def __init__(self, file_path: str, version: str, force_download: bool, rt_destination: str, supported_target: str, md5: str):
        ...

    @overload
    def __init__(self, file_path: str, type: DependentFileType, version: str, force_download: bool, rt_destination: str, supported_target: str, md5: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFile:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFile(*_unwrap(None, *args))

    @property
    def path(self) -> str:
        """Gets the path to the file on the host computer."""
        return _wrap(self._dotnet_instance.Path)

    @property
    def type(self) -> DependentFileType:
        """Gets whether the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFile.Path" crefType="Unqualified" /> to the dependent file is absolute or relative to another directory."""
        return _wrap(self._dotnet_instance.Type)

    @property
    def version(self) -> str:
        """Gets or sets version information for the dependent file."""
        return _wrap(self._dotnet_instance.Version)

    @version.setter
    def version(self, value: str):
        """Gets or sets version information for the dependent file."""
        self._dotnet_instance.Version = next(_unwrap(None, value))

    @property
    def force_download(self) -> bool:
        """Gets or sets whether the file is set to force-download to the target."""
        return _wrap(self._dotnet_instance.ForceDownload)

    @force_download.setter
    def force_download(self, value: bool):
        """Gets or sets whether the file is set to force-download to the target."""
        self._dotnet_instance.ForceDownload = next(_unwrap(None, value))

    @property
    def rt_destination(self) -> str:
        """Gets or sets the destination path, including the filename, for the file on the target. This property must be an absolute path."""
        return _wrap(self._dotnet_instance.RTDestination)

    @rt_destination.setter
    def rt_destination(self, value: str):
        """Gets or sets the destination path, including the filename, for the file on the target. This property must be an absolute path."""
        self._dotnet_instance.RTDestination = next(_unwrap(None, value))

    @property
    def supported_target(self) -> str:
        """Gets or sets the target operating system(s) to which the file is deployed."""
        return _wrap(self._dotnet_instance.SupportedTarget)

    @supported_target.setter
    def supported_target(self, value: str):
        """Gets or sets the target operating system(s) to which the file is deployed."""
        self._dotnet_instance.SupportedTarget = next(_unwrap(None, value))

    @property
    def md5(self) -> str:
        """Gets or sets the MD5 message-digest for the file."""
        return _wrap(self._dotnet_instance.MD5)

    @md5.setter
    def md5(self, value: str):
        """Gets or sets the MD5 message-digest for the file."""
        self._dotnet_instance.MD5 = next(_unwrap(None, value))

    @overload
    def set_path(self, file_path: str, sdf_path: str):
        ...

    def set_path(self, *args):
        return _wrap(self._dotnet_instance.SetPath(*_unwrap(None, *args)))

    @overload
    def get_absolute_path(self, base_absolute_path: str) -> str:
        ...

    def get_absolute_path(self, *args):
        return _wrap(self._dotnet_instance.GetAbsolutePath(*_unwrap(None, *args)))


class DependentFileType(_DotNetEnum):
    """Specifies the type of path used for the location of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFile" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFileType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DependentFileType")

    @_staticproperty
    def ABSOLUTE() -> DependentFileType:
        return DependentFileType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFileType, "Absolute"), "ABSOLUTE")

    @_staticproperty
    def RELATIVE() -> DependentFileType:
        return DependentFileType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFileType, "Relative"), "RELATIVE")

    @_staticproperty
    def TO_COMMON_DOC_DIR() -> DependentFileType:
        return DependentFileType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFileType, "ToCommonDocDir"), "TO_COMMON_DOC_DIR")

    @_staticproperty
    def TO_APP_DATA_DIR() -> DependentFileType:
        return DependentFileType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFileType, "ToAppDataDir"), "TO_APP_DATA_DIR")


class Dictionary(_DotNetBase):
    """Represents a dictionary, which is an associative array. You can set dictionaries as values for <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDevice" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.TimingAndSyncDevice" crefType="Unqualified" /> items."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, to_copy: Dictionary):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary(*_unwrap(None, *args))

    @property
    def count(self) -> int:
        """Gets the total number of key/value pairs in a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.Count)

    @property
    def elem(self) -> Sequence[DictionaryElement]:
        """Gets all the elements in the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.Elem)

    @overload
    def add_boolean(self, name: str, value: bool) -> bool:
        ...

    def add_boolean(self, *args):
        return _wrap(self._dotnet_instance.AddBoolean(*_unwrap(None, *args)))

    @overload
    def add_boolean_array(self, name: str, value: Sequence[bool]) -> bool:
        ...

    def add_boolean_array(self, *args):
        return _wrap(self._dotnet_instance.AddBooleanArray(*_unwrap(None, *args)))

    @overload
    def add_u16(self, name: str, value: int) -> bool:
        ...

    def add_u16(self, *args):
        return _wrap(self._dotnet_instance.AddU16(*_unwrap(None, *args)))

    @overload
    def add_u16_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_u16_array(self, *args):
        return _wrap(self._dotnet_instance.AddU16Array(*_unwrap(None, *args)))

    @overload
    def add_u32(self, name: str, value: int) -> bool:
        ...

    def add_u32(self, *args):
        return _wrap(self._dotnet_instance.AddU32(*_unwrap(None, *args)))

    @overload
    def add_u32_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_u32_array(self, *args):
        return _wrap(self._dotnet_instance.AddU32Array(*_unwrap(None, *args)))

    @overload
    def add_u64(self, name: str, value: int) -> bool:
        ...

    def add_u64(self, *args):
        return _wrap(self._dotnet_instance.AddU64(*_unwrap(None, *args)))

    @overload
    def add_u64_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_u64_array(self, *args):
        return _wrap(self._dotnet_instance.AddU64Array(*_unwrap(None, *args)))

    @overload
    def add_i16(self, name: str, value: int) -> bool:
        ...

    def add_i16(self, *args):
        return _wrap(self._dotnet_instance.AddI16(*_unwrap(None, *args)))

    @overload
    def add_i16_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_i16_array(self, *args):
        return _wrap(self._dotnet_instance.AddI16Array(*_unwrap(None, *args)))

    @overload
    def add_i32(self, name: str, value: int) -> bool:
        ...

    def add_i32(self, *args):
        return _wrap(self._dotnet_instance.AddI32(*_unwrap(None, *args)))

    @overload
    def add_i32_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_i32_array(self, *args):
        return _wrap(self._dotnet_instance.AddI32Array(*_unwrap(None, *args)))

    @overload
    def add_i64(self, name: str, value: int) -> bool:
        ...

    def add_i64(self, *args):
        return _wrap(self._dotnet_instance.AddI64(*_unwrap(None, *args)))

    @overload
    def add_i64_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_i64_array(self, *args):
        return _wrap(self._dotnet_instance.AddI64Array(*_unwrap(None, *args)))

    @overload
    def add_double(self, name: str, value: float) -> bool:
        ...

    def add_double(self, *args):
        return _wrap(self._dotnet_instance.AddDouble(*_unwrap(None, *args)))

    @overload
    def add_double_array(self, name: str, value: Sequence[float]) -> bool:
        ...

    def add_double_array(self, *args):
        return _wrap(self._dotnet_instance.AddDoubleArray(*_unwrap(None, *args)))

    @overload
    def add_string(self, name: str, value: str) -> bool:
        ...

    def add_string(self, *args):
        return _wrap(self._dotnet_instance.AddString(*_unwrap(None, *args)))

    @overload
    def add_string_array(self, name: str, value: Sequence[str]) -> bool:
        ...

    def add_string_array(self, *args):
        return _wrap(self._dotnet_instance.AddStringArray(*_unwrap(None, *args)))

    @overload
    def clear(self):
        ...

    def clear(self, *args):
        return _wrap(self._dotnet_instance.Clear(*_unwrap(None, *args)))

    @overload
    def get_boolean(self, name: str) -> Tuple[bool, bool]:
        ...

    def get_boolean(self, *args):
        return _wrap(self._dotnet_instance.GetBoolean(*_unwrap(None, *args)))

    @overload
    def get_boolean_array(self, name: str) -> Tuple[bool, Sequence[bool]]:
        ...

    def get_boolean_array(self, *args):
        return _wrap(self._dotnet_instance.GetBooleanArray(*_unwrap(None, *args)))

    @overload
    def get_u16(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u16(self, *args):
        return _wrap(self._dotnet_instance.GetU16(*_unwrap(None, *args)))

    @overload
    def get_u16_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u16_array(self, *args):
        return _wrap(self._dotnet_instance.GetU16Array(*_unwrap(None, *args)))

    @overload
    def get_u32(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u32(self, *args):
        return _wrap(self._dotnet_instance.GetU32(*_unwrap(None, *args)))

    @overload
    def get_u32_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u32_array(self, *args):
        return _wrap(self._dotnet_instance.GetU32Array(*_unwrap(None, *args)))

    @overload
    def get_u64(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u64(self, *args):
        return _wrap(self._dotnet_instance.GetU64(*_unwrap(None, *args)))

    @overload
    def get_u64_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u64_array(self, *args):
        return _wrap(self._dotnet_instance.GetU64Array(*_unwrap(None, *args)))

    @overload
    def get_i16(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i16(self, *args):
        return _wrap(self._dotnet_instance.GetI16(*_unwrap(None, *args)))

    @overload
    def get_i16_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i16_array(self, *args):
        return _wrap(self._dotnet_instance.GetI16Array(*_unwrap(None, *args)))

    @overload
    def get_i32(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i32(self, *args):
        return _wrap(self._dotnet_instance.GetI32(*_unwrap(None, *args)))

    @overload
    def get_i32_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i32_array(self, *args):
        return _wrap(self._dotnet_instance.GetI32Array(*_unwrap(None, *args)))

    @overload
    def get_i64(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i64(self, *args):
        return _wrap(self._dotnet_instance.GetI64(*_unwrap(None, *args)))

    @overload
    def get_i64_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i64_array(self, *args):
        return _wrap(self._dotnet_instance.GetI64Array(*_unwrap(None, *args)))

    @overload
    def get_double(self, name: str) -> Tuple[bool, float]:
        ...

    def get_double(self, *args):
        return _wrap(self._dotnet_instance.GetDouble(*_unwrap(None, *args)))

    @overload
    def get_double_array(self, name: str) -> Tuple[bool, Sequence[float]]:
        ...

    def get_double_array(self, *args):
        return _wrap(self._dotnet_instance.GetDoubleArray(*_unwrap(None, *args)))

    @overload
    def get_string(self, name: str) -> Tuple[bool, str]:
        ...

    def get_string(self, *args):
        return _wrap(self._dotnet_instance.GetString(*_unwrap(None, *args)))

    @overload
    def get_string_array(self, name: str) -> Tuple[bool, Sequence[str]]:
        ...

    def get_string_array(self, *args):
        return _wrap(self._dotnet_instance.GetStringArray(*_unwrap(None, *args)))

    @overload
    def remove_element(self, key: str) -> bool:
        ...

    def remove_element(self, *args):
        return _wrap(self._dotnet_instance.RemoveElement(*_unwrap(None, *args)))


class DictionaryElement(_DotNetBase):
    """Represents an element, or a key/value pair, in a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary" crefType="Unqualified" />."""

    @overload
    def __init__(self, to_copy: DictionaryElement):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DictionaryElement:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DictionaryElement(*_unwrap(None, *args))

    @property
    def item(self) -> Any:
        """Gets or sets a reference to a value of a dictionary element."""
        return _wrap(self._dotnet_instance.Item)

    @item.setter
    def item(self, value: Any):
        """Gets or sets a reference to a value of a dictionary element."""
        self._dotnet_instance.Item = next(_unwrap(None, value))

    @property
    def key(self) -> str:
        """Gets or sets the key, or name, of a dictionary element."""
        return _wrap(self._dotnet_instance.Key)

    @key.setter
    def key(self, value: str):
        """Gets or sets the key, or name, of a dictionary element."""
        self._dotnet_instance.Key = next(_unwrap(None, value))


class DirectionType(_DotNetEnum):
    """Defines the direction of a signal slope or edge that causes a trigger."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DirectionType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DirectionType")

    @_staticproperty
    def RISING() -> DirectionType:
        return DirectionType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DirectionType, "Rising"), "RISING")

    @_staticproperty
    def FALLING() -> DirectionType:
        return DirectionType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DirectionType, "Falling"), "FALLING")


class EdgeType(_DotNetEnum):
    """Defines the edge type of the sample clock."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.EdgeType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for EdgeType")

    @_staticproperty
    def RISING() -> EdgeType:
        return EdgeType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.EdgeType, "Rising"), "RISING")

    @_staticproperty
    def FALLING() -> EdgeType:
        return EdgeType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.EdgeType, "Falling"), "FALLING")


class FDISOMode(_DotNetEnum):
    """Specifies whether the interface is working in the ISO CAN FD standard (ISO standard 11898-1:2015)
            or non-ISO CAN FD standard (Bosch CAN FD 1.0 specification). Two ports using different standards
            (ISO CAN FD vs. non-ISO CAN FD) cannot communicate with each other."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FDISOMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for FDISOMode")

    @_staticproperty
    def ISO() -> FDISOMode:
        return FDISOMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FDISOMode, "ISO"), "ISO")

    @_staticproperty
    def NON_ISO() -> FDISOMode:
        return FDISOMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FDISOMode, "NonISO"), "NON_ISO")

    @_staticproperty
    def ISO_LEGACY() -> FDISOMode:
        return FDISOMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FDISOMode, "ISOLegacy"), "ISO_LEGACY")


class FileLimitationType(_DotNetEnum):
    """Specifies the type of limit used to stop logging incoming frame data to an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FileLimitationType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for FileLimitationType")

    @_staticproperty
    def FOOTPRINT() -> FileLimitationType:
        return FileLimitationType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FileLimitationType, "Footprint"), "FOOTPRINT")

    @_staticproperty
    def TIME() -> FileLimitationType:
        return FileLimitationType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FileLimitationType, "Time"), "TIME")


class FileType(_DotNetEnum):
    """Specifies the file type of an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FileType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for FileType")

    @_staticproperty
    def TDMS() -> FileType:
        return FileType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FileType, "TDMS"), "TDMS")

    @_staticproperty
    def NCL() -> FileType:
        return FileType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FileType, "NCL"), "NCL")


class FramePhaseType(_DotNetEnum):
    """Specifies whether to reset the timer of a software cyclic trigger after each transmission of an outgoing frame."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FramePhaseType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for FramePhaseType")

    @_staticproperty
    def UNCHANGED() -> FramePhaseType:
        return FramePhaseType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FramePhaseType, "Unchanged"), "UNCHANGED")

    @_staticproperty
    def RESET() -> FramePhaseType:
        return FramePhaseType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FramePhaseType, "Reset"), "RESET")


class FrameTriggerType(_DotNetEnum):
    """Specifies a condition that a trigger channel must meet to trigger transmission of an outgoing frame."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FrameTriggerType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for FrameTriggerType")

    @_staticproperty
    def CHANNEL_VALUE_CHANGE() -> FrameTriggerType:
        return FrameTriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameTriggerType, "ChannelValueChange"), "CHANNEL_VALUE_CHANGE")

    @_staticproperty
    def TRIGGER_CHANNEL_NOT_ZERO() -> FrameTriggerType:
        return FrameTriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameTriggerType, "TriggerChannelNotZero"), "TRIGGER_CHANNEL_NOT_ZERO")

    @_staticproperty
    def CHANNEL_VALUE_CHANGE_OR_TRIGGER_CHANNEL_NOT_ZERO() -> FrameTriggerType:
        return FrameTriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameTriggerType, "ChannelValueChangeOrTriggerChannelNotZero"), "CHANNEL_VALUE_CHANGE_OR_TRIGGER_CHANNEL_NOT_ZERO")

    @_staticproperty
    def TRIGGER_CHANNEL_ANY_VALUE_CHANGE() -> FrameTriggerType:
        return FrameTriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameTriggerType, "TriggerChannelAnyValueChange"), "TRIGGER_CHANNEL_ANY_VALUE_CHANGE")

    @_staticproperty
    def CHANNEL_VALUE_CHANGE_OR_TRIGGER_CHANNEL_ANY_VALUE_CHANGE() -> FrameTriggerType:
        return FrameTriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameTriggerType, "ChannelValueChangeOrTriggerChannelAnyValueChange"), "CHANNEL_VALUE_CHANGE_OR_TRIGGER_CHANNEL_ANY_VALUE_CHANGE")


class FrameType(_DotNetEnum):
    """Specifies the type of a CAN or FlexRay frame."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FrameType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for FrameType")

    @_staticproperty
    def CAN_DATA_FRAME() -> FrameType:
        return FrameType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameType, "CANDataFrame"), "CAN_DATA_FRAME")

    @_staticproperty
    def CAN_REMOTE_FRAME() -> FrameType:
        return FrameType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameType, "CANRemoteFrame"), "CAN_REMOTE_FRAME")

    @_staticproperty
    def FLEX_RAY_DATA_FRAME() -> FrameType:
        return FrameType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameType, "FlexRayDataFrame"), "FLEX_RAY_DATA_FRAME")

    @_staticproperty
    def FLEX_RAY_NULL_FRAME() -> FrameType:
        return FrameType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameType, "FlexRayNullFrame"), "FLEX_RAY_NULL_FRAME")


class GlobalParameterScopes(_DotNetEnum):
    """Specifies whether global parameters in a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" /> share their values with other models."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalParameterScopes:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for GlobalParameterScopes")

    @_staticproperty
    def TARGET() -> GlobalParameterScopes:
        return GlobalParameterScopes(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalParameterScopes, "Target"), "TARGET")

    @_staticproperty
    def MODEL() -> GlobalParameterScopes:
        return GlobalParameterScopes(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalParameterScopes, "Model"), "MODEL")


class GlobalSequenceCommand(_DotNetEnum):
    """Specifies the command for all running sequences."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalSequenceCommand:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for GlobalSequenceCommand")

    @_staticproperty
    def STOP_ALL() -> GlobalSequenceCommand:
        return GlobalSequenceCommand(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalSequenceCommand, "StopAll"), "STOP_ALL")

    @_staticproperty
    def ABORT_ALL() -> GlobalSequenceCommand:
        return GlobalSequenceCommand(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalSequenceCommand, "AbortAll"), "ABORT_ALL")

    @_staticproperty
    def STOP_GROUP() -> GlobalSequenceCommand:
        return GlobalSequenceCommand(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalSequenceCommand, "StopGroup"), "STOP_GROUP")


class IChannel(_DotNetBase):
    """An interface defining system definition channel behavior"""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IChannel")

    @property
    def data_source(self) -> BaseNode:
        """Gets or sets the source channel that maps to the current channel and provides it data."""
        return _wrap(self._dotnet_instance.DataSource)

    @data_source.setter
    def data_source(self, value: BaseNode):
        """Gets or sets the source channel that maps to the current channel and provides it data."""
        self._dotnet_instance.DataSource = next(_unwrap(None, value))

    @property
    def column_dimensions(self) -> int:
        """Gets the number of columns in the channel value."""
        return _wrap(self._dotnet_instance.ColumnDimensions)

    @property
    def row_dimensions(self) -> int:
        """Gets the number of rows in the channel value."""
        return _wrap(self._dotnet_instance.RowDimensions)

    @property
    def units(self) -> str:
        """Gets or sets the units associated with the channel. This can be any arbitrary string."""
        return _wrap(self._dotnet_instance.Units)

    @units.setter
    def units(self, value: str):
        """Gets or sets the units associated with the channel. This can be any arbitrary string."""
        self._dotnet_instance.Units = next(_unwrap(None, value))

    @property
    def is_readable(self) -> bool:
        """Gets a value indicating whether the channel is readable."""
        return _wrap(self._dotnet_instance.IsReadable)

    @property
    def is_writable(self) -> bool:
        """Gets a value indicating whether the channel is writable."""
        return _wrap(self._dotnet_instance.IsWritable)

    @property
    def scale_units(self) -> str:
        """Gets the units of the scale associated with the channel."""
        return _wrap(self._dotnet_instance.ScaleUnits)

    @overload
    def remove_data_source(self):
        ...

    def remove_data_source(self, *args):
        return _wrap(self._dotnet_instance.RemoveDataSource(*_unwrap(None, *args)))

    @overload
    def get_value_table(self) -> Tuple[bool, Sequence[str], Sequence[float]]:
        ...

    def get_value_table(self, *args):
        return _wrap(self._dotnet_instance.GetValueTable(*_unwrap(None, *args)))


class LUTValue(_DotNetBase):
    """Represents a pair of values in a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LookupTable" /> scale: a pre-scaled value and the corresponding scaled value."""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.LUTValue:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.LUTValue(*_unwrap(None, *args))

    @property
    def pre_scaled(self) -> float:
        """Gets or sets the pre-scaled LUTValue."""
        return _wrap(self._dotnet_instance.PreScaled)

    @pre_scaled.setter
    def pre_scaled(self, value: float):
        """Gets or sets the pre-scaled LUTValue."""
        self._dotnet_instance.PreScaled = next(_unwrap(None, value))

    @property
    def scaled(self) -> float:
        """Gets or sets the scaled LUTValue."""
        return _wrap(self._dotnet_instance.Scaled)

    @scaled.setter
    def scaled(self, value: float):
        """Gets or sets the scaled LUTValue."""
        self._dotnet_instance.Scaled = next(_unwrap(None, value))


class LogMode(_DotNetEnum):
    """The logging mode that determines whether components in the NI VeriStand system can read data as you log it."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.LogMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for LogMode")

    @_staticproperty
    def LOG() -> LogMode:
        return LogMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.LogMode, "Log"), "LOG")

    @_staticproperty
    def LOG_AND_READ() -> LogMode:
        return LogMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.LogMode, "LogAndRead"), "LOG_AND_READ")


class ModelCommandState(_DotNetEnum):
    """Specifies the current state of the model."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommandState:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ModelCommandState")

    @_staticproperty
    def START() -> ModelCommandState:
        return ModelCommandState(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommandState, "Start"), "START")

    @_staticproperty
    def PAUSE() -> ModelCommandState:
        return ModelCommandState(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommandState, "Pause"), "PAUSE")

    @_staticproperty
    def RESET() -> ModelCommandState:
        return ModelCommandState(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommandState, "Reset"), "RESET")

    @_staticproperty
    def SAVE() -> ModelCommandState:
        return ModelCommandState(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommandState, "Save"), "SAVE")

    @_staticproperty
    def RESTORE() -> ModelCommandState:
        return ModelCommandState(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommandState, "Restore"), "RESTORE")


class NodeIDUtil(_DotNetBase):
    """Provides methods for converting node IDs, or pointers, to nodes in a system definition file into item references to the same node."""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil(*_unwrap(None, *args))

    @staticmethod
    @overload
    def id_to_base_node(node_id: int) -> BaseNode:
        ...

    def id_to_base_node(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToBaseNode(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def id_to_custom_device_base(node_id: int) -> CustomDeviceBase:
        ...

    def id_to_custom_device_base(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToCustomDeviceBase(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def id_to_custom_device_channel(node_id: int) -> CustomDeviceChannel:
        ...

    def id_to_custom_device_channel(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToCustomDeviceChannel(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def id_to_custom_device_waveform(node_id: int) -> CustomDeviceWaveform:
        ...

    def id_to_custom_device_waveform(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToCustomDeviceWaveform(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def id_to_custom_device_section(node_id: int) -> CustomDeviceSection:
        ...

    def id_to_custom_device_section(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToCustomDeviceSection(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def id_to_custom_device(node_id: int) -> CustomDevice:
        ...

    def id_to_custom_device(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToCustomDevice(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def id_to_timing_sync_device(node_id: int) -> TimingAndSyncDevice:
        ...

    def id_to_timing_sync_device(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToTimingSyncDevice(*_unwrap(None, *args)))


class PXIBackplaneReferenceClock(_DotNetEnum):
    """Specifies the PXI chassis backplane reference clock."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.PXIBackplaneReferenceClock:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for PXIBackplaneReferenceClock")

    @_staticproperty
    def AUTOMATIC() -> PXIBackplaneReferenceClock:
        return PXIBackplaneReferenceClock(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.PXIBackplaneReferenceClock, "Automatic"), "AUTOMATIC")

    @_staticproperty
    def NONE() -> PXIBackplaneReferenceClock:
        return PXIBackplaneReferenceClock(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.PXIBackplaneReferenceClock, "None"), "NONE")

    @_staticproperty
    def CLK10() -> PXIBackplaneReferenceClock:
        return PXIBackplaneReferenceClock(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.PXIBackplaneReferenceClock, "Clk10"), "CLK10")

    @_staticproperty
    def CLK100() -> PXIBackplaneReferenceClock:
        return PXIBackplaneReferenceClock(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.PXIBackplaneReferenceClock, "Clk100"), "CLK100")


class ParameterAccess(_DotNetEnum):
    """Defines the parameter access mode on the engine. The user can select to access only the imported parameters or all the parameters from the models."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ParameterAccess:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ParameterAccess")

    @_staticproperty
    def ONLY_IMPORTED_PARAMETERS() -> ParameterAccess:
        return ParameterAccess(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ParameterAccess, "OnlyImportedParameters"), "ONLY_IMPORTED_PARAMETERS")

    @_staticproperty
    def ANY_PARAMETER() -> ParameterAccess:
        return ParameterAccess(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ParameterAccess, "AnyParameter"), "ANY_PARAMETER")


class ReflectiveMemoryDataChannelAccessType(_DotNetEnum):
    """Specifies the access type (read or write) of a data channel on a reflective memory device."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelAccessType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ReflectiveMemoryDataChannelAccessType")

    @_staticproperty
    def READ() -> ReflectiveMemoryDataChannelAccessType:
        return ReflectiveMemoryDataChannelAccessType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelAccessType, "Read"), "READ")

    @_staticproperty
    def WRITE() -> ReflectiveMemoryDataChannelAccessType:
        return ReflectiveMemoryDataChannelAccessType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelAccessType, "Write"), "WRITE")


class ReflectiveMemoryDataChannelDataType(_DotNetEnum):
    """Specifies the data type of a data channel on a reflective memory device."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ReflectiveMemoryDataChannelDataType")

    @_staticproperty
    def U_INT8() -> ReflectiveMemoryDataChannelDataType:
        return ReflectiveMemoryDataChannelDataType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "UInt8"), "U_INT8")

    @_staticproperty
    def INT8() -> ReflectiveMemoryDataChannelDataType:
        return ReflectiveMemoryDataChannelDataType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "Int8"), "INT8")

    @_staticproperty
    def U_INT16() -> ReflectiveMemoryDataChannelDataType:
        return ReflectiveMemoryDataChannelDataType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "UInt16"), "U_INT16")

    @_staticproperty
    def INT16() -> ReflectiveMemoryDataChannelDataType:
        return ReflectiveMemoryDataChannelDataType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "Int16"), "INT16")

    @_staticproperty
    def U_INT32() -> ReflectiveMemoryDataChannelDataType:
        return ReflectiveMemoryDataChannelDataType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "UInt32"), "U_INT32")

    @_staticproperty
    def INT32() -> ReflectiveMemoryDataChannelDataType:
        return ReflectiveMemoryDataChannelDataType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "Int32"), "INT32")

    @_staticproperty
    def U_INT64() -> ReflectiveMemoryDataChannelDataType:
        return ReflectiveMemoryDataChannelDataType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "UInt64"), "U_INT64")

    @_staticproperty
    def INT64() -> ReflectiveMemoryDataChannelDataType:
        return ReflectiveMemoryDataChannelDataType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "Int64"), "INT64")

    @_staticproperty
    def DOUBLE() -> ReflectiveMemoryDataChannelDataType:
        return ReflectiveMemoryDataChannelDataType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "Double"), "DOUBLE")


class ReflectiveMemoryInterruptType(_DotNetEnum):
    """Specifies the type of interrupt a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemory" crefType="Unqualified" /> device sends or receives."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ReflectiveMemoryInterruptType")

    @_staticproperty
    def LINK_RESET_INTERRUPT() -> ReflectiveMemoryInterruptType:
        return ReflectiveMemoryInterruptType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptType, "LinkResetInterrupt"), "LINK_RESET_INTERRUPT")

    @_staticproperty
    def NETWORK_INTERRUPT1() -> ReflectiveMemoryInterruptType:
        return ReflectiveMemoryInterruptType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptType, "NetworkInterrupt1"), "NETWORK_INTERRUPT1")

    @_staticproperty
    def NETWORK_INTERRUPT2() -> ReflectiveMemoryInterruptType:
        return ReflectiveMemoryInterruptType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptType, "NetworkInterrupt2"), "NETWORK_INTERRUPT2")

    @_staticproperty
    def NETWORK_INTERRUPT3() -> ReflectiveMemoryInterruptType:
        return ReflectiveMemoryInterruptType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptType, "NetworkInterrupt3"), "NETWORK_INTERRUPT3")

    @_staticproperty
    def NETWORK_INIT_INTERRUPT() -> ReflectiveMemoryInterruptType:
        return ReflectiveMemoryInterruptType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptType, "NetworkInitInterrupt"), "NETWORK_INIT_INTERRUPT")


class ReplayBehavior(_DotNetEnum):
    """Specifies whether and how frames in a data replay file on an NI-XNET CAN port are filtered."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ReplayBehavior")

    @_staticproperty
    def REPLAY_ENTIRE_FILE() -> ReplayBehavior:
        return ReplayBehavior(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior, "ReplayEntireFile"), "REPLAY_ENTIRE_FILE")

    @_staticproperty
    def EXCLUDE_FRAME_I_DS() -> ReplayBehavior:
        return ReplayBehavior(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior, "ExcludeFrameIDs"), "EXCLUDE_FRAME_I_DS")

    @_staticproperty
    def INCLUDE_FRAME_I_DS() -> ReplayBehavior:
        return ReplayBehavior(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior, "IncludeFrameIDs"), "INCLUDE_FRAME_I_DS")


class Root(BaseNode):
    """Represents the root node of the system definition."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Root:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Root")

    @property
    def version(self) -> str:
        """Gets or sets the system definition file version number."""
        return _wrap(self._dotnet_instance.Version)

    @version.setter
    def version(self, value: str):
        """Gets or sets the system definition file version number."""
        self._dotnet_instance.Version = next(_unwrap(None, value))

    @property
    def creator(self) -> str:
        """Gets or sets the user account name of the system definition file creator."""
        return _wrap(self._dotnet_instance.Creator)

    @creator.setter
    def creator(self, value: str):
        """Gets or sets the user account name of the system definition file creator."""
        self._dotnet_instance.Creator = next(_unwrap(None, value))

    @property
    def creation_date(self) -> float:
        """Gets or sets the creation date of the system definition file."""
        return _wrap(self._dotnet_instance.CreationDate)

    @creation_date.setter
    def creation_date(self, value: float):
        """Gets or sets the creation date of the system definition file."""
        self._dotnet_instance.CreationDate = next(_unwrap(None, value))

    @overload
    def delete_channel_mappings(self, channel_path_destinations: Sequence[str]):
        ...

    def delete_channel_mappings(self, *args):
        return _wrap(self._dotnet_instance.DeleteChannelMappings(*_unwrap(None, *args)))

    @overload
    def add_channel_mappings(self, channel_path_sources: Sequence[str], channel_path_destinations: Sequence[str]) -> bool:
        ...

    def add_channel_mappings(self, *args):
        return _wrap(self._dotnet_instance.AddChannelMappings(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def get_channel_mappings(self) -> Tuple[Sequence[str], Sequence[str]]:
        ...

    def get_channel_mappings(self, *args):
        return _wrap(self._dotnet_instance.GetChannelMappings(*_unwrap(None, *args)))

    @overload
    def clear_channel_mappings(self):
        ...

    def clear_channel_mappings(self, *args):
        return _wrap(self._dotnet_instance.ClearChannelMappings(*_unwrap(None, *args)))

    @overload
    def get_targets(self) -> Targets:
        ...

    def get_targets(self, *args):
        return _wrap(self._dotnet_instance.GetTargets(*_unwrap(None, *args)))

    @overload
    def refresh_node_dependencies(self):
        ...

    def refresh_node_dependencies(self, *args):
        return _wrap(self._dotnet_instance.RefreshNodeDependencies(*_unwrap(None, *args)))

    @overload
    def get_aliases(self) -> Aliases:
        ...

    def get_aliases(self, *args):
        return _wrap(self._dotnet_instance.GetAliases(*_unwrap(None, *args)))

    @overload
    def get_scales(self) -> Scales:
        ...

    def get_scales(self, *args):
        return _wrap(self._dotnet_instance.GetScales(*_unwrap(None, *args)))

    @overload
    def get_system_mappings(self) -> SystemMappings:
        ...

    def get_system_mappings(self, *args):
        return _wrap(self._dotnet_instance.GetSystemMappings(*_unwrap(None, *args)))

    @overload
    def get_data_sharing_network(self) -> DataSharingNetwork:
        ...

    def get_data_sharing_network(self, *args):
        return _wrap(self._dotnet_instance.GetDataSharingNetwork(*_unwrap(None, *args)))

    @overload
    def get_system_initialization(self) -> SystemInitialization:
        ...

    def get_system_initialization(self, *args):
        return _wrap(self._dotnet_instance.GetSystemInitialization(*_unwrap(None, *args)))


class SampleMode(_DotNetEnum):
    """Whether the AI acquisition is single-point or buffered."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SampleMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for SampleMode")

    @_staticproperty
    def SINGLE_POINT() -> SampleMode:
        return SampleMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SampleMode, "SinglePoint"), "SINGLE_POINT")

    @_staticproperty
    def WAVEFORM() -> SampleMode:
        return SampleMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SampleMode, "Waveform"), "WAVEFORM")


class ScaleType(_DotNetEnum):
    """This enumeration is used to select the Scale Type."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ScaleType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ScaleType")

    @_staticproperty
    def POLYNOMIAL() -> ScaleType:
        return ScaleType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ScaleType, "Polynomial"), "POLYNOMIAL")

    @_staticproperty
    def THERMOCOUPLE() -> ScaleType:
        return ScaleType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ScaleType, "Thermocouple"), "THERMOCOUPLE")

    @_staticproperty
    def LOOKUP_TABLE() -> ScaleType:
        return ScaleType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ScaleType, "LookupTable"), "LOOKUP_TABLE")


class Section(BaseNode):
    """Represents a section or node in the system definition. A section represents any node that contains additional nodes."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Section:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Section")


class SetVariableStepFunction(_DotNetEnum):
    """Specifies the function to use on <format type="italics">Value1</format> and <format type="italics">Value2</format> of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable" crefType="Unqualified" /> procedure step."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariableStepFunction:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for SetVariableStepFunction")

    @_staticproperty
    def NONE() -> SetVariableStepFunction:
        return SetVariableStepFunction(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariableStepFunction, "None"), "NONE")

    @_staticproperty
    def ADD() -> SetVariableStepFunction:
        return SetVariableStepFunction(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariableStepFunction, "Add"), "ADD")

    @_staticproperty
    def SUBTRACT() -> SetVariableStepFunction:
        return SetVariableStepFunction(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariableStepFunction, "Subtract"), "SUBTRACT")

    @_staticproperty
    def MULTIPLY() -> SetVariableStepFunction:
        return SetVariableStepFunction(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariableStepFunction, "Multiply"), "MULTIPLY")

    @_staticproperty
    def DIVIDE() -> SetVariableStepFunction:
        return SetVariableStepFunction(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariableStepFunction, "Divide"), "DIVIDE")


class SignalBasedFrame(Section):
    """Represents a signal format frame under an NI-XNET LIN, FlexRay, or CAN port."""

    @overload
    def __init__(self, name: str, id: int, owning_database: Database, cluster_name: str, payload_length: int, start_time_offset: float, enable64_bit: bool, signal_names: Sequence[str]):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame(*_unwrap(None, *args))

    @property
    def transmit_trigger(self) -> FrameTriggerType:
        """Gets the trigger type (channel value change, trigger channel not zero, and so on) specified for an event-triggered frame."""
        return _wrap(self._dotnet_instance.TransmitTrigger)

    @property
    def phase(self) -> FramePhaseType:
        """Gets or sets whether to reset the timer after <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        return _wrap(self._dotnet_instance.Phase)

    @phase.setter
    def phase(self, value: FramePhaseType):
        """Gets or sets whether to reset the timer after <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        self._dotnet_instance.Phase = next(_unwrap(None, value))

    @property
    def frame_type(self) -> FrameType:
        """Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port."""
        return _wrap(self._dotnet_instance.FrameType)

    @frame_type.setter
    def frame_type(self, value: FrameType):
        """Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port."""
        self._dotnet_instance.FrameType = next(_unwrap(None, value))

    @property
    def id(self) -> int:
        """Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent."""
        return _wrap(self._dotnet_instance.ID)

    @id.setter
    def id(self, value: int):
        """Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent."""
        self._dotnet_instance.ID = next(_unwrap(None, value))

    @property
    def payload_length(self) -> int:
        """Gets or sets the number of bytes in the payload of the frame."""
        return _wrap(self._dotnet_instance.PayloadLength)

    @payload_length.setter
    def payload_length(self, value: int):
        """Gets or sets the number of bytes in the payload of the frame."""
        self._dotnet_instance.PayloadLength = next(_unwrap(None, value))

    @property
    def md5(self) -> Sequence[int]:
        """Gets the MD5 message digest for the frame."""
        return _wrap(self._dotnet_instance.MD5)

    @property
    def start_time_offset(self) -> float:
        """Gets or sets the amount of time that elapses between the session start and the transmission of the first frame."""
        return _wrap(self._dotnet_instance.StartTimeOffset)

    @start_time_offset.setter
    def start_time_offset(self, value: float):
        """Gets or sets the amount of time that elapses between the session start and the transmission of the first frame."""
        self._dotnet_instance.StartTimeOffset = next(_unwrap(None, value))

    @property
    def enable64_bit(self) -> bool:
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        return _wrap(self._dotnet_instance.Enable64Bit)

    @enable64_bit.setter
    def enable64_bit(self, value: bool):
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        self._dotnet_instance.Enable64Bit = next(_unwrap(None, value))

    @property
    def owning_database(self) -> BaseNode:
        """Gets or sets a reference to the XNET database that contains the frame."""
        return _wrap(self._dotnet_instance.OwningDatabase)

    @owning_database.setter
    def owning_database(self, value: BaseNode):
        """Gets or sets a reference to the XNET database that contains the frame."""
        self._dotnet_instance.OwningDatabase = next(_unwrap(None, value))

    @property
    def cluster_name(self) -> str:
        """Gets or sets the name of the cluster in the XNET database that contains the frame."""
        return _wrap(self._dotnet_instance.ClusterName)

    @cluster_name.setter
    def cluster_name(self, value: str):
        """Gets or sets the name of the cluster in the XNET database that contains the frame."""
        self._dotnet_instance.ClusterName = next(_unwrap(None, value))

    @property
    def database_alias(self) -> str:
        """Gets or sets the alias for the XNET database that contains the frame."""
        return _wrap(self._dotnet_instance.DatabaseAlias)

    @database_alias.setter
    def database_alias(self, value: str):
        """Gets or sets the alias for the XNET database that contains the frame."""
        self._dotnet_instance.DatabaseAlias = next(_unwrap(None, value))

    @property
    def disabled(self) -> bool:
        """Gets whether transmission of the outgoing frame is disabled."""
        return _wrap(self._dotnet_instance.Disabled)

    @property
    def disable_channel(self) -> BaseNode:
        """Gets a reference to the disable channel for the frame. A disable channel disables transmission of an outgoing frame when the value of the disable channel is non-zero."""
        return _wrap(self._dotnet_instance.DisableChannel)

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets a reference to the channel that is checked for a non-zero value when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableFrameCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        return _wrap(self._dotnet_instance.TriggerChannel)

    @property
    def enable_software_cyclic_trigger(self) -> bool:
        """Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame."""
        return _wrap(self._dotnet_instance.EnableSoftwareCyclicTrigger)

    @enable_software_cyclic_trigger.setter
    def enable_software_cyclic_trigger(self, value: bool):
        """Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame."""
        self._dotnet_instance.EnableSoftwareCyclicTrigger = next(_unwrap(None, value))

    @property
    def enable_frame_cyclic_trigger(self) -> bool:
        """Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame."""
        return _wrap(self._dotnet_instance.EnableFrameCyclicTrigger)

    @enable_frame_cyclic_trigger.setter
    def enable_frame_cyclic_trigger(self, value: bool):
        """Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame."""
        self._dotnet_instance.EnableFrameCyclicTrigger = next(_unwrap(None, value))

    @property
    def transmit_time(self) -> float:
        """Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        return _wrap(self._dotnet_instance.TransmitTime)

    @transmit_time.setter
    def transmit_time(self, value: float):
        """Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        self._dotnet_instance.TransmitTime = next(_unwrap(None, value))

    @overload
    def create_multiplexer(self, multiplexer_value: int) -> Multiplexer:
        ...

    @overload
    def create_multiplexer(self, multiplexer_value: int, signal_name: str) -> Multiplexer:
        ...

    def create_multiplexer(self, *args):
        return _wrap(self._dotnet_instance.CreateMultiplexer(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_mode(self, multiplexer_value: int, signal_name: str, description: str, units: str, default_value: float) -> Mode:
        ...

    def create_mode(self, *args):
        return _wrap(self._dotnet_instance.CreateMode(*_unwrap({None: (5, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_signal_based_signal(self, name: str, description: str, units: str, default_value: float) -> SignalBasedSignal:
        ...

    def create_signal_based_signal(self, *args):
        return _wrap(self._dotnet_instance.CreateSignalBasedSignal(*_unwrap({None: (4, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_frame_information(self) -> FrameInformation:
        ...

    def create_frame_information(self, *args):
        return _wrap(self._dotnet_instance.CreateFrameInformation(*_unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_frame_faulting(self, create_skip_cyclic_frames: bool, create_transmit_time: bool) -> FrameFaulting:
        ...

    def create_frame_faulting(self, *args):
        return _wrap(self._dotnet_instance.CreateFrameFaulting(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_automatic_frame_processing(self) -> AutomaticFrameProcessing:
        ...

    def create_automatic_frame_processing(self, *args):
        return _wrap(self._dotnet_instance.CreateAutomaticFrameProcessing(*_unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def enable_transmission(self):
        ...

    def enable_transmission(self, *args):
        return _wrap(self._dotnet_instance.EnableTransmission(*_unwrap(None, *args)))

    @overload
    def disable_transmission(self, disable_channel: BaseNode):
        ...

    def disable_transmission(self, *args):
        return _wrap(self._dotnet_instance.DisableTransmission(*_unwrap(None, *args)))

    @overload
    def set_transmit_trigger(self, trigger_type: FrameTriggerType, trigger_channel: BaseNode):
        ...

    def set_transmit_trigger(self, *args):
        return _wrap(self._dotnet_instance.SetTransmitTrigger(*_unwrap(None, *args)))

    @overload
    def get_multiplexer(self) -> Multiplexer:
        ...

    def get_multiplexer(self, *args):
        return _wrap(self._dotnet_instance.GetMultiplexer(*_unwrap(None, *args)))

    @overload
    def get_mode_list(self) -> Sequence[Mode]:
        ...

    def get_mode_list(self, *args):
        return _wrap(self._dotnet_instance.GetModeList(*_unwrap(None, *args)))

    @overload
    def get_signal_based_signal_list(self) -> Sequence[SignalBasedSignal]:
        ...

    def get_signal_based_signal_list(self, *args):
        return _wrap(self._dotnet_instance.GetSignalBasedSignalList(*_unwrap(None, *args)))

    @overload
    def get_frame_information(self) -> FrameInformation:
        ...

    def get_frame_information(self, *args):
        return _wrap(self._dotnet_instance.GetFrameInformation(*_unwrap(None, *args)))

    @overload
    def get_frame_faulting(self) -> FrameFaulting:
        ...

    def get_frame_faulting(self, *args):
        return _wrap(self._dotnet_instance.GetFrameFaulting(*_unwrap(None, *args)))

    @overload
    def get_automatic_frame_processing(self) -> AutomaticFrameProcessing:
        ...

    def get_automatic_frame_processing(self, *args):
        return _wrap(self._dotnet_instance.GetAutomaticFrameProcessing(*_unwrap(None, *args)))


class SimulationModels(Section):
    """Represents the <format type="bold">Simulation Models</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains any models you import and information about the order in which they execute."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SimulationModels")

    @property
    def apply_parameter_file(self) -> bool:
        """Gets or sets a value indicating whether to apply the parameter values defined in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" /> when you deploy a system definition file."""
        return _wrap(self._dotnet_instance.ApplyParameterFile)

    @apply_parameter_file.setter
    def apply_parameter_file(self, value: bool):
        """Gets or sets a value indicating whether to apply the parameter values defined in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" /> when you deploy a system definition file."""
        self._dotnet_instance.ApplyParameterFile = next(_unwrap(None, value))

    @property
    def parameter_file_delimiter(self) -> Delimiter:
        """Gets or sets the delimiter used to separate parameter-value pairs in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />."""
        return _wrap(self._dotnet_instance.ParameterFileDelimiter)

    @parameter_file_delimiter.setter
    def parameter_file_delimiter(self, value: Delimiter):
        """Gets or sets the delimiter used to separate parameter-value pairs in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />."""
        self._dotnet_instance.ParameterFileDelimiter = next(_unwrap(None, value))

    @property
    def parameter_access(self) -> ParameterAccess:
        """Gets or sets the flag used to allow or deny reading and writing non-imported parameters."""
        return _wrap(self._dotnet_instance.ParameterAccess)

    @parameter_access.setter
    def parameter_access(self, value: ParameterAccess):
        """Gets or sets the flag used to allow or deny reading and writing non-imported parameters."""
        self._dotnet_instance.ParameterAccess = next(_unwrap(None, value))

    @property
    def parameter_file_allow_temp_variable(self) -> bool:
        """Gets or sets a value indicating whether the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" /> allows temporary variables. Temporary variables are always local to the file in which you define them."""
        return _wrap(self._dotnet_instance.ParameterFileAllowTempVariable)

    @parameter_file_allow_temp_variable.setter
    def parameter_file_allow_temp_variable(self, value: bool):
        """Gets or sets a value indicating whether the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" /> allows temporary variables. Temporary variables are always local to the file in which you define them."""
        self._dotnet_instance.ParameterFileAllowTempVariable = next(_unwrap(None, value))

    @property
    def parameter_file(self) -> str:
        """Gets or sets the parameter calibration <format type="monospace">.txt</format> file to apply when you deploy a system definition file."""
        return _wrap(self._dotnet_instance.ParameterFile)

    @parameter_file.setter
    def parameter_file(self, value: str):
        """Gets or sets the parameter calibration <format type="monospace">.txt</format> file to apply when you deploy a system definition file."""
        self._dotnet_instance.ParameterFile = next(_unwrap(None, value))

    @property
    def parameter_alias_file(self) -> str:
        """Gets or sets the parameter alias file to use with the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />."""
        return _wrap(self._dotnet_instance.ParameterAliasFile)

    @parameter_alias_file.setter
    def parameter_alias_file(self, value: str):
        """Gets or sets the parameter alias file to use with the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />."""
        self._dotnet_instance.ParameterAliasFile = next(_unwrap(None, value))

    @overload
    def remove_parameter_alias_file(self):
        ...

    def remove_parameter_alias_file(self, *args):
        return _wrap(self._dotnet_instance.RemoveParameterAliasFile(*_unwrap(None, *args)))

    @overload
    def get_models(self) -> Models:
        ...

    def get_models(self, *args):
        return _wrap(self._dotnet_instance.GetModels(*_unwrap(None, *args)))

    @overload
    def get_execution_order(self) -> ExecutionOrder:
        ...

    def get_execution_order(self, *args):
        return _wrap(self._dotnet_instance.GetExecutionOrder(*_unwrap(None, *args)))


class SinglePoint(Section):
    """Represents the <format type="bold">Single-Point</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Incoming" crefType="Unqualified" /> section of an NI-XNET CAN, LIN, or FlexRay port. When you import single-point frames, NI VeriStand reads the most recent value received for the frame."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SinglePoint:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SinglePoint")

    @overload
    def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]:
        ...

    def get_signal_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetSignalBasedFrameList(*_unwrap(None, *args)))

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetRawDataBasedFrameList(*_unwrap(None, *args)))

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddSignalBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddRawDataBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Sporadic(Section):
    """Represents the <format type="bold">Sporadic</format> section that contains outgoing, sporadic frames under an NI-XNET LIN port."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Sporadic:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Sporadic")

    @overload
    def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]:
        ...

    def get_signal_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetSignalBasedFrameList(*_unwrap(None, *args)))

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetRawDataBasedFrameList(*_unwrap(None, *args)))

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddSignalBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddRawDataBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Stimulus(Section):
    """Represents the <format type="bold">Stimulus</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains the stimulus generators available in the Legacy Stimulus Profile Editor."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Stimulus:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Stimulus")

    @property
    def max_gen_maps(self) -> int:
        """Gets or sets the maximum number of stimulus generator mappings across the entire system."""
        return _wrap(self._dotnet_instance.MaxGenMaps)

    @max_gen_maps.setter
    def max_gen_maps(self, value: int):
        """Gets or sets the maximum number of stimulus generator mappings across the entire system."""
        self._dotnet_instance.MaxGenMaps = next(_unwrap(None, value))

    @property
    def max_steps(self) -> int:
        """Gets or sets the maximum number of steps a stimulus generator can contain. Set this value to a number that is larger than the number of steps in the longest generator script."""
        return _wrap(self._dotnet_instance.MaxSteps)

    @max_steps.setter
    def max_steps(self, value: int):
        """Gets or sets the maximum number of steps a stimulus generator can contain. Set this value to a number that is larger than the number of steps in the longest generator script."""
        self._dotnet_instance.MaxSteps = next(_unwrap(None, value))

    @property
    def auxilliary_buffer_size(self) -> int:
        """Gets or sets the size of the auxiliary buffer. The auxiliary buffer stores multi-point playback data in comma-separated value (CSV), files. Set this buffer size to a number that matches or exceeds the number of data points in the CSV file you want to play back. The auxiliary buffer size is shared by all active stimulus generators, so all generators can have up to Auxiliary Buffer Size total in data points for playback."""
        return _wrap(self._dotnet_instance.AuxilliaryBufferSize)

    @auxilliary_buffer_size.setter
    def auxilliary_buffer_size(self, value: int):
        """Gets or sets the size of the auxiliary buffer. The auxiliary buffer stores multi-point playback data in comma-separated value (CSV), files. Set this buffer size to a number that matches or exceeds the number of data points in the CSV file you want to play back. The auxiliary buffer size is shared by all active stimulus generators, so all generators can have up to Auxiliary Buffer Size total in data points for playback."""
        self._dotnet_instance.AuxilliaryBufferSize = next(_unwrap(None, value))

    @property
    def analysis_buffer_size(self) -> int:
        """Gets or sets the size of the analysis buffer. The analysis buffer stores the expected result values for a table test. Set this value to a number that matches or exceeds the number of expected result values in a given table test."""
        return _wrap(self._dotnet_instance.AnalysisBufferSize)

    @analysis_buffer_size.setter
    def analysis_buffer_size(self, value: int):
        """Gets or sets the size of the analysis buffer. The analysis buffer stores the expected result values for a table test. Set this value to a number that matches or exceeds the number of expected result values in a given table test."""
        self._dotnet_instance.AnalysisBufferSize = next(_unwrap(None, value))

    @property
    def analysis_result_size(self) -> int:
        """Gets or sets the size of the analysis failure result buffer. The analysis failure result buffer stores the failure results for a table test. Set this value to a number that meets or exceeds the maximum number of failures you expect to occur in the table test."""
        return _wrap(self._dotnet_instance.AnalysisResultSize)

    @analysis_result_size.setter
    def analysis_result_size(self, value: int):
        """Gets or sets the size of the analysis failure result buffer. The analysis failure result buffer stores the failure results for a table test. Set this value to a number that meets or exceeds the maximum number of failures you expect to occur in the table test."""
        self._dotnet_instance.AnalysisResultSize = next(_unwrap(None, value))

    @overload
    def set_generator_count(self, count: int) -> bool:
        ...

    def set_generator_count(self, *args):
        return _wrap(self._dotnet_instance.SetGeneratorCount(*_unwrap(None, *args)))

    @overload
    def get_generator_list(self) -> Sequence[Generator]:
        ...

    def get_generator_list(self, *args):
        return _wrap(self._dotnet_instance.GetGeneratorList(*_unwrap(None, *args)))


class SystemChannels(Section):
    """Represents the <format type="bold">System Channels</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains a variety of channels that monitor the state and condition of various aspects of the system."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SystemChannels:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SystemChannels")

    @overload
    def get_system_channels(self) -> Sequence[SystemChannel]:
        ...

    def get_system_channels(self, *args):
        return _wrap(self._dotnet_instance.GetSystemChannels(*_unwrap(None, *args)))


class SystemDefinition(_DotNetBase):
    """Represents a system definition file, which contains configuration settings for the VeriStand Engine. This class is the base class for configuring system definitions through this API."""

    @overload
    def __init__(self, name: str, description: str, creator: str, version: str, target_name: str, target_type: str, filepath: str):
        ...

    @overload
    def __init__(self, nivssdf_file: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinition:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinition(*_unwrap(None, *args))

    @property
    def version(self) -> Tuple[int, int, int, int]:
        """Gets the version number of the system definition file."""
        return _wrap(self._dotnet_instance.Version)

    @property
    def document_type(self) -> DocumentType:
        """The DocumentType for this SystemDefinition"""
        return _wrap(self._dotnet_instance.DocumentType)

    @property
    def root(self) -> Root:
        """Gets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Root" crefType="Unqualified" /> node of the system definition file."""
        return _wrap(self._dotnet_instance.Root)

    @overload
    def save_system_definition_file(self, filepath: str) -> Tuple[bool, str]:
        ...

    @overload
    def save_system_definition_file(self) -> Tuple[bool, str]:
        ...

    def save_system_definition_file(self, *args):
        return _wrap(self._dotnet_instance.SaveSystemDefinitionFile(*_unwrap(None, *args)))


class SystemDefinitionExtensions(_DotNetBase):
    """Extension methods to assist with manipulating the SystemDefinition"""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinitionExtensions:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SystemDefinitionExtensions")

    @staticmethod
    @overload
    def get_parent(base_node: BaseNode) -> BaseNode:
        ...

    @staticmethod
    @overload
    def get_parent(base_node_type: BaseNodeType) -> BaseNodeType:
        ...

    def get_parent(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinitionExtensions.GetParent(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def is_self_or_ancestor_of(base_node: BaseNode, potential_child: BaseNode) -> bool:
        ...

    @staticmethod
    @overload
    def is_self_or_ancestor_of(base_node_type: BaseNodeType, potential_child: BaseNodeType) -> bool:
        ...

    def is_self_or_ancestor_of(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinitionExtensions.IsSelfOrAncestorOf(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def get_descendant_channels(base_node: BaseNode) -> Iterable[BaseNode]:
        ...

    @staticmethod
    @overload
    def get_descendant_channels(base_nodes: Iterable[BaseNode], inclusion_filter: Callable[[IChannel], bool]) -> Iterable[BaseNode]:
        ...

    @staticmethod
    @overload
    def get_descendant_channels(base_node: BaseNode, inclusion_filter: Callable[[IChannel], bool]) -> Iterable[BaseNode]:
        ...

    @staticmethod
    @overload
    def get_descendant_channels(base_node: BaseNode, inclusion_filter: Callable[[IChannel], bool], recurse_predicate: Callable[[BaseNode], bool]) -> Iterable[BaseNode]:
        ...

    @staticmethod
    @overload
    def get_descendant_channels(base_node_type: BaseNodeType, inclusion_filter: Callable[[BaseNodeType], bool]) -> Iterable[BaseNodeType]:
        ...

    @staticmethod
    @overload
    def get_descendant_channels(base_node_type: BaseNodeType, inclusion_filter: Callable[[BaseNodeType], bool], recurse_predicate: Callable[[BaseNodeType], bool]) -> Iterable[BaseNodeType]:
        ...

    def get_descendant_channels(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinitionExtensions.GetDescendantChannels(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def is_deprecated(node: BaseNode) -> bool:
        ...

    @staticmethod
    @overload
    def is_deprecated(base_node_type: BaseNodeType) -> bool:
        ...

    def is_deprecated(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinitionExtensions.IsDeprecated(*_unwrap(None, *args)))


class SystemInitialization(Section):
    """Represents the <format type="bold">System Initialization</format> section of the system definition, which contains information about the order that multiple targets deploy relative to each other."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SystemInitialization:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SystemInitialization")

    @property
    def auto_start(self) -> bool:
        """Gets or sets whether the system runs the system definition file automatically after a target reboots or waits for a user to redeploy the file."""
        return _wrap(self._dotnet_instance.AutoStart)

    @auto_start.setter
    def auto_start(self, value: bool):
        """Gets or sets whether the system runs the system definition file automatically after a target reboots or waits for a user to redeploy the file."""
        self._dotnet_instance.AutoStart = next(_unwrap(None, value))


class SystemMappings(Section):
    """Represents the <format type="bold">System Mappings</format> section of the system definition, which stores information about how source channels within the system definition map to destination channels. Destination channels store the mapping information."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SystemMappings:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SystemMappings")


class Target(BaseNode):
    """Represents a target in the system definition."""

    @overload
    def __init__(self, name: str, target_type: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Target:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Target(*_unwrap(None, *args))

    @_staticproperty
    def username_property_string() -> str:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Target.UsernamePropertyString)

    @_staticproperty
    def password_property_string() -> str:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Target.PasswordPropertyString)

    @property
    def timing_source_daq_settings(self) -> TimingSourceSettingsOptions:
        """Gets or sets the timing source setting for the DAQ device that is timing the Primary Control Loop. This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.TimingSourceDAQSettings)

    @timing_source_daq_settings.setter
    def timing_source_daq_settings(self, value: TimingSourceSettingsOptions):
        """Gets or sets the timing source setting for the DAQ device that is timing the Primary Control Loop. This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        self._dotnet_instance.TimingSourceDAQSettings = next(_unwrap(None, value))

    @property
    def execution_mode(self) -> TargetExecutionMode:
        """Gets or sets the execution mode (parallel or low latency) of the loops of the VeriStand Engine."""
        return _wrap(self._dotnet_instance.ExecutionMode)

    @execution_mode.setter
    def execution_mode(self, value: TargetExecutionMode):
        """Gets or sets the execution mode (parallel or low latency) of the loops of the VeriStand Engine."""
        self._dotnet_instance.ExecutionMode = next(_unwrap(None, value))

    @property
    def control_loop_timing_source(self) -> TargetControlLoopTimingSource:
        """Gets the timing source for the Primary Control Loop."""
        return _wrap(self._dotnet_instance.ControlLoopTimingSource)

    @property
    def daq_timing_device(self) -> DAQDevice:
        """Gets or sets the DAQ device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.DAQTimingDevice)

    @property
    def custom_timing_device(self) -> CustomDevice:
        """Gets or sets the custom device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.CustomDeviceTiming" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.CustomTimingDevice)

    @property
    def daq_digital_lines_decimation(self) -> int:
        """Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at a rate of 100Hz. If you set the PCL to execute at a rate faster than 100Hz, use this property to specify a higher decimation value and reduce the frequency with which the PCL reads and writes the digital line values."""
        return _wrap(self._dotnet_instance.DAQDigitalLinesDecimation)

    @daq_digital_lines_decimation.setter
    def daq_digital_lines_decimation(self, value: int):
        """Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at a rate of 100Hz. If you set the PCL to execute at a rate faster than 100Hz, use this property to specify a higher decimation value and reduce the frequency with which the PCL reads and writes the digital line values."""
        self._dotnet_instance.DAQDigitalLinesDecimation = next(_unwrap(None, value))

    @property
    def daq_digital_lines_rate(self) -> float:
        """Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values.
            The DIO Loop, which receives and sends these values from and to the PCL, executes at this rate and cannot be faster than the PCL loop."""
        return _wrap(self._dotnet_instance.DAQDigitalLinesRate)

    @daq_digital_lines_rate.setter
    def daq_digital_lines_rate(self, value: float):
        """Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values.
            The DIO Loop, which receives and sends these values from and to the PCL, executes at this rate and cannot be faster than the PCL loop."""
        self._dotnet_instance.DAQDigitalLinesRate = next(_unwrap(None, value))

    @property
    def disable_target(self) -> bool:
        """Gets or sets the Boolean flag indicating whether a target is disabled."""
        return _wrap(self._dotnet_instance.DisableTarget)

    @disable_target.setter
    def disable_target(self, value: bool):
        """Gets or sets the Boolean flag indicating whether a target is disabled."""
        self._dotnet_instance.DisableTarget = next(_unwrap(None, value))

    @property
    def operating_system(self) -> str:
        """Gets or sets the operating system of the target."""
        return _wrap(self._dotnet_instance.OperatingSystem)

    @operating_system.setter
    def operating_system(self, value: str):
        """Gets or sets the operating system of the target."""
        self._dotnet_instance.OperatingSystem = next(_unwrap(None, value))

    @property
    def ip_address(self) -> str:
        """Gets or sets the IP address of the target."""
        return _wrap(self._dotnet_instance.IPAddress)

    @ip_address.setter
    def ip_address(self, value: str):
        """Gets or sets the IP address of the target."""
        self._dotnet_instance.IPAddress = next(_unwrap(None, value))

    @property
    def username(self) -> str:
        """Gets or sets the username for the target."""
        return _wrap(self._dotnet_instance.Username)

    @username.setter
    def username(self, value: str):
        """Gets or sets the username for the target."""
        self._dotnet_instance.Username = next(_unwrap(None, value))

    @property
    def password(self) -> str:
        """Gets or sets the password for the target."""
        return _wrap(self._dotnet_instance.Password)

    @password.setter
    def password(self, value: str):
        """Gets or sets the password for the target."""
        self._dotnet_instance.Password = next(_unwrap(None, value))

    @property
    def fpga_scan_interface_mode(self) -> int:
        """Gets or sets the interface mode for the NI Scan Engine on RT targets. You can use this property to override the current settings of the NI Scan Engine, which can be useful for certain C Series modules, such as NI 986x series devices. <format type="bold">(Windows)</format> This setting has no effect on Windows targets."""
        return _wrap(self._dotnet_instance.FPGAScanInterfaceMode)

    @fpga_scan_interface_mode.setter
    def fpga_scan_interface_mode(self, value: int):
        """Gets or sets the interface mode for the NI Scan Engine on RT targets. You can use this property to override the current settings of the NI Scan Engine, which can be useful for certain C Series modules, such as NI 986x series devices. <format type="bold">(Windows)</format> This setting has no effect on Windows targets."""
        self._dotnet_instance.FPGAScanInterfaceMode = next(_unwrap(None, value))

    @property
    def target_timing_mode(self) -> TargetTimingMode:
        """Gets or sets the timing mode for the target.  When an FPGA serves as the Primary Control Loop timing source, the mode affects certain performance characteristics of the system."""
        return _wrap(self._dotnet_instance.TargetTimingMode)

    @target_timing_mode.setter
    def target_timing_mode(self, value: TargetTimingMode):
        """Gets or sets the timing mode for the target.  When an FPGA serves as the Primary Control Loop timing source, the mode affects certain performance characteristics of the system."""
        self._dotnet_instance.TargetTimingMode = next(_unwrap(None, value))

    @property
    def primary_control_loop_processor(self) -> int:
        """Gets or sets the processor on which to execute the Primary Control Loop (PCL)."""
        return _wrap(self._dotnet_instance.PrimaryControlLoopProcessor)

    @primary_control_loop_processor.setter
    def primary_control_loop_processor(self, value: int):
        """Gets or sets the processor on which to execute the Primary Control Loop (PCL)."""
        self._dotnet_instance.PrimaryControlLoopProcessor = next(_unwrap(None, value))

    @property
    def data_processing_loop_processor(self) -> int:
        """Gets or sets the processor on which to execute the Data Processing Loop. -2 is any available processor. If you specify an invalid processor, the loop executes on the first available processor."""
        return _wrap(self._dotnet_instance.DataProcessingLoopProcessor)

    @data_processing_loop_processor.setter
    def data_processing_loop_processor(self, value: int):
        """Gets or sets the processor on which to execute the Data Processing Loop. -2 is any available processor. If you specify an invalid processor, the loop executes on the first available processor."""
        self._dotnet_instance.DataProcessingLoopProcessor = next(_unwrap(None, value))

    @property
    def data_processing_loop_decimation(self) -> int:
        """Gets or sets the execution rate of the Data Processing Loop (DPL). A value of 1 specifies that the DPL reads values on every iteration of the Primary Control Loop (PCL). You can specify a value higher than 1 to read PCL values less frequently and increase system execution."""
        return _wrap(self._dotnet_instance.DataProcessingLoopDecimation)

    @data_processing_loop_decimation.setter
    def data_processing_loop_decimation(self, value: int):
        """Gets or sets the execution rate of the Data Processing Loop (DPL). A value of 1 specifies that the DPL reads values on every iteration of the Primary Control Loop (PCL). You can specify a value higher than 1 to read PCL values less frequently and increase system execution."""
        self._dotnet_instance.DataProcessingLoopDecimation = next(_unwrap(None, value))

    @property
    def maximum_streamed_channels(self) -> int:
        """Gets or sets the maximum number of channels that the VeriStand Engine can stream to the host."""
        return _wrap(self._dotnet_instance.MaximumStreamedChannels)

    @maximum_streamed_channels.setter
    def maximum_streamed_channels(self, value: int):
        """Gets or sets the maximum number of channels that the VeriStand Engine can stream to the host."""
        self._dotnet_instance.MaximumStreamedChannels = next(_unwrap(None, value))

    @property
    def filter_daq_errors(self) -> bool:
        """Gets or sets whether to filter errors from NI-DAQmx function calls. Set this property to <see langword="true" /> if you do not want the system to shut down when an NI-DAQ device reports an error."""
        return _wrap(self._dotnet_instance.FilterDAQErrors)

    @filter_daq_errors.setter
    def filter_daq_errors(self, value: bool):
        """Gets or sets whether to filter errors from NI-DAQmx function calls. Set this property to <see langword="true" /> if you do not want the system to shut down when an NI-DAQ device reports an error."""
        self._dotnet_instance.FilterDAQErrors = next(_unwrap(None, value))

    @property
    def filter_watchdog_errors(self) -> bool:
        """Gets or sets whether to filter errors reported by the timing watchdog. For example, if you set the Primary Control Loop to execute at a high rate and your system contains large or complex models, the watchdog reports an error if the models cannot execute quickly enough to keep up with the Primary Control Loop. Set this property to <see langword="true" /> if you want NI VeriStand to ignore these errors."""
        return _wrap(self._dotnet_instance.FilterWatchdogErrors)

    @filter_watchdog_errors.setter
    def filter_watchdog_errors(self, value: bool):
        """Gets or sets whether to filter errors reported by the timing watchdog. For example, if you set the Primary Control Loop to execute at a high rate and your system contains large or complex models, the watchdog reports an error if the models cannot execute quickly enough to keep up with the Primary Control Loop. Set this property to <see langword="true" /> if you want NI VeriStand to ignore these errors."""
        self._dotnet_instance.FilterWatchdogErrors = next(_unwrap(None, value))

    @property
    def target_rate(self) -> float:
        """Gets or sets the execution rate of the target in hertz."""
        return _wrap(self._dotnet_instance.TargetRate)

    @target_rate.setter
    def target_rate(self, value: float):
        """Gets or sets the execution rate of the target in hertz."""
        self._dotnet_instance.TargetRate = next(_unwrap(None, value))

    @property
    def timeout(self) -> float:
        """Gets or sets the amount of time to wait for a start trigger from the DAQ device before timing out. This property is only valid if the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.Timeout)

    @timeout.setter
    def timeout(self, value: float):
        """Gets or sets the amount of time to wait for a start trigger from the DAQ device before timing out. This property is only valid if the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        self._dotnet_instance.Timeout = next(_unwrap(None, value))

    @property
    def daq_timeout(self) -> int:
        """Gets the amount of time to wait for a DAQ device to transfer data before timing out. This property is only valid of the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.DAQTimeout)

    @property
    def timed_loop_sleep_time(self) -> int:
        """Gets the amount of time in microseconds the Primary Control Loop (PCL) sleeps after each tick. NI VeriStand ignores this value if the master timing device has an external timing source."""
        return _wrap(self._dotnet_instance.TimedLoopSleepTime)

    @property
    def deployment_group(self) -> int:
        """Gets or sets the deployment group to which a target belongs."""
        return _wrap(self._dotnet_instance.DeploymentGroup)

    @deployment_group.setter
    def deployment_group(self, value: int):
        """Gets or sets the deployment group to which a target belongs."""
        self._dotnet_instance.DeploymentGroup = next(_unwrap(None, value))

    @property
    def warmup_time_ms(self) -> int:
        """Gets or sets the amount of time the system waits before considering late flags. You can set a warm-up time to give the system time to allocate and manage resources."""
        return _wrap(self._dotnet_instance.WarmupTime_ms)

    @warmup_time_ms.setter
    def warmup_time_ms(self, value: int):
        """Gets or sets the amount of time the system waits before considering late flags. You can set a warm-up time to give the system time to allocate and manage resources."""
        self._dotnet_instance.WarmupTime_ms = next(_unwrap(None, value))

    @property
    def data_rate(self) -> float:
        """Gets or sets the rate for updating channel values in the Send Communication Loop."""
        return _wrap(self._dotnet_instance.DataRate)

    @data_rate.setter
    def data_rate(self, value: float):
        """Gets or sets the rate for updating channel values in the Send Communication Loop."""
        self._dotnet_instance.DataRate = next(_unwrap(None, value))

    @overload
    def set_control_loop_timing_source_to_automatic(self) -> bool:
        ...

    def set_control_loop_timing_source_to_automatic(self, *args):
        return _wrap(self._dotnet_instance.SetControlLoopTimingSourceToAutomatic(*_unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def set_control_loop_timing_source_to_daq(self, daq_device_name: str, daq_timeout: int, timed_loop_sleep_time: int) -> bool:
        ...

    def set_control_loop_timing_source_to_daq(self, *args):
        return _wrap(self._dotnet_instance.SetControlLoopTimingSourceToDAQ(*_unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def set_control_loop_timing_source_to_custom_device(self, custom_device_name: str) -> bool:
        ...

    def set_control_loop_timing_source_to_custom_device(self, *args):
        return _wrap(self._dotnet_instance.SetControlLoopTimingSourceToCustomDevice(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def get_system_channels(self) -> SystemChannels:
        ...

    def get_system_channels(self, *args):
        return _wrap(self._dotnet_instance.GetSystemChannels(*_unwrap(None, *args)))

    @overload
    def get_hardware(self) -> Hardware:
        ...

    def get_hardware(self, *args):
        return _wrap(self._dotnet_instance.GetHardware(*_unwrap(None, *args)))

    @overload
    def get_stimulus(self) -> Stimulus:
        ...

    def get_stimulus(self, *args):
        return _wrap(self._dotnet_instance.GetStimulus(*_unwrap(None, *args)))

    @overload
    def get_simulation_models(self) -> SimulationModels:
        ...

    def get_simulation_models(self, *args):
        return _wrap(self._dotnet_instance.GetSimulationModels(*_unwrap(None, *args)))

    @overload
    def get_alarms(self) -> Alarms:
        ...

    def get_alarms(self, *args):
        return _wrap(self._dotnet_instance.GetAlarms(*_unwrap(None, *args)))

    @overload
    def get_procedures(self) -> Procedures:
        ...

    def get_procedures(self, *args):
        return _wrap(self._dotnet_instance.GetProcedures(*_unwrap(None, *args)))

    @overload
    def get_custom_devices(self) -> CustomDevices:
        ...

    def get_custom_devices(self, *args):
        return _wrap(self._dotnet_instance.GetCustomDevices(*_unwrap(None, *args)))

    @overload
    def get_user_channels(self) -> UserChannels:
        ...

    def get_user_channels(self, *args):
        return _wrap(self._dotnet_instance.GetUserChannels(*_unwrap(None, *args)))

    @overload
    def get_calculated_channels(self) -> CalculatedChannels:
        ...

    def get_calculated_channels(self, *args):
        return _wrap(self._dotnet_instance.GetCalculatedChannels(*_unwrap(None, *args)))

    @overload
    def get_xnet_databases(self) -> XNETDatabases:
        ...

    def get_xnet_databases(self, *args):
        return _wrap(self._dotnet_instance.GetXNETDatabases(*_unwrap(None, *args)))


class TargetControlLoopTimingSource(_DotNetEnum):
    """Specifies the timing source for the system. The timing source times the system by sending ticks to the Primary Control Loop."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for TargetControlLoopTimingSource")

    @_staticproperty
    def AUTOMATIC_TIMING() -> TargetControlLoopTimingSource:
        return TargetControlLoopTimingSource(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource, "AutomaticTiming"), "AUTOMATIC_TIMING")

    @_staticproperty
    def DAQ_TIMING() -> TargetControlLoopTimingSource:
        return TargetControlLoopTimingSource(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource, "DAQTiming"), "DAQ_TIMING")

    @_staticproperty
    def CUSTOM_DEVICE_TIMING() -> TargetControlLoopTimingSource:
        return TargetControlLoopTimingSource(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource, "CustomDeviceTiming"), "CUSTOM_DEVICE_TIMING")


class TargetExecutionMode(_DotNetEnum):
    """Specifies the execution mode for the loops of the VeriStand Engine."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TargetExecutionMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for TargetExecutionMode")

    @_staticproperty
    def PARALLEL() -> TargetExecutionMode:
        return TargetExecutionMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetExecutionMode, "Parallel"), "PARALLEL")

    @_staticproperty
    def LOW_LATENCY() -> TargetExecutionMode:
        return TargetExecutionMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetExecutionMode, "LowLatency"), "LOW_LATENCY")


class TargetTimingMode(_DotNetEnum):
    """The timing mode of the target."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TargetTimingMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for TargetTimingMode")

    @_staticproperty
    def AUTO() -> TargetTimingMode:
        return TargetTimingMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetTimingMode, "Auto"), "AUTO")

    @_staticproperty
    def WAIT_ON_INTERRUPT() -> TargetTimingMode:
        return TargetTimingMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetTimingMode, "WaitOnInterrupt"), "WAIT_ON_INTERRUPT")

    @_staticproperty
    def WAIT_ON_DMA_READ() -> TargetTimingMode:
        return TargetTimingMode(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetTimingMode, "WaitOnDmaRead"), "WAIT_ON_DMA_READ")


class Targets(BaseNode):
    """Represents the <format type="bold">Targets</format> section of the system definition, which contains all the targets you configure."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Targets:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Targets")

    @overload
    def get_target_list(self) -> Sequence[Target]:
        ...

    def get_target_list(self, *args):
        return _wrap(self._dotnet_instance.GetTargetList(*_unwrap(None, *args)))

    @overload
    def add_target(self, target: Target) -> bool:
        ...

    def add_target(self, *args):
        return _wrap(self._dotnet_instance.AddTarget(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class TaskType(_DotNetEnum):
    """This enumeration is used to select the Task Type."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TaskType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for TaskType")

    @_staticproperty
    def ANALOG_INPUT() -> TaskType:
        return TaskType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TaskType, "AnalogInput"), "ANALOG_INPUT")


class TemperatureUnit(_DotNetEnum):
    """Defines the Temperature Unit of the thermocouple."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TemperatureUnit:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for TemperatureUnit")

    @_staticproperty
    def CELSIUS() -> TemperatureUnit:
        return TemperatureUnit(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TemperatureUnit, "Celsius"), "CELSIUS")

    @_staticproperty
    def FAHRENHEIT() -> TemperatureUnit:
        return TemperatureUnit(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TemperatureUnit, "Fahrenheit"), "FAHRENHEIT")

    @_staticproperty
    def KELVIN() -> TemperatureUnit:
        return TemperatureUnit(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TemperatureUnit, "Kelvin"), "KELVIN")

    @_staticproperty
    def RANKINE() -> TemperatureUnit:
        return TemperatureUnit(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TemperatureUnit, "Rankine"), "RANKINE")


class ThermocoupleCJCType(_DotNetEnum):
    """Defines the CJC type."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ThermocoupleCJCType")

    @_staticproperty
    def IC_SENSOR() -> ThermocoupleCJCType:
        return ThermocoupleCJCType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "ICSensor"), "IC_SENSOR")

    @_staticproperty
    def THERMISTOR() -> ThermocoupleCJCType:
        return ThermocoupleCJCType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "Thermistor"), "THERMISTOR")

    @_staticproperty
    def TEMPERATURE() -> ThermocoupleCJCType:
        return ThermocoupleCJCType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "Temperature"), "TEMPERATURE")

    @_staticproperty
    def NI9211() -> ThermocoupleCJCType:
        return ThermocoupleCJCType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "NI9211"), "NI9211")

    @_staticproperty
    def NI9213() -> ThermocoupleCJCType:
        return ThermocoupleCJCType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "NI9213"), "NI9213")

    @_staticproperty
    def NI9219() -> ThermocoupleCJCType:
        return ThermocoupleCJCType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "NI9219"), "NI9219")

    @_staticproperty
    def NI9214() -> ThermocoupleCJCType:
        return ThermocoupleCJCType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "NI9214"), "NI9214")


class ThermocoupleType(_DotNetEnum):
    """Defines the thermocouple type."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ThermocoupleType")

    @_staticproperty
    def B() -> ThermocoupleType:
        return ThermocoupleType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "B"), "B")

    @_staticproperty
    def E() -> ThermocoupleType:
        return ThermocoupleType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "E"), "E")

    @_staticproperty
    def J() -> ThermocoupleType:
        return ThermocoupleType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "J"), "J")

    @_staticproperty
    def K() -> ThermocoupleType:
        return ThermocoupleType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "K"), "K")

    @_staticproperty
    def R() -> ThermocoupleType:
        return ThermocoupleType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "R"), "R")

    @_staticproperty
    def S() -> ThermocoupleType:
        return ThermocoupleType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "S"), "S")

    @_staticproperty
    def T() -> ThermocoupleType:
        return ThermocoupleType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "T"), "T")

    @_staticproperty
    def N() -> ThermocoupleType:
        return ThermocoupleType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "N"), "N")


class TimingAndSync(Section):
    """Represents the <format type="bold">Timing and Sync</format> section of the system definition, which contains all configured timing and sync devices."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TimingAndSync:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for TimingAndSync")

    @overload
    def get_timing_and_sync_device_list(self) -> Sequence[TimingAndSyncDevice]:
        ...

    def get_timing_and_sync_device_list(self, *args):
        return _wrap(self._dotnet_instance.GetTimingAndSyncDeviceList(*_unwrap(None, *args)))

    @overload
    def add_timing_and_sync_device(self, timing_and_sync_device: TimingAndSyncDevice) -> bool:
        ...

    def add_timing_and_sync_device(self, *args):
        return _wrap(self._dotnet_instance.AddTimingAndSyncDevice(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class TimingSourceSettingsOptions(_DotNetEnum):
    """Specifies the DAQ timing source setting for the Primary Control Loop when the PCL timing source is set to DAQ."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TimingSourceSettingsOptions:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for TimingSourceSettingsOptions")

    @_staticproperty
    def CONTROL_LOOP_FROM_TASK() -> TimingSourceSettingsOptions:
        return TimingSourceSettingsOptions(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TimingSourceSettingsOptions, "ControlLoopFromTask"), "CONTROL_LOOP_FROM_TASK")

    @_staticproperty
    def SIGNAL_FROM_TASK__SAMPLE_COMPLETE() -> TimingSourceSettingsOptions:
        return TimingSourceSettingsOptions(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TimingSourceSettingsOptions, "SignalFromTask_SampleComplete"), "SIGNAL_FROM_TASK__SAMPLE_COMPLETE")


class TriggerType(_DotNetEnum):
    """Defines the type of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TriggerType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for TriggerType")

    @_staticproperty
    def NONE() -> TriggerType:
        return TriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TriggerType, "None"), "NONE")

    @_staticproperty
    def ANALOG_EDGE() -> TriggerType:
        return TriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TriggerType, "AnalogEdge"), "ANALOG_EDGE")

    @_staticproperty
    def ANALOG_WINDOW() -> TriggerType:
        return TriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TriggerType, "AnalogWindow"), "ANALOG_WINDOW")

    @_staticproperty
    def DIGITAL_EDGE() -> TriggerType:
        return TriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TriggerType, "DigitalEdge"), "DIGITAL_EDGE")

    @_staticproperty
    def SOFTWARE() -> TriggerType:
        return TriggerType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TriggerType, "Software"), "SOFTWARE")


class Unconditional(Section):
    """Represents the <format type="bold">Unconditional</format> section that contains outgoing, unconditional frames under an NI-XNET LIN port."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Unconditional:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Unconditional")

    @overload
    def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]:
        ...

    def get_signal_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetSignalBasedFrameList(*_unwrap(None, *args)))

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetRawDataBasedFrameList(*_unwrap(None, *args)))

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddSignalBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddRawDataBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class UserChannels(Section):
    """Represents the <format type="bold">User Channels</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains any user channels you configure. User channels store a single value, and can be variables in procedures, stimulus profiles, and so on."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.UserChannels:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for UserChannels")

    @overload
    def get_user_channel_list(self) -> Sequence[UserChannel]:
        ...

    @overload
    def get_user_channel_list(self, deep: bool) -> Sequence[UserChannel]:
        ...

    def get_user_channel_list(self, *args):
        return _wrap(self._dotnet_instance.GetUserChannelList(*_unwrap(None, *args)))

    @overload
    def get_user_channel_folder_list(self) -> Sequence[UserChannelsFolder]:
        ...

    @overload
    def get_user_channel_folder_list(self, deep: bool) -> Sequence[UserChannelsFolder]:
        ...

    def get_user_channel_folder_list(self, *args):
        return _wrap(self._dotnet_instance.GetUserChannelFolderList(*_unwrap(None, *args)))

    @overload
    def add_user_channel(self, channel: UserChannel) -> bool:
        ...

    def add_user_channel(self, *args):
        return _wrap(self._dotnet_instance.AddUserChannel(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_user_channels_folder(self, folder: UserChannelsFolder) -> bool:
        ...

    def add_user_channels_folder(self, *args):
        return _wrap(self._dotnet_instance.AddUserChannelsFolder(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_user_channel(self, name: str, description: str, units: str, default_value: float) -> UserChannel:
        ...

    def add_new_user_channel(self, *args):
        return _wrap(self._dotnet_instance.AddNewUserChannel(*_unwrap({None: (4, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_user_channels_folder(self, name: str, description: str) -> UserChannelsFolder:
        ...

    def add_new_user_channels_folder(self, *args):
        return _wrap(self._dotnet_instance.AddNewUserChannelsFolder(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class UserChannelsFolder(Section):
    """Represents a folder under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.UserChannels" crefType="Unqualified" /> section of a target. Folders simply organize user channels into logical groups."""

    @overload
    def __init__(self, name: str, description: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.UserChannelsFolder:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.UserChannelsFolder(*_unwrap(None, *args))

    @overload
    def get_user_channel_list(self) -> Sequence[UserChannel]:
        ...

    @overload
    def get_user_channel_list(self, deep: bool) -> Sequence[UserChannel]:
        ...

    def get_user_channel_list(self, *args):
        return _wrap(self._dotnet_instance.GetUserChannelList(*_unwrap(None, *args)))

    @overload
    def get_user_channel_folder_list(self) -> Sequence[UserChannelsFolder]:
        ...

    @overload
    def get_user_channel_folder_list(self, deep: bool) -> Sequence[UserChannelsFolder]:
        ...

    def get_user_channel_folder_list(self, *args):
        return _wrap(self._dotnet_instance.GetUserChannelFolderList(*_unwrap(None, *args)))

    @overload
    def add_user_channel(self, channel: UserChannel) -> bool:
        ...

    def add_user_channel(self, *args):
        return _wrap(self._dotnet_instance.AddUserChannel(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_user_channels_folder(self, folder: UserChannelsFolder) -> bool:
        ...

    def add_user_channels_folder(self, *args):
        return _wrap(self._dotnet_instance.AddUserChannelsFolder(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_user_channel(self, name: str, description: str, units: str, default_value: float) -> UserChannel:
        ...

    def add_new_user_channel(self, *args):
        return _wrap(self._dotnet_instance.AddNewUserChannel(*_unwrap({None: (4, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_user_channels_folder(self, name: str, description: str) -> UserChannelsFolder:
        ...

    def add_new_user_channels_folder(self, *args):
        return _wrap(self._dotnet_instance.AddNewUserChannelsFolder(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Utilities(_DotNetBase):
    """Class that provides a way to perform various common operations within the system definition, such as stripping paths, converting data types, and creating channel mappings."""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities(*_unwrap(None, *args))

    @_staticproperty
    def current_version() -> VersionType:
        """Gets the current version information for the system definition file."""
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.CurrentVersion)

    @staticmethod
    @overload
    def serialize_slsc(filepath: str, node: BaseNodeType):
        ...

    def serialize_slsc(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.SerializeSLSC(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @staticmethod
    @overload
    def deserialize_slsc(filepath: str, base_node: BaseNodeType):
        ...

    def deserialize_slsc(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.DeserializeSLSC(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @staticmethod
    @overload
    def reset_all_identifiers(base_node_type: BaseNodeType):
        ...

    def reset_all_identifiers(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.ResetAllIdentifiers(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def date_time_to_double(date_time: System.DateTime) -> float:
        ...

    def date_time_to_double(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.DateTimeToDouble(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def double_to_date_time(total_seconds: float) -> System.DateTime:
        ...

    def double_to_date_time(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.DoubleToDateTime(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def version_type_to_version(versiontype: VersionType) -> Tuple[int, int, int, int]:
        ...

    def version_type_to_version(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.VersionTypeToVersion(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def get_localized_name_by_guid(guid: str) -> str:
        ...

    def get_localized_name_by_guid(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.GetLocalizedNameByGUID(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def resolve_path_type(root_path: str, file_path: str) -> DependentFileType:
        ...

    def resolve_path_type(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.ResolvePathType(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def strip_path(path: str) -> Tuple[str, str]:
        ...

    def strip_path(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.StripPath(*_unwrap({None: (1, "")}, *args)))

    @staticmethod
    @overload
    def get_filename(path: str) -> str:
        ...

    def get_filename(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.GetFilename(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def build_path(path: str, relative: str) -> str:
        ...

    def build_path(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.BuildPath(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def rt_main_path() -> str:
        ...

    def rt_main_path(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.RtMainPath(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def data_replay_rt_path() -> str:
        ...

    def data_replay_rt_path(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.DataReplayRTPath(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def relative_afp_ini_path() -> str:
        ...

    def relative_afp_ini_path(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.RelativeAfpIniPath(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def afp_rt_path() -> str:
        ...

    def afp_rt_path(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.AfpRtPath(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def path_type_pair_to_absolute_path(path: str, type: PathType) -> str:
        ...

    @staticmethod
    @overload
    def path_type_pair_to_absolute_path(path: str, type: DependentFilePropertyType, base_path: str) -> str:
        ...

    def path_type_pair_to_absolute_path(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.PathTypePairToAbsolutePath(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def strip_path_if_in_llb(file_path: str) -> str:
        ...

    def strip_path_if_in_llb(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.StripPathIfInLLB(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def add_mapping(source: Channel, destination: Channel):
        ...

    def add_mapping(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.AddMapping(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def clear_mapping(destination: Channel):
        ...

    def clear_mapping(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.ClearMapping(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def auto_map_channels(source_node: BaseNode, destination_node: BaseNode) -> Iterable[System.Collections.Generic.KeyValuePair[NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel,NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel]]:
        ...

    @staticmethod
    @overload
    def auto_map_channels(source_node: BaseNode, destination_node: BaseNode, comparer: System.IEqualityComparer) -> Iterable[System.Collections.Generic.KeyValuePair[NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel,NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel]]:
        ...

    @staticmethod
    @overload
    def auto_map_channels(source_node: BaseNode, destination_node: BaseNode, comparer: System.IEqualityComparer, inclusion_filter: Callable[[IChannel], bool]) -> Iterable[System.Collections.Generic.KeyValuePair[NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel,NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel]]:
        ...

    @staticmethod
    @overload
    def auto_map_channels(source_node: BaseNode, destination_node: BaseNode, comparer: System.IEqualityComparer, inclusion_filter: Callable[[IChannel], bool], recurse_predicate: Callable[[BaseNode], bool]) -> Iterable[System.Collections.Generic.KeyValuePair[NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel,NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel]]:
        ...

    def auto_map_channels(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.AutoMapChannels(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def default_auto_map_recursion_filter(node: BaseNode) -> bool:
        ...

    def default_auto_map_recursion_filter(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.DefaultAutoMapRecursionFilter(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def find_name_matches(source_channels: Iterable[IChannel], destination_channels: Iterable[IChannel], comparer: System.IEqualityComparer) -> Iterable[System.Collections.Generic.KeyValuePair[NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel,NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel]]:
        ...

    def find_name_matches(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.FindNameMatches(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def create_base_node_from_system_storage_node(storage_node: BaseNodeType) -> BaseNode:
        ...

    def create_base_node_from_system_storage_node(*args):
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.CreateBaseNodeFromSystemStorageNode(*_unwrap(None, *args)))


class ValueSource(_DotNetBase):
    """Represents the source of a channel value as a constant or a channel."""

    @overload
    def __init__(self, constant: float):
        ...

    @overload
    def __init__(self, channel: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ValueSource:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ValueSource(*_unwrap(None, *args))

    @property
    def is_constant(self) -> bool:
        return _wrap(self._dotnet_instance.isConstant)

    @property
    def channel(self) -> BaseNode:
        return _wrap(self._dotnet_instance.Channel)

    @property
    def constant(self) -> float:
        return _wrap(self._dotnet_instance.Constant)


class Waveform(BaseNode):
    """Represents a waveform in the system definition. This is a base class for more specific waveform classes, including hardware waveforms, custom device waveforms, and so on."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Waveform:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Waveform")

    @property
    def units(self) -> str:
        """Gets or sets the units associated with the waveform. This can be any arbitrary string."""
        return _wrap(self._dotnet_instance.Units)

    @units.setter
    def units(self, value: str):
        """Gets or sets the units associated with the waveform. This can be any arbitrary string."""
        self._dotnet_instance.Units = next(_unwrap(None, value))

    @property
    def data_type(self) -> WaveformTypeDataType:
        """Gets or sets the data type associated with the waveform."""
        return _wrap(self._dotnet_instance.DataType)

    @data_type.setter
    def data_type(self, value: WaveformTypeDataType):
        """Gets or sets the data type associated with the waveform."""
        self._dotnet_instance.DataType = next(_unwrap(None, value))


class WindowConditionType(_DotNetEnum):
    """Defines the signal condition that causes a window trigger."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.WindowConditionType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for WindowConditionType")

    @_staticproperty
    def ENTERING_WINDOW() -> WindowConditionType:
        return WindowConditionType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.WindowConditionType, "EnteringWindow"), "ENTERING_WINDOW")

    @_staticproperty
    def LEAVING_WINDOW() -> WindowConditionType:
        return WindowConditionType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.WindowConditionType, "LeavingWindow"), "LEAVING_WINDOW")


class XNET(Section):
    """Represents the <format type="bold">NI-XNET</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis" crefType="Unqualified" />, which contains any <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CAN" crefType="Unqualified" />, <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LIN" crefType="Unqualified" />, or <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRay" crefType="Unqualified" /> devices you configure."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.XNET:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for XNET")

    @property
    def decimation(self) -> int:
        """Gets or sets the processing rate for inline incoming and outgoing frames of an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> device, which NI VeriStand uses to calculate the decimation factor (decimation factor = Primary Control Loop rate/processing rate). This value determines how many iterations of the Primary Control Loop occur between calls to the device."""
        return _wrap(self._dotnet_instance.Decimation)

    @decimation.setter
    def decimation(self, value: int):
        """Gets or sets the processing rate for inline incoming and outgoing frames of an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> device, which NI VeriStand uses to calculate the decimation factor (decimation factor = Primary Control Loop rate/processing rate). This value determines how many iterations of the Primary Control Loop occur between calls to the device."""
        self._dotnet_instance.Decimation = next(_unwrap(None, value))

    @overload
    def enable_xnet(self):
        ...

    def enable_xnet(self, *args):
        return _wrap(self._dotnet_instance.EnableXNET(*_unwrap(None, *args)))

    @overload
    def disable_xnet(self):
        ...

    def disable_xnet(self, *args):
        return _wrap(self._dotnet_instance.DisableXNET(*_unwrap(None, *args)))

    @overload
    def get_can(self) -> CAN:
        ...

    def get_can(self, *args):
        return _wrap(self._dotnet_instance.GetCAN(*_unwrap(None, *args)))

    @overload
    def get_flex_ray(self) -> FlexRay:
        ...

    def get_flex_ray(self, *args):
        return _wrap(self._dotnet_instance.GetFlexRay(*_unwrap(None, *args)))

    @overload
    def get_lin(self) -> LIN:
        ...

    def get_lin(self, *args):
        return _wrap(self._dotnet_instance.GetLIN(*_unwrap(None, *args)))


class XNETDatabases(Section):
    """Represents the <format type="bold">XNET Databases</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains any XNET Databases you add to the system definition to run <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> devices."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.XNETDatabases:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for XNETDatabases")

    @overload
    def get_database_list(self) -> Sequence[Database]:
        ...

    def get_database_list(self, *args):
        return _wrap(self._dotnet_instance.GetDatabaseList(*_unwrap(None, *args)))

    @overload
    def add_database(self, database: Database) -> bool:
        ...

    def add_database(self, *args):
        return _wrap(self._dotnet_instance.AddDatabase(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class XNETTermination(_DotNetEnum):
    """Configures onboard termination for the XNET port. Termination behavior differs depending on the type of device you are using (CAN, FlexRay, or LIN)."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for XNETTermination")

    @_staticproperty
    def OFF() -> XNETTermination:
        return XNETTermination(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination, "Off"), "OFF")

    @_staticproperty
    def ON() -> XNETTermination:
        return XNETTermination(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination, "On"), "ON")


class Alarm(Section):
    """Represents an alarm, which notifies the user that the value of a particular channel has gone outside a specified range of values. Alarms also can trigger the execution of a specified procedure."""

    @overload
    def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: ValueSource, lower_limit: ValueSource, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, group_number: int, priority_number: int, delay: float, trip_message: str):
        ...

    @overload
    def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: ValueSource, lower_limit: ValueSource, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, group_number: int, priority_number: int, delay: float, trip_message: str, auto_reset_alarm: bool, require_alarm_acknowledgement: bool):
        ...

    @overload
    def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: float, lower_limit: float, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str):
        ...

    @overload
    def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: float, lower_limit: BaseNode, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str):
        ...

    @overload
    def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: BaseNode, lower_limit: float, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str):
        ...

    @overload
    def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: BaseNode, lower_limit: BaseNode, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm(*_unwrap(None, *args))

    @property
    def mode(self) -> AlarmMode:
        """Gets or sets the mode of the alarm (<format type="monospace">Normal</format> or <format type="monospace">IndicateOnly</format>)."""
        return _wrap(self._dotnet_instance.Mode)

    @mode.setter
    def mode(self, value: AlarmMode):
        """Gets or sets the mode of the alarm (<format type="monospace">Normal</format> or <format type="monospace">IndicateOnly</format>)."""
        self._dotnet_instance.Mode = next(_unwrap(None, value))

    @property
    def priority_number(self) -> int:
        """Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31."""
        return _wrap(self._dotnet_instance.PriorityNumber)

    @priority_number.setter
    def priority_number(self, value: int):
        """Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31."""
        self._dotnet_instance.PriorityNumber = next(_unwrap(None, value))

    @property
    def group_number(self) -> int:
        """Gets or sets the number of the group to which an alarm belongs."""
        return _wrap(self._dotnet_instance.GroupNumber)

    @group_number.setter
    def group_number(self, value: int):
        """Gets or sets the number of the group to which an alarm belongs."""
        self._dotnet_instance.GroupNumber = next(_unwrap(None, value))

    @property
    def priority(self) -> AlarmPriority:
        """This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>"""
        return _wrap(self._dotnet_instance.Priority)

    @priority.setter
    def priority(self, value: AlarmPriority):
        """This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>"""
        self._dotnet_instance.Priority = next(_unwrap(None, value))

    @property
    def default_state(self) -> AlarmState:
        """Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm."""
        return _wrap(self._dotnet_instance.DefaultState)

    @default_state.setter
    def default_state(self, value: AlarmState):
        """Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm."""
        self._dotnet_instance.DefaultState = next(_unwrap(None, value))

    @property
    def auto_reset_alarm(self) -> bool:
        """Gets or sets the reset behavior of the alarm. This property defines whether the alarm automatically resets when the channel is back in range, as opposed to being reset by a procedure."""
        return _wrap(self._dotnet_instance.AutoResetAlarm)

    @auto_reset_alarm.setter
    def auto_reset_alarm(self, value: bool):
        """Gets or sets the reset behavior of the alarm. This property defines whether the alarm automatically resets when the channel is back in range, as opposed to being reset by a procedure."""
        self._dotnet_instance.AutoResetAlarm = next(_unwrap(None, value))

    @property
    def require_alarm_acknowledgement(self) -> bool:
        """Gets or sets the acknowledgement behavior of the alarm. This property defines whether the alarm must be manually acknowledged before it can reset. Otherwise, alarm is automatically acknowledged when the channel is back in range."""
        return _wrap(self._dotnet_instance.RequireAlarmAcknowledgement)

    @require_alarm_acknowledgement.setter
    def require_alarm_acknowledgement(self, value: bool):
        """Gets or sets the acknowledgement behavior of the alarm. This property defines whether the alarm must be manually acknowledged before it can reset. Otherwise, alarm is automatically acknowledged when the channel is back in range."""
        self._dotnet_instance.RequireAlarmAcknowledgement = next(_unwrap(None, value))

    @property
    def delay(self) -> float:
        """Gets or sets the amount of time to wait before triggering the alarm."""
        return _wrap(self._dotnet_instance.Delay)

    @delay.setter
    def delay(self, value: float):
        """Gets or sets the amount of time to wait before triggering the alarm."""
        self._dotnet_instance.Delay = next(_unwrap(None, value))

    @property
    def alarm_source(self) -> BaseNode:
        """Gets or sets the channel to monitor for alarm conditions."""
        return _wrap(self._dotnet_instance.AlarmSource)

    @alarm_source.setter
    def alarm_source(self, value: BaseNode):
        """Gets or sets the channel to monitor for alarm conditions."""
        self._dotnet_instance.AlarmSource = next(_unwrap(None, value))

    @property
    def upper_limit_is_constant(self) -> int:
        """Gets whether the upper limit value of the alarm is specified by a constant or a channel."""
        return _wrap(self._dotnet_instance.UpperLimitIsConstant)

    @property
    def upper_limit_constant(self) -> float:
        """Gets the constant that determines the upper limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered."""
        return _wrap(self._dotnet_instance.UpperLimitConstant)

    @property
    def lower_limit_is_constant(self) -> int:
        """Gets whether the lower limit value of the alarm is specified by a constant or a channel."""
        return _wrap(self._dotnet_instance.LowerLimitIsConstant)

    @property
    def lower_limit_constant(self) -> float:
        """Gets the constant value that determines the lower limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered."""
        return _wrap(self._dotnet_instance.LowerLimitConstant)

    @property
    def upper_limit_channel(self) -> BaseNode:
        """Gets the channel that determines the upper limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered."""
        return _wrap(self._dotnet_instance.UpperLimitChannel)

    @property
    def lower_limit_channel(self) -> BaseNode:
        """Gets the channel that determines the lower limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered."""
        return _wrap(self._dotnet_instance.LowerLimitChannel)

    @property
    def alarm_action(self) -> BaseNode:
        """Gets or sets the procedure to initiate when the alarm conditions are met."""
        return _wrap(self._dotnet_instance.AlarmAction)

    @alarm_action.setter
    def alarm_action(self, value: BaseNode):
        """Gets or sets the procedure to initiate when the alarm conditions are met."""
        self._dotnet_instance.AlarmAction = next(_unwrap(None, value))

    @property
    def trip_message(self) -> str:
        """Gets or sets the message to display when the alarm is tripped."""
        return _wrap(self._dotnet_instance.TripMessage)

    @trip_message.setter
    def trip_message(self, value: str):
        """Gets or sets the message to display when the alarm is tripped."""
        self._dotnet_instance.TripMessage = next(_unwrap(None, value))

    @overload
    def set_upper_limit(self, upper_limit: float):
        ...

    @overload
    def set_upper_limit(self, upper_limit: BaseNode):
        ...

    @overload
    def set_upper_limit(self, limit: ValueSource):
        ...

    def set_upper_limit(self, *args):
        return _wrap(self._dotnet_instance.SetUpperLimit(*_unwrap(None, *args)))

    @overload
    def set_lower_limit(self, lower_limit: float):
        ...

    @overload
    def set_lower_limit(self, lower_limit: BaseNode):
        ...

    @overload
    def set_lower_limit(self, limit: ValueSource):
        ...

    def set_lower_limit(self, *args):
        return _wrap(self._dotnet_instance.SetLowerLimit(*_unwrap(None, *args)))

    @overload
    def add_alarm_status_channel(self) -> bool:
        ...

    def add_alarm_status_channel(self, *args):
        return _wrap(self._dotnet_instance.AddAlarmStatusChannel(*_unwrap(None, *args)))

    @overload
    def get_alarm_status_channel(self) -> AlarmStatus:
        ...

    def get_alarm_status_channel(self, *args):
        return _wrap(self._dotnet_instance.GetAlarmStatusChannel(*_unwrap(None, *args)))


class AlarmFolder(Section):
    """Represents an alarm folder, which organizes alarms under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarms" crefType="Unqualified" /> section."""

    @overload
    def __init__(self, name: str, description: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmFolder:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmFolder(*_unwrap(None, *args))

    @overload
    def get_alarm_list(self) -> Sequence[Alarm]:
        ...

    @overload
    def get_alarm_list(self, deep: bool) -> Sequence[Alarm]:
        ...

    def get_alarm_list(self, *args):
        return _wrap(self._dotnet_instance.GetAlarmList(*_unwrap(None, *args)))

    @overload
    def get_alarm_folder_list(self) -> Sequence[AlarmFolder]:
        ...

    @overload
    def get_alarm_folder_list(self, deep: bool) -> Sequence[AlarmFolder]:
        ...

    def get_alarm_folder_list(self, *args):
        return _wrap(self._dotnet_instance.GetAlarmFolderList(*_unwrap(None, *args)))

    @overload
    def add_alarm(self, alarm: Alarm) -> bool:
        ...

    def add_alarm(self, *args):
        return _wrap(self._dotnet_instance.AddAlarm(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_alarm_folder(self, folder: AlarmFolder) -> bool:
        ...

    def add_alarm_folder(self, *args):
        return _wrap(self._dotnet_instance.AddAlarmFolder(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: ValueSource, lower_limit: ValueSource, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, group_number: int, priority_number: int, delay: float, trip_message: str) -> Alarm:
        ...

    def add_new_alarm(self, *args):
        return _wrap(self._dotnet_instance.AddNewAlarm(*_unwrap({None: (12, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_alarm_folder(self, name: str, description: str) -> AlarmFolder:
        ...

    def add_new_alarm_folder(self, *args):
        return _wrap(self._dotnet_instance.AddNewAlarmFolder(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Alarms(Section):
    """Represents the <format type="bold">Alarms</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains any configured <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmFolder" crefType="Unqualified" /> objects."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Alarms:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Alarms")

    @overload
    def get_alarm_list(self) -> Sequence[Alarm]:
        ...

    @overload
    def get_alarm_list(self, deep: bool) -> Sequence[Alarm]:
        ...

    def get_alarm_list(self, *args):
        return _wrap(self._dotnet_instance.GetAlarmList(*_unwrap(None, *args)))

    @overload
    def get_alarm_folder_list(self) -> Sequence[AlarmFolder]:
        ...

    @overload
    def get_alarm_folder_list(self, deep: bool) -> Sequence[AlarmFolder]:
        ...

    def get_alarm_folder_list(self, *args):
        return _wrap(self._dotnet_instance.GetAlarmFolderList(*_unwrap(None, *args)))

    @overload
    def add_alarm(self, alarm: Alarm) -> bool:
        ...

    def add_alarm(self, *args):
        return _wrap(self._dotnet_instance.AddAlarm(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_alarm_folder(self, folder: AlarmFolder) -> bool:
        ...

    def add_alarm_folder(self, *args):
        return _wrap(self._dotnet_instance.AddAlarmFolder(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: float, lower_limit: float, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str) -> Alarm:
        ...

    @overload
    def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: float, lower_limit: BaseNode, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str) -> Alarm:
        ...

    @overload
    def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: BaseNode, lower_limit: float, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str) -> Alarm:
        ...

    @overload
    def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: BaseNode, lower_limit: BaseNode, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str) -> Alarm:
        ...

    @overload
    def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: ValueSource, lower_limit: ValueSource, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, group_number: int, priority_number: int, delay: float, trip_message: str) -> Alarm:
        ...

    def add_new_alarm(self, *args):
        return _wrap(self._dotnet_instance.AddNewAlarm(*_unwrap({(str, str, Channel, (float, int), (float, int), Procedure, AlarmMode, AlarmState, AlarmPriority, (float, int), str): (11, NationalInstruments.VeriStand.Error.NoError), (str, str, Channel, (float, int), BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, (float, int), str): (11, NationalInstruments.VeriStand.Error.NoError), (str, str, Channel, BaseNode, (float, int), Procedure, AlarmMode, AlarmState, AlarmPriority, (float, int), str): (11, NationalInstruments.VeriStand.Error.NoError), (str, str, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, (float, int), str): (11, NationalInstruments.VeriStand.Error.NoError), (str, str, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, int, int, (float, int), str): (12, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_alarm_folder(self, name: str, description: str) -> AlarmFolder:
        ...

    def add_new_alarm_folder(self, *args):
        return _wrap(self._dotnet_instance.AddNewAlarmFolder(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Alias(BaseNode, IChannel):
    """Represents an alias, which defines an alternate name for a channel in a system definition file. You can use the alias name, rather than the full channel path, in the <format type="bold">Workspace</format> window and Stimulus Profile Editor."""

    @overload
    def __init__(self, name: str, description: str, linked_channel_path: str):
        ...

    @overload
    def __init__(self, name: str, description: str, linked_channel_reference: Channel):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Alias:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Alias(*_unwrap(None, *args))

    @property
    def linked_channel(self) -> BaseNode:
        """Gets or sets the channel that the alias represents."""
        return _wrap(self._dotnet_instance.LinkedChannel)

    @linked_channel.setter
    def linked_channel(self, value: BaseNode):
        """Gets or sets the channel that the alias represents."""
        self._dotnet_instance.LinkedChannel = next(_unwrap(None, value))


class AliasFolder(Section):
    """Represents a folder under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Aliases" crefType="Unqualified" /> section of the system definition. Folders simply organize aliases into logical groups."""

    @overload
    def __init__(self, name: str, description: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.AliasFolder:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.AliasFolder(*_unwrap(None, *args))

    @overload
    def get_aliases_list(self) -> Sequence[Alias]:
        ...

    @overload
    def get_aliases_list(self, deep: bool) -> Sequence[Alias]:
        ...

    def get_aliases_list(self, *args):
        return _wrap(self._dotnet_instance.GetAliasesList(*_unwrap(None, *args)))

    @overload
    def get_alias_folder_list(self) -> Sequence[AliasFolder]:
        ...

    @overload
    def get_alias_folder_list(self, deep: bool) -> Sequence[AliasFolder]:
        ...

    def get_alias_folder_list(self, *args):
        return _wrap(self._dotnet_instance.GetAliasFolderList(*_unwrap(None, *args)))

    @overload
    def add_alias(self, alias: Alias) -> bool:
        ...

    def add_alias(self, *args):
        return _wrap(self._dotnet_instance.AddAlias(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_alias_folder(self, folder: AliasFolder) -> bool:
        ...

    def add_alias_folder(self, *args):
        return _wrap(self._dotnet_instance.AddAliasFolder(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_alias_by_path(self, name: str, description: str, linked_channel_path: str) -> Alias:
        ...

    def add_new_alias_by_path(self, *args):
        return _wrap(self._dotnet_instance.AddNewAliasByPath(*_unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_alias_by_reference(self, name: str, description: str, linked_channel_reference: Channel) -> Alias:
        ...

    def add_new_alias_by_reference(self, *args):
        return _wrap(self._dotnet_instance.AddNewAliasByReference(*_unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_alias_folder(self, name: str, description: str) -> AliasFolder:
        ...

    def add_new_alias_folder(self, *args):
        return _wrap(self._dotnet_instance.AddNewAliasFolder(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Aliases(Section):
    """Represents the <format type="bold">Aliases</format> section of the system definition, which contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alias" crefType="Unqualified" /> objects that define names you can use in place of full channel paths."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Aliases:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Aliases")

    @overload
    def delete_unmapped_aliases(self):
        ...

    def delete_unmapped_aliases(self, *args):
        return _wrap(self._dotnet_instance.DeleteUnmappedAliases(*_unwrap(None, *args)))

    @overload
    def import_aliases_from_file(self, file_path: str, inclusion_filter: Callable[[str], bool]):
        ...

    def import_aliases_from_file(self, *args):
        return _wrap(self._dotnet_instance.ImportAliasesFromFile(*_unwrap(None, *args)))

    @overload
    def export_aliases_to_file(self, file_path: str, inclusion_filter: Callable[[IChannel], bool], recurse_predicate: Callable[[BaseNode], bool]):
        ...

    def export_aliases_to_file(self, *args):
        return _wrap(self._dotnet_instance.ExportAliasesToFile(*_unwrap(None, *args)))

    @overload
    def get_aliases_list(self) -> Sequence[Alias]:
        ...

    @overload
    def get_aliases_list(self, deep: bool) -> Sequence[Alias]:
        ...

    def get_aliases_list(self, *args):
        return _wrap(self._dotnet_instance.GetAliasesList(*_unwrap(None, *args)))

    @overload
    def get_alias_folder_list(self) -> Sequence[AliasFolder]:
        ...

    @overload
    def get_alias_folder_list(self, deep: bool) -> Sequence[AliasFolder]:
        ...

    def get_alias_folder_list(self, *args):
        return _wrap(self._dotnet_instance.GetAliasFolderList(*_unwrap(None, *args)))

    @overload
    def add_alias(self, alias: Alias) -> bool:
        ...

    def add_alias(self, *args):
        return _wrap(self._dotnet_instance.AddAlias(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_alias_folder(self, folder: AliasFolder) -> bool:
        ...

    def add_alias_folder(self, *args):
        return _wrap(self._dotnet_instance.AddAliasFolder(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_alias_by_path(self, name: str, description: str, linked_channel_path: str) -> Alias:
        ...

    def add_new_alias_by_path(self, *args):
        return _wrap(self._dotnet_instance.AddNewAliasByPath(*_unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_alias_by_reference(self, name: str, description: str, linked_channel_reference: Channel) -> Alias:
        ...

    def add_new_alias_by_reference(self, *args):
        return _wrap(self._dotnet_instance.AddNewAliasByReference(*_unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_alias_folder(self, name: str, description: str) -> AliasFolder:
        ...

    def add_new_alias_folder(self, *args):
        return _wrap(self._dotnet_instance.AddNewAliasFolder(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class AutomaticFrameProcessing(Section):
    """Represents an <format type="bold">Automatic Frame Processing</format> section under an outgoing frame of an NI-XNET CAN port. The <format type="bold">Automatic Frame Processing</format> section contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter" crefType="Unqualified" /> channels."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for AutomaticFrameProcessing")

    @overload
    def get_crc(self) -> CRC:
        ...

    def get_crc(self, *args):
        return _wrap(self._dotnet_instance.GetCRC(*_unwrap(None, *args)))

    @overload
    def get_counter(self) -> Counter:
        ...

    def get_counter(self, *args):
        return _wrap(self._dotnet_instance.GetCounter(*_unwrap(None, *args)))


class CAN(Section):
    """Represents the <format type="bold">CAN</format> section under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> in the system definition."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CAN:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for CAN")

    @overload
    def get_can_port_list(self) -> Sequence[CANPort]:
        ...

    def get_can_port_list(self, *args):
        return _wrap(self._dotnet_instance.GetCANPortList(*_unwrap(None, *args)))

    @overload
    def add_can_port(self, can_port: CANPort) -> bool:
        ...

    def add_can_port(self, *args):
        return _wrap(self._dotnet_instance.AddCANPort(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class CANInterfaceChannels(Section):
    """Represents the <format type="bold">Interface</format> section under an NI-XNET CAN port. This section contains the port-specific channel that controls the port's sleep mode and channels which provide status information."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CANInterfaceChannels:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for CANInterfaceChannels")

    @overload
    def get_communication_state_channel(self) -> Channel:
        ...

    def get_communication_state_channel(self, *args):
        return _wrap(self._dotnet_instance.GetCommunicationStateChannel(*_unwrap(None, *args)))

    @overload
    def get_fault_channel(self) -> Channel:
        ...

    def get_fault_channel(self, *args):
        return _wrap(self._dotnet_instance.GetFaultChannel(*_unwrap(None, *args)))

    @overload
    def get_last_error_channel(self) -> Channel:
        ...

    def get_last_error_channel(self, *args):
        return _wrap(self._dotnet_instance.GetLastErrorChannel(*_unwrap(None, *args)))

    @overload
    def get_last_error_timestamp_channel(self) -> Channel:
        ...

    def get_last_error_timestamp_channel(self, *args):
        return _wrap(self._dotnet_instance.GetLastErrorTimestampChannel(*_unwrap(None, *args)))

    @overload
    def get_receive_error_counter_channel(self) -> Channel:
        ...

    def get_receive_error_counter_channel(self, *args):
        return _wrap(self._dotnet_instance.GetReceiveErrorCounterChannel(*_unwrap(None, *args)))

    @overload
    def get_sleep_mode_channel(self) -> SleepMode:
        ...

    def get_sleep_mode_channel(self, *args):
        return _wrap(self._dotnet_instance.GetSleepModeChannel(*_unwrap(None, *args)))

    @overload
    def get_transceiver_error_channel(self) -> Channel:
        ...

    def get_transceiver_error_channel(self, *args):
        return _wrap(self._dotnet_instance.GetTransceiverErrorChannel(*_unwrap(None, *args)))

    @overload
    def get_transmit_error_counter_channel(self) -> Channel:
        ...

    def get_transmit_error_counter_channel(self, *args):
        return _wrap(self._dotnet_instance.GetTransmitErrorCounterChannel(*_unwrap(None, *args)))

    @overload
    def add_sleep_mode_channel(self, sleep_mode: SleepMode) -> bool:
        ...

    def add_sleep_mode_channel(self, *args):
        return _wrap(self._dotnet_instance.AddSleepModeChannel(*_unwrap(None, *args)))

    @overload
    def create_communication_state_channel(self) -> Channel:
        ...

    def create_communication_state_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateCommunicationStateChannel(*_unwrap(None, *args)))

    @overload
    def create_fault_channel(self) -> Channel:
        ...

    def create_fault_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateFaultChannel(*_unwrap(None, *args)))

    @overload
    def create_last_error_channel(self) -> Channel:
        ...

    def create_last_error_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateLastErrorChannel(*_unwrap(None, *args)))

    @overload
    def create_last_error_timestamp_channel(self) -> Channel:
        ...

    def create_last_error_timestamp_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateLastErrorTimestampChannel(*_unwrap(None, *args)))

    @overload
    def create_receive_error_counter_channel(self) -> Channel:
        ...

    def create_receive_error_counter_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateReceiveErrorCounterChannel(*_unwrap(None, *args)))

    @overload
    def create_transceiver_error_channel(self) -> Channel:
        ...

    def create_transceiver_error_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateTransceiverErrorChannel(*_unwrap(None, *args)))

    @overload
    def create_transmit_error_counter_channel(self) -> Channel:
        ...

    def create_transmit_error_counter_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateTransmitErrorCounterChannel(*_unwrap(None, *args)))


class CANPort(Section):
    """Represents a port under the NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CAN" crefType="Unqualified" /> section."""

    @overload
    def __init__(self, name: str, port_number: int, linked_database: Database, cluster_name: str, baud_rate: int):
        ...

    @overload
    def __init__(self, name: str, port_number: int, linked_database: Database, cluster_name: str, baud_rate: int, fd_baud_rate: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort(*_unwrap(None, *args))

    @property
    def port_number(self) -> int:
        """Gets or sets the physical address of the CAN port."""
        return _wrap(self._dotnet_instance.PortNumber)

    @port_number.setter
    def port_number(self, value: int):
        """Gets or sets the physical address of the CAN port."""
        self._dotnet_instance.PortNumber = next(_unwrap(None, value))

    @property
    def linked_database(self) -> BaseNode:
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.LinkedDatabase)

    @linked_database.setter
    def linked_database(self, value: BaseNode):
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />."""
        self._dotnet_instance.LinkedDatabase = next(_unwrap(None, value))

    @property
    def baud_rate_bitfield(self) -> int:
        """Gets or sets the baud rate bitfield of the CAN port."""
        return _wrap(self._dotnet_instance.BaudRateBitfield)

    @baud_rate_bitfield.setter
    def baud_rate_bitfield(self, value: int):
        """Gets or sets the baud rate bitfield of the CAN port."""
        self._dotnet_instance.BaudRateBitfield = next(_unwrap(None, value))

    @property
    def baud_rate(self) -> int:
        """Gets or sets the baud rate of the CAN port."""
        return _wrap(self._dotnet_instance.BaudRate)

    @baud_rate.setter
    def baud_rate(self, value: int):
        """Gets or sets the baud rate of the CAN port."""
        self._dotnet_instance.BaudRate = next(_unwrap(None, value))

    @property
    def fd_baud_rate_bitfield(self) -> int:
        """Gets or sets the FD baud rate bitfield of the CAN port."""
        return _wrap(self._dotnet_instance.FDBaudRateBitfield)

    @fd_baud_rate_bitfield.setter
    def fd_baud_rate_bitfield(self, value: int):
        """Gets or sets the FD baud rate bitfield of the CAN port."""
        self._dotnet_instance.FDBaudRateBitfield = next(_unwrap(None, value))

    @property
    def fd_baud_rate(self) -> int:
        """Gets or sets the FD baud rate of the CAN port."""
        return _wrap(self._dotnet_instance.FDBaudRate)

    @fd_baud_rate.setter
    def fd_baud_rate(self, value: int):
        """Gets or sets the FD baud rate of the CAN port."""
        self._dotnet_instance.FDBaudRate = next(_unwrap(None, value))

    @property
    def fdiso_mode(self) -> FDISOMode:
        """Gets or sets the FD ISO mode of the CAN port."""
        return _wrap(self._dotnet_instance.FDISOMode)

    @fdiso_mode.setter
    def fdiso_mode(self, value: FDISOMode):
        """Gets or sets the FD ISO mode of the CAN port."""
        self._dotnet_instance.FDISOMode = next(_unwrap(None, value))

    @property
    def cluster_name(self) -> str:
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.ClusterName)

    @cluster_name.setter
    def cluster_name(self, value: str):
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />."""
        self._dotnet_instance.ClusterName = next(_unwrap(None, value))

    @property
    def incoming_rate(self) -> int:
        """Gets or sets the processing rate for incoming frames in hertz."""
        return _wrap(self._dotnet_instance.IncomingRate)

    @incoming_rate.setter
    def incoming_rate(self, value: int):
        """Gets or sets the processing rate for incoming frames in hertz."""
        self._dotnet_instance.IncomingRate = next(_unwrap(None, value))

    @property
    def outgoing_rate(self) -> int:
        """Gets or sets the processing rate for outgoing frames in hertz."""
        return _wrap(self._dotnet_instance.OutgoingRate)

    @outgoing_rate.setter
    def outgoing_rate(self, value: int):
        """Gets or sets the processing rate for outgoing frames in hertz."""
        self._dotnet_instance.OutgoingRate = next(_unwrap(None, value))

    @property
    def echo(self) -> bool:
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        return _wrap(self._dotnet_instance.Echo)

    @echo.setter
    def echo(self, value: bool):
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        self._dotnet_instance.Echo = next(_unwrap(None, value))

    @property
    def input_stream_queue_size(self) -> int:
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        return _wrap(self._dotnet_instance.InputStreamQueueSize)

    @input_stream_queue_size.setter
    def input_stream_queue_size(self, value: int):
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        self._dotnet_instance.InputStreamQueueSize = next(_unwrap(None, value))

    @property
    def can_bus_off(self) -> bool:
        """Gets or sets whether the CAN bus is recovered if it switches off due to a physical fault on the bus."""
        return _wrap(self._dotnet_instance.CANBusOff)

    @can_bus_off.setter
    def can_bus_off(self, value: bool):
        """Gets or sets whether the CAN bus is recovered if it switches off due to a physical fault on the bus."""
        self._dotnet_instance.CANBusOff = next(_unwrap(None, value))

    @property
    def can_bus_off_rate(self) -> int:
        """Gets or sets the bit rate at which to check the state of the CAN bus (active or off)."""
        return _wrap(self._dotnet_instance.CANBusOffRate)

    @can_bus_off_rate.setter
    def can_bus_off_rate(self, value: int):
        """Gets or sets the bit rate at which to check the state of the CAN bus (active or off)."""
        self._dotnet_instance.CANBusOffRate = next(_unwrap(None, value))

    @property
    def afpini_file(self) -> str:
        """Gets the name of the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort.AFPBinaryFile" crefType="Unqualified" /> used for automatic frame processing."""
        return _wrap(self._dotnet_instance.AFPINIFile)

    @property
    def afp_binary_file(self) -> DependentFile:
        """Gets the binary (<format type="monospace">.ini</format>) file used for automatic frame processing."""
        return _wrap(self._dotnet_instance.AFPBinaryFile)

    @property
    def afp_global_data(self) -> Sequence[int]:
        """Gets the global data used for automatic frame processing."""
        return _wrap(self._dotnet_instance.AFPGlobalData)

    @property
    def inline_incoming(self) -> bool:
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        return _wrap(self._dotnet_instance.InlineIncoming)

    @inline_incoming.setter
    def inline_incoming(self, value: bool):
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        self._dotnet_instance.InlineIncoming = next(_unwrap(None, value))

    @property
    def inline_outgoing(self) -> bool:
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        return _wrap(self._dotnet_instance.InlineOutgoing)

    @inline_outgoing.setter
    def inline_outgoing(self, value: bool):
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        self._dotnet_instance.InlineOutgoing = next(_unwrap(None, value))

    @property
    def disabled(self) -> bool:
        """Gets or sets whether the port is disabled."""
        return _wrap(self._dotnet_instance.Disabled)

    @disabled.setter
    def disabled(self, value: bool):
        """Gets or sets whether the port is disabled."""
        self._dotnet_instance.Disabled = next(_unwrap(None, value))

    @property
    def termination(self) -> XNETTermination:
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.Termination)

    @termination.setter
    def termination(self, value: XNETTermination):
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />."""
        self._dotnet_instance.Termination = next(_unwrap(None, value))

    @property
    def transceiver_type(self) -> CANTransceiverType:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType" crefType="Unqualified" /> for the port. Transceivers can be high-speed (<format type="monospace">HS</format>), low-speed (<format type="monospace">LS</format>), or single wire (<format type="monospace">SW</format>)."""
        return _wrap(self._dotnet_instance.TransceiverType)

    @transceiver_type.setter
    def transceiver_type(self, value: CANTransceiverType):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType" crefType="Unqualified" /> for the port. Transceivers can be high-speed (<format type="monospace">HS</format>), low-speed (<format type="monospace">LS</format>), or single wire (<format type="monospace">SW</format>)."""
        self._dotnet_instance.TransceiverType = next(_unwrap(None, value))

    @property
    def transmit_order_type(self) -> CANTransmitOrderType:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransmitOrderType" crefType="Unqualified" /> for the port. You can transmit frames to the CAN bus <format type="monospace">AsSubmitted</format> or <format type="monospace">ByIdentifier</format>."""
        return _wrap(self._dotnet_instance.TransmitOrderType)

    @transmit_order_type.setter
    def transmit_order_type(self, value: CANTransmitOrderType):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransmitOrderType" crefType="Unqualified" /> for the port. You can transmit frames to the CAN bus <format type="monospace">AsSubmitted</format> or <format type="monospace">ByIdentifier</format>."""
        self._dotnet_instance.TransmitOrderType = next(_unwrap(None, value))

    @property
    def input_stream_read_time(self) -> float:
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        return _wrap(self._dotnet_instance.InputStreamReadTime)

    @input_stream_read_time.setter
    def input_stream_read_time(self, value: float):
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        self._dotnet_instance.InputStreamReadTime = next(_unwrap(None, value))

    @overload
    def get_incoming(self) -> Incoming:
        ...

    def get_incoming(self, *args):
        return _wrap(self._dotnet_instance.GetIncoming(*_unwrap(None, *args)))

    @overload
    def get_outgoing(self) -> Outgoing:
        ...

    def get_outgoing(self, *args):
        return _wrap(self._dotnet_instance.GetOutgoing(*_unwrap(None, *args)))

    @overload
    def get_interface_section(self) -> CANInterfaceChannels:
        ...

    def get_interface_section(self, *args):
        return _wrap(self._dotnet_instance.GetInterfaceSection(*_unwrap(None, *args)))

    @overload
    def create_interface_section(self) -> CANInterfaceChannels:
        ...

    def create_interface_section(self, *args):
        return _wrap(self._dotnet_instance.CreateInterfaceSection(*_unwrap(None, *args)))

    @overload
    def remove_automatic_frame_processing(self):
        ...

    def remove_automatic_frame_processing(self, *args):
        return _wrap(self._dotnet_instance.RemoveAutomaticFrameProcessing(*_unwrap(None, *args)))

    @overload
    def remove986x_support(self):
        ...

    def remove986x_support(self, *args):
        return _wrap(self._dotnet_instance.Remove986xSupport(*_unwrap(None, *args)))

    @overload
    def set986x_support(self, file: DependentFile, rio_port_number: int):
        ...

    def set986x_support(self, *args):
        return _wrap(self._dotnet_instance.Set986xSupport(*_unwrap(None, *args)))

    @overload
    def set_automatic_frame_processing(self, ini_file_name: str, binary_file_path: str, global_data: Sequence[int]):
        ...

    def set_automatic_frame_processing(self, *args):
        return _wrap(self._dotnet_instance.SetAutomaticFrameProcessing(*_unwrap(None, *args)))


class CRC(Section):
    """Represents the <format type="bold">CRC</format> section under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" /> section of an outgoing frame of an NI-XNET CAN port. This feature performs a cyclic redundancy check."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CRC:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for CRC")

    @property
    def max_afp_length(self) -> int:
        """Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC."""
        return _wrap(self._dotnet_instance.MaxAFPLength)

    @max_afp_length.setter
    def max_afp_length(self, value: int):
        """Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC."""
        self._dotnet_instance.MaxAFPLength = next(_unwrap(None, value))

    @property
    def index_crc(self) -> int:
        """Gets or sets the index of the CRC within the frame."""
        return _wrap(self._dotnet_instance.IndexCRC)

    @index_crc.setter
    def index_crc(self, value: int):
        """Gets or sets the index of the CRC within the frame."""
        self._dotnet_instance.IndexCRC = next(_unwrap(None, value))

    @property
    def afp_data(self) -> Sequence[int]:
        """Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.AFPData)

    @afp_data.setter
    def afp_data(self, value: Sequence[int]):
        """Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />."""
        self._dotnet_instance.AFPData = next(_unwrap(None, value))

    @property
    def use_alternate_channel(self) -> bool:
        """Gets whether the <format type="italics">AlternateChannel</format> specified by <see cref="M:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC.SetAlternateChannel(NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode)" crefType="Unqualified" /> is used to trigger writing data."""
        return _wrap(self._dotnet_instance.UseAlternateChannel)

    @property
    def alternate_channel(self) -> BaseNode:
        """Gets the channel used to trigger writing data when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC.UseAlternateChannel" crefType="Unqualified" /> is <see langword="true" />."""
        return _wrap(self._dotnet_instance.AlternateChannel)

    @overload
    def remove_alternate_channel(self):
        ...

    def remove_alternate_channel(self, *args):
        return _wrap(self._dotnet_instance.RemoveAlternateChannel(*_unwrap(None, *args)))

    @overload
    def set_alternate_channel(self, alternate_channel: BaseNode):
        ...

    def set_alternate_channel(self, *args):
        return _wrap(self._dotnet_instance.SetAlternateChannel(*_unwrap(None, *args)))


class CalculatedChannelFolder(Section):
    """Represents a folder under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannels" crefType="Unqualified" /> section of the system definition. Folders simply organize CalculatedChannels into logical groups."""

    @overload
    def __init__(self, name: str, description: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannelFolder:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannelFolder(*_unwrap(None, *args))

    @overload
    def get_calculated_channels_list(self) -> Sequence[CalculatedChannel]:
        ...

    @overload
    def get_calculated_channels_list(self, deep: bool) -> Sequence[CalculatedChannel]:
        ...

    def get_calculated_channels_list(self, *args):
        return _wrap(self._dotnet_instance.GetCalculatedChannelsList(*_unwrap(None, *args)))

    @overload
    def get_calculated_channel_folder_list(self) -> Sequence[CalculatedChannelFolder]:
        ...

    @overload
    def get_calculated_channel_folder_list(self, deep: bool) -> Sequence[CalculatedChannelFolder]:
        ...

    def get_calculated_channel_folder_list(self, *args):
        return _wrap(self._dotnet_instance.GetCalculatedChannelFolderList(*_unwrap(None, *args)))

    @overload
    def add_calculated_channel(self, calculated_channel: CalculatedChannel) -> bool:
        ...

    def add_calculated_channel(self, *args):
        return _wrap(self._dotnet_instance.AddCalculatedChannel(*_unwrap(None, *args)))

    @overload
    def add_calculated_channel_folder(self, folder: CalculatedChannelFolder) -> bool:
        ...

    def add_calculated_channel_folder(self, *args):
        return _wrap(self._dotnet_instance.AddCalculatedChannelFolder(*_unwrap(None, *args)))


class CalculatedChannels(Section):
    """Represents the <format type="bold">Calculated Channels</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />. This section contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel" crefType="Unqualified" /> objects that perform calculations on other channels in the system."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannels:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for CalculatedChannels")

    @overload
    def reorder_channel_list(self, channels: Sequence[CalculatedChannel]) -> bool:
        ...

    def reorder_channel_list(self, *args):
        return _wrap(self._dotnet_instance.ReorderChannelList(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def get_ordered_channel_list(self) -> Sequence[CalculatedChannel]:
        ...

    def get_ordered_channel_list(self, *args):
        return _wrap(self._dotnet_instance.GetOrderedChannelList(*_unwrap(None, *args)))

    @overload
    def get_calculated_channel_folder_list(self) -> Sequence[CalculatedChannelFolder]:
        ...

    @overload
    def get_calculated_channel_folder_list(self, deep: bool) -> Sequence[CalculatedChannelFolder]:
        ...

    def get_calculated_channel_folder_list(self, *args):
        return _wrap(self._dotnet_instance.GetCalculatedChannelFolderList(*_unwrap(None, *args)))

    @overload
    def add_calculated_channel_folder(self, folder: CalculatedChannelFolder) -> bool:
        ...

    def add_calculated_channel_folder(self, *args):
        return _wrap(self._dotnet_instance.AddCalculatedChannelFolder(*_unwrap(None, *args)))

    @overload
    def get_calculated_channel_list(self) -> Sequence[CalculatedChannel]:
        ...

    def get_calculated_channel_list(self, *args):
        return _wrap(self._dotnet_instance.GetCalculatedChannelList(*_unwrap(None, *args)))

    @overload
    def add_calculated_channel(self, calculated_channel: CalculatedChannel) -> bool:
        ...

    def add_calculated_channel(self, *args):
        return _wrap(self._dotnet_instance.AddCalculatedChannel(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_formula(self, formula: Formula) -> bool:
        ...

    def add_formula(self, *args):
        return _wrap(self._dotnet_instance.AddFormula(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_maximum(self, maximum: Maximum) -> bool:
        ...

    def add_maximum(self, *args):
        return _wrap(self._dotnet_instance.AddMaximum(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_minimum(self, minimum: Minimum) -> bool:
        ...

    def add_minimum(self, *args):
        return _wrap(self._dotnet_instance.AddMinimum(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_lowpass_filter(self, lowpass_filter: LowpassFilter) -> bool:
        ...

    def add_lowpass_filter(self, *args):
        return _wrap(self._dotnet_instance.AddLowpassFilter(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_peak_and_valley(self, peak_and_valley: PeakAndValley) -> bool:
        ...

    def add_peak_and_valley(self, *args):
        return _wrap(self._dotnet_instance.AddPeakAndValley(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_acceleration(self, acceleration: Acceleration) -> bool:
        ...

    def add_acceleration(self, *args):
        return _wrap(self._dotnet_instance.AddAcceleration(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_average(self, average: Average) -> bool:
        ...

    def add_average(self, *args):
        return _wrap(self._dotnet_instance.AddAverage(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_conditional(self, conditional: Conditional) -> bool:
        ...

    def add_conditional(self, *args):
        return _wrap(self._dotnet_instance.AddConditional(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Channel(BaseNode, IChannel):
    """Represents a channel in the system definition. This is a base class for more specific channel classes, including hardware channels, system channels, user channels, calculated channels, and so on."""

    @overload
    def __init__(self, node: BaseNodeType):
        ...

    @overload
    def __init__(self, node: ChannelType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Channel:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Channel(*_unwrap(None, *args))

    @_staticproperty
    def k_readable() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Channel.K_READABLE)

    @_staticproperty
    def k_writable() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Channel.K_WRITABLE)

    @_staticproperty
    def k_faultable() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Channel.K_FAULTABLE)

    @_staticproperty
    def k_scalable() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Channel.K_SCALABLE)

    @property
    def scale(self) -> Scale:
        """Gets or sets the value of the scale property on the channel."""
        return _wrap(self._dotnet_instance.Scale)

    @scale.setter
    def scale(self, value: Scale):
        """Gets or sets the value of the scale property on the channel."""
        self._dotnet_instance.Scale = next(_unwrap(None, value))

    @property
    def bit_fields(self) -> int:
        """Gets a bitfield mask that is set on the channel."""
        return _wrap(self._dotnet_instance.BitFields)

    @property
    def default_value(self) -> Sequence[float]:
        """Gets the default value of the channel."""
        return _wrap(self._dotnet_instance.DefaultValue)


class Chassis(Section):
    """Represents a chassis, which contains any NI-DAQ devices, reflective memory devices, NI FPGA targets, NI-XNET devices, and timing and sync devices you add."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis(*_unwrap(None, *args))

    @overload
    def clear_chassis_master_device(self):
        ...

    def clear_chassis_master_device(self, *args):
        return _wrap(self._dotnet_instance.ClearChassisMasterDevice(*_unwrap(None, *args)))

    @overload
    def set_chassis_master_to_daq(self, daq_name: str, clk_src: DAQCM_Clock_Source, active_edge: DAQCM_Active_Edge, export_clk: DAQCM_Export_Sample_Clock, export_clk_to_line: DAQCM_Export_Clk_On_Line, trigger_line: DAQCM_Trigger_Line, trigger_slope: DAQCM_Slope, start_trigger: DAQCM_Export_Start_Trigger, start_trigger_line: DAQCM_Export_StartTrigger_On_Line) -> bool:
        ...

    def set_chassis_master_to_daq(self, *args):
        return _wrap(self._dotnet_instance.SetChassisMasterToDAQ(*_unwrap({None: (9, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def set_chassis_master_to_fpga(self, fpga_name: str) -> bool:
        ...

    def set_chassis_master_to_fpga(self, *args):
        return _wrap(self._dotnet_instance.SetChassisMasterToFPGA(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def set_chassis_master_to_timing_and_sync(self, timing_and_sync_name: str) -> bool:
        ...

    def set_chassis_master_to_timing_and_sync(self, *args):
        return _wrap(self._dotnet_instance.SetChassisMasterToTimingAndSync(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def get_timing_and_sync(self) -> TimingAndSync:
        ...

    def get_timing_and_sync(self, *args):
        return _wrap(self._dotnet_instance.GetTimingAndSync(*_unwrap(None, *args)))

    @overload
    def get_daq(self) -> DAQ:
        ...

    def get_daq(self, *args):
        return _wrap(self._dotnet_instance.GetDAQ(*_unwrap(None, *args)))

    @overload
    def get_fpga(self) -> FPGA:
        ...

    def get_fpga(self, *args):
        return _wrap(self._dotnet_instance.GetFPGA(*_unwrap(None, *args)))

    @overload
    def get_xnet(self) -> XNET:
        ...

    def get_xnet(self, *args):
        return _wrap(self._dotnet_instance.GetXNET(*_unwrap(None, *args)))

    @overload
    def get_data_sharing(self) -> DataSharing:
        ...

    def get_data_sharing(self, *args):
        return _wrap(self._dotnet_instance.GetDataSharing(*_unwrap(None, *args)))


class Command(Section):
    """Represents a parent class for the different <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure" crefType="Unqualified" /> command types."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Command:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Command")


class Condition(Command):
    """Represents a <format type="bold">Condition</format> step that you can add to a procedure. The <format type="bold">Condition</format> step executes a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel" crefType="Unqualified" /> step based on the comparison of a constant value or channel value."""

    @overload
    def __init__(self, name: str, description: str, variable: BaseNode, comparison: ConditionStepComparison, value: float, goto_label: Command):
        ...

    @overload
    def __init__(self, name: str, description: str, variable: BaseNode, comparison: ConditionStepComparison, value: BaseNode, goto_label: Command):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Condition:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Condition(*_unwrap(None, *args))

    @property
    def comparison(self) -> ConditionStepComparison:
        """Gets or sets the condition to use when comparing <format type="italics">Variable</format> and <format type="italics">Value</format>."""
        return _wrap(self._dotnet_instance.Comparison)

    @comparison.setter
    def comparison(self, value: ConditionStepComparison):
        """Gets or sets the condition to use when comparing <format type="italics">Variable</format> and <format type="italics">Value</format>."""
        self._dotnet_instance.Comparison = next(_unwrap(None, value))

    @property
    def value_constant(self) -> float:
        """Gets the constant value that is compared to <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Condition.Variable" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.ValueConstant)

    @property
    def value_is_constant(self) -> bool:
        """Gets whether the value compared to <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Condition.Variable" crefType="Unqualified" /> is determined by a channel or by a constant."""
        return _wrap(self._dotnet_instance.ValueIsConstant)

    @property
    def goto_label(self) -> BaseNode:
        """Gets or sets the procedure step to go to if the condition is met."""
        return _wrap(self._dotnet_instance.GotoLabel)

    @goto_label.setter
    def goto_label(self, value: BaseNode):
        """Gets or sets the procedure step to go to if the condition is met."""
        self._dotnet_instance.GotoLabel = next(_unwrap(None, value))

    @property
    def variable(self) -> BaseNode:
        """Gets or sets the channel against which to test the condition."""
        return _wrap(self._dotnet_instance.Variable)

    @variable.setter
    def variable(self, value: BaseNode):
        """Gets or sets the channel against which to test the condition."""
        self._dotnet_instance.Variable = next(_unwrap(None, value))

    @property
    def value_channel(self) -> BaseNode:
        """Gets the channel that specifies the value that is compared to <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Condition.Variable" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.ValueChannel)

    @overload
    def set_value(self, value: float):
        ...

    @overload
    def set_value(self, value: BaseNode):
        ...

    def set_value(self, *args):
        return _wrap(self._dotnet_instance.SetValue(*_unwrap(None, *args)))


class Counter(Section):
    """Represents the <format type="bold">Counter</format> section under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" /> section of an outgoing frame of an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />. This feature increments specific bits every time the frame is transmitted across the bus."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Counter:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Counter")

    @property
    def max_afp_length(self) -> int:
        """Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC."""
        return _wrap(self._dotnet_instance.MaxAFPLength)

    @max_afp_length.setter
    def max_afp_length(self, value: int):
        """Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC."""
        self._dotnet_instance.MaxAFPLength = next(_unwrap(None, value))

    @property
    def index_counter(self) -> int:
        """Gets or sets the index of the counter within the frame."""
        return _wrap(self._dotnet_instance.IndexCounter)

    @index_counter.setter
    def index_counter(self, value: int):
        """Gets or sets the index of the counter within the frame."""
        self._dotnet_instance.IndexCounter = next(_unwrap(None, value))

    @property
    def afp_data(self) -> Sequence[int]:
        """Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.AFPData)

    @afp_data.setter
    def afp_data(self, value: Sequence[int]):
        """Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />."""
        self._dotnet_instance.AFPData = next(_unwrap(None, value))

    @property
    def use_alternate_channel(self) -> bool:
        """Gets whether the <format type="italics">AlternateChannel</format> specified by <see cref="M:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter.SetAlternateChannel(NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode)" crefType="Unqualified" /> is used to trigger writing data."""
        return _wrap(self._dotnet_instance.UseAlternateChannel)

    @property
    def alternate_channel(self) -> BaseNode:
        """Gets the channel used to trigger writing data when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter.UseAlternateChannel" crefType="Unqualified" /> is <see langword="true" />."""
        return _wrap(self._dotnet_instance.AlternateChannel)

    @overload
    def remove_alternate_channel(self):
        ...

    def remove_alternate_channel(self, *args):
        return _wrap(self._dotnet_instance.RemoveAlternateChannel(*_unwrap(None, *args)))

    @overload
    def set_alternate_channel(self, alternate_channel: BaseNode):
        ...

    def set_alternate_channel(self, *args):
        return _wrap(self._dotnet_instance.SetAlternateChannel(*_unwrap(None, *args)))


class CustomDevice(CustomDeviceSection):
    """Represents a custom device in NI VeriStand."""

    @overload
    def __init__(self, name: str, guid: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDevice:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDevice(*_unwrap(None, *args))

    @property
    def timed_loop_priority(self) -> CDTimeLoopPriority:
        """Gets or sets the priority (<format type="monospace">High</format>, <format type="monospace">Low</format>, or <format type="monospace">Medium</format>) of the Timed Loop in which an asynchronous custom device runs. This property only applies to asynchronous custom devices that run in Timed Loops."""
        return _wrap(self._dotnet_instance.TimedLoopPriority)

    @timed_loop_priority.setter
    def timed_loop_priority(self, value: CDTimeLoopPriority):
        """Gets or sets the priority (<format type="monospace">High</format>, <format type="monospace">Low</format>, or <format type="monospace">Medium</format>) of the Timed Loop in which an asynchronous custom device runs. This property only applies to asynchronous custom devices that run in Timed Loops."""
        self._dotnet_instance.TimedLoopPriority = next(_unwrap(None, value))

    @property
    def loop_type(self) -> CDLoopType:
        """Gets or sets the type of loop (<format type="monospace">TimedLoop</format> or <format type="monospace">WhileLoop</format>) in which the custom device runs. This property only applies to asynchronous custom devices."""
        return _wrap(self._dotnet_instance.LoopType)

    @loop_type.setter
    def loop_type(self, value: CDLoopType):
        """Gets or sets the type of loop (<format type="monospace">TimedLoop</format> or <format type="monospace">WhileLoop</format>) in which the custom device runs. This property only applies to asynchronous custom devices."""
        self._dotnet_instance.LoopType = next(_unwrap(None, value))

    @property
    def driver_vi_execution_mode(self) -> CDDriverExecMode:
        """Gets or sets the execution mode of the custom device, such as if it runs inline with the Primary Control Loop or asynchronously."""
        return _wrap(self._dotnet_instance.DriverVIExecutionMode)

    @driver_vi_execution_mode.setter
    def driver_vi_execution_mode(self, value: CDDriverExecMode):
        """Gets or sets the execution mode of the custom device, such as if it runs inline with the Primary Control Loop or asynchronously."""
        self._dotnet_instance.DriverVIExecutionMode = next(_unwrap(None, value))

    @property
    def device_enabled_state(self) -> bool:
        """Gets or sets the state (enabled or disabled) of the custom device.
            
             The effect of setting this property will not be visible in System Explorer. Many custom devices provide an alternate TypeGUID and associated glyph to indicate whether the custom device is disabled."""
        return _wrap(self._dotnet_instance.DeviceEnabledState)

    @device_enabled_state.setter
    def device_enabled_state(self, value: bool):
        """Gets or sets the state (enabled or disabled) of the custom device.
            
             The effect of setting this property will not be visible in System Explorer. Many custom devices provide an alternate TypeGUID and associated glyph to indicate whether the custom device is disabled."""
        self._dotnet_instance.DeviceEnabledState = next(_unwrap(None, value))

    @property
    def version(self) -> str:
        """Gets or sets information stored with a custom device, such as version information. You can read this string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code."""
        return _wrap(self._dotnet_instance.Version)

    @version.setter
    def version(self, value: str):
        """Gets or sets information stored with a custom device, such as version information. You can read this string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code."""
        self._dotnet_instance.Version = next(_unwrap(None, value))

    @property
    def use_device_clock(self) -> bool:
        """Gets or sets whether the Timed Loop in which an asynchronous custom device runs is synchronized with the Primary Control Loop (PCL) timing source. This property only applies to asynchronous custom devices that run in Timed Loops."""
        return _wrap(self._dotnet_instance.UseDeviceClock)

    @use_device_clock.setter
    def use_device_clock(self, value: bool):
        """Gets or sets whether the Timed Loop in which an asynchronous custom device runs is synchronized with the Primary Control Loop (PCL) timing source. This property only applies to asynchronous custom devices that run in Timed Loops."""
        self._dotnet_instance.UseDeviceClock = next(_unwrap(None, value))

    @property
    def decimation(self) -> int:
        """Gets or sets the decimation factor for the custom device, which determines how many iterations of the Primary Control Loop (PCL) occur between calls to the custom device."""
        return _wrap(self._dotnet_instance.Decimation)

    @decimation.setter
    def decimation(self, value: int):
        """Gets or sets the decimation factor for the custom device, which determines how many iterations of the Primary Control Loop (PCL) occur between calls to the custom device."""
        self._dotnet_instance.Decimation = next(_unwrap(None, value))

    @property
    def fifo_source_depth(self) -> int:
        """Gets or sets the depth of the FIFO at the source. This property defines the size of the buffer for incoming data. This property only applies to asynchronous custom devices."""
        return _wrap(self._dotnet_instance.FIFOSourceDepth)

    @fifo_source_depth.setter
    def fifo_source_depth(self, value: int):
        """Gets or sets the depth of the FIFO at the source. This property defines the size of the buffer for incoming data. This property only applies to asynchronous custom devices."""
        self._dotnet_instance.FIFOSourceDepth = next(_unwrap(None, value))

    @property
    def fifo_sink_depth(self) -> int:
        """Gets or sets the depth of the FIFO at the sink. This property defines the size of the buffer for outgoing data. This property only applies to asynchronous custom devices."""
        return _wrap(self._dotnet_instance.FIFOSinkDepth)

    @fifo_sink_depth.setter
    def fifo_sink_depth(self, value: int):
        """Gets or sets the depth of the FIFO at the sink. This property defines the size of the buffer for outgoing data. This property only applies to asynchronous custom devices."""
        self._dotnet_instance.FIFOSinkDepth = next(_unwrap(None, value))

    @overload
    def get_custom_device_channel_list(self) -> Sequence[CustomDeviceChannel]:
        ...

    def get_custom_device_channel_list(self, *args):
        return _wrap(self._dotnet_instance.GetCustomDeviceChannelList(*_unwrap(None, *args)))

    @overload
    def get_custom_device_waveform_list(self) -> Sequence[CustomDeviceWaveform]:
        ...

    def get_custom_device_waveform_list(self, *args):
        return _wrap(self._dotnet_instance.GetCustomDeviceWaveformList(*_unwrap(None, *args)))

    @overload
    def get_custom_device_section_list(self) -> Sequence[CustomDeviceSection]:
        ...

    def get_custom_device_section_list(self, *args):
        return _wrap(self._dotnet_instance.GetCustomDeviceSectionList(*_unwrap(None, *args)))

    @overload
    def get_dependencies(self) -> Sequence[DependentFile]:
        ...

    def get_dependencies(self, *args):
        return _wrap(self._dotnet_instance.GetDependencies(*_unwrap(None, *args)))

    @overload
    def get_driver_vi_for_owner_target_type(self) -> DependentFile:
        ...

    def get_driver_vi_for_owner_target_type(self, *args):
        return _wrap(self._dotnet_instance.GetDriverVIForOwnerTargetType(*_unwrap(None, *args)))

    @overload
    def get_driver_v_is(self) -> Sequence[DependentFile]:
        ...

    def get_driver_v_is(self, *args):
        return _wrap(self._dotnet_instance.GetDriverVIs(*_unwrap(None, *args)))

    @overload
    def get_timing_source_init_v_is(self) -> Sequence[DependentFile]:
        ...

    def get_timing_source_init_v_is(self, *args):
        return _wrap(self._dotnet_instance.GetTimingSourceInitVIs(*_unwrap(None, *args)))

    @overload
    def add_dependencies(self, dependencies: Sequence[DependentFile]):
        ...

    def add_dependencies(self, *args):
        return _wrap(self._dotnet_instance.AddDependencies(*_unwrap(None, *args)))

    @overload
    def set_driver_v_is(self, driver_v_is: Sequence[DependentFile]):
        ...

    def set_driver_v_is(self, *args):
        return _wrap(self._dotnet_instance.SetDriverVIs(*_unwrap(None, *args)))

    @overload
    def set_timing_source_init_v_is(self, timing_source_init_v_is: Sequence[DependentFile]):
        ...

    def set_timing_source_init_v_is(self, *args):
        return _wrap(self._dotnet_instance.SetTimingSourceInitVIs(*_unwrap(None, *args)))

    @overload
    def reset_dependencies(self):
        ...

    def reset_dependencies(self, *args):
        return _wrap(self._dotnet_instance.ResetDependencies(*_unwrap(None, *args)))


class CustomDeviceChannel(CustomDeviceBase, IChannel):
    """Represents a channel in a custom device."""

    @overload
    def __init__(self, name: str, guid: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel(*_unwrap(None, *args))

    @property
    def type(self) -> CDChannel_Type:
        """Gets or sets whether a custom device channel is an input or output channel. Only input channels are writable."""
        return _wrap(self._dotnet_instance.Type)

    @type.setter
    def type(self, value: CDChannel_Type):
        """Gets or sets whether a custom device channel is an input or output channel. Only input channels are writable."""
        self._dotnet_instance.Type = next(_unwrap(None, value))

    @property
    def faultable(self) -> bool:
        """Gets or sets whether a custom device channel is faultable, meaning the VeriStand Engine can fault the channel using software fault insertion."""
        return _wrap(self._dotnet_instance.Faultable)

    @faultable.setter
    def faultable(self, value: bool):
        """Gets or sets whether a custom device channel is faultable, meaning the VeriStand Engine can fault the channel using software fault insertion."""
        self._dotnet_instance.Faultable = next(_unwrap(None, value))

    @property
    def scalable(self) -> bool:
        """Gets or sets whether a custom device channel can be calibrated or scaled into specific engineering units."""
        return _wrap(self._dotnet_instance.Scalable)

    @scalable.setter
    def scalable(self, value: bool):
        """Gets or sets whether a custom device channel can be calibrated or scaled into specific engineering units."""
        self._dotnet_instance.Scalable = next(_unwrap(None, value))

    @property
    def default_value(self) -> float:
        """Gets or sets the default value for a custom device channel."""
        return _wrap(self._dotnet_instance.DefaultValue)

    @default_value.setter
    def default_value(self, value: float):
        """Gets or sets the default value for a custom device channel."""
        self._dotnet_instance.DefaultValue = next(_unwrap(None, value))

    @property
    def scale(self) -> Scale:
        """Gets or sets the value of the scale property on the channel."""
        return _wrap(self._dotnet_instance.Scale)

    @scale.setter
    def scale(self, value: Scale):
        """Gets or sets the value of the scale property on the channel."""
        self._dotnet_instance.Scale = next(_unwrap(None, value))

    @property
    def bit_fields(self) -> int:
        """For internal use only. Stores various channel settings, such as its type, default value, whether it is faultable or scalable, and so on. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.DefaultValue" crefType="Unqualified" />, <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.Faultable" crefType="Unqualified" />, <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.Scalable" crefType="Unqualified" />, and <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.Type" crefType="Unqualified" /> properties to get the information the bit field contains."""
        return _wrap(self._dotnet_instance.BitFields)

    @overload
    def set_value_table(self, names: Sequence[str], values: Sequence[float]):
        ...

    def set_value_table(self, *args):
        return _wrap(self._dotnet_instance.SetValueTable(*_unwrap(None, *args)))


class CustomDevices(Section):
    """Represents the top-level <format type="bold">Custom Devices</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />. This section contains all the custom devices (except timing and sync devices) that you add to the system definition."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDevices:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for CustomDevices")

    @overload
    def get_custom_device_list(self) -> Sequence[CustomDevice]:
        ...

    def get_custom_device_list(self, *args):
        return _wrap(self._dotnet_instance.GetCustomDeviceList(*_unwrap(None, *args)))

    @overload
    def add_custom_device(self, custom_device: CustomDevice) -> bool:
        ...

    def add_custom_device(self, *args):
        return _wrap(self._dotnet_instance.AddCustomDevice(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Cyclic(Section):
    """Represents the <format type="bold">Cyclic</format> section that contains outgoing cyclic frames under an NI-XNET CAN or FlexRay port. Use cyclic frames when you want data changes to arrive at other ECUs within a well-defined deadline."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Cyclic:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Cyclic")

    @overload
    def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]:
        ...

    def get_signal_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetSignalBasedFrameList(*_unwrap(None, *args)))

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetRawDataBasedFrameList(*_unwrap(None, *args)))

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddSignalBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddRawDataBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class CyclicEvent(Section):
    """Represents the <format type="bold">CyclicEvent</format> section that contains outgoing cyclic/event frames under an NI-XNET CAN port. Use cyclic/event frames when you want data changes to arrive at other ECUs within a well-defined deadline with the additional ability to send frames on demand."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CyclicEvent:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for CyclicEvent")

    @overload
    def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]:
        ...

    def get_signal_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetSignalBasedFrameList(*_unwrap(None, *args)))

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetRawDataBasedFrameList(*_unwrap(None, *args)))

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddSignalBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddRawDataBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class DAQ(Section):
    """Represents the <format type="bold">DAQ</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis" crefType="Unqualified" /> in the system definition. This section contains all the DAQ devices you add under the chassis."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQ:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQ")

    @overload
    def get_device_list(self) -> Sequence[DAQDevice]:
        ...

    def get_device_list(self, *args):
        return _wrap(self._dotnet_instance.GetDeviceList(*_unwrap(None, *args)))

    @overload
    def get_tasks(self) -> DAQTasks:
        ...

    def get_tasks(self, *args):
        return _wrap(self._dotnet_instance.GetTasks(*_unwrap(None, *args)))

    @overload
    def add_device(self, device: DAQDevice) -> bool:
        ...

    def add_device(self, *args):
        return _wrap(self._dotnet_instance.AddDevice(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class DAQAnalogInputs(Section):
    """Represents an <format type="bold">Analog Input</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains all <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogInput" crefType="Unqualified" /> channels you add for the device."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogInputs:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQAnalogInputs")

    @property
    def sample_mode(self) -> SampleMode:
        """Gets or sets whether the acquisition is single-point or buffered."""
        return _wrap(self._dotnet_instance.SampleMode)

    @sample_mode.setter
    def sample_mode(self, value: SampleMode):
        """Gets or sets whether the acquisition is single-point or buffered."""
        self._dotnet_instance.SampleMode = next(_unwrap(None, value))

    @property
    def waveform_analog_input_task(self) -> DAQTaskAI:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> associated with the buffered acquisition."""
        return _wrap(self._dotnet_instance.WaveformAnalogInputTask)

    @waveform_analog_input_task.setter
    def waveform_analog_input_task(self, value: DAQTaskAI):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> associated with the buffered acquisition."""
        self._dotnet_instance.WaveformAnalogInputTask = next(_unwrap(None, value))

    @property
    def is_slow_background_convert_enabled(self) -> bool:
        """Gets whether the Slow Background Convert configuration is enabled."""
        return _wrap(self._dotnet_instance.IsSlowBackgroundConvertEnabled)

    @property
    def slow_background_convert_rate(self) -> float:
        """Gets the Slow Background Convert sample rate."""
        return _wrap(self._dotnet_instance.SlowBackgroundConvertRate)

    @overload
    def get_analog_input_list(self) -> Sequence[DAQAnalogInput]:
        ...

    def get_analog_input_list(self, *args):
        return _wrap(self._dotnet_instance.GetAnalogInputList(*_unwrap(None, *args)))

    @overload
    def get_waveform_analog_input_list(self) -> Sequence[DAQWaveformAnalogInput]:
        ...

    def get_waveform_analog_input_list(self, *args):
        return _wrap(self._dotnet_instance.GetWaveformAnalogInputList(*_unwrap(None, *args)))

    @overload
    def add_analog_input(self, analog_input: DAQAnalogInput) -> bool:
        ...

    def add_analog_input(self, *args):
        return _wrap(self._dotnet_instance.AddAnalogInput(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_waveform_analog_input(self, waveform_analog_input: DAQWaveformAnalogInput) -> bool:
        ...

    def add_waveform_analog_input(self, *args):
        return _wrap(self._dotnet_instance.AddWaveformAnalogInput(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def slow_background_convert_mode(self, enable: bool, rate: float):
        ...

    def slow_background_convert_mode(self, *args):
        return _wrap(self._dotnet_instance.SlowBackgroundConvertMode(*_unwrap(None, *args)))


class DAQAnalogOutputs(Section):
    """Represents an <format type="bold">Analog Output</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains all <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogOutput" crefType="Unqualified" /> channels you add for the device."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogOutputs:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQAnalogOutputs")

    @overload
    def get_analog_output_list(self) -> Sequence[DAQAnalogOutput]:
        ...

    def get_analog_output_list(self, *args):
        return _wrap(self._dotnet_instance.GetAnalogOutputList(*_unwrap(None, *args)))

    @overload
    def add_analog_output(self, analog_output: DAQAnalogOutput) -> bool:
        ...

    def add_analog_output(self, *args):
        return _wrap(self._dotnet_instance.AddAnalogOutput(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class DAQChannel(Channel, IChannel):
    """Provides an abstract base class for implementing DAQ device channels and their measurement types based on DAQ plug-in XML files."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQChannel:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQChannel")

    @property
    def plugin_guid(self) -> str:
        """Gets the GUID that corresponds to the type of measurement or generation the channel performs."""
        return _wrap(self._dotnet_instance.PluginGUID)

    @property
    def measurement_type(self) -> DAQMeasurementType:
        """Gets the type of measurement or generation the DAQ channel performs."""
        return _wrap(self._dotnet_instance.MeasurementType)

    @overload
    def get_double_property(self, property_name: str) -> float:
        ...

    def get_double_property(self, *args):
        return _wrap(self._dotnet_instance.GetDoubleProperty(*_unwrap(None, *args)))

    @overload
    def get_u64_property(self, property_name: str) -> int:
        ...

    def get_u64_property(self, *args):
        return _wrap(self._dotnet_instance.GetU64Property(*_unwrap(None, *args)))

    @overload
    def get_u32_property(self, property_name: str) -> int:
        ...

    def get_u32_property(self, *args):
        return _wrap(self._dotnet_instance.GetU32Property(*_unwrap(None, *args)))

    @overload
    def get_u16_property(self, property_name: str) -> int:
        ...

    def get_u16_property(self, *args):
        return _wrap(self._dotnet_instance.GetU16Property(*_unwrap(None, *args)))

    @overload
    def get_i64_property(self, property_name: str) -> int:
        ...

    def get_i64_property(self, *args):
        return _wrap(self._dotnet_instance.GetI64Property(*_unwrap(None, *args)))

    @overload
    def get_i32_property(self, property_name: str) -> int:
        ...

    def get_i32_property(self, *args):
        return _wrap(self._dotnet_instance.GetI32Property(*_unwrap(None, *args)))

    @overload
    def get_i16_property(self, property_name: str) -> int:
        ...

    def get_i16_property(self, *args):
        return _wrap(self._dotnet_instance.GetI16Property(*_unwrap(None, *args)))

    @overload
    def get_boolean_property(self, property_name: str) -> bool:
        ...

    def get_boolean_property(self, *args):
        return _wrap(self._dotnet_instance.GetBooleanProperty(*_unwrap(None, *args)))

    @overload
    def get_string_property(self, property_name: str) -> str:
        ...

    def get_string_property(self, *args):
        return _wrap(self._dotnet_instance.GetStringProperty(*_unwrap(None, *args)))

    @overload
    def get_enum_property(self, property_name: str) -> Tuple[str, int]:
        ...

    def get_enum_property(self, *args):
        return _wrap(self._dotnet_instance.GetEnumProperty(*_unwrap(None, *args)))

    @overload
    def get_properties(self) -> Tuple[Sequence[str], Sequence[ValueDataType]]:
        ...

    def get_properties(self, *args):
        return _wrap(self._dotnet_instance.GetProperties(*_unwrap(None, *args)))

    @overload
    def reset_property_values(self):
        ...

    def reset_property_values(self, *args):
        return _wrap(self._dotnet_instance.ResetPropertyValues(*_unwrap(None, *args)))

    @overload
    def set_double_property(self, property_name: str, value: float):
        ...

    def set_double_property(self, *args):
        return _wrap(self._dotnet_instance.SetDoubleProperty(*_unwrap(None, *args)))

    @overload
    def set_u64_property(self, property_name: str, value: int):
        ...

    def set_u64_property(self, *args):
        return _wrap(self._dotnet_instance.SetU64Property(*_unwrap(None, *args)))

    @overload
    def set_u32_property(self, property_name: str, value: int):
        ...

    def set_u32_property(self, *args):
        return _wrap(self._dotnet_instance.SetU32Property(*_unwrap(None, *args)))

    @overload
    def set_u16_property(self, property_name: str, value: int):
        ...

    def set_u16_property(self, *args):
        return _wrap(self._dotnet_instance.SetU16Property(*_unwrap(None, *args)))

    @overload
    def set_i64_property(self, property_name: str, value: int):
        ...

    def set_i64_property(self, *args):
        return _wrap(self._dotnet_instance.SetI64Property(*_unwrap(None, *args)))

    @overload
    def set_i32_property(self, property_name: str, value: int):
        ...

    def set_i32_property(self, *args):
        return _wrap(self._dotnet_instance.SetI32Property(*_unwrap(None, *args)))

    @overload
    def set_i16_property(self, property_name: str, value: int):
        ...

    def set_i16_property(self, *args):
        return _wrap(self._dotnet_instance.SetI16Property(*_unwrap(None, *args)))

    @overload
    def set_boolean_property(self, property_name: str, value: bool):
        ...

    def set_boolean_property(self, *args):
        return _wrap(self._dotnet_instance.SetBooleanProperty(*_unwrap(None, *args)))

    @overload
    def set_string_property(self, property_name: str, value: str):
        ...

    def set_string_property(self, *args):
        return _wrap(self._dotnet_instance.SetStringProperty(*_unwrap(None, *args)))

    @overload
    def set_enum_property(self, property_name: str, enum_string: str):
        ...

    @overload
    def set_enum_property(self, property_name: str, value: int):
        ...

    def set_enum_property(self, *args):
        return _wrap(self._dotnet_instance.SetEnumProperty(*_unwrap(None, *args)))


class DAQCounter(DAQChannel, IChannel):
    """Represents a DAQ counter channel."""

    @overload
    def __init__(self, name: str, index: int, plugin_guid: str):
        ...

    @overload
    def __init__(self, name: str, index: int, plugin_guid: str, initial_value: float):
        ...

    @overload
    def __init__(self, name: str, index: int, measurement_type: DAQMeasurementType):
        ...

    @overload
    def __init__(self, name: str, index: int, measurement_type: DAQMeasurementType, initial_value: float):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter(*_unwrap(None, *args))

    @_staticproperty
    def default_terminal() -> str:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal)

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of the counter channel."""
        return _wrap(self._dotnet_instance.InitialValue)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the counter channel."""
        self._dotnet_instance.InitialValue = next(_unwrap(None, value))

    @property
    def data_task(self) -> DAQCounterType:
        """Gets the type of task the counter performs (frequency measurement, period measurement, count up/down, or position measurement)."""
        return _wrap(self._dotnet_instance.DataTask)

    @property
    def counter(self) -> str:
        """Gets the counter channel number."""
        return _wrap(self._dotnet_instance.Counter)

    @overload
    def downcast(self) -> DAQCounter:
        ...

    def downcast(self, *args):
        return _wrap(self._dotnet_instance.Downcast(*_unwrap(None, *args)))

    @overload
    def set_counter_index(self, index: int) -> bool:
        ...

    def set_counter_index(self, *args):
        return _wrap(self._dotnet_instance.SetCounterIndex(*_unwrap(None, *args)))


class DAQCounters(Section):
    """Represents a <format type="bold">Counter</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains all <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter" crefType="Unqualified" /> channels you add for the device."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounters:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQCounters")

    @overload
    def get_counter_list(self) -> Sequence[DAQCounter]:
        ...

    def get_counter_list(self, *args):
        return _wrap(self._dotnet_instance.GetCounterList(*_unwrap(None, *args)))

    @overload
    def get_counter_outputs(self) -> Sequence[DAQCounterOutput]:
        ...

    def get_counter_outputs(self, *args):
        return _wrap(self._dotnet_instance.GetCounterOutputs(*_unwrap(None, *args)))

    @overload
    def get_counter_inputs(self) -> Sequence[DAQCounterInput]:
        ...

    def get_counter_inputs(self, *args):
        return _wrap(self._dotnet_instance.GetCounterInputs(*_unwrap(None, *args)))

    @overload
    def add_counter(self, counter: DAQCounter) -> bool:
        ...

    def add_counter(self, *args):
        return _wrap(self._dotnet_instance.AddCounter(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_counter_input(self, counter: DAQCounterInput) -> bool:
        ...

    def add_counter_input(self, *args):
        return _wrap(self._dotnet_instance.AddCounterInput(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_counter_output(self, counter: DAQCounterOutput) -> bool:
        ...

    def add_counter_output(self, *args):
        return _wrap(self._dotnet_instance.AddCounterOutput(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class DAQDIOPort(Section):
    """Represents a DAQ DIO port, which contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalInput" crefType="Unqualified" /> and/or <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalOutput" crefType="Unqualified" /> channels."""

    @overload
    def __init__(self, port_number: int, inverted: bool):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDIOPort:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDIOPort(*_unwrap(None, *args))

    @property
    def inverted(self) -> bool:
        """Gets or sets whether the digital lines are inverted."""
        return _wrap(self._dotnet_instance.Inverted)

    @inverted.setter
    def inverted(self, value: bool):
        """Gets or sets whether the digital lines are inverted."""
        self._dotnet_instance.Inverted = next(_unwrap(None, value))

    @overload
    def get_digital_inputs(self) -> Sequence[DAQDigitalInput]:
        ...

    def get_digital_inputs(self, *args):
        return _wrap(self._dotnet_instance.GetDigitalInputs(*_unwrap(None, *args)))

    @overload
    def get_digital_outputs(self) -> Sequence[DAQDigitalOutput]:
        ...

    def get_digital_outputs(self, *args):
        return _wrap(self._dotnet_instance.GetDigitalOutputs(*_unwrap(None, *args)))

    @overload
    def add_digital_input(self, digital_input: DAQDigitalInput) -> bool:
        ...

    def add_digital_input(self, *args):
        return _wrap(self._dotnet_instance.AddDigitalInput(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_digital_output(self, digital_output: DAQDigitalOutput) -> bool:
        ...

    def add_digital_output(self, *args):
        return _wrap(self._dotnet_instance.AddDigitalOutput(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class DAQDevice(Section):
    """Represents a DAQ device."""

    @overload
    def __init__(self, name: str, description: str, input_configuration: DAQDeviceInputConfiguration):
        ...

    @overload
    def __init__(self, name: str, description: str, input_configuration: DAQDeviceInputConfiguration, num_ai_channels: int, num_ao_channels: int, num_di_channels: int, num_do_channels: int, port_width: int):
        ...

    @overload
    def __init__(self, name: str, description: str, input_configuration: DAQDeviceInputConfiguration, num_ai_channels: int, num_ao_channels: int, num_di_channels: int, num_do_channels: int, port_width: int, counter_types: Sequence[DAQCounterType], num_internal_channels: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice(*_unwrap(None, *args))

    @property
    def backplane_reference_clock(self) -> PXIBackplaneReferenceClock:
        """Sets or gets the reference clock on the PXI/PXIe chassis backplane to which the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" /> synchronizes its timing."""
        return _wrap(self._dotnet_instance.BackplaneReferenceClock)

    @backplane_reference_clock.setter
    def backplane_reference_clock(self, value: PXIBackplaneReferenceClock):
        """Sets or gets the reference clock on the PXI/PXIe chassis backplane to which the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" /> synchronizes its timing."""
        self._dotnet_instance.BackplaneReferenceClock = next(_unwrap(None, value))

    @property
    def product_id(self) -> int:
        """Public, always writable version of DAQ Product ID
            DAQ Product ID is the unique numeric identifier for a DAQ device."""
        return _wrap(self._dotnet_instance.ProductID)

    @product_id.setter
    def product_id(self, value: int):
        """Public, always writable version of DAQ Product ID
            DAQ Product ID is the unique numeric identifier for a DAQ device."""
        self._dotnet_instance.ProductID = next(_unwrap(None, value))

    @property
    def product_category(self) -> int:
        """Public, always writable version of DAQ Product Category.
            Unique identifier for each DAQ Product category."""
        return _wrap(self._dotnet_instance.ProductCategory)

    @product_category.setter
    def product_category(self, value: int):
        """Public, always writable version of DAQ Product Category.
            Unique identifier for each DAQ Product category."""
        self._dotnet_instance.ProductCategory = next(_unwrap(None, value))

    @property
    def product_name(self) -> str:
        """Public, always writable version of DAQ Product Name."""
        return _wrap(self._dotnet_instance.ProductName)

    @product_name.setter
    def product_name(self, value: str):
        """Public, always writable version of DAQ Product Name."""
        self._dotnet_instance.ProductName = next(_unwrap(None, value))

    @property
    def input_configuration(self) -> DAQDeviceInputConfiguration:
        """Gets or sets the input terminal configuration applied to device channels."""
        return _wrap(self._dotnet_instance.InputConfiguration)

    @input_configuration.setter
    def input_configuration(self, value: DAQDeviceInputConfiguration):
        """Gets or sets the input terminal configuration applied to device channels."""
        self._dotnet_instance.InputConfiguration = next(_unwrap(None, value))

    @property
    def daq_conversion_rate_option(self) -> DAQConversionRate:
        """Gets or sets the rate used to run the analog-digital converters on the DAQ device."""
        return _wrap(self._dotnet_instance.DAQConversionRateOption)

    @daq_conversion_rate_option.setter
    def daq_conversion_rate_option(self, value: DAQConversionRate):
        """Gets or sets the rate used to run the analog-digital converters on the DAQ device."""
        self._dotnet_instance.DAQConversionRateOption = next(_unwrap(None, value))

    @property
    def turn_off_hw_timed_single_point_ai(self) -> bool:
        """Gets or sets whether hardware-timed single-point support is disabled for analog input tasks."""
        return _wrap(self._dotnet_instance.TurnOffHWTimedSinglePointAI)

    @turn_off_hw_timed_single_point_ai.setter
    def turn_off_hw_timed_single_point_ai(self, value: bool):
        """Gets or sets whether hardware-timed single-point support is disabled for analog input tasks."""
        self._dotnet_instance.TurnOffHWTimedSinglePointAI = next(_unwrap(None, value))

    @property
    def port_width(self) -> int:
        """Gets or sets the total number of lines per port."""
        return _wrap(self._dotnet_instance.PortWidth)

    @port_width.setter
    def port_width(self, value: int):
        """Gets or sets the total number of lines per port."""
        self._dotnet_instance.PortWidth = next(_unwrap(None, value))

    @property
    def turn_off_hw_timed_single_point_ao(self) -> bool:
        """Gets or sets whether hardware-timed single-point support is disabled for analog output tasks."""
        return _wrap(self._dotnet_instance.TurnOffHWTimedSinglePointAO)

    @turn_off_hw_timed_single_point_ao.setter
    def turn_off_hw_timed_single_point_ao(self, value: bool):
        """Gets or sets whether hardware-timed single-point support is disabled for analog output tasks."""
        self._dotnet_instance.TurnOffHWTimedSinglePointAO = next(_unwrap(None, value))

    @overload
    def create_analog_inputs(self) -> DAQAnalogInputs:
        ...

    @overload
    def create_analog_inputs(self, mode: SampleMode) -> DAQAnalogInputs:
        ...

    def create_analog_inputs(self, *args):
        return _wrap(self._dotnet_instance.CreateAnalogInputs(*_unwrap({(): (0, NationalInstruments.VeriStand.Error.NoError), (SampleMode,): (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_analog_outputs(self) -> DAQAnalogOutputs:
        ...

    def create_analog_outputs(self, *args):
        return _wrap(self._dotnet_instance.CreateAnalogOutputs(*_unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_counters(self) -> DAQCounters:
        ...

    def create_counters(self, *args):
        return _wrap(self._dotnet_instance.CreateCounters(*_unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_digital_inputs(self) -> DAQDigitalInputs:
        ...

    def create_digital_inputs(self, *args):
        return _wrap(self._dotnet_instance.CreateDigitalInputs(*_unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_digital_outputs(self) -> DAQDigitalOutputs:
        ...

    def create_digital_outputs(self, *args):
        return _wrap(self._dotnet_instance.CreateDigitalOutputs(*_unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_scxi_chassis(self) -> SCXIChassis:
        ...

    def create_scxi_chassis(self, *args):
        return _wrap(self._dotnet_instance.CreateSCXIChassis(*_unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_internal_channels(self) -> DAQInternalChannels:
        ...

    def create_internal_channels(self, *args):
        return _wrap(self._dotnet_instance.CreateInternalChannels(*_unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def populate_device(self, num_ai_channels: int, num_ao_channels: int, num_di_channels: int, num_do_channels: int, port_width: int):
        ...

    @overload
    def populate_device(self, num_ai_channels: int, num_ao_channels: int, num_di_channels: int, num_do_channels: int, port_width: int, counter_types: Sequence[DAQCounterType], num_internal_channels: int):
        ...

    def populate_device(self, *args):
        return _wrap(self._dotnet_instance.PopulateDevice(*_unwrap({None: (7, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def get_analog_input_section(self) -> DAQAnalogInputs:
        ...

    def get_analog_input_section(self, *args):
        return _wrap(self._dotnet_instance.GetAnalogInputSection(*_unwrap(None, *args)))

    @overload
    def get_analog_output_section(self) -> DAQAnalogOutputs:
        ...

    def get_analog_output_section(self, *args):
        return _wrap(self._dotnet_instance.GetAnalogOutputSection(*_unwrap(None, *args)))

    @overload
    def get_counter_section(self) -> DAQCounters:
        ...

    def get_counter_section(self, *args):
        return _wrap(self._dotnet_instance.GetCounterSection(*_unwrap(None, *args)))

    @overload
    def get_digital_input_section(self) -> DAQDigitalInputs:
        ...

    def get_digital_input_section(self, *args):
        return _wrap(self._dotnet_instance.GetDigitalInputSection(*_unwrap(None, *args)))

    @overload
    def get_digital_output_section(self) -> DAQDigitalOutputs:
        ...

    def get_digital_output_section(self, *args):
        return _wrap(self._dotnet_instance.GetDigitalOutputSection(*_unwrap(None, *args)))

    @overload
    def get_scxi_chassis_section(self) -> SCXIChassis:
        ...

    def get_scxi_chassis_section(self, *args):
        return _wrap(self._dotnet_instance.GetSCXIChassisSection(*_unwrap(None, *args)))

    @overload
    def get_internal_channels_section(self) -> DAQInternalChannels:
        ...

    def get_internal_channels_section(self, *args):
        return _wrap(self._dotnet_instance.GetInternalChannelsSection(*_unwrap(None, *args)))


class DAQDigitalInput(DAQChannel, IChannel):
    """Represents a DAQ digital input channel."""

    @overload
    def __init__(self, name: str, digital_line: int, port_number: int, plugin_guid: str):
        ...

    @overload
    def __init__(self, name: str, digital_line: int, port_number: int, initial_value: bool, plugin_guid: str):
        ...

    @overload
    def __init__(self, name: str, digital_line: int, port_number: int, measurement_type: DAQMeasurementType):
        ...

    @overload
    def __init__(self, name: str, digital_line: int, port_number: int, initial_value: bool, measurement_type: DAQMeasurementType):
        ...

    @overload
    def __init__(self, name: str, initial_value: bool, digital_line: int, port_number: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalInput:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalInput(*_unwrap(None, *args))

    @property
    def inital_value(self) -> bool:
        """Gets or sets the initial value of the digital input channel."""
        return _wrap(self._dotnet_instance.InitalValue)

    @inital_value.setter
    def inital_value(self, value: bool):
        """Gets or sets the initial value of the digital input channel."""
        self._dotnet_instance.InitalValue = next(_unwrap(None, value))

    @property
    def digital_line(self) -> int:
        """Gets or sets the digital line for the channel."""
        return _wrap(self._dotnet_instance.DigitalLine)

    @digital_line.setter
    def digital_line(self, value: int):
        """Gets or sets the digital line for the channel."""
        self._dotnet_instance.DigitalLine = next(_unwrap(None, value))

    @property
    def port_number(self) -> int:
        """Gets or sets the port to which the channel belongs."""
        return _wrap(self._dotnet_instance.PortNumber)

    @port_number.setter
    def port_number(self, value: int):
        """Gets or sets the port to which the channel belongs."""
        self._dotnet_instance.PortNumber = next(_unwrap(None, value))

    @property
    def is_scxi(self) -> bool:
        """Gets whether the channel belongs to an SCXI module."""
        return _wrap(self._dotnet_instance.IsSCXI)


class DAQDigitalInputs(Section):
    """Represents a <format type="bold">Digital Input</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDIOPort" crefType="Unqualified" /> ports for <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalInput" crefType="Unqualified" /> channels."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalInputs:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQDigitalInputs")

    @overload
    def get_dio_ports(self) -> Sequence[DAQDIOPort]:
        ...

    def get_dio_ports(self, *args):
        return _wrap(self._dotnet_instance.GetDIOPorts(*_unwrap(None, *args)))

    @overload
    def add_dio_port(self, dio_port: DAQDIOPort) -> bool:
        ...

    def add_dio_port(self, *args):
        return _wrap(self._dotnet_instance.AddDIOPort(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class DAQDigitalOutput(DAQChannel, IChannel):
    """Represents a DAQ digital output channel."""

    @overload
    def __init__(self, name: str, digital_line: int, port_number: int, plugin_guid: str):
        ...

    @overload
    def __init__(self, name: str, digital_line: int, port_number: int, initial_value: bool, plugin_guid: str):
        ...

    @overload
    def __init__(self, name: str, digital_line: int, port_number: int, measurement_type: DAQMeasurementType):
        ...

    @overload
    def __init__(self, name: str, digital_line: int, port_number: int, initial_value: bool, measurement_type: DAQMeasurementType):
        ...

    @overload
    def __init__(self, name: str, initial_value: bool, digital_line: int, port_number: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalOutput:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalOutput(*_unwrap(None, *args))

    @property
    def inital_value(self) -> bool:
        """Gets or sets the initial value of the digital output channel."""
        return _wrap(self._dotnet_instance.InitalValue)

    @inital_value.setter
    def inital_value(self, value: bool):
        """Gets or sets the initial value of the digital output channel."""
        self._dotnet_instance.InitalValue = next(_unwrap(None, value))

    @property
    def digital_line(self) -> int:
        """Gets or sets the digital line for the channel."""
        return _wrap(self._dotnet_instance.DigitalLine)

    @digital_line.setter
    def digital_line(self, value: int):
        """Gets or sets the digital line for the channel."""
        self._dotnet_instance.DigitalLine = next(_unwrap(None, value))

    @property
    def port_number(self) -> int:
        """Gets or sets the port to which the channel belongs."""
        return _wrap(self._dotnet_instance.PortNumber)

    @port_number.setter
    def port_number(self, value: int):
        """Gets or sets the port to which the channel belongs."""
        self._dotnet_instance.PortNumber = next(_unwrap(None, value))

    @property
    def is_scxi(self) -> bool:
        """Gets whether the channel belongs to an SCXI module."""
        return _wrap(self._dotnet_instance.IsSCXI)


class DAQDigitalOutputs(Section):
    """Represents a <format type="bold">Digital Output</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDIOPort" crefType="Unqualified" /> ports for <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalOutput" crefType="Unqualified" /> channels."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalOutputs:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQDigitalOutputs")

    @overload
    def get_dio_ports(self) -> Sequence[DAQDIOPort]:
        ...

    def get_dio_ports(self, *args):
        return _wrap(self._dotnet_instance.GetDIOPorts(*_unwrap(None, *args)))

    @overload
    def add_dio_port(self, dio_port: DAQDIOPort) -> bool:
        ...

    def add_dio_port(self, *args):
        return _wrap(self._dotnet_instance.AddDIOPort(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class DAQFrequencyMeasurement(DAQCounter, IChannel):
    """Represents a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter" crefType="Unqualified" /> channel with the frequency measurement task type."""

    @overload
    def __init__(self, name: str, description: str, index: int, default_value: float, maximum: float, minimum: float, edge: DAQCounterEdge):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQFrequencyMeasurement:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQFrequencyMeasurement(*_unwrap(None, *args))

    @property
    def edge(self) -> DAQCounterEdge:
        """Gets or sets the edge on which to count (rising or falling)."""
        return _wrap(self._dotnet_instance.Edge)

    @edge.setter
    def edge(self, value: DAQCounterEdge):
        """Gets or sets the edge on which to count (rising or falling)."""
        self._dotnet_instance.Edge = next(_unwrap(None, value))

    @property
    def input_terminal(self) -> str:
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        return _wrap(self._dotnet_instance.InputTerminal)

    @input_terminal.setter
    def input_terminal(self, value: str):
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        self._dotnet_instance.InputTerminal = next(_unwrap(None, value))

    @property
    def max(self) -> float:
        """Gets or sets the maximum value of the channel in hertz."""
        return _wrap(self._dotnet_instance.Max)

    @max.setter
    def max(self, value: float):
        """Gets or sets the maximum value of the channel in hertz."""
        self._dotnet_instance.Max = next(_unwrap(None, value))

    @property
    def min(self) -> float:
        """Gets or sets the minimum value of the channel in hertz."""
        return _wrap(self._dotnet_instance.Min)

    @min.setter
    def min(self, value: float):
        """Gets or sets the minimum value of the channel in hertz."""
        self._dotnet_instance.Min = next(_unwrap(None, value))


class DAQInternalChannel(Channel, IChannel):
    """Represents a DAQ internal channel."""

    @overload
    def __init__(self, name: str, default_value: float):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQInternalChannel:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQInternalChannel(*_unwrap(None, *args))

    @property
    def low_level(self) -> float:
        """Gets or sets the minimum value of the channel."""
        return _wrap(self._dotnet_instance.LowLevel)

    @low_level.setter
    def low_level(self, value: float):
        """Gets or sets the minimum value of the channel."""
        self._dotnet_instance.LowLevel = next(_unwrap(None, value))

    @property
    def high_level(self) -> float:
        """Gets or sets the maximum value of the channel."""
        return _wrap(self._dotnet_instance.HighLevel)

    @high_level.setter
    def high_level(self, value: float):
        """Gets or sets the maximum value of the channel."""
        self._dotnet_instance.HighLevel = next(_unwrap(None, value))

    @property
    def channel(self) -> str:
        """Gets or sets the physical name for the channel."""
        return _wrap(self._dotnet_instance.Channel)

    @channel.setter
    def channel(self, value: str):
        """Gets or sets the physical name for the channel."""
        self._dotnet_instance.Channel = next(_unwrap(None, value))


class DAQInternalChannels(Section):
    """Represents an <format type="bold">Internal Channels</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains any <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQInternalChannel" crefType="Unqualified" /> objects to add to the device."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQInternalChannels:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQInternalChannels")

    @overload
    def get_internal_channel_list(self) -> Sequence[DAQInternalChannel]:
        ...

    def get_internal_channel_list(self, *args):
        return _wrap(self._dotnet_instance.GetInternalChannelList(*_unwrap(None, *args)))

    @overload
    def add_internal_channel(self, internal_channel: DAQInternalChannel) -> bool:
        ...

    def add_internal_channel(self, *args):
        return _wrap(self._dotnet_instance.AddInternalChannel(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class DAQLogging(Section):
    """Represents the <format type="bold">Logging</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQLogging")

    @property
    def use_task_as_filename(self) -> bool:
        """Gets or sets a value indicating whether to use the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> name from the system definition as the base of log filenames."""
        return _wrap(self._dotnet_instance.UseTaskAsFilename)

    @use_task_as_filename.setter
    def use_task_as_filename(self, value: bool):
        """Gets or sets a value indicating whether to use the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> name from the system definition as the base of log filenames."""
        self._dotnet_instance.UseTaskAsFilename = next(_unwrap(None, value))

    @property
    def filename_base(self) -> str:
        """Gets or sets the base string used in log filenames. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsFilename" /> is <see langword="false" /> to specify a filename base other than the task name."""
        return _wrap(self._dotnet_instance.FilenameBase)

    @filename_base.setter
    def filename_base(self, value: str):
        """Gets or sets the base string used in log filenames. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsFilename" /> is <see langword="false" /> to specify a filename base other than the task name."""
        self._dotnet_instance.FilenameBase = next(_unwrap(None, value))

    @property
    def log_directory(self) -> str:
        """Gets or sets the directory in which to save log files on the target."""
        return _wrap(self._dotnet_instance.LogDirectory)

    @log_directory.setter
    def log_directory(self, value: str):
        """Gets or sets the directory in which to save log files on the target."""
        self._dotnet_instance.LogDirectory = next(_unwrap(None, value))

    @property
    def timestamp_filename(self) -> bool:
        """Gets or sets a value indicating whether to append timestamps to the log filenames."""
        return _wrap(self._dotnet_instance.TimestampFilename)

    @timestamp_filename.setter
    def timestamp_filename(self, value: bool):
        """Gets or sets a value indicating whether to append timestamps to the log filenames."""
        self._dotnet_instance.TimestampFilename = next(_unwrap(None, value))

    @property
    def action_on_new(self) -> ActionOnNew:
        """Gets or sets the location to log data when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> begins a new acquisition."""
        return _wrap(self._dotnet_instance.ActionOnNew)

    @action_on_new.setter
    def action_on_new(self, value: ActionOnNew):
        """Gets or sets the location to log data when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> begins a new acquisition."""
        self._dotnet_instance.ActionOnNew = next(_unwrap(None, value))

    @property
    def use_task_as_group_name(self) -> bool:
        """Gets or sets a value indicating whether to use the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> name from the system definition as the group name under which data is logged in the TDMS file."""
        return _wrap(self._dotnet_instance.UseTaskAsGroupName)

    @use_task_as_group_name.setter
    def use_task_as_group_name(self, value: bool):
        """Gets or sets a value indicating whether to use the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> name from the system definition as the group name under which data is logged in the TDMS file."""
        self._dotnet_instance.UseTaskAsGroupName = next(_unwrap(None, value))

    @property
    def group_name(self) -> str:
        """Gets or sets the group name to which the task logs data in the TDMS file. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsGroupName" /> is <see langword="false" /> to specify a group name other than the task name."""
        return _wrap(self._dotnet_instance.GroupName)

    @group_name.setter
    def group_name(self, value: str):
        """Gets or sets the group name to which the task logs data in the TDMS file. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsGroupName" /> is <see langword="false" /> to specify a group name other than the task name."""
        self._dotnet_instance.GroupName = next(_unwrap(None, value))

    @property
    def logging_enabled(self) -> bool:
        """Gets or sets a value indicating whether the Logging Enabled <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskCommand" /> channel is allowed to start and stop logging. Note that this property does not toggle logging; the Logging Enabled channel toggles logging."""
        return _wrap(self._dotnet_instance.LoggingEnabled)

    @logging_enabled.setter
    def logging_enabled(self, value: bool):
        """Gets or sets a value indicating whether the Logging Enabled <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskCommand" /> channel is allowed to start and stop logging. Note that this property does not toggle logging; the Logging Enabled channel toggles logging."""
        self._dotnet_instance.LoggingEnabled = next(_unwrap(None, value))

    @property
    def logging_mode(self) -> LogMode:
        """Gets or sets whether data is available to components in the NI VeriStand system while you log it.  This property valid only if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.LoggingEnabled" /> is <see langword="true" />."""
        return _wrap(self._dotnet_instance.LoggingMode)

    @logging_mode.setter
    def logging_mode(self, value: LogMode):
        """Gets or sets whether data is available to components in the NI VeriStand system while you log it.  This property valid only if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.LoggingEnabled" /> is <see langword="true" />."""
        self._dotnet_instance.LoggingMode = next(_unwrap(None, value))

    @property
    def span_multiple_files(self) -> bool:
        """Gets or sets a value indicating whether to create a new log file when you reach the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SamplesPerFile" /> limit."""
        return _wrap(self._dotnet_instance.SpanMultipleFiles)

    @span_multiple_files.setter
    def span_multiple_files(self, value: bool):
        """Gets or sets a value indicating whether to create a new log file when you reach the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SamplesPerFile" /> limit."""
        self._dotnet_instance.SpanMultipleFiles = next(_unwrap(None, value))

    @property
    def samples_per_file(self) -> int:
        """Gets or sets a limit to the number of samples per channel to log to the current file when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="true" />. This property not active if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="false" /> because NI VeriStand logs to the current file without limiting the number of samples."""
        return _wrap(self._dotnet_instance.SamplesPerFile)

    @samples_per_file.setter
    def samples_per_file(self, value: int):
        """Gets or sets a limit to the number of samples per channel to log to the current file when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="true" />. This property not active if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="false" /> because NI VeriStand logs to the current file without limiting the number of samples."""
        self._dotnet_instance.SamplesPerFile = next(_unwrap(None, value))

    @overload
    def get_logging_enabled_channel(self) -> DAQTaskCommand:
        ...

    def get_logging_enabled_channel(self, *args):
        return _wrap(self._dotnet_instance.GetLoggingEnabledChannel(*_unwrap(None, *args)))

    @overload
    def get_start_new_file_channel(self) -> DAQTaskCommand:
        ...

    def get_start_new_file_channel(self, *args):
        return _wrap(self._dotnet_instance.GetStartNewFileChannel(*_unwrap(None, *args)))


class DAQPeriodMeasurement(DAQCounter, IChannel):
    """Represents a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter" crefType="Unqualified" /> channel with the period measurement task type."""

    @overload
    def __init__(self, name: str, description: str, index: int, default_value: float, maximum: float, minimum: float, edge: DAQCounterEdge):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPeriodMeasurement:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPeriodMeasurement(*_unwrap(None, *args))

    @property
    def edge(self) -> DAQCounterEdge:
        """Gets or sets the edge on which to count (rising or falling)."""
        return _wrap(self._dotnet_instance.Edge)

    @edge.setter
    def edge(self, value: DAQCounterEdge):
        """Gets or sets the edge on which to count (rising or falling)."""
        self._dotnet_instance.Edge = next(_unwrap(None, value))

    @property
    def input_terminal(self) -> str:
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        return _wrap(self._dotnet_instance.InputTerminal)

    @input_terminal.setter
    def input_terminal(self, value: str):
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        self._dotnet_instance.InputTerminal = next(_unwrap(None, value))

    @property
    def max(self) -> float:
        """Gets or sets the maximum value of the channel in seconds."""
        return _wrap(self._dotnet_instance.Max)

    @max.setter
    def max(self, value: float):
        """Gets or sets the maximum value of the channel in seconds."""
        self._dotnet_instance.Max = next(_unwrap(None, value))

    @property
    def min(self) -> float:
        """Gets or sets the minimum value of the channel in seconds."""
        return _wrap(self._dotnet_instance.Min)

    @min.setter
    def min(self, value: float):
        """Gets or sets the minimum value of the channel in seconds."""
        self._dotnet_instance.Min = next(_unwrap(None, value))


class DAQPositionMeasurement(DAQCounter, IChannel):
    """Represents a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter" crefType="Unqualified" /> channel with the position measurement task type."""

    @overload
    def __init__(self, name: str, description: str, index: int, default_value: float, decoding: DAQCounterDecoding, z_index_mode: DAQCounterZIndexMode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPositionMeasurement:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPositionMeasurement(*_unwrap(None, *args))

    @property
    def decoding(self) -> DAQCounterDecoding:
        """Gets or sets the method used to count and interpret the pulses the encoder generates on signal A and signal B."""
        return _wrap(self._dotnet_instance.Decoding)

    @decoding.setter
    def decoding(self, value: DAQCounterDecoding):
        """Gets or sets the method used to count and interpret the pulses the encoder generates on signal A and signal B."""
        self._dotnet_instance.Decoding = next(_unwrap(None, value))

    @property
    def z_index_mode(self) -> DAQCounterZIndexMode:
        """Gets or sets the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement."""
        return _wrap(self._dotnet_instance.ZIndexMode)

    @z_index_mode.setter
    def z_index_mode(self, value: DAQCounterZIndexMode):
        """Gets or sets the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement."""
        self._dotnet_instance.ZIndexMode = next(_unwrap(None, value))

    @property
    def a_input_terminal(self) -> str:
        """Gets or sets the A input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        return _wrap(self._dotnet_instance.AInputTerminal)

    @a_input_terminal.setter
    def a_input_terminal(self, value: str):
        """Gets or sets the A input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        self._dotnet_instance.AInputTerminal = next(_unwrap(None, value))

    @property
    def b_input_terminal(self) -> str:
        """Gets or sets the B input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        return _wrap(self._dotnet_instance.BInputTerminal)

    @b_input_terminal.setter
    def b_input_terminal(self, value: str):
        """Gets or sets the B input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        self._dotnet_instance.BInputTerminal = next(_unwrap(None, value))

    @property
    def z_input_terminal(self) -> str:
        """Gets or sets the Z input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        return _wrap(self._dotnet_instance.ZInputTerminal)

    @z_input_terminal.setter
    def z_input_terminal(self, value: str):
        """Gets or sets the Z input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        self._dotnet_instance.ZInputTerminal = next(_unwrap(None, value))


class DAQSectionType(Section):
    """Represents a generic DAQ data section."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQSectionType:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQSectionType")

    @property
    def plugin_guid(self) -> str:
        """Gets the GUID specifying DAQPlugin XML/Measurement Type."""
        return _wrap(self._dotnet_instance.PluginGUID)

    @property
    def measurement_type(self) -> DAQMeasurementType:
        """Gets the enum specifying DAQ Measurement Type."""
        return _wrap(self._dotnet_instance.MeasurementType)

    @property
    def data_channels(self) -> Sequence[Channel]:
        """Gets all registered data channels for a measurement type."""
        return _wrap(self._dotnet_instance.DataChannels)

    @overload
    def get_double_property(self, property_name: str) -> float:
        ...

    def get_double_property(self, *args):
        return _wrap(self._dotnet_instance.GetDoubleProperty(*_unwrap(None, *args)))

    @overload
    def get_u64_property(self, property_name: str) -> int:
        ...

    def get_u64_property(self, *args):
        return _wrap(self._dotnet_instance.GetU64Property(*_unwrap(None, *args)))

    @overload
    def get_u32_property(self, property_name: str) -> int:
        ...

    def get_u32_property(self, *args):
        return _wrap(self._dotnet_instance.GetU32Property(*_unwrap(None, *args)))

    @overload
    def get_u16_property(self, property_name: str) -> int:
        ...

    def get_u16_property(self, *args):
        return _wrap(self._dotnet_instance.GetU16Property(*_unwrap(None, *args)))

    @overload
    def get_i64_property(self, property_name: str) -> int:
        ...

    def get_i64_property(self, *args):
        return _wrap(self._dotnet_instance.GetI64Property(*_unwrap(None, *args)))

    @overload
    def get_i32_property(self, property_name: str) -> int:
        ...

    def get_i32_property(self, *args):
        return _wrap(self._dotnet_instance.GetI32Property(*_unwrap(None, *args)))

    @overload
    def get_i16_property(self, property_name: str) -> int:
        ...

    def get_i16_property(self, *args):
        return _wrap(self._dotnet_instance.GetI16Property(*_unwrap(None, *args)))

    @overload
    def get_boolean_property(self, property_name: str) -> bool:
        ...

    def get_boolean_property(self, *args):
        return _wrap(self._dotnet_instance.GetBooleanProperty(*_unwrap(None, *args)))

    @overload
    def get_string_property(self, property_name: str) -> str:
        ...

    def get_string_property(self, *args):
        return _wrap(self._dotnet_instance.GetStringProperty(*_unwrap(None, *args)))

    @overload
    def get_enum_property(self, property_name: str) -> Tuple[str, int]:
        ...

    def get_enum_property(self, *args):
        return _wrap(self._dotnet_instance.GetEnumProperty(*_unwrap(None, *args)))

    @overload
    def get_properties(self) -> Tuple[Sequence[str], Sequence[ValueDataType]]:
        ...

    def get_properties(self, *args):
        return _wrap(self._dotnet_instance.GetProperties(*_unwrap(None, *args)))

    @overload
    def reset_property_values(self):
        ...

    def reset_property_values(self, *args):
        return _wrap(self._dotnet_instance.ResetPropertyValues(*_unwrap(None, *args)))

    @overload
    def set_double_property(self, property_name: str, value: float):
        ...

    def set_double_property(self, *args):
        return _wrap(self._dotnet_instance.SetDoubleProperty(*_unwrap(None, *args)))

    @overload
    def set_u64_property(self, property_name: str, value: int):
        ...

    def set_u64_property(self, *args):
        return _wrap(self._dotnet_instance.SetU64Property(*_unwrap(None, *args)))

    @overload
    def set_u32_property(self, property_name: str, value: int):
        ...

    def set_u32_property(self, *args):
        return _wrap(self._dotnet_instance.SetU32Property(*_unwrap(None, *args)))

    @overload
    def set_u16_property(self, property_name: str, value: int):
        ...

    def set_u16_property(self, *args):
        return _wrap(self._dotnet_instance.SetU16Property(*_unwrap(None, *args)))

    @overload
    def set_i64_property(self, property_name: str, value: int):
        ...

    def set_i64_property(self, *args):
        return _wrap(self._dotnet_instance.SetI64Property(*_unwrap(None, *args)))

    @overload
    def set_i32_property(self, property_name: str, value: int):
        ...

    def set_i32_property(self, *args):
        return _wrap(self._dotnet_instance.SetI32Property(*_unwrap(None, *args)))

    @overload
    def set_i16_property(self, property_name: str, value: int):
        ...

    def set_i16_property(self, *args):
        return _wrap(self._dotnet_instance.SetI16Property(*_unwrap(None, *args)))

    @overload
    def set_boolean_property(self, property_name: str, value: bool):
        ...

    def set_boolean_property(self, *args):
        return _wrap(self._dotnet_instance.SetBooleanProperty(*_unwrap(None, *args)))

    @overload
    def set_string_property(self, property_name: str, value: str):
        ...

    def set_string_property(self, *args):
        return _wrap(self._dotnet_instance.SetStringProperty(*_unwrap(None, *args)))

    @overload
    def set_enum_property(self, property_name: str, enum_string: str):
        ...

    @overload
    def set_enum_property(self, property_name: str, value: int):
        ...

    def set_enum_property(self, *args):
        return _wrap(self._dotnet_instance.SetEnumProperty(*_unwrap(None, *args)))

    @overload
    def get_data_channel(self, type: DAQDataChannelType) -> Channel:
        ...

    def get_data_channel(self, *args):
        return _wrap(self._dotnet_instance.GetDataChannel(*_unwrap(None, *args)))


class DAQTask(Section):
    """Provides an <see langword="abstract" /> base class for different types of tasks you can assign to DAQ channels."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQTask")

    @property
    def task_type(self) -> TaskType:
        """Gets the task type."""
        return _wrap(self._dotnet_instance.TaskType)


class DAQTaskAI(DAQTask):
    """Represents a DAQmx task you can assign to one or more DAQ analog input channels to configure timing properties, triggers, and logging."""

    @overload
    def __init__(self, name: str, rate: float, mode: AcquisitionMode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI(*_unwrap(None, *args))

    @property
    def rate(self) -> float:
        """Gets or sets the sampling rate, in samples per channel per second, or Hz."""
        return _wrap(self._dotnet_instance.Rate)

    @rate.setter
    def rate(self, value: float):
        """Gets or sets the sampling rate, in samples per channel per second, or Hz."""
        self._dotnet_instance.Rate = next(_unwrap(None, value))

    @property
    def acquisition_mode(self) -> AcquisitionMode:
        """Gets or sets the type of acquisition the task performs."""
        return _wrap(self._dotnet_instance.AcquisitionMode)

    @acquisition_mode.setter
    def acquisition_mode(self, value: AcquisitionMode):
        """Gets or sets the type of acquisition the task performs."""
        self._dotnet_instance.AcquisitionMode = next(_unwrap(None, value))

    @property
    def automatic_read_size(self) -> bool:
        """Gets or sets a value indicating whether to automatically determine the size of read operations that make up an acquisition."""
        return _wrap(self._dotnet_instance.AutomaticReadSize)

    @automatic_read_size.setter
    def automatic_read_size(self, value: bool):
        """Gets or sets a value indicating whether to automatically determine the size of read operations that make up an acquisition."""
        self._dotnet_instance.AutomaticReadSize = next(_unwrap(None, value))

    @property
    def read_samples(self) -> int:
        """Gets or sets the requested number of samples per channel to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />."""
        return _wrap(self._dotnet_instance.ReadSamples)

    @read_samples.setter
    def read_samples(self, value: int):
        """Gets or sets the requested number of samples per channel to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />."""
        self._dotnet_instance.ReadSamples = next(_unwrap(None, value))

    @property
    def read_time(self) -> float:
        """Gets or sets the number of seconds to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />."""
        return _wrap(self._dotnet_instance.ReadTime)

    @read_time.setter
    def read_time(self, value: float):
        """Gets or sets the number of seconds to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />."""
        self._dotnet_instance.ReadTime = next(_unwrap(None, value))

    @property
    def read_units(self) -> AcquisitionUnits:
        """Gets or sets whether the task uses <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadTime" /> or <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadSamples" /> as the read size. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that do not automatically determine the read size."""
        return _wrap(self._dotnet_instance.ReadUnits)

    @read_units.setter
    def read_units(self, value: AcquisitionUnits):
        """Gets or sets whether the task uses <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadTime" /> or <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadSamples" /> as the read size. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that do not automatically determine the read size."""
        self._dotnet_instance.ReadUnits = next(_unwrap(None, value))

    @property
    def acquisition_samples(self) -> int:
        """Gets or sets the total number of samples per channel to acquire. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        return _wrap(self._dotnet_instance.AcquisitionSamples)

    @acquisition_samples.setter
    def acquisition_samples(self, value: int):
        """Gets or sets the total number of samples per channel to acquire. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        self._dotnet_instance.AcquisitionSamples = next(_unwrap(None, value))

    @property
    def acquisition_time(self) -> float:
        """Gets or sets the total number of seconds to acquire data. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        return _wrap(self._dotnet_instance.AcquisitionTime)

    @acquisition_time.setter
    def acquisition_time(self, value: float):
        """Gets or sets the total number of seconds to acquire data. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        self._dotnet_instance.AcquisitionTime = next(_unwrap(None, value))

    @property
    def acquisition_units(self) -> AcquisitionUnits:
        """Gets or sets whether the task uses time in seconds or number of samples as the size of the acquisitions it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        return _wrap(self._dotnet_instance.AcquisitionUnits)

    @acquisition_units.setter
    def acquisition_units(self, value: AcquisitionUnits):
        """Gets or sets whether the task uses time in seconds or number of samples as the size of the acquisitions it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        self._dotnet_instance.AcquisitionUnits = next(_unwrap(None, value))

    @property
    def clock_source(self) -> str:
        """Gets or sets the source terminal of the sample clock that you want to control acquisition timing.  An empty string corresponds to the default onboard clock of the device."""
        return _wrap(self._dotnet_instance.ClockSource)

    @clock_source.setter
    def clock_source(self, value: str):
        """Gets or sets the source terminal of the sample clock that you want to control acquisition timing.  An empty string corresponds to the default onboard clock of the device."""
        self._dotnet_instance.ClockSource = next(_unwrap(None, value))

    @property
    def active_edge(self) -> EdgeType:
        """Gets or sets the type of edge in the pulses of the sample clock that cause the task to acquire samples: rising or falling."""
        return _wrap(self._dotnet_instance.ActiveEdge)

    @active_edge.setter
    def active_edge(self, value: EdgeType):
        """Gets or sets the type of edge in the pulses of the sample clock that cause the task to acquire samples: rising or falling."""
        self._dotnet_instance.ActiveEdge = next(_unwrap(None, value))

    @property
    def channel_names(self) -> ChannelNames:
        """Gets or sets a value that indicates how the names of AI channels appear in log files that this task creates."""
        return _wrap(self._dotnet_instance.ChannelNames)

    @channel_names.setter
    def channel_names(self, value: ChannelNames):
        """Gets or sets a value that indicates how the names of AI channels appear in log files that this task creates."""
        self._dotnet_instance.ChannelNames = next(_unwrap(None, value))

    @overload
    def get_logging(self) -> DAQLogging:
        ...

    def get_logging(self, *args):
        return _wrap(self._dotnet_instance.GetLogging(*_unwrap(None, *args)))

    @overload
    def get_triggers(self) -> DAQTriggers:
        ...

    def get_triggers(self, *args):
        return _wrap(self._dotnet_instance.GetTriggers(*_unwrap(None, *args)))

    @overload
    def get_task_enabled_channel(self) -> DAQTaskCommand:
        ...

    def get_task_enabled_channel(self, *args):
        return _wrap(self._dotnet_instance.GetTaskEnabledChannel(*_unwrap(None, *args)))

    @overload
    def get_devices(self) -> Sequence[DAQDevice]:
        ...

    def get_devices(self, *args):
        return _wrap(self._dotnet_instance.GetDevices(*_unwrap(None, *args)))


class DAQTaskCommand(Channel, IChannel):
    """Represents one of the channels under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />, <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers" />, or <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging" /> sections. Task command channels control the execution of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskCommand:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQTaskCommand")

    @property
    def initial_value(self) -> bool:
        """Gets or sets a value indicating whether the channel is initially enabled or disabled."""
        return _wrap(self._dotnet_instance.InitialValue)

    @initial_value.setter
    def initial_value(self, value: bool):
        """Gets or sets a value indicating whether the channel is initially enabled or disabled."""
        self._dotnet_instance.InitialValue = next(_unwrap(None, value))


class DAQTasks(Section):
    """Represents the <format type="bold">Waveform Tasks</format> section in a system definition. This section contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> objects."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTasks:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQTasks")

    @overload
    def get_task_list(self) -> Sequence[DAQTask]:
        ...

    def get_task_list(self, *args):
        return _wrap(self._dotnet_instance.GetTaskList(*_unwrap(None, *args)))

    @overload
    def add_task(self, task: DAQTask) -> bool:
        ...

    def add_task(self, *args):
        return _wrap(self._dotnet_instance.AddTask(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def reorder_task_list(self, tasks: Sequence[DAQTask]) -> bool:
        ...

    def reorder_task_list(self, *args):
        return _wrap(self._dotnet_instance.ReorderTaskList(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class DAQTriggers(Section):
    """Represents the <format type="bold">Triggers</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers(*_unwrap(None, *args))

    @property
    def start_trigger(self) -> DAQTrigger:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the start trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />."""
        return _wrap(self._dotnet_instance.StartTrigger)

    @start_trigger.setter
    def start_trigger(self, value: DAQTrigger):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the start trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />."""
        self._dotnet_instance.StartTrigger = next(_unwrap(None, value))

    @property
    def reference_trigger(self) -> DAQTrigger:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the reference trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />."""
        return _wrap(self._dotnet_instance.ReferenceTrigger)

    @reference_trigger.setter
    def reference_trigger(self, value: DAQTrigger):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the reference trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />."""
        self._dotnet_instance.ReferenceTrigger = next(_unwrap(None, value))

    @property
    def pretrigger_samples(self) -> int:
        """Gets or sets the number of samples per channel prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs."""
        return _wrap(self._dotnet_instance.PretriggerSamples)

    @pretrigger_samples.setter
    def pretrigger_samples(self, value: int):
        """Gets or sets the number of samples per channel prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs."""
        self._dotnet_instance.PretriggerSamples = next(_unwrap(None, value))

    @property
    def pretrigger_time(self) -> float:
        """Gets or sets the length of time, in seconds, prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs."""
        return _wrap(self._dotnet_instance.PretriggerTime)

    @pretrigger_time.setter
    def pretrigger_time(self, value: float):
        """Gets or sets the length of time, in seconds, prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs."""
        self._dotnet_instance.PretriggerTime = next(_unwrap(None, value))

    @property
    def pretrigger_units(self) -> AcquisitionUnits:
        """Gets or sets whether the task uses samples or seconds of time as the size of the pre-trigger acquisition it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serve as the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> for the task."""
        return _wrap(self._dotnet_instance.PretriggerUnits)

    @pretrigger_units.setter
    def pretrigger_units(self, value: AcquisitionUnits):
        """Gets or sets whether the task uses samples or seconds of time as the size of the pre-trigger acquisition it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serve as the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> for the task."""
        self._dotnet_instance.PretriggerUnits = next(_unwrap(None, value))

    @overload
    def get_retriggerable_channel(self) -> DAQTaskCommand:
        ...

    def get_retriggerable_channel(self, *args):
        return _wrap(self._dotnet_instance.GetRetriggerableChannel(*_unwrap(None, *args)))

    @overload
    def get_start_trigger_channel(self) -> DAQTaskCommand:
        ...

    def get_start_trigger_channel(self, *args):
        return _wrap(self._dotnet_instance.GetStartTriggerChannel(*_unwrap(None, *args)))


class DAQWaveform(Waveform):
    """Represents a generic DAQ waveform."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQWaveform:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQWaveform")

    @property
    def plugin_guid(self) -> str:
        """Gets the GUID specifying DAQPlugin XML/Measurement Type."""
        return _wrap(self._dotnet_instance.PluginGUID)

    @property
    def measurement_type(self) -> DAQMeasurementType:
        """Gets the enum specifying DAQ Measurement Type."""
        return _wrap(self._dotnet_instance.MeasurementType)

    @overload
    def get_double_property(self, property_name: str) -> float:
        ...

    def get_double_property(self, *args):
        return _wrap(self._dotnet_instance.GetDoubleProperty(*_unwrap(None, *args)))

    @overload
    def get_u64_property(self, property_name: str) -> int:
        ...

    def get_u64_property(self, *args):
        return _wrap(self._dotnet_instance.GetU64Property(*_unwrap(None, *args)))

    @overload
    def get_u32_property(self, property_name: str) -> int:
        ...

    def get_u32_property(self, *args):
        return _wrap(self._dotnet_instance.GetU32Property(*_unwrap(None, *args)))

    @overload
    def get_u16_property(self, property_name: str) -> int:
        ...

    def get_u16_property(self, *args):
        return _wrap(self._dotnet_instance.GetU16Property(*_unwrap(None, *args)))

    @overload
    def get_i64_property(self, property_name: str) -> int:
        ...

    def get_i64_property(self, *args):
        return _wrap(self._dotnet_instance.GetI64Property(*_unwrap(None, *args)))

    @overload
    def get_i32_property(self, property_name: str) -> int:
        ...

    def get_i32_property(self, *args):
        return _wrap(self._dotnet_instance.GetI32Property(*_unwrap(None, *args)))

    @overload
    def get_i16_property(self, property_name: str) -> int:
        ...

    def get_i16_property(self, *args):
        return _wrap(self._dotnet_instance.GetI16Property(*_unwrap(None, *args)))

    @overload
    def get_boolean_property(self, property_name: str) -> bool:
        ...

    def get_boolean_property(self, *args):
        return _wrap(self._dotnet_instance.GetBooleanProperty(*_unwrap(None, *args)))

    @overload
    def get_string_property(self, property_name: str) -> str:
        ...

    def get_string_property(self, *args):
        return _wrap(self._dotnet_instance.GetStringProperty(*_unwrap(None, *args)))

    @overload
    def get_enum_property(self, property_name: str) -> Tuple[str, int]:
        ...

    def get_enum_property(self, *args):
        return _wrap(self._dotnet_instance.GetEnumProperty(*_unwrap(None, *args)))

    @overload
    def get_properties(self) -> Tuple[Sequence[str], Sequence[ValueDataType]]:
        ...

    def get_properties(self, *args):
        return _wrap(self._dotnet_instance.GetProperties(*_unwrap(None, *args)))

    @overload
    def reset_property_values(self):
        ...

    def reset_property_values(self, *args):
        return _wrap(self._dotnet_instance.ResetPropertyValues(*_unwrap(None, *args)))

    @overload
    def set_double_property(self, property_name: str, value: float):
        ...

    def set_double_property(self, *args):
        return _wrap(self._dotnet_instance.SetDoubleProperty(*_unwrap(None, *args)))

    @overload
    def set_u64_property(self, property_name: str, value: int):
        ...

    def set_u64_property(self, *args):
        return _wrap(self._dotnet_instance.SetU64Property(*_unwrap(None, *args)))

    @overload
    def set_u32_property(self, property_name: str, value: int):
        ...

    def set_u32_property(self, *args):
        return _wrap(self._dotnet_instance.SetU32Property(*_unwrap(None, *args)))

    @overload
    def set_u16_property(self, property_name: str, value: int):
        ...

    def set_u16_property(self, *args):
        return _wrap(self._dotnet_instance.SetU16Property(*_unwrap(None, *args)))

    @overload
    def set_i64_property(self, property_name: str, value: int):
        ...

    def set_i64_property(self, *args):
        return _wrap(self._dotnet_instance.SetI64Property(*_unwrap(None, *args)))

    @overload
    def set_i32_property(self, property_name: str, value: int):
        ...

    def set_i32_property(self, *args):
        return _wrap(self._dotnet_instance.SetI32Property(*_unwrap(None, *args)))

    @overload
    def set_i16_property(self, property_name: str, value: int):
        ...

    def set_i16_property(self, *args):
        return _wrap(self._dotnet_instance.SetI16Property(*_unwrap(None, *args)))

    @overload
    def set_boolean_property(self, property_name: str, value: bool):
        ...

    def set_boolean_property(self, *args):
        return _wrap(self._dotnet_instance.SetBooleanProperty(*_unwrap(None, *args)))

    @overload
    def set_string_property(self, property_name: str, value: str):
        ...

    def set_string_property(self, *args):
        return _wrap(self._dotnet_instance.SetStringProperty(*_unwrap(None, *args)))

    @overload
    def set_enum_property(self, property_name: str, enum_string: str):
        ...

    @overload
    def set_enum_property(self, property_name: str, value: int):
        ...

    def set_enum_property(self, *args):
        return _wrap(self._dotnet_instance.SetEnumProperty(*_unwrap(None, *args)))


class DAQWaveformAnalogInput(DAQWaveform):
    """Represents a DAQ analog input waveform used in a buffered acquisition."""

    @overload
    def __init__(self, name: str, channel: int, plugin_guid: str):
        ...

    @overload
    def __init__(self, name: str, channel: int, measurement_type: DAQMeasurementType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQWaveformAnalogInput:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQWaveformAnalogInput(*_unwrap(None, *args))

    @property
    def channel(self) -> int:
        """Gets or sets the channel number."""
        return _wrap(self._dotnet_instance.Channel)

    @channel.setter
    def channel(self, value: int):
        """Gets or sets the channel number."""
        self._dotnet_instance.Channel = next(_unwrap(None, value))

    @property
    def low_level(self) -> float:
        """Gets or sets the minimum value of the channel."""
        return _wrap(self._dotnet_instance.LowLevel)

    @low_level.setter
    def low_level(self, value: float):
        """Gets or sets the minimum value of the channel."""
        self._dotnet_instance.LowLevel = next(_unwrap(None, value))

    @property
    def high_level(self) -> float:
        """Gets or sets the maximum value of the channel."""
        return _wrap(self._dotnet_instance.HighLevel)

    @high_level.setter
    def high_level(self, value: float):
        """Gets or sets the maximum value of the channel."""
        self._dotnet_instance.HighLevel = next(_unwrap(None, value))


class DataFileError(Channel, IChannel):
    """Represents the <format type="bold">Error</format> channel associated with a raw frame data logging file or data replay file under an NI-XNET port."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileError:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DataFileError")


class DataFileReplay(Section):
    """Represents a data replay file, which is a raw frame data logging (TDMS or NCL) file that you replay onto a CAN bus."""

    @overload
    def __init__(self, name: str, path: str, tdms_group_name: str, tdms_channel_name: str):
        ...

    @overload
    def __init__(self, name: str, path: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay(*_unwrap(None, *args))

    @property
    def behavior(self) -> ReplayBehavior:
        """Gets or sets whether and how frames in the data replay file are filtered."""
        return _wrap(self._dotnet_instance.Behavior)

    @behavior.setter
    def behavior(self, value: ReplayBehavior):
        """Gets or sets whether and how frames in the data replay file are filtered."""
        self._dotnet_instance.Behavior = next(_unwrap(None, value))

    @property
    def tdms_group_name(self) -> str:
        """Gets or sets the name of the group in a TDMS file that contains the logged data for replay."""
        return _wrap(self._dotnet_instance.TDMSGroupName)

    @tdms_group_name.setter
    def tdms_group_name(self, value: str):
        """Gets or sets the name of the group in a TDMS file that contains the logged data for replay."""
        self._dotnet_instance.TDMSGroupName = next(_unwrap(None, value))

    @property
    def tdms_channel_name(self) -> str:
        """Gets or sets the name of the channel in a TDMS file that contains the logged data for replay."""
        return _wrap(self._dotnet_instance.TDMSChannelName)

    @tdms_channel_name.setter
    def tdms_channel_name(self, value: str):
        """Gets or sets the name of the channel in a TDMS file that contains the logged data for replay."""
        self._dotnet_instance.TDMSChannelName = next(_unwrap(None, value))

    @property
    def path(self) -> DependentFile:
        """Gets or sets the path to the replay file on disk."""
        return _wrap(self._dotnet_instance.Path)

    @path.setter
    def path(self, value: DependentFile):
        """Gets or sets the path to the replay file on disk."""
        self._dotnet_instance.Path = next(_unwrap(None, value))

    @property
    def frame_cache_size(self) -> int:
        """Gets or sets the number of frames cached during replay."""
        return _wrap(self._dotnet_instance.FrameCacheSize)

    @frame_cache_size.setter
    def frame_cache_size(self, value: int):
        """Gets or sets the number of frames cached during replay."""
        self._dotnet_instance.FrameCacheSize = next(_unwrap(None, value))

    @property
    def loop_rate(self) -> int:
        """Gets or sets the rate in hertz at which the frames to send in the outgoing queue are updated. This property does not affect the actual update rate of frames on the CAN bus."""
        return _wrap(self._dotnet_instance.LoopRate)

    @loop_rate.setter
    def loop_rate(self, value: int):
        """Gets or sets the rate in hertz at which the frames to send in the outgoing queue are updated. This property does not affect the actual update rate of frames on the CAN bus."""
        self._dotnet_instance.LoopRate = next(_unwrap(None, value))

    @property
    def frame_i_ds(self) -> Sequence[str]:
        """Gets or sets the IDs of the frames in the log file that are included or excluded from the file replay when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay.Behavior" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.ExcludeFrameIDs" crefType="Unqualified" /> or <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.IncludeFrameIDs" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.FrameIDs)

    @frame_i_ds.setter
    def frame_i_ds(self, value: Sequence[str]):
        """Gets or sets the IDs of the frames in the log file that are included or excluded from the file replay when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay.Behavior" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.ExcludeFrameIDs" crefType="Unqualified" /> or <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.IncludeFrameIDs" crefType="Unqualified" />."""
        self._dotnet_instance.FrameIDs = next(_unwrap(None, value))

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets or sets the channel used to trigger replay. Replay begins as soon as the value of this channel becomes non-zero. If desired, you can select or configure a channel that triggers multiple replays of the file."""
        return _wrap(self._dotnet_instance.TriggerChannel)

    @trigger_channel.setter
    def trigger_channel(self, value: BaseNode):
        """Gets or sets the channel used to trigger replay. Replay begins as soon as the value of this channel becomes non-zero. If desired, you can select or configure a channel that triggers multiple replays of the file."""
        self._dotnet_instance.TriggerChannel = next(_unwrap(None, value))

    @overload
    def get_data_file_error(self) -> DataFileError:
        ...

    def get_data_file_error(self, *args):
        return _wrap(self._dotnet_instance.GetDataFileError(*_unwrap(None, *args)))

    @overload
    def get_data_file_status(self) -> DataFileStatus:
        ...

    def get_data_file_status(self, *args):
        return _wrap(self._dotnet_instance.GetDataFileStatus(*_unwrap(None, *args)))


class DataFileStatus(Channel, IChannel):
    """Represents the <format type="bold">Status</format> channel associated with a raw frame data logging file or data replay file under an NI-XNET port."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileStatus:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DataFileStatus")


class DataLoggingFile(Section):
    """Represents a raw frame data logging (TDMS or NCL) file under an NI-XNET port. You can use raw frame data logging files to record incoming frame data during an NI-XNET session."""

    @overload
    def __init__(self, name: str, filename: str, destination: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile(*_unwrap(None, *args))

    @property
    def data_logging_file_type(self) -> FileType:
        """Gets or sets the file type of an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />. Log files can be TDMS or NCL files."""
        return _wrap(self._dotnet_instance.DataLoggingFileType)

    @data_logging_file_type.setter
    def data_logging_file_type(self, value: FileType):
        """Gets or sets the file type of an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />. Log files can be TDMS or NCL files."""
        self._dotnet_instance.DataLoggingFileType = next(_unwrap(None, value))

    @property
    def tdms_group_name(self) -> str:
        """Gets or sets the name of the group in the TDMS file to log data to."""
        return _wrap(self._dotnet_instance.TDMSGroupName)

    @tdms_group_name.setter
    def tdms_group_name(self, value: str):
        """Gets or sets the name of the group in the TDMS file to log data to."""
        self._dotnet_instance.TDMSGroupName = next(_unwrap(None, value))

    @property
    def tdms_channel_name(self) -> str:
        """Gets or sets the name of the channel in the TDMS file to log data to."""
        return _wrap(self._dotnet_instance.TDMSChannelName)

    @tdms_channel_name.setter
    def tdms_channel_name(self, value: str):
        """Gets or sets the name of the channel in the TDMS file to log data to."""
        self._dotnet_instance.TDMSChannelName = next(_unwrap(None, value))

    @property
    def limit_type(self) -> FileLimitationType:
        """Gets or sets the criteria to use to stop logging data to the current file. When the limit you specify occurs, NI VeriStand either stops logging completely or continues logging in a new file, depending on the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Operation" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.LimitType)

    @limit_type.setter
    def limit_type(self, value: FileLimitationType):
        """Gets or sets the criteria to use to stop logging data to the current file. When the limit you specify occurs, NI VeriStand either stops logging completely or continues logging in a new file, depending on the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Operation" crefType="Unqualified" />."""
        self._dotnet_instance.LimitType = next(_unwrap(None, value))

    @property
    def trigger_type(self) -> DataLoggingTriggerType:
        """Gets or sets the type of trigger to use to start or stop data logging."""
        return _wrap(self._dotnet_instance.TriggerType)

    @trigger_type.setter
    def trigger_type(self, value: DataLoggingTriggerType):
        """Gets or sets the type of trigger to use to start or stop data logging."""
        self._dotnet_instance.TriggerType = next(_unwrap(None, value))

    @property
    def filter(self) -> DataLoggingFilterType:
        """Gets or sets whether and how to filter the logged frames."""
        return _wrap(self._dotnet_instance.Filter)

    @filter.setter
    def filter(self, value: DataLoggingFilterType):
        """Gets or sets whether and how to filter the logged frames."""
        self._dotnet_instance.Filter = next(_unwrap(None, value))

    @property
    def operation(self) -> DataLoggingOperationType:
        """Gets or sets the action to take when a trigger condition is met."""
        return _wrap(self._dotnet_instance.Operation)

    @operation.setter
    def operation(self, value: DataLoggingOperationType):
        """Gets or sets the action to take when a trigger condition is met."""
        self._dotnet_instance.Operation = next(_unwrap(None, value))

    @property
    def buffer_time(self) -> float:
        """Gets or sets the buffer time of the log file in seconds. Frames read will be added to the buffer until the specified amount of time has elapsed, at which point all buffered data will be written to the file.  If the buffer is partially full when a file is finished, the remaining data in the buffer will be written to the file.  If the buffer time is set to 0, data will be immediately written to the file when read."""
        return _wrap(self._dotnet_instance.BufferTime)

    @buffer_time.setter
    def buffer_time(self, value: float):
        """Gets or sets the buffer time of the log file in seconds. Frames read will be added to the buffer until the specified amount of time has elapsed, at which point all buffered data will be written to the file.  If the buffer is partially full when a file is finished, the remaining data in the buffer will be written to the file.  If the buffer time is set to 0, data will be immediately written to the file when read."""
        self._dotnet_instance.BufferTime = next(_unwrap(None, value))

    @property
    def destination(self) -> str:
        """Gets or sets the destination for a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" /> on disk."""
        return _wrap(self._dotnet_instance.Destination)

    @destination.setter
    def destination(self, value: str):
        """Gets or sets the destination for a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" /> on disk."""
        self._dotnet_instance.Destination = next(_unwrap(None, value))

    @property
    def filename(self) -> str:
        """Gets or sets the filename of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.Filename)

    @filename.setter
    def filename(self, value: str):
        """Gets or sets the filename of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />."""
        self._dotnet_instance.Filename = next(_unwrap(None, value))

    @property
    def retriggerable(self) -> bool:
        """Gets or sets whether logging can be retriggered after a stop. If <see langword="true" />, logging begins again when the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerChannel" crefType="Unqualified" /> reaches the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.Retriggerable)

    @retriggerable.setter
    def retriggerable(self, value: bool):
        """Gets or sets whether logging can be retriggered after a stop. If <see langword="true" />, logging begins again when the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerChannel" crefType="Unqualified" /> reaches the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />."""
        self._dotnet_instance.Retriggerable = next(_unwrap(None, value))

    @property
    def limit_value(self) -> int:
        """Gets or sets the value used to determine when to stop logging data to the current log file. This property can represent a size in kilobytes or a time in seconds, depending on the file's <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.LimitType" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.LimitValue)

    @limit_value.setter
    def limit_value(self, value: int):
        """Gets or sets the value used to determine when to stop logging data to the current log file. This property can represent a size in kilobytes or a time in seconds, depending on the file's <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.LimitType" crefType="Unqualified" />."""
        self._dotnet_instance.LimitValue = next(_unwrap(None, value))

    @property
    def number_of_bytes_to_read(self) -> int:
        """Gets or sets the maximum number of raw bytes to read. This number does not represent the number of frames to read. CAN and LIN frames are always 24 bytes long. FlexRay frames vary in length."""
        return _wrap(self._dotnet_instance.NumberOfBytesToRead)

    @number_of_bytes_to_read.setter
    def number_of_bytes_to_read(self, value: int):
        """Gets or sets the maximum number of raw bytes to read. This number does not represent the number of frames to read. CAN and LIN frames are always 24 bytes long. FlexRay frames vary in length."""
        self._dotnet_instance.NumberOfBytesToRead = next(_unwrap(None, value))

    @property
    def trigger_channel(self) -> BaseNode:
        """The channel to watch for the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.TriggerChannel)

    @trigger_channel.setter
    def trigger_channel(self, value: BaseNode):
        """The channel to watch for the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />."""
        self._dotnet_instance.TriggerChannel = next(_unwrap(None, value))

    @property
    def frame_i_ds(self) -> Sequence[str]:
        """Gets or sets the frame IDs in the XNET database cluster to either include in or exclude from data logging. Use this property when you configure a <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Filter" crefType="Unqualified" /> for the data logging file."""
        return _wrap(self._dotnet_instance.FrameIDs)

    @frame_i_ds.setter
    def frame_i_ds(self, value: Sequence[str]):
        """Gets or sets the frame IDs in the XNET database cluster to either include in or exclude from data logging. Use this property when you configure a <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Filter" crefType="Unqualified" /> for the data logging file."""
        self._dotnet_instance.FrameIDs = next(_unwrap(None, value))

    @overload
    def get_data_file_error(self) -> DataFileError:
        ...

    def get_data_file_error(self, *args):
        return _wrap(self._dotnet_instance.GetDataFileError(*_unwrap(None, *args)))

    @overload
    def get_data_file_status(self) -> DataFileStatus:
        ...

    def get_data_file_status(self, *args):
        return _wrap(self._dotnet_instance.GetDataFileStatus(*_unwrap(None, *args)))


class DataReplay(Section):
    """Represents the <format type="bold">Data Replay</format> section under an NI-XNET CAN port, which contains any <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay" crefType="Unqualified" /> files you want to replay onto the CAN bus."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DataReplay:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DataReplay")

    @overload
    def get_data_file_replay_list(self) -> Sequence[DataFileReplay]:
        ...

    def get_data_file_replay_list(self, *args):
        return _wrap(self._dotnet_instance.GetDataFileReplayList(*_unwrap(None, *args)))

    @overload
    def add_data_file_replay(self, data_file_replay: DataFileReplay) -> bool:
        ...

    def add_data_file_replay(self, *args):
        return _wrap(self._dotnet_instance.AddDataFileReplay(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class DataSharing(Section):
    """Represents the <format type="bold">Data Sharing</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis" crefType="Unqualified" />. This section contains any reflective memory devices you add to the system definition."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DataSharing:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DataSharing")

    @overload
    def get_reflective_memory(self) -> ReflectiveMemory:
        ...

    def get_reflective_memory(self, *args):
        return _wrap(self._dotnet_instance.GetReflectiveMemory(*_unwrap(None, *args)))

    @overload
    def add_reflective_memory(self, name: str) -> bool:
        ...

    def add_reflective_memory(self, *args):
        return _wrap(self._dotnet_instance.AddReflectiveMemory(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class DataSharingNetwork(Section):
    """Represents the <format type="bold">Data Sharing Network</format> section of the system definition, under which you can add and configure a reflective memory network. You can only configure one reflective memory network per system definition."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DataSharingNetwork:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DataSharingNetwork")

    @property
    def dynamic_data_size(self) -> int:
        """Gets or sets the number of channels in reflective memory to reserve for dynamically mapping channel data at run-time. For example, in a distributed system, if target A needs to access data provided by a channel on target B at run-time, the targets require a channel in reflective memory that target B can copy data to and target A can read data from."""
        return _wrap(self._dotnet_instance.DynamicDataSize)

    @dynamic_data_size.setter
    def dynamic_data_size(self, value: int):
        """Gets or sets the number of channels in reflective memory to reserve for dynamically mapping channel data at run-time. For example, in a distributed system, if target A needs to access data provided by a channel on target B at run-time, the targets require a channel in reflective memory that target B can copy data to and target A can read data from."""
        self._dotnet_instance.DynamicDataSize = next(_unwrap(None, value))

    @overload
    def get_reflective_memory_network(self) -> ReflectiveMemoryNetwork:
        ...

    def get_reflective_memory_network(self, *args):
        return _wrap(self._dotnet_instance.GetReflectiveMemoryNetwork(*_unwrap(None, *args)))

    @overload
    def add_reflective_memory_network(self, name: str) -> bool:
        ...

    def add_reflective_memory_network(self, *args):
        return _wrap(self._dotnet_instance.AddReflectiveMemoryNetwork(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Database(Section):
    """Represents an XNET database. XNET databases can be CANdb (<format type="monospace">.dbc</format>), NI-CAN (<format type="monospace">.ncd</format>), LDF (<format type="monospace">.ldf</format>), or FIBEX (<format type="monospace">.xml</format>) files."""

    @overload
    def __init__(self, name: str, md5: str):
        ...

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Database:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Database(*_unwrap(None, *args))

    @property
    def md5(self) -> Sequence[int]:
        """Gets the MD5 message-digest for the database as a byte array."""
        return _wrap(self._dotnet_instance.MD5)


class Dwell(Command):
    """Represents a <format type="bold">Dwell</format> step that you add to a procedure. The <format type="bold">Dwell</format> step suspends the procedure by the amount of time you specify."""

    @overload
    def __init__(self, name: str, description: str, dwell_time: float):
        ...

    @overload
    def __init__(self, name: str, description: str, dwell_time: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Dwell:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Dwell(*_unwrap(None, *args))

    @property
    def dwell_time_constant(self) -> float:
        """Gets the constant value that determines the amount of time to suspend the procedure."""
        return _wrap(self._dotnet_instance.DwellTimeConstant)

    @property
    def dwell_time_channel(self) -> BaseNode:
        """Gets the channel whose value determines the amount of time to suspend the procedure."""
        return _wrap(self._dotnet_instance.DwellTimeChannel)

    @property
    def dwell_time_is_constant(self) -> int:
        """Gets whether the amount of time to suspend the procedure is determined by a constant value or by a channel value."""
        return _wrap(self._dotnet_instance.DwellTimeIsConstant)

    @overload
    def set_dwell_time(self, dwell_time: float):
        ...

    @overload
    def set_dwell_time(self, dwell_time: BaseNode):
        ...

    def set_dwell_time(self, *args):
        return _wrap(self._dotnet_instance.SetDwellTime(*_unwrap(None, *args)))


class DynamicSignal(Channel, IChannel):
    """Represents a dynamic signal contained in a multiplexed frame. NI VeriStand organizes dynamic signals under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Mode" crefType="Unqualified" /> nodes."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DynamicSignal:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DynamicSignal")

    @property
    def md5(self) -> Sequence[int]:
        """Gets the MD5 message-digest for the signal."""
        return _wrap(self._dotnet_instance.MD5)


class End(Command):
    """Represents an <format type="bold">End</format> step that you can add to a procedure. The <format type="bold">End</format> step stops the procedure."""

    @overload
    def __init__(self, name: str, description: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.End:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.End(*_unwrap(None, *args))


class EventTriggered(Section):
    """Represents the <format type="bold">Event Triggered</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Outgoing" crefType="Unqualified" /> section of an NI-XNET CAN or FlexRay port."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.EventTriggered:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for EventTriggered")

    @overload
    def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]:
        ...

    def get_signal_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetSignalBasedFrameList(*_unwrap(None, *args)))

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        return _wrap(self._dotnet_instance.GetRawDataBasedFrameList(*_unwrap(None, *args)))

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddSignalBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        return _wrap(self._dotnet_instance.AddRawDataBasedFrame(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Execution(Section):
    """Represents the <format type="bold">Execution</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" crefType="Unqualified" />. This section contains channels that get and set execution details of the model, such as its current status and the amount of time that has elapsed since it began executing."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Execution:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Execution")

    @overload
    def get_model_command(self) -> ModelCommand:
        ...

    def get_model_command(self, *args):
        return _wrap(self._dotnet_instance.GetModelCommand(*_unwrap(None, *args)))

    @overload
    def get_model_status(self) -> ModelStatus:
        ...

    def get_model_status(self, *args):
        return _wrap(self._dotnet_instance.GetModelStatus(*_unwrap(None, *args)))

    @overload
    def get_model_time(self) -> ModelTime:
        ...

    def get_model_time(self, *args):
        return _wrap(self._dotnet_instance.GetModelTime(*_unwrap(None, *args)))


class ExecutionOrder(Section):
    """Represents the <format type="bold">Execution Order</format> section under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels" crefType="Unqualified" />, which contains information about the order that your models execute relative to each other in the VeriStand Engine."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ExecutionOrder:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ExecutionOrder")


class ExitSubroutine(Command):
    """Represents an <format type="bold">Exit Subroutine</format> step that you can add to a procedure. The <format type="bold">Exit Subroutine</format> step is typically used in procedures that are called from other procedures by a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CallProcedure" crefType="Unqualified" /> step. The <format type="bold">Exit Subroutine</format> step stops the current procedure and returns to the calling procedure."""

    @overload
    def __init__(self, name: str, description: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ExitSubroutine:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ExitSubroutine(*_unwrap(None, *args))


class FPGA(Section):
    """Represents the <format type="bold">FPGA</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis" crefType="Unqualified" /> in the system definition. This section contains all the FPGA devices you add under the chassis."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGA")

    @overload
    def add_fpga_device(self, fpga_config_file: str) -> FPGADevice:
        ...

    @overload
    def add_fpga_device(self) -> FPGADevice:
        ...

    def add_fpga_device(self, *args):
        return _wrap(self._dotnet_instance.AddFPGADevice(*_unwrap({(str,): (1, NationalInstruments.VeriStand.Error.NoError), (): (0, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def get_fpga_device_list(self) -> Sequence[FPGADevice]:
        ...

    def get_fpga_device_list(self, *args):
        return _wrap(self._dotnet_instance.GetFPGADeviceList(*_unwrap(None, *args)))


class FPGACategory(Section):
    """Represents a section under an FPGA device. Sections organize channels according to type. For example, <format type="bold">Input<entity value="raquo" />Analog</format>, <format type="bold">Output<entity value="raquo" />Digital</format>, and so on."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGACategory:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGACategory")

    @overload
    def get_category_list(self) -> Sequence[FPGACategory]:
        ...

    def get_category_list(self, *args):
        return _wrap(self._dotnet_instance.GetCategoryList(*_unwrap(None, *args)))

    @overload
    def get_channel_list(self) -> Sequence[FPGAChannel]:
        ...

    def get_channel_list(self, *args):
        return _wrap(self._dotnet_instance.GetChannelList(*_unwrap(None, *args)))


class FPGAChannel(Channel, IChannel):
    """Represents a channel of an FPGA device."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGAChannel:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGAChannel")

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of the FPGA channel."""
        return _wrap(self._dotnet_instance.InitialValue)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the FPGA channel."""
        self._dotnet_instance.InitialValue = next(_unwrap(None, value))

    @property
    def channel_bit_offset(self) -> int:
        """Gets the bit offset of the FPGA channel in the DMA packet."""
        return _wrap(self._dotnet_instance.ChannelBitOffset)

    @property
    def fxpiwl(self) -> int:
        """Gets the integer word length of a fixed-point FPGA channel."""
        return _wrap(self._dotnet_instance.FXPIWL)

    @property
    def fxpwl(self) -> int:
        """Gets the word length of a fixed-point FPGA channel."""
        return _wrap(self._dotnet_instance.FXPWL)

    @property
    def offset(self) -> float:
        """Gets or sets the offset of the FPGA channel."""
        return _wrap(self._dotnet_instance.Offset)

    @offset.setter
    def offset(self, value: float):
        """Gets or sets the offset of the FPGA channel."""
        self._dotnet_instance.Offset = next(_unwrap(None, value))

    @property
    def packet_index(self) -> int:
        """Gets the index of the packet in the DMA FIFO that defines the channel."""
        return _wrap(self._dotnet_instance.PacketIndex)

    @property
    def period_pwm(self) -> int:
        """Gets or sets the pulse width modulation (PWM) period for an output channel."""
        return _wrap(self._dotnet_instance.PeriodPWM)

    @period_pwm.setter
    def period_pwm(self, value: int):
        """Gets or sets the pulse width modulation (PWM) period for an output channel."""
        self._dotnet_instance.PeriodPWM = next(_unwrap(None, value))

    @property
    def representation(self) -> int:
        """Gets the data type of the FPGA channel as it is represented in the DMA packet."""
        return _wrap(self._dotnet_instance.Representation)

    @property
    def scaling(self) -> float:
        """Gets or sets the scaling value applied to a channel."""
        return _wrap(self._dotnet_instance.Scaling)

    @scaling.setter
    def scaling(self, value: float):
        """Gets or sets the scaling value applied to a channel."""
        self._dotnet_instance.Scaling = next(_unwrap(None, value))


class FPGADICategory(FPGACategory):
    """Represents the <format type="bold">Input<entity value="raquo" />Digital</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADICategory:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGADICategory")


class FPGADOCategory(FPGACategory):
    """Represents the <format type="bold">Output<entity value="raquo" />Digital</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADOCategory:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGADOCategory")


class FPGADevice(Section):
    """Represents an FPGA target under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA" crefType="Unqualified" /> section."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice(*_unwrap(None, *args))

    @property
    def read_packets(self) -> int:
        """Gets the number of DMA read packets."""
        return _wrap(self._dotnet_instance.ReadPackets)

    @property
    def write_packets(self) -> int:
        """Gets the number of DMA write packets."""
        return _wrap(self._dotnet_instance.WritePackets)

    @property
    def fpga_config_file(self) -> DependentFile:
        """Gets the FPGA configuration file used to define the FPGA target."""
        return _wrap(self._dotnet_instance.FPGAConfigFile)

    @property
    def fpga_bitfile(self) -> DependentFile:
        """Gets the name of the FPGA bitfile used for the FPGA target."""
        return _wrap(self._dotnet_instance.FPGABitfile)

    @property
    def latest_refresh(self) -> str:
        """Gets a timestamp indicating the last date and time that the FPGA configuration file, which specifies the content of the DMA FIFOs and how the device appears in System Explorer, was refreshed. Refreshing the configuration file essentially re-creates the device."""
        return _wrap(self._dotnet_instance.LatestRefresh)

    @overload
    def change_rio_address(self, address_number: int) -> bool:
        ...

    def change_rio_address(self, *args):
        return _wrap(self._dotnet_instance.ChangeRIOAddress(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def get_category_list(self) -> Sequence[FPGACategory]:
        ...

    def get_category_list(self, *args):
        return _wrap(self._dotnet_instance.GetCategoryList(*_unwrap(None, *args)))


class FPGADigitalInput(FPGAChannel, IChannel):
    """Represents an FPGA digital input channel."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADigitalInput:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGADigitalInput")


class FPGADigitalOutput(FPGAChannel, IChannel):
    """Represents an FPGA digital output channel."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADigitalOutput:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGADigitalOutput")


class FPGAPWMInCategory(FPGACategory):
    """Represents the <format type="bold">Input<entity value="raquo" />PWM</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGAPWMInCategory:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGAPWMInCategory")


class FPGAPWMInput(FPGAChannel, IChannel):
    """Represents an FPGA PWM input channel."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGAPWMInput:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGAPWMInput")


class FPGAPWMOutCategory(FPGACategory):
    """Represents the <format type="bold">Output<entity value="raquo" />PWM</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGAPWMOutCategory:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGAPWMOutCategory")


class FPGAPWMOutput(FPGAChannel, IChannel):
    """Represents an FPGA PWM output channel."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGAPWMOutput:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGAPWMOutput")


class FinishedFiles(Channel, IChannel):
    """Represents a <format type="bold">Finished Files</format> channel associated with an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.RawFrameDataLogging" crefType="Unqualified" /> file. This channel stores the number of completed log files for the current session of the VeriStand Engine. You can use this channel to determine when a file is ready for use by other processes."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FinishedFiles:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FinishedFiles")


class FlexRay(Section):
    """Represents the <format type="bold">FlexRay</format> section under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> in the system definition."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRay:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FlexRay")

    @overload
    def get_flex_ray_port_list(self) -> Sequence[FlexRayPort]:
        ...

    def get_flex_ray_port_list(self, *args):
        return _wrap(self._dotnet_instance.GetFlexRayPortList(*_unwrap(None, *args)))

    @overload
    def add_flex_ray_port(self, flex_ray_port: FlexRayPort) -> bool:
        ...

    def add_flex_ray_port(self, *args):
        return _wrap(self._dotnet_instance.AddFlexRayPort(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class FlexRayInterfaceChannels(Section):
    """Represents the <format type="bold">Interface</format> section under an NI-XNET FlexRay port. This section contains the port-specific channels which provide status information."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayInterfaceChannels:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FlexRayInterfaceChannels")

    @overload
    def get_poc_state_channel(self) -> Channel:
        ...

    def get_poc_state_channel(self, *args):
        return _wrap(self._dotnet_instance.GetPOCStateChannel(*_unwrap(None, *args)))

    @overload
    def get_clock_correction_failed_channel(self) -> Channel:
        ...

    def get_clock_correction_failed_channel(self, *args):
        return _wrap(self._dotnet_instance.GetClockCorrectionFailedChannel(*_unwrap(None, *args)))

    @overload
    def get_passive_to_active_count_channel(self) -> Channel:
        ...

    def get_passive_to_active_count_channel(self, *args):
        return _wrap(self._dotnet_instance.GetPassiveToActiveCountChannel(*_unwrap(None, *args)))

    @overload
    def get_channel_a_sleep_channel(self) -> Channel:
        ...

    def get_channel_a_sleep_channel(self, *args):
        return _wrap(self._dotnet_instance.GetChannelASleepChannel(*_unwrap(None, *args)))

    @overload
    def get_channel_b_sleep_channel(self) -> Channel:
        ...

    def get_channel_b_sleep_channel(self, *args):
        return _wrap(self._dotnet_instance.GetChannelBSleepChannel(*_unwrap(None, *args)))

    @overload
    def get_fault_channel(self) -> Channel:
        ...

    def get_fault_channel(self, *args):
        return _wrap(self._dotnet_instance.GetFaultChannel(*_unwrap(None, *args)))

    @overload
    def get_fault_code_channel(self) -> Channel:
        ...

    def get_fault_code_channel(self, *args):
        return _wrap(self._dotnet_instance.GetFaultCodeChannel(*_unwrap(None, *args)))

    @overload
    def create_poc_state_channel(self) -> Channel:
        ...

    def create_poc_state_channel(self, *args):
        return _wrap(self._dotnet_instance.CreatePOCStateChannel(*_unwrap(None, *args)))

    @overload
    def create_clock_correction_failed_channel(self) -> Channel:
        ...

    def create_clock_correction_failed_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateClockCorrectionFailedChannel(*_unwrap(None, *args)))

    @overload
    def create_passive_to_active_count_channel(self) -> Channel:
        ...

    def create_passive_to_active_count_channel(self, *args):
        return _wrap(self._dotnet_instance.CreatePassiveToActiveCountChannel(*_unwrap(None, *args)))

    @overload
    def create_channel_a_sleep_channel(self) -> Channel:
        ...

    def create_channel_a_sleep_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateChannelASleepChannel(*_unwrap(None, *args)))

    @overload
    def create_channel_b_sleep_channel(self) -> Channel:
        ...

    def create_channel_b_sleep_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateChannelBSleepChannel(*_unwrap(None, *args)))

    @overload
    def create_fault_channel(self) -> Channel:
        ...

    def create_fault_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateFaultChannel(*_unwrap(None, *args)))

    @overload
    def create_fault_code_channel(self) -> Channel:
        ...

    def create_fault_code_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateFaultCodeChannel(*_unwrap(None, *args)))


class FlexRayPort(Section):
    """Represents a port under an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRay" crefType="Unqualified" /> device."""

    @overload
    def __init__(self, name: str, port_number: int, linked_database: Database, cluster_name: str, baud_rate: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort(*_unwrap(None, *args))

    @property
    def disabled(self) -> bool:
        """Gets or sets whether the port is disabled."""
        return _wrap(self._dotnet_instance.Disabled)

    @disabled.setter
    def disabled(self, value: bool):
        """Gets or sets whether the port is disabled."""
        self._dotnet_instance.Disabled = next(_unwrap(None, value))

    @property
    def termination(self) -> XNETTermination:
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. This setting applies to both FlexRay communication channels (A and B) on each FlexRay interface."""
        return _wrap(self._dotnet_instance.Termination)

    @termination.setter
    def termination(self, value: XNETTermination):
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. This setting applies to both FlexRay communication channels (A and B) on each FlexRay interface."""
        self._dotnet_instance.Termination = next(_unwrap(None, value))

    @property
    def input_stream_read_time(self) -> float:
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        return _wrap(self._dotnet_instance.InputStreamReadTime)

    @input_stream_read_time.setter
    def input_stream_read_time(self, value: float):
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        self._dotnet_instance.InputStreamReadTime = next(_unwrap(None, value))

    @property
    def enable_passive_to_active(self) -> int:
        """Corresponds to the `Interface:FlexRay:Allow Passive to Active` property for the FlexRay port."""
        return _wrap(self._dotnet_instance.EnablePassiveToActive)

    @enable_passive_to_active.setter
    def enable_passive_to_active(self, value: int):
        """Corresponds to the `Interface:FlexRay:Allow Passive to Active` property for the FlexRay port."""
        self._dotnet_instance.EnablePassiveToActive = next(_unwrap(None, value))

    @property
    def port_number(self) -> int:
        """Gets or sets the physical address of the FlexRay port."""
        return _wrap(self._dotnet_instance.PortNumber)

    @port_number.setter
    def port_number(self, value: int):
        """Gets or sets the physical address of the FlexRay port."""
        self._dotnet_instance.PortNumber = next(_unwrap(None, value))

    @property
    def linked_database(self) -> BaseNode:
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.LinkedDatabase)

    @linked_database.setter
    def linked_database(self, value: BaseNode):
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />."""
        self._dotnet_instance.LinkedDatabase = next(_unwrap(None, value))

    @property
    def baud_rate(self) -> int:
        """Gets or sets the baud rate that all cluster nodes use."""
        return _wrap(self._dotnet_instance.BaudRate)

    @baud_rate.setter
    def baud_rate(self, value: int):
        """Gets or sets the baud rate that all cluster nodes use."""
        self._dotnet_instance.BaudRate = next(_unwrap(None, value))

    @property
    def cluster_name(self) -> str:
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.ClusterName)

    @cluster_name.setter
    def cluster_name(self, value: str):
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />."""
        self._dotnet_instance.ClusterName = next(_unwrap(None, value))

    @property
    def enable_cold_start(self) -> bool:
        """Gets or sets whether the FlexRay interface operates as a cold-start node on the cluster."""
        return _wrap(self._dotnet_instance.EnableColdStart)

    @enable_cold_start.setter
    def enable_cold_start(self, value: bool):
        """Gets or sets whether the FlexRay interface operates as a cold-start node on the cluster."""
        self._dotnet_instance.EnableColdStart = next(_unwrap(None, value))

    @property
    def key_slot(self) -> int:
        """Gets or sets the FlexRay slot number from which the XNET FlexRay interface transmits a startup frame during the process of integration with other cluster nodes."""
        return _wrap(self._dotnet_instance.KeySlot)

    @key_slot.setter
    def key_slot(self, value: int):
        """Gets or sets the FlexRay slot number from which the XNET FlexRay interface transmits a startup frame during the process of integration with other cluster nodes."""
        self._dotnet_instance.KeySlot = next(_unwrap(None, value))

    @property
    def incoming_rate(self) -> int:
        """Gets or sets the processing rate for incoming frames in hertz."""
        return _wrap(self._dotnet_instance.IncomingRate)

    @incoming_rate.setter
    def incoming_rate(self, value: int):
        """Gets or sets the processing rate for incoming frames in hertz."""
        self._dotnet_instance.IncomingRate = next(_unwrap(None, value))

    @property
    def outgoing_rate(self) -> int:
        """Gets or sets the processing rate for outgoing frames in hertz."""
        return _wrap(self._dotnet_instance.OutgoingRate)

    @outgoing_rate.setter
    def outgoing_rate(self, value: int):
        """Gets or sets the processing rate for outgoing frames in hertz."""
        self._dotnet_instance.OutgoingRate = next(_unwrap(None, value))

    @property
    def echo(self) -> bool:
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        return _wrap(self._dotnet_instance.Echo)

    @echo.setter
    def echo(self, value: bool):
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        self._dotnet_instance.Echo = next(_unwrap(None, value))

    @property
    def input_stream_queue_size(self) -> int:
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        return _wrap(self._dotnet_instance.InputStreamQueueSize)

    @input_stream_queue_size.setter
    def input_stream_queue_size(self, value: int):
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        self._dotnet_instance.InputStreamQueueSize = next(_unwrap(None, value))

    @property
    def inline_incoming(self) -> bool:
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        return _wrap(self._dotnet_instance.InlineIncoming)

    @inline_incoming.setter
    def inline_incoming(self, value: bool):
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        self._dotnet_instance.InlineIncoming = next(_unwrap(None, value))

    @property
    def inline_outgoing(self) -> bool:
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        return _wrap(self._dotnet_instance.InlineOutgoing)

    @inline_outgoing.setter
    def inline_outgoing(self, value: bool):
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        self._dotnet_instance.InlineOutgoing = next(_unwrap(None, value))

    @overload
    def get_interface_section(self) -> FlexRayInterfaceChannels:
        ...

    def get_interface_section(self, *args):
        return _wrap(self._dotnet_instance.GetInterfaceSection(*_unwrap(None, *args)))

    @overload
    def create_interface_section(self) -> FlexRayInterfaceChannels:
        ...

    def create_interface_section(self, *args):
        return _wrap(self._dotnet_instance.CreateInterfaceSection(*_unwrap(None, *args)))

    @overload
    def get_incoming(self) -> Incoming:
        ...

    def get_incoming(self, *args):
        return _wrap(self._dotnet_instance.GetIncoming(*_unwrap(None, *args)))

    @overload
    def get_outgoing(self) -> Outgoing:
        ...

    def get_outgoing(self, *args):
        return _wrap(self._dotnet_instance.GetOutgoing(*_unwrap(None, *args)))


class FrameFaulting(Section):
    """Represents a <format type="bold">Frame Faulting</format> section under an outgoing cyclic frame of an NI-XNET CAN port. This section contains channels you can use to configure the transmission of cyclic frames."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FrameFaulting:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FrameFaulting")

    @overload
    def get_skip_cyclic_frames(self) -> SkipCyclicFrames:
        ...

    def get_skip_cyclic_frames(self, *args):
        return _wrap(self._dotnet_instance.GetSkipCyclicFrames(*_unwrap(None, *args)))

    @overload
    def get_transmit_time(self) -> TransmitTime:
        ...

    def get_transmit_time(self, *args):
        return _wrap(self._dotnet_instance.GetTransmitTime(*_unwrap(None, *args)))


class FrameID(Channel, IChannel):
    """Represents a <format type="bold">Frame ID</format> channel under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FrameInformation" crefType="Unqualified" /> section of an incoming, raw data format NI-XNET frame. This channel contains the ID number that identifies the frame."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FrameID:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FrameID")

    @property
    def id(self) -> int:
        """Gets the ID number of the current incoming frame."""
        return _wrap(self._dotnet_instance.ID)


class FrameInformation(Section):
    """Represents a <format type="bold">Frame Information</format> section under an incoming NI-XNET frame. This section contains channels that store information about the frame, such as the timestamp at which it was received and the ID number of the current frame."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FrameInformation:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FrameInformation")

    @overload
    def get_receive_time(self) -> ReceiveTime:
        ...

    def get_receive_time(self, *args):
        return _wrap(self._dotnet_instance.GetReceiveTime(*_unwrap(None, *args)))

    @overload
    def get_time_difference(self) -> TimeDifference:
        ...

    def get_time_difference(self, *args):
        return _wrap(self._dotnet_instance.GetTimeDifference(*_unwrap(None, *args)))

    @overload
    def get_frame_id(self) -> FrameID:
        ...

    def get_frame_id(self, *args):
        return _wrap(self._dotnet_instance.GetFrameID(*_unwrap(None, *args)))


class Generator(Section):
    """Represents a stimulus generator in the Legacy Stimulus Profile Editor, which produces simulated real-world signals that stimulus profiles use to perform tests on a system."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Generator:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Generator")

    @overload
    def get_stimulus_channel_list(self) -> Sequence[StimulusChannel]:
        ...

    def get_stimulus_channel_list(self, *args):
        return _wrap(self._dotnet_instance.GetStimulusChannelList(*_unwrap(None, *args)))


class GotoLabel(Command):
    """Represents a <format type="bold">Goto Label</format> step that you can add to a procedure. When this step executes, the procedure jumps to the step specified by <see cref="M:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel.Label" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str, description: str, label: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel(*_unwrap(None, *args))

    @property
    def label(self) -> BaseNode:
        """Gets or sets the procedure step to execute when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel" crefType="Unqualified" /> step is executed."""
        return _wrap(self._dotnet_instance.Label)

    @label.setter
    def label(self, value: BaseNode):
        """Gets or sets the procedure step to execute when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel" crefType="Unqualified" /> step is executed."""
        self._dotnet_instance.Label = next(_unwrap(None, value))


class Hardware(Section):
    """Represents the <format type="bold">Hardware</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains any chassis you add."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Hardware:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Hardware")

    @overload
    def get_chassis_list(self) -> Sequence[Chassis]:
        ...

    def get_chassis_list(self, *args):
        return _wrap(self._dotnet_instance.GetChassisList(*_unwrap(None, *args)))

    @overload
    def get_slsc(self) -> SLSC:
        ...

    def get_slsc(self, *args):
        return _wrap(self._dotnet_instance.GetSLSC(*_unwrap(None, *args)))

    @overload
    def add_chassis(self, chassis: Chassis) -> bool:
        ...

    def add_chassis(self, *args):
        return _wrap(self._dotnet_instance.AddChassis(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_chassis(self, name: str) -> Chassis:
        ...

    def add_new_chassis(self, *args):
        return _wrap(self._dotnet_instance.AddNewChassis(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Incoming(Section):
    """Represent the <format type="bold">Incoming</format> section under an NI-XNET CAN, LIN, or FlexRay ports, which contains any incoming frames and data logging files ."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Incoming:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Incoming")

    @overload
    def get_single_point(self) -> SinglePoint:
        ...

    def get_single_point(self, *args):
        return _wrap(self._dotnet_instance.GetSinglePoint(*_unwrap(None, *args)))

    @overload
    def get_raw_frame_data_logging(self) -> RawFrameDataLogging:
        ...

    def get_raw_frame_data_logging(self, *args):
        return _wrap(self._dotnet_instance.GetRawFrameDataLogging(*_unwrap(None, *args)))


class Inport(Channel, IChannel):
    """Represents a model inport, or input."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Inport:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Inport")

    @property
    def initial_value(self) -> Union[System.Array[System.Double], Sequence[Sequence[float]]]:
        """Gets or sets the initial value of the model inport."""
        return _wrap(self._dotnet_instance.InitialValue)

    @initial_value.setter
    def initial_value(self, value: Union[System.Array[System.Double], Sequence[Sequence[float]]]):
        """Gets or sets the initial value of the model inport."""
        self._dotnet_instance.InitialValue = next(_unwrap(None, value))

    @property
    def index(self) -> int:
        """Gets the index of the inport in the inport vector (array)."""
        return _wrap(self._dotnet_instance.Index)


class Inports(Section):
    """Represents the top-level <format type="bold">Inports</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" crefType="Unqualified" />. This section contains all the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Inport" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.InportGroup" crefType="Unqualified" /> objects for the model."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Inports:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Inports")

    @overload
    def get_inports(self) -> Sequence[Inport]:
        ...

    @overload
    def get_inports(self, deep: bool) -> Sequence[Inport]:
        ...

    def get_inports(self, *args):
        return _wrap(self._dotnet_instance.GetInports(*_unwrap(None, *args)))

    @overload
    def get_inport_groups(self) -> Sequence[InportGroup]:
        ...

    def get_inport_groups(self, *args):
        return _wrap(self._dotnet_instance.GetInportGroups(*_unwrap(None, *args)))


class InputOverflowChannel(CustomDeviceChannel, IChannel):
    """Represents an input overflow count channel, which tracks the number of times the system fails to write data to an asynchronous custom device because the FIFO is full. A single custom device can have only one input overflow count channel."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.InputOverflowChannel:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.InputOverflowChannel(*_unwrap(None, *args))


class LIN(Section):
    """Represents the <format type="bold">LIN</format> section under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> in the system definition."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.LIN:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for LIN")

    @overload
    def get_lin_port_list(self) -> Sequence[LINPort]:
        ...

    def get_lin_port_list(self, *args):
        return _wrap(self._dotnet_instance.GetLINPortList(*_unwrap(None, *args)))

    @overload
    def add_lin_port(self, lin_port: LINPort) -> bool:
        ...

    def add_lin_port(self, *args):
        return _wrap(self._dotnet_instance.AddLINPort(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class LINInterfaceChannels(Section):
    """Represents the <format type="bold">Interface</format> section under an NI-XNET LIN port. This section contains the port-specific channels which provide status information."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.LINInterfaceChannels:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for LINInterfaceChannels")

    @overload
    def get_communication_state_channel(self) -> Channel:
        ...

    def get_communication_state_channel(self, *args):
        return _wrap(self._dotnet_instance.GetCommunicationStateChannel(*_unwrap(None, *args)))

    @overload
    def get_fault_channel(self) -> Channel:
        ...

    def get_fault_channel(self, *args):
        return _wrap(self._dotnet_instance.GetFaultChannel(*_unwrap(None, *args)))

    @overload
    def get_fault_code_channel(self) -> Channel:
        ...

    def get_fault_code_channel(self, *args):
        return _wrap(self._dotnet_instance.GetFaultCodeChannel(*_unwrap(None, *args)))

    @overload
    def get_last_error_channel(self) -> Channel:
        ...

    def get_last_error_channel(self, *args):
        return _wrap(self._dotnet_instance.GetLastErrorChannel(*_unwrap(None, *args)))

    @overload
    def get_last_error_expected_channel(self) -> Channel:
        ...

    def get_last_error_expected_channel(self, *args):
        return _wrap(self._dotnet_instance.GetLastErrorExpectedChannel(*_unwrap(None, *args)))

    @overload
    def get_last_error_identifier_channel(self) -> Channel:
        ...

    def get_last_error_identifier_channel(self, *args):
        return _wrap(self._dotnet_instance.GetLastErrorIdentifierChannel(*_unwrap(None, *args)))

    @overload
    def get_last_error_received_channel(self) -> Channel:
        ...

    def get_last_error_received_channel(self, *args):
        return _wrap(self._dotnet_instance.GetLastErrorReceivedChannel(*_unwrap(None, *args)))

    @overload
    def get_last_error_timestamp_channel(self) -> Channel:
        ...

    def get_last_error_timestamp_channel(self, *args):
        return _wrap(self._dotnet_instance.GetLastErrorTimestampChannel(*_unwrap(None, *args)))

    @overload
    def get_sleep_channel(self) -> Channel:
        ...

    def get_sleep_channel(self, *args):
        return _wrap(self._dotnet_instance.GetSleepChannel(*_unwrap(None, *args)))

    @overload
    def get_transceiver_ready_channel(self) -> Channel:
        ...

    def get_transceiver_ready_channel(self, *args):
        return _wrap(self._dotnet_instance.GetTransceiverReadyChannel(*_unwrap(None, *args)))

    @overload
    def create_communication_state_channel(self) -> Channel:
        ...

    def create_communication_state_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateCommunicationStateChannel(*_unwrap(None, *args)))

    @overload
    def create_fault_channel(self) -> Channel:
        ...

    def create_fault_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateFaultChannel(*_unwrap(None, *args)))

    @overload
    def create_fault_code_channel(self) -> Channel:
        ...

    def create_fault_code_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateFaultCodeChannel(*_unwrap(None, *args)))

    @overload
    def create_last_error_channel(self) -> Channel:
        ...

    def create_last_error_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateLastErrorChannel(*_unwrap(None, *args)))

    @overload
    def create_last_error_expected_channel(self) -> Channel:
        ...

    def create_last_error_expected_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateLastErrorExpectedChannel(*_unwrap(None, *args)))

    @overload
    def create_last_error_identifier_channel(self) -> Channel:
        ...

    def create_last_error_identifier_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateLastErrorIdentifierChannel(*_unwrap(None, *args)))

    @overload
    def create_last_error_received_channel(self) -> Channel:
        ...

    def create_last_error_received_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateLastErrorReceivedChannel(*_unwrap(None, *args)))

    @overload
    def create_last_error_timestamp_channel(self) -> Channel:
        ...

    def create_last_error_timestamp_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateLastErrorTimestampChannel(*_unwrap(None, *args)))

    @overload
    def create_sleep_channel(self) -> Channel:
        ...

    def create_sleep_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateSleepChannel(*_unwrap(None, *args)))

    @overload
    def create_transceiver_state_channel(self) -> Channel:
        ...

    def create_transceiver_state_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateTransceiverStateChannel(*_unwrap(None, *args)))


class LINPort(Section):
    """Represents a port under an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LIN" crefType="Unqualified" /> device."""

    @overload
    def __init__(self, name: str, port_number: int, linked_database: Database, cluster_name: str, baud_rate: int, lin_schedules: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort(*_unwrap(None, *args))

    @property
    def disabled(self) -> bool:
        """Gets or sets whether the port is disabled."""
        return _wrap(self._dotnet_instance.Disabled)

    @disabled.setter
    def disabled(self, value: bool):
        """Gets or sets whether the port is disabled."""
        self._dotnet_instance.Disabled = next(_unwrap(None, value))

    @property
    def termination(self) -> XNETTermination:
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. You can select <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.Off" crefType="Unqualified" /> (disabled) and <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.On" crefType="Unqualified" /> (enabled)."""
        return _wrap(self._dotnet_instance.Termination)

    @termination.setter
    def termination(self, value: XNETTermination):
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. You can select <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.Off" crefType="Unqualified" /> (disabled) and <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.On" crefType="Unqualified" /> (enabled)."""
        self._dotnet_instance.Termination = next(_unwrap(None, value))

    @property
    def input_stream_read_time(self) -> float:
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        return _wrap(self._dotnet_instance.InputStreamReadTime)

    @input_stream_read_time.setter
    def input_stream_read_time(self, value: float):
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        self._dotnet_instance.InputStreamReadTime = next(_unwrap(None, value))

    @property
    def port_number(self) -> int:
        """Gets or sets the physical address of the LIN port."""
        return _wrap(self._dotnet_instance.PortNumber)

    @port_number.setter
    def port_number(self, value: int):
        """Gets or sets the physical address of the LIN port."""
        self._dotnet_instance.PortNumber = next(_unwrap(None, value))

    @property
    def linked_database(self) -> BaseNode:
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.LinkedDatabase)

    @linked_database.setter
    def linked_database(self, value: BaseNode):
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />."""
        self._dotnet_instance.LinkedDatabase = next(_unwrap(None, value))

    @property
    def baud_rate(self) -> int:
        """Gets or sets the baud rate that all cluster nodes use."""
        return _wrap(self._dotnet_instance.BaudRate)

    @baud_rate.setter
    def baud_rate(self, value: int):
        """Gets or sets the baud rate that all cluster nodes use."""
        self._dotnet_instance.BaudRate = next(_unwrap(None, value))

    @property
    def cluster_name(self) -> str:
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.ClusterName)

    @cluster_name.setter
    def cluster_name(self, value: str):
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />."""
        self._dotnet_instance.ClusterName = next(_unwrap(None, value))

    @property
    def lin_schedules(self) -> str:
        """Gets or sets the names of all the available LIN schedules."""
        return _wrap(self._dotnet_instance.LINSchedules)

    @lin_schedules.setter
    def lin_schedules(self, value: str):
        """Gets or sets the names of all the available LIN schedules."""
        self._dotnet_instance.LINSchedules = next(_unwrap(None, value))

    @property
    def incoming_rate(self) -> int:
        """Gets or sets the processing rate for outgoing frames in hertz."""
        return _wrap(self._dotnet_instance.IncomingRate)

    @incoming_rate.setter
    def incoming_rate(self, value: int):
        """Gets or sets the processing rate for outgoing frames in hertz."""
        self._dotnet_instance.IncomingRate = next(_unwrap(None, value))

    @property
    def outgoing_rate(self) -> int:
        """Gets or sets the processing rate for outgoing frames in hertz."""
        return _wrap(self._dotnet_instance.OutgoingRate)

    @outgoing_rate.setter
    def outgoing_rate(self, value: int):
        """Gets or sets the processing rate for outgoing frames in hertz."""
        self._dotnet_instance.OutgoingRate = next(_unwrap(None, value))

    @property
    def echo(self) -> bool:
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        return _wrap(self._dotnet_instance.Echo)

    @echo.setter
    def echo(self, value: bool):
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        self._dotnet_instance.Echo = next(_unwrap(None, value))

    @property
    def input_stream_queue_size(self) -> int:
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        return _wrap(self._dotnet_instance.InputStreamQueueSize)

    @input_stream_queue_size.setter
    def input_stream_queue_size(self, value: int):
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        self._dotnet_instance.InputStreamQueueSize = next(_unwrap(None, value))

    @property
    def is_master(self) -> bool:
        """Gets or sets whether the port is the master for the network. A LIN network always consists of one master and several slaves. The master transmits the schedule for frame headers, which are remote requests for specific frame IDs."""
        return _wrap(self._dotnet_instance.IsMaster)

    @is_master.setter
    def is_master(self, value: bool):
        """Gets or sets whether the port is the master for the network. A LIN network always consists of one master and several slaves. The master transmits the schedule for frame headers, which are remote requests for specific frame IDs."""
        self._dotnet_instance.IsMaster = next(_unwrap(None, value))

    @property
    def inline_incoming(self) -> bool:
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        return _wrap(self._dotnet_instance.InlineIncoming)

    @inline_incoming.setter
    def inline_incoming(self, value: bool):
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        self._dotnet_instance.InlineIncoming = next(_unwrap(None, value))

    @property
    def inline_outgoing(self) -> bool:
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        return _wrap(self._dotnet_instance.InlineOutgoing)

    @inline_outgoing.setter
    def inline_outgoing(self, value: bool):
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        self._dotnet_instance.InlineOutgoing = next(_unwrap(None, value))

    @overload
    def get_interface_section(self) -> LINInterfaceChannels:
        ...

    def get_interface_section(self, *args):
        return _wrap(self._dotnet_instance.GetInterfaceSection(*_unwrap(None, *args)))

    @overload
    def create_interface_section(self) -> LINInterfaceChannels:
        ...

    def create_interface_section(self, *args):
        return _wrap(self._dotnet_instance.CreateInterfaceSection(*_unwrap(None, *args)))

    @overload
    def get_incoming(self) -> Incoming:
        ...

    def get_incoming(self, *args):
        return _wrap(self._dotnet_instance.GetIncoming(*_unwrap(None, *args)))

    @overload
    def get_outgoing(self) -> Outgoing:
        ...

    def get_outgoing(self, *args):
        return _wrap(self._dotnet_instance.GetOutgoing(*_unwrap(None, *args)))

    @overload
    def get_lin_scheduler(self) -> LINScheduler:
        ...

    def get_lin_scheduler(self, *args):
        return _wrap(self._dotnet_instance.GetLINScheduler(*_unwrap(None, *args)))


class LINScheduler(Channel, IChannel):
    """Represents the <format type="bold">LIN Scheduler</format> channel under an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />. The LIN Scheduler specifies which schedule to use to determine when to transmit frames. This channel is only valid if the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" /> to which is belongs is configured as the master port (<see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort.IsMaster" crefType="PartiallyQualified" /> is <see langword="true" />)."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.LINScheduler:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for LINScheduler")

    @property
    def units(self) -> str:
        """Gets the units associated with the LIN Scheduler channel."""
        return _wrap(self._dotnet_instance.Units)

    @property
    def active_schedule(self) -> str:
        """Gets or sets the name of the active LIN schedule."""
        return _wrap(self._dotnet_instance.ActiveSchedule)

    @active_schedule.setter
    def active_schedule(self, value: str):
        """Gets or sets the name of the active LIN schedule."""
        self._dotnet_instance.ActiveSchedule = next(_unwrap(None, value))

    @overload
    def set_active_schedule(self, lin_schedules: Sequence[str], active_schedule_index: int) -> bool:
        ...

    @overload
    def set_active_schedule(self, lin_schedules: Sequence[str], active_schedule: str) -> bool:
        ...

    def set_active_schedule(self, *args):
        return _wrap(self._dotnet_instance.SetActiveSchedule(*_unwrap(None, *args)))


class Mode(Section):
    """Represents a <format type="bold">Mode</format> section under a signal format NI-XNET CAN frame. The <format type="bold">Mode</format> section organizes dynamic (multiplexed) signals according to their mode values."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Mode:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Mode")

    @overload
    def get_dynamic_signal(self) -> DynamicSignal:
        ...

    def get_dynamic_signal(self, *args):
        return _wrap(self._dotnet_instance.GetDynamicSignal(*_unwrap(None, *args)))

    @overload
    def get_all_dynamic_signals(self) -> Sequence[DynamicSignal]:
        ...

    def get_all_dynamic_signals(self, *args):
        return _wrap(self._dotnet_instance.GetAllDynamicSignals(*_unwrap(None, *args)))

    @overload
    def get_mode_information(self) -> ModeInformation:
        ...

    def get_mode_information(self, *args):
        return _wrap(self._dotnet_instance.GetModeInformation(*_unwrap(None, *args)))

    @overload
    def create_mode_information(self) -> ModeInformation:
        ...

    def create_mode_information(self, *args):
        return _wrap(self._dotnet_instance.CreateModeInformation(*_unwrap(None, *args)))

    @overload
    def add_dynamic_signal(self, signal_name: str, description: str, units: str, default_value: float) -> bool:
        ...

    def add_dynamic_signal(self, *args):
        return _wrap(self._dotnet_instance.AddDynamicSignal(*_unwrap({None: (4, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class ModeInformation(Section):
    """Represents a <format type="bold">Mode Information</format> section under an NI-XNET CAN multiplexer mode. This section contains channels that store information about the mode, such as the timestamp at which it was received."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModeInformation:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ModeInformation")

    @overload
    def get_receive_time(self) -> ModeReceiveTime:
        ...

    def get_receive_time(self, *args):
        return _wrap(self._dotnet_instance.GetReceiveTime(*_unwrap(None, *args)))

    @overload
    def get_time_difference(self) -> ModeTimeDifference:
        ...

    def get_time_difference(self, *args):
        return _wrap(self._dotnet_instance.GetTimeDifference(*_unwrap(None, *args)))


class ModeReceiveTime(Channel, IChannel):
    """Represents the <format type="bold">Mode Receive Time</format> channel for an incoming NI-XNET CAN multiplexer mode. This channel contains the most recent timestamp at which the mode was received."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModeReceiveTime:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ModeReceiveTime")

    @overload
    def remove_node(self) -> bool:
        ...

    def remove_node(self, *args):
        return _wrap(self._dotnet_instance.RemoveNode(*_unwrap(None, *args)))


class ModeTimeDifference(Channel, IChannel):
    """Represents the <format type="bold">Mode Time Difference</format> channel for an incoming NI-XNET CAN multiplexer mode. This channel stores the difference between the two most recent <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModeReceiveTime" /> timestamps."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModeTimeDifference:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ModeTimeDifference")


class Model(Section):
    """Represents a model, which is a mathematical representation of a real-world system. A model responds to stimuli by producing outputs in a way that emulates the behavior of the modeled item. Models contain inputs and outputs that send and receive data. Models contain parameters you can manipulate and signals whose values you can view. For example, a model that generates a sine wave contains parameters that adjust the amplitude and frequency of the sine wave. You can view the value of the sine wave using the model signal."""

    @overload
    def __init__(self, name: str, description: str, model_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, parameter_regular_expression: str, global_parameter_scope: GlobalParameterScopes, import_signals: bool, signal_regular_expression: str, import_only_named_signals: bool, ni_veri_stand_server_port: int):
        ...

    @overload
    def __init__(self, name: str, description: str, model_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, parameter_regular_expression: str, import_signals: bool, signal_regular_expression: str, import_only_named_signals: bool):
        ...

    @overload
    def __init__(self, name: str, description: str, model_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, parameter_regular_expression: str, import_signals: bool, signal_regular_expression: str, import_only_named_signals: bool, ni_veri_stand_server_port: int):
        ...

    @overload
    def __init__(self, name: str, description: str, model_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, import_signals: bool):
        ...

    @overload
    def __init__(self, name: str, description: str, model_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, import_signals: bool, ni_veri_stand_server_port: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Model:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Model(*_unwrap(None, *args))

    @_staticproperty
    def automatic_processor_value() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Model.AutomaticProcessorValue)

    @property
    def load_success(self) -> bool:
        """Gets whether NI VeriStand loaded the model successfully."""
        return _wrap(self._dotnet_instance.LoadSuccess)

    @property
    def global_parameter_scope(self) -> GlobalParameterScopes:
        """Gets or sets whether global parameters in the current model share their values with other models on the same target."""
        return _wrap(self._dotnet_instance.GlobalParameterScope)

    @global_parameter_scope.setter
    def global_parameter_scope(self, value: GlobalParameterScopes):
        """Gets or sets whether global parameters in the current model share their values with other models on the same target."""
        self._dotnet_instance.GlobalParameterScope = next(_unwrap(None, value))

    @property
    def model_execution_group(self) -> int:
        """Gets or sets the model execution group"""
        return _wrap(self._dotnet_instance.ModelExecutionGroup)

    @model_execution_group.setter
    def model_execution_group(self, value: int):
        """Gets or sets the model execution group"""
        self._dotnet_instance.ModelExecutionGroup = next(_unwrap(None, value))

    @property
    def model_descriptor(self) -> IModelDescriptor:
        """Gets the model descriptor"""
        return _wrap(self._dotnet_instance.ModelDescriptor)

    @property
    def base_rate(self) -> float:
        """Gets the base rate of the model in microseconds."""
        return _wrap(self._dotnet_instance.BaseRate)

    @property
    def dll_size(self) -> int:
        """Gets the size, in bytes, of the compiled version of the model (<format type="monospace">.dll</format> file)."""
        return _wrap(self._dotnet_instance.DLLSize)

    @property
    def dll_timestamp(self) -> float:
        """Gets the time at which the model DLL was compiled."""
        return _wrap(self._dotnet_instance.DLLTimestamp)

    @property
    def model_bitness(self) -> int:
        """Gets the bitness of the compiled model (32- or 64-bit)."""
        return _wrap(self._dotnet_instance.ModelBitness)

    @property
    def decimation(self) -> int:
        """Gets or sets the decimation applied to the Primary Control Loop rate to determine the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Model.BaseRate" crefType="Unqualified" /> of the model."""
        return _wrap(self._dotnet_instance.Decimation)

    @decimation.setter
    def decimation(self, value: int):
        """Gets or sets the decimation applied to the Primary Control Loop rate to determine the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Model.BaseRate" crefType="Unqualified" /> of the model."""
        self._dotnet_instance.Decimation = next(_unwrap(None, value))

    @property
    def model_timestamp(self) -> float:
        """Gets the time at which the model was last saved."""
        return _wrap(self._dotnet_instance.ModelTimestamp)

    @property
    def processor(self) -> int:
        """Gets or sets the processor on which the Model Execution Loop executes. -2 (AutomaticProcessorValue) automatically assigns the processor to <entity value="quot" />any available<entity value="quot" />."""
        return _wrap(self._dotnet_instance.Processor)

    @processor.setter
    def processor(self, value: int):
        """Gets or sets the processor on which the Model Execution Loop executes. -2 (AutomaticProcessorValue) automatically assigns the processor to <entity value="quot" />any available<entity value="quot" />."""
        self._dotnet_instance.Processor = next(_unwrap(None, value))

    @property
    def show_unnamed_signals(self) -> bool:
        """Gets whether signals without names are visible."""
        return _wrap(self._dotnet_instance.ShowUnnamedSignals)

    @property
    def user_rate(self) -> float:
        """<para>THIS PROPERTY IS OBSOLETE in NI VeriStand 2011 SP1 and later. Use <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Model.BaseRate" crefType="Unqualified" /> instead.</para>
            Gets the user rate of the model."""
        return _wrap(self._dotnet_instance.UserRate)

    @property
    def segment_vectors(self) -> bool:
        """Gets information about whether or not vector inputs, outputs, parameters, and signals were split up into scalar channels when the model was loaded."""
        return _wrap(self._dotnet_instance.SegmentVectors)

    @property
    def md5(self) -> str:
        """Gets the MD5 message-digest for the model."""
        return _wrap(self._dotnet_instance.MD5)

    @property
    def ni_veri_stand_server_port(self) -> int:
        """Gets or sets the network port that the model uses for communication via TCP. This property only applies to uncompiled models from The MathWorks, Inc. Simulink<entity value="reg" /> software. DLLs and <format type="monospace">.lvmodel</format> files do not require a network port."""
        return _wrap(self._dotnet_instance.NIVeriStandServerPort)

    @ni_veri_stand_server_port.setter
    def ni_veri_stand_server_port(self, value: int):
        """Gets or sets the network port that the model uses for communication via TCP. This property only applies to uncompiled models from The MathWorks, Inc. Simulink<entity value="reg" /> software. DLLs and <format type="monospace">.lvmodel</format> files do not require a network port."""
        self._dotnet_instance.NIVeriStandServerPort = next(_unwrap(None, value))

    @property
    def dll_path(self) -> DependentFile:
        """Gets a reference to the compiled version of the model (<format type="monospace">.dll</format> file)."""
        return _wrap(self._dotnet_instance.DLLPath)

    @property
    def model_path(self) -> DependentFile:
        """Gets a reference to the uncompiled model file."""
        return _wrap(self._dotnet_instance.ModelPath)

    @property
    def file_version(self) -> str:
        """Gets the model version"""
        return _wrap(self._dotnet_instance.FileVersion)

    @property
    def model_generation_toolchain_version(self) -> str:
        """Version of the tool that was used to generate the model"""
        return _wrap(self._dotnet_instance.ModelGenerationToolchainVersion)

    @property
    def model_author(self) -> str:
        """Author of the model"""
        return _wrap(self._dotnet_instance.ModelAuthor)

    @property
    def target_platforms(self) -> Sequence[str]:
        """Target platforms supported by the model"""
        return _wrap(self._dotnet_instance.TargetPlatforms)

    @property
    def product_name(self) -> str:
        """Gets the product name"""
        return _wrap(self._dotnet_instance.ProductName)

    @property
    def internal_name(self) -> str:
        """Gets the internal name"""
        return _wrap(self._dotnet_instance.InternalName)

    @property
    def company_name(self) -> str:
        """Gets the company name"""
        return _wrap(self._dotnet_instance.CompanyName)

    @property
    def legal_copyright(self) -> str:
        """Gets the legal copyright"""
        return _wrap(self._dotnet_instance.LegalCopyright)

    @property
    def file_description(self) -> str:
        """Gets the file description"""
        return _wrap(self._dotnet_instance.FileDescription)

    @overload
    def get_section_with_all_parameters(self) -> ModelParameters:
        ...

    def get_section_with_all_parameters(self, *args):
        return _wrap(self._dotnet_instance.GetSectionWithAllParameters(*_unwrap(None, *args)))

    @overload
    def get_section_with_all_signals(self) -> ModelSignals:
        ...

    def get_section_with_all_signals(self, *args):
        return _wrap(self._dotnet_instance.GetSectionWithAllSignals(*_unwrap(None, *args)))

    @overload
    def reload_model_from_path(self, new_path: str, segment_vectors: bool) -> Sequence[str]:
        ...

    @overload
    def reload_model_from_path(self, new_path: str) -> Sequence[str]:
        ...

    def reload_model_from_path(self, *args):
        return _wrap(self._dotnet_instance.ReloadModelFromPath(*_unwrap(None, *args)))

    @overload
    def rename_node(self, new_name: str) -> bool:
        ...

    def rename_node(self, *args):
        return _wrap(self._dotnet_instance.RenameNode(*_unwrap(None, *args)))

    @overload
    def get_model_details(self) -> System.Collections.Generic.Dictionary[System.String,System.String]:
        ...

    def get_model_details(self, *args):
        return _wrap(self._dotnet_instance.GetModelDetails(*_unwrap(None, *args)))

    @overload
    def import_parameters(self, parameters: Iterable[ModelParameter]) -> bool:
        ...

    def import_parameters(self, *args):
        return _wrap(self._dotnet_instance.ImportParameters(*_unwrap(None, *args)))

    @overload
    def import_signals(self, signals: Iterable[ModelSignal]) -> bool:
        ...

    def import_signals(self, *args):
        return _wrap(self._dotnet_instance.ImportSignals(*_unwrap(None, *args)))

    @overload
    def remove_parameters(self, parameters: Iterable[ModelParameter]):
        ...

    def remove_parameters(self, *args):
        return _wrap(self._dotnet_instance.RemoveParameters(*_unwrap(None, *args)))

    @overload
    def remove_signals(self, signals: Iterable[ModelSignal]):
        ...

    def remove_signals(self, *args):
        return _wrap(self._dotnet_instance.RemoveSignals(*_unwrap(None, *args)))

    @overload
    def get_execution_section(self) -> Execution:
        ...

    def get_execution_section(self, *args):
        return _wrap(self._dotnet_instance.GetExecutionSection(*_unwrap(None, *args)))

    @overload
    def get_inports_section(self) -> Inports:
        ...

    def get_inports_section(self, *args):
        return _wrap(self._dotnet_instance.GetInportsSection(*_unwrap(None, *args)))

    @overload
    def get_outports_section(self) -> Outports:
        ...

    def get_outports_section(self, *args):
        return _wrap(self._dotnet_instance.GetOutportsSection(*_unwrap(None, *args)))

    @overload
    def get_parameters_section(self) -> ModelParameters:
        ...

    def get_parameters_section(self, *args):
        return _wrap(self._dotnet_instance.GetParametersSection(*_unwrap(None, *args)))

    @overload
    def get_signals_section(self) -> ModelSignals:
        ...

    def get_signals_section(self, *args):
        return _wrap(self._dotnet_instance.GetSignalsSection(*_unwrap(None, *args)))


class ModelCommand(Channel, IChannel):
    """Represents a <format type="bold">Model Command</format> channel, which you can use to send commands to the model running on the target."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommand:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ModelCommand")

    @property
    def initial_state(self) -> ModelCommandState:
        """Gets or sets the initial execution state of the model."""
        return _wrap(self._dotnet_instance.InitialState)

    @initial_state.setter
    def initial_state(self, value: ModelCommandState):
        """Gets or sets the initial execution state of the model."""
        self._dotnet_instance.InitialState = next(_unwrap(None, value))


class ModelDefaultGroup(Section):
    """Represents a parent class for the different types of sub-folders and sections a model can have."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelDefaultGroup:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ModelDefaultGroup")


class ModelParameter(Channel, IChannel):
    """Represents a model parameter."""

    @overload
    def __init__(self, parameter: ModelParamType, expression: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameter:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameter(*_unwrap(None, *args))

    @property
    def model_path(self) -> str:
        """Gets the symbolic path to the parameter within the model."""
        return _wrap(self._dotnet_instance.ModelPath)

    @property
    def expression(self) -> str:
        """Gets the expression of the model parameter."""
        return _wrap(self._dotnet_instance.Expression)

    @property
    def index(self) -> int:
        """Gets the index of the model parameter."""
        return _wrap(self._dotnet_instance.Index)


class ModelParameterGroup(ModelDefaultGroup):
    """Represents a sub-section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameters" crefType="Unqualified" /> section of a model. Parameter groups provide organization within the model."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameterGroup:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameterGroup(*_unwrap(None, *args))

    @overload
    def get_model_parameter_groups(self) -> Sequence[ModelParameterGroup]:
        ...

    def get_model_parameter_groups(self, *args):
        return _wrap(self._dotnet_instance.GetModelParameterGroups(*_unwrap(None, *args)))

    @overload
    def get_parameters(self) -> Sequence[ModelParameter]:
        ...

    @overload
    def get_parameters(self, deep: bool) -> Sequence[ModelParameter]:
        ...

    def get_parameters(self, *args):
        return _wrap(self._dotnet_instance.GetParameters(*_unwrap(None, *args)))

    @overload
    def add_model_parameter_group(self, model_parameter_group: ModelParameterGroup) -> bool:
        ...

    def add_model_parameter_group(self, *args):
        return _wrap(self._dotnet_instance.AddModelParameterGroup(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_model_parameter(self, model_parameter: ModelParameter) -> bool:
        ...

    def add_model_parameter(self, *args):
        return _wrap(self._dotnet_instance.AddModelParameter(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_model_parameters(self, model_parameters: Sequence[ModelParameter]) -> bool:
        ...

    def add_model_parameters(self, *args):
        return _wrap(self._dotnet_instance.AddModelParameters(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class ModelParameters(Section):
    """Represents the top-level <format type="bold">Parameters</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" crefType="Unqualified" />. This section contains all the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameter" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameterGroup" crefType="Unqualified" /> objects under the model."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameters:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ModelParameters")

    @overload
    def get_parameters(self) -> Sequence[ModelParameter]:
        ...

    @overload
    def get_parameters(self, deep: bool) -> Sequence[ModelParameter]:
        ...

    def get_parameters(self, *args):
        return _wrap(self._dotnet_instance.GetParameters(*_unwrap(None, *args)))

    @overload
    def get_model_parameter_groups(self) -> Sequence[ModelParameterGroup]:
        ...

    def get_model_parameter_groups(self, *args):
        return _wrap(self._dotnet_instance.GetModelParameterGroups(*_unwrap(None, *args)))

    @overload
    def add_parameter(self, parameter: ModelParameter) -> bool:
        ...

    def add_parameter(self, *args):
        return _wrap(self._dotnet_instance.AddParameter(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_parameters(self, model_parameters: Sequence[ModelParameter]) -> bool:
        ...

    def add_parameters(self, *args):
        return _wrap(self._dotnet_instance.AddParameters(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_model_parameter_group(self, model_parameter_group: ModelParameterGroup) -> bool:
        ...

    def add_model_parameter_group(self, *args):
        return _wrap(self._dotnet_instance.AddModelParameterGroup(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class ModelSignal(Channel, IChannel):
    """Represents a model signal."""

    @overload
    def __init__(self, signal: ModelSignalType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignal:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignal(*_unwrap(None, *args))

    @property
    def index(self) -> int:
        """Gets the index of the model signal."""
        return _wrap(self._dotnet_instance.Index)

    @property
    def model_path(self) -> str:
        """Gets the symbolic path to the parameter within the model."""
        return _wrap(self._dotnet_instance.ModelPath)

    @property
    def path(self) -> str:
        """Gets the path to the model that contains the signal."""
        return _wrap(self._dotnet_instance.Path)


class ModelSignalGroup(ModelDefaultGroup):
    """Represents a sub-section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignals" crefType="Unqualified" /> section of a model. Signal groups provide organization within the model."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignalGroup:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignalGroup(*_unwrap(None, *args))

    @overload
    def get_model_signal_groups(self) -> Sequence[ModelSignalGroup]:
        ...

    def get_model_signal_groups(self, *args):
        return _wrap(self._dotnet_instance.GetModelSignalGroups(*_unwrap(None, *args)))

    @overload
    def get_signals(self) -> Sequence[ModelSignal]:
        ...

    @overload
    def get_signals(self, deep: bool) -> Sequence[ModelSignal]:
        ...

    def get_signals(self, *args):
        return _wrap(self._dotnet_instance.GetSignals(*_unwrap(None, *args)))

    @overload
    def add_model_signal_group(self, model_signal_group: ModelSignalGroup) -> bool:
        ...

    def add_model_signal_group(self, *args):
        return _wrap(self._dotnet_instance.AddModelSignalGroup(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_model_signal(self, model_signal: ModelSignal) -> bool:
        ...

    def add_model_signal(self, *args):
        return _wrap(self._dotnet_instance.AddModelSignal(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class ModelSignals(Section):
    """Represents the top-level <format type="bold">Signal</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" crefType="Unqualified" />. This section contains all the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignal" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignalGroup" crefType="Unqualified" /> objects under the model."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignals:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ModelSignals")

    @overload
    def get_signals(self) -> Sequence[ModelSignal]:
        ...

    @overload
    def get_signals(self, deep: bool) -> Sequence[ModelSignal]:
        ...

    def get_signals(self, *args):
        return _wrap(self._dotnet_instance.GetSignals(*_unwrap(None, *args)))

    @overload
    def get_model_signal_groups(self) -> Sequence[ModelSignalGroup]:
        ...

    def get_model_signal_groups(self, *args):
        return _wrap(self._dotnet_instance.GetModelSignalGroups(*_unwrap(None, *args)))

    @overload
    def add_signal(self, signal: ModelSignal) -> bool:
        ...

    def add_signal(self, *args):
        return _wrap(self._dotnet_instance.AddSignal(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_model_signal_group(self, model_signal_group: ModelSignalGroup) -> bool:
        ...

    def add_model_signal_group(self, *args):
        return _wrap(self._dotnet_instance.AddModelSignalGroup(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class ModelStatus(Channel, IChannel):
    """Represents a <format type="bold">Model Status</format> channel, which you can use to get information about the current status of the model running on the target."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelStatus:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ModelStatus")


class ModelTime(Channel, IChannel):
    """Represents a <format type="bold">Model Time</format> channel, which you can use to get information about the current running time, in seconds, of the model running on the target."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelTime:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ModelTime")


class Models(Section):
    """Represents the <format type="bold">Models</format> section under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels" crefType="Unqualified" />. This section contains any compiled or uncompiled models you add to the system definition. NI VeriStand supports importing <format type="monospace">.dll</format>, <format type="monospace">.mdl</format>, and <format type="monospace">.lvmodel</format> file types."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Models:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Models")

    @overload
    def get_models(self) -> Sequence[Model]:
        ...

    def get_models(self, *args):
        return _wrap(self._dotnet_instance.GetModels(*_unwrap(None, *args)))

    @overload
    def add_model(self, model: Model) -> bool:
        ...

    def add_model(self, *args):
        return _wrap(self._dotnet_instance.AddModel(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Multiplexer(Channel, IChannel):
    """Represents a multiplexer signal under an NI-XNET signal format CAN frame. The multiplexer signal defines an area within the frame to contain different <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DynamicSignal" crefType="Unqualified" /> signals."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Multiplexer:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Multiplexer")

    @property
    def multiplexer_value(self) -> int:
        """Gets or sets the value of a multiplexer signal, which defines the dynamic signals to transmit in a given frame."""
        return _wrap(self._dotnet_instance.MultiplexerValue)

    @multiplexer_value.setter
    def multiplexer_value(self, value: int):
        """Gets or sets the value of a multiplexer signal, which defines the dynamic signals to transmit in a given frame."""
        self._dotnet_instance.MultiplexerValue = next(_unwrap(None, value))


class Outgoing(Section):
    """Represents the <format type="bold">Outgoing</format> section under an NI-XNET CAN, LIN, or FlexRay port, which contains any outgoing frames and data replay files."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Outgoing:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Outgoing")

    @overload
    def get_event_triggered(self) -> EventTriggered:
        ...

    def get_event_triggered(self, *args):
        return _wrap(self._dotnet_instance.GetEventTriggered(*_unwrap(None, *args)))

    @overload
    def get_cyclic(self) -> Cyclic:
        ...

    def get_cyclic(self, *args):
        return _wrap(self._dotnet_instance.GetCyclic(*_unwrap(None, *args)))

    @overload
    def get_cyclic_event(self) -> CyclicEvent:
        ...

    def get_cyclic_event(self, *args):
        return _wrap(self._dotnet_instance.GetCyclicEvent(*_unwrap(None, *args)))

    @overload
    def get_data_replay(self) -> DataReplay:
        ...

    def get_data_replay(self, *args):
        return _wrap(self._dotnet_instance.GetDataReplay(*_unwrap(None, *args)))

    @overload
    def get_sporadic(self) -> Sporadic:
        ...

    def get_sporadic(self, *args):
        return _wrap(self._dotnet_instance.GetSporadic(*_unwrap(None, *args)))

    @overload
    def get_unconditional(self) -> Unconditional:
        ...

    def get_unconditional(self, *args):
        return _wrap(self._dotnet_instance.GetUnconditional(*_unwrap(None, *args)))


class Outport(Channel, IChannel):
    """Represents a model outport, or output."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Outport:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Outport")

    @property
    def initial_value(self) -> Union[System.Array[System.Double], Sequence[Sequence[float]]]:
        """Gets or sets the initial value of the model outport."""
        return _wrap(self._dotnet_instance.InitialValue)

    @initial_value.setter
    def initial_value(self, value: Union[System.Array[System.Double], Sequence[Sequence[float]]]):
        """Gets or sets the initial value of the model outport."""
        self._dotnet_instance.InitialValue = next(_unwrap(None, value))

    @property
    def index(self) -> int:
        """Gets the index number of the outport in the outport vector (array)."""
        return _wrap(self._dotnet_instance.Index)


class OutportGroup(ModelDefaultGroup):
    """Represents a sub-section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Outports" crefType="Unqualified" /> section of a model. Outport groups provide organization within the model."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.OutportGroup:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for OutportGroup")

    @overload
    def get_outport_groups(self) -> Sequence[OutportGroup]:
        ...

    def get_outport_groups(self, *args):
        return _wrap(self._dotnet_instance.GetOutportGroups(*_unwrap(None, *args)))

    @overload
    def get_outports(self) -> Sequence[Outport]:
        ...

    @overload
    def get_outports(self, deep: bool) -> Sequence[Outport]:
        ...

    def get_outports(self, *args):
        return _wrap(self._dotnet_instance.GetOutports(*_unwrap(None, *args)))


class Outports(Section):
    """Represents the top-level <format type="bold">Outports</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" crefType="Unqualified" />. This section contains all the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Outport" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.OutportGroup" crefType="Unqualified" /> objects for the model."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Outports:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Outports")

    @overload
    def get_outports(self) -> Sequence[Outport]:
        ...

    @overload
    def get_outports(self, deep: bool) -> Sequence[Outport]:
        ...

    def get_outports(self, *args):
        return _wrap(self._dotnet_instance.GetOutports(*_unwrap(None, *args)))

    @overload
    def get_outport_groups(self) -> Sequence[OutportGroup]:
        ...

    def get_outport_groups(self, *args):
        return _wrap(self._dotnet_instance.GetOutportGroups(*_unwrap(None, *args)))


class OutputUnderflowChannel(CustomDeviceChannel, IChannel):
    """Represents an output underflow count channel, which tracks the number of times the system fails to read data from an asynchronous custom device because there is no data to read. A single custom device can have only one output underflow count channel."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.OutputUnderflowChannel:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.OutputUnderflowChannel(*_unwrap(None, *args))


class PendingFrames(Channel, IChannel):
    """Represents a <format type="bold">Pending Frames</format> channel associate with an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay" crefType="Unqualified" /> file. This channel stores the number of frames in the outgoing transmission queue of the current NI-XNET streaming session. You can use this channel to determine whether data is replaying as expected."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.PendingFrames:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for PendingFrames")


class Procedure(Section):
    """Represents a procedure, which determines a set of actions that the VeriStand Engine executes. You can configure procedures to run in response to an alarm, when called from another procedure, or on startup."""

    @overload
    def __init__(self, name: str, description: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure(*_unwrap(None, *args))

    @overload
    def reorder_command_list(self, commands: Sequence[Command]) -> bool:
        ...

    def reorder_command_list(self, *args):
        return _wrap(self._dotnet_instance.ReorderCommandList(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def get_command_list(self) -> Sequence[Command]:
        ...

    def get_command_list(self, *args):
        return _wrap(self._dotnet_instance.GetCommandList(*_unwrap(None, *args)))

    @overload
    def add_command(self, command: Command) -> bool:
        ...

    def add_command(self, *args):
        return _wrap(self._dotnet_instance.AddCommand(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_alarming(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: float, lower_limit: float) -> bool:
        ...

    @overload
    def add_new_alarming(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: float, lower_limit: BaseNode) -> bool:
        ...

    @overload
    def add_new_alarming(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: BaseNode, lower_limit: float) -> bool:
        ...

    @overload
    def add_new_alarming(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: BaseNode, lower_limit: BaseNode) -> bool:
        ...

    @overload
    def add_new_alarming(self, name: str, description: str, function: AlarmingStepFunction, alarm: BaseNode) -> bool:
        ...

    def add_new_alarming(self, *args):
        return _wrap(self._dotnet_instance.AddNewAlarming(*_unwrap({(str, str, AlarmPriority, AlarmState, BaseNode, (float, int), BaseNode, BaseNode, (float, int), (float, int)): (10, NationalInstruments.VeriStand.Error.NoError), (str, str, AlarmPriority, AlarmState, BaseNode, (float, int), BaseNode, BaseNode, (float, int), BaseNode): (10, NationalInstruments.VeriStand.Error.NoError), (str, str, AlarmPriority, AlarmState, BaseNode, (float, int), BaseNode, BaseNode, BaseNode, (float, int)): (10, NationalInstruments.VeriStand.Error.NoError), (str, str, AlarmPriority, AlarmState, BaseNode, (float, int), BaseNode, BaseNode, BaseNode, BaseNode): (10, NationalInstruments.VeriStand.Error.NoError), (str, str, AlarmingStepFunction, BaseNode): (4, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_call_procedure(self, name: str, description: str, procedure: Procedure) -> bool:
        ...

    def add_new_call_procedure(self, *args):
        return _wrap(self._dotnet_instance.AddNewCallProcedure(*_unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_condition(self, name: str, description: str, variable: BaseNode, comparison: ConditionStepComparison, value: float, goto_label: Command) -> bool:
        ...

    @overload
    def add_new_condition(self, name: str, description: str, variable: BaseNode, comparison: ConditionStepComparison, value: BaseNode, goto_label: Command) -> bool:
        ...

    def add_new_condition(self, *args):
        return _wrap(self._dotnet_instance.AddNewCondition(*_unwrap({(str, str, BaseNode, ConditionStepComparison, (float, int), Command): (6, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, ConditionStepComparison, BaseNode, Command): (6, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_dwell(self, name: str, description: str, dwell_time: float) -> bool:
        ...

    @overload
    def add_new_dwell(self, name: str, description: str, dwell_time: BaseNode) -> bool:
        ...

    def add_new_dwell(self, *args):
        return _wrap(self._dotnet_instance.AddNewDwell(*_unwrap({(str, str, (float, int)): (3, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode): (3, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_end(self, name: str, description: str) -> bool:
        ...

    def add_new_end(self, *args):
        return _wrap(self._dotnet_instance.AddNewEnd(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_exit_subroutine(self, name: str, description: str) -> bool:
        ...

    def add_new_exit_subroutine(self, *args):
        return _wrap(self._dotnet_instance.AddNewExitSubroutine(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_goto_label(self, name: str, description: str, label: Command) -> bool:
        ...

    def add_new_goto_label(self, *args):
        return _wrap(self._dotnet_instance.AddNewGotoLabel(*_unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_set_multiple_variables(self, name: str, description: str, channels: Sequence[BaseNode], values: Sequence[float]) -> bool:
        ...

    def add_new_set_multiple_variables(self, *args):
        return _wrap(self._dotnet_instance.AddNewSetMultipleVariables(*_unwrap({None: (4, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_set_variable(self, name: str, description: str, variable: BaseNode, value: float) -> bool:
        ...

    @overload
    def add_new_set_variable(self, name: str, description: str, variable: BaseNode, value: BaseNode) -> bool:
        ...

    @overload
    def add_new_set_variable(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: float, value2: float) -> bool:
        ...

    @overload
    def add_new_set_variable(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: float, value2: BaseNode) -> bool:
        ...

    @overload
    def add_new_set_variable(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: BaseNode, value2: float) -> bool:
        ...

    @overload
    def add_new_set_variable(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: BaseNode, value2: BaseNode) -> bool:
        ...

    def add_new_set_variable(self, *args):
        return _wrap(self._dotnet_instance.AddNewSetVariable(*_unwrap({(str, str, BaseNode, (float, int)): (4, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, BaseNode): (4, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, SetVariableStepFunction, (float, int), (float, int)): (6, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, SetVariableStepFunction, (float, int), BaseNode): (6, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, SetVariableStepFunction, BaseNode, (float, int)): (6, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, SetVariableStepFunction, BaseNode, BaseNode): (6, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_real_time_sequence_command(self, name: str, description: str, sequence_command: GlobalSequenceCommand, wait_for_sequences_to_complete: bool, wait_timeout: float, abort_sequences_on_timeout: bool) -> RealTimeSequenceCommand:
        ...

    @overload
    def add_new_real_time_sequence_command(self, name: str, description: str, sequence_command: GlobalSequenceCommand, wait_for_sequences_to_complete: bool, wait_timeout: float, abort_sequences_on_timeout: bool, group_number: int) -> RealTimeSequenceCommand:
        ...

    def add_new_real_time_sequence_command(self, *args):
        return _wrap(self._dotnet_instance.AddNewRealTimeSequenceCommand(*_unwrap(None, *args)))


class Procedures(Section):
    """Represents the <format type="bold">Procedures</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains all the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure" crefType="Unqualified" /> objects you configure."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Procedures:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Procedures")

    @property
    def startup_procedure(self) -> Procedure:
        """Gets or sets a value indicating the procedure that runs on startup."""
        return _wrap(self._dotnet_instance.StartupProcedure)

    @startup_procedure.setter
    def startup_procedure(self, value: Procedure):
        """Gets or sets a value indicating the procedure that runs on startup."""
        self._dotnet_instance.StartupProcedure = next(_unwrap(None, value))

    @overload
    def reorder_procedure_list(self, procedures: Sequence[Procedure]) -> bool:
        ...

    def reorder_procedure_list(self, *args):
        return _wrap(self._dotnet_instance.ReorderProcedureList(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def get_procedures_list(self) -> Sequence[Procedure]:
        ...

    def get_procedures_list(self, *args):
        return _wrap(self._dotnet_instance.GetProceduresList(*_unwrap(None, *args)))

    @overload
    def add_procedure(self, procedure: Procedure) -> bool:
        ...

    def add_procedure(self, *args):
        return _wrap(self._dotnet_instance.AddProcedure(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class RawDataBasedChannel(Channel, IChannel):
    """Represents a raw data format channel under an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedChannel:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for RawDataBasedChannel")

    @property
    def default_value(self) -> float:
        """Gets or sets the default value of the channel."""
        return _wrap(self._dotnet_instance.DefaultValue)

    @default_value.setter
    def default_value(self, value: float):
        """Gets or sets the default value of the channel."""
        self._dotnet_instance.DefaultValue = next(_unwrap(None, value))

    @property
    def start_bit(self) -> int:
        """Gets or sets the start bit, or the least significant signal bit position in the frame payload. This value determines the signal starting point in the frame."""
        return _wrap(self._dotnet_instance.StartBit)

    @start_bit.setter
    def start_bit(self, value: int):
        """Gets or sets the start bit, or the least significant signal bit position in the frame payload. This value determines the signal starting point in the frame."""
        self._dotnet_instance.StartBit = next(_unwrap(None, value))

    @property
    def number_of_bits(self) -> int:
        """Gets or sets the number of bits the signal uses in the frame payload."""
        return _wrap(self._dotnet_instance.NumberOfBits)

    @number_of_bits.setter
    def number_of_bits(self, value: int):
        """Gets or sets the number of bits the signal uses in the frame payload."""
        self._dotnet_instance.NumberOfBits = next(_unwrap(None, value))

    @property
    def enable64_bit(self) -> bool:
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        return _wrap(self._dotnet_instance.Enable64Bit)

    @enable64_bit.setter
    def enable64_bit(self, value: bool):
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        self._dotnet_instance.Enable64Bit = next(_unwrap(None, value))


class RawDataBasedFrame(Section):
    """Represents a raw data format frame of an NI-XNET CAN, LIN, or FlexRay device."""

    @overload
    def __init__(self, name: str, id: int, owning_database: Database, cluster_name: str, payload_length: int, start_time_offset: float, enable64_bit: bool, signal_names: Sequence[str]):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame(*_unwrap(None, *args))

    @property
    def transmit_trigger(self) -> FrameTriggerType:
        """Gets the trigger type (channel value change, trigger channel not zero, and so on) specified for an event-triggered frame."""
        return _wrap(self._dotnet_instance.TransmitTrigger)

    @property
    def phase(self) -> FramePhaseType:
        """Gets or sets whether to reset the timer after the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        return _wrap(self._dotnet_instance.Phase)

    @phase.setter
    def phase(self, value: FramePhaseType):
        """Gets or sets whether to reset the timer after the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        self._dotnet_instance.Phase = next(_unwrap(None, value))

    @property
    def frame_type(self) -> FrameType:
        """Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port."""
        return _wrap(self._dotnet_instance.FrameType)

    @frame_type.setter
    def frame_type(self, value: FrameType):
        """Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port."""
        self._dotnet_instance.FrameType = next(_unwrap(None, value))

    @property
    def id(self) -> int:
        """Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent."""
        return _wrap(self._dotnet_instance.ID)

    @id.setter
    def id(self, value: int):
        """Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent."""
        self._dotnet_instance.ID = next(_unwrap(None, value))

    @property
    def payload_length(self) -> int:
        """Gets or sets the number of bytes in the payload of the frame."""
        return _wrap(self._dotnet_instance.PayloadLength)

    @payload_length.setter
    def payload_length(self, value: int):
        """Gets or sets the number of bytes in the payload of the frame."""
        self._dotnet_instance.PayloadLength = next(_unwrap(None, value))

    @property
    def md5(self) -> Sequence[int]:
        """Gets the MD5 message digest for the frame."""
        return _wrap(self._dotnet_instance.MD5)

    @property
    def start_time_offset(self) -> float:
        """Gets or sets the amount of time that elapses between the session start and the transmission of the first frame."""
        return _wrap(self._dotnet_instance.StartTimeOffset)

    @start_time_offset.setter
    def start_time_offset(self, value: float):
        """Gets or sets the amount of time that elapses between the session start and the transmission of the first frame."""
        self._dotnet_instance.StartTimeOffset = next(_unwrap(None, value))

    @property
    def enable64_bit(self) -> bool:
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        return _wrap(self._dotnet_instance.Enable64Bit)

    @enable64_bit.setter
    def enable64_bit(self, value: bool):
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        self._dotnet_instance.Enable64Bit = next(_unwrap(None, value))

    @property
    def owning_database(self) -> BaseNode:
        """Gets or sets a reference to the XNET database that contains the frame."""
        return _wrap(self._dotnet_instance.OwningDatabase)

    @owning_database.setter
    def owning_database(self, value: BaseNode):
        """Gets or sets a reference to the XNET database that contains the frame."""
        self._dotnet_instance.OwningDatabase = next(_unwrap(None, value))

    @property
    def cluster_name(self) -> str:
        """Gets or sets the name of the cluster in the XNET database that contains the frame."""
        return _wrap(self._dotnet_instance.ClusterName)

    @cluster_name.setter
    def cluster_name(self, value: str):
        """Gets or sets the name of the cluster in the XNET database that contains the frame."""
        self._dotnet_instance.ClusterName = next(_unwrap(None, value))

    @property
    def database_alias(self) -> str:
        """Gets or sets the alias for the XNET database that contains the frame."""
        return _wrap(self._dotnet_instance.DatabaseAlias)

    @database_alias.setter
    def database_alias(self, value: str):
        """Gets or sets the alias for the XNET database that contains the frame."""
        self._dotnet_instance.DatabaseAlias = next(_unwrap(None, value))

    @property
    def disabled(self) -> bool:
        """Gets whether transmission of the outgoing frame is disabled."""
        return _wrap(self._dotnet_instance.Disabled)

    @property
    def enable_software_cyclic_trigger(self) -> bool:
        """Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame."""
        return _wrap(self._dotnet_instance.EnableSoftwareCyclicTrigger)

    @enable_software_cyclic_trigger.setter
    def enable_software_cyclic_trigger(self, value: bool):
        """Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame."""
        self._dotnet_instance.EnableSoftwareCyclicTrigger = next(_unwrap(None, value))

    @property
    def enable_frame_cyclic_trigger(self) -> bool:
        """Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame."""
        return _wrap(self._dotnet_instance.EnableFrameCyclicTrigger)

    @enable_frame_cyclic_trigger.setter
    def enable_frame_cyclic_trigger(self, value: bool):
        """Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame."""
        self._dotnet_instance.EnableFrameCyclicTrigger = next(_unwrap(None, value))

    @property
    def disable_channel(self) -> BaseNode:
        """Gets a reference to the disable channel for the frame. A disable channel disables transmission of an outgoing frame when the value of the disable channel is non-zero."""
        return _wrap(self._dotnet_instance.DisableChannel)

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets a reference to the channel that is checked for a non-zero value when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableFrameCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        return _wrap(self._dotnet_instance.TriggerChannel)

    @property
    def transmit_time(self) -> float:
        """Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        return _wrap(self._dotnet_instance.TransmitTime)

    @transmit_time.setter
    def transmit_time(self, value: float):
        """Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        self._dotnet_instance.TransmitTime = next(_unwrap(None, value))

    @overload
    def create_raw_data_based_channel(self, start_bit: int, number_of_bits: int) -> RawDataBasedChannel:
        ...

    def create_raw_data_based_channel(self, *args):
        return _wrap(self._dotnet_instance.CreateRawDataBasedChannel(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_frame_information(self, create_time_information_channels: bool, create_frame_id: bool) -> FrameInformation:
        ...

    def create_frame_information(self, *args):
        return _wrap(self._dotnet_instance.CreateFrameInformation(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_frame_faulting(self, create_skip_cyclic_frames: bool, create_transmit_time: bool) -> FrameFaulting:
        ...

    def create_frame_faulting(self, *args):
        return _wrap(self._dotnet_instance.CreateFrameFaulting(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def create_automatic_frame_processing(self) -> AutomaticFrameProcessing:
        ...

    def create_automatic_frame_processing(self, *args):
        return _wrap(self._dotnet_instance.CreateAutomaticFrameProcessing(*_unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def disable_transmission_trigger(self):
        ...

    def disable_transmission_trigger(self, *args):
        return _wrap(self._dotnet_instance.DisableTransmissionTrigger(*_unwrap(None, *args)))

    @overload
    def enable_transmission_trigger(self, disable_channel: BaseNode):
        ...

    def enable_transmission_trigger(self, *args):
        return _wrap(self._dotnet_instance.EnableTransmissionTrigger(*_unwrap(None, *args)))

    @overload
    def set_transmit_trigger(self, trigger_type: FrameTriggerType, trigger_channel: BaseNode):
        ...

    def set_transmit_trigger(self, *args):
        return _wrap(self._dotnet_instance.SetTransmitTrigger(*_unwrap(None, *args)))

    @overload
    def get_raw_data_based_channel_list(self) -> Sequence[RawDataBasedChannel]:
        ...

    def get_raw_data_based_channel_list(self, *args):
        return _wrap(self._dotnet_instance.GetRawDataBasedChannelList(*_unwrap(None, *args)))

    @overload
    def get_frame_information(self) -> FrameInformation:
        ...

    def get_frame_information(self, *args):
        return _wrap(self._dotnet_instance.GetFrameInformation(*_unwrap(None, *args)))

    @overload
    def get_frame_faulting(self) -> FrameFaulting:
        ...

    def get_frame_faulting(self, *args):
        return _wrap(self._dotnet_instance.GetFrameFaulting(*_unwrap(None, *args)))

    @overload
    def get_automatic_frame_processing(self) -> AutomaticFrameProcessing:
        ...

    def get_automatic_frame_processing(self, *args):
        return _wrap(self._dotnet_instance.GetAutomaticFrameProcessing(*_unwrap(None, *args)))


class RawFrameDataLogging(Section):
    """Represents the <format type="bold">Raw Frame Data Logging</format> section under an NI-XNET CAN, LIN, or FlexRay port."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.RawFrameDataLogging:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for RawFrameDataLogging")

    @overload
    def get_data_logging_file_list(self) -> Sequence[DataLoggingFile]:
        ...

    def get_data_logging_file_list(self, *args):
        return _wrap(self._dotnet_instance.GetDataLoggingFileList(*_unwrap(None, *args)))

    @overload
    def add_data_logging_file(self, data_logging_file: DataLoggingFile) -> bool:
        ...

    def add_data_logging_file(self, *args):
        return _wrap(self._dotnet_instance.AddDataLoggingFile(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class RealTimeSequenceCommand(Command):
    """A procedure command for commanding real-time sequences."""

    @overload
    def __init__(self, name: str, sequence_command: GlobalSequenceCommand, wait_for_sequences_to_complete: bool, wait_timeout: float, abort_sequences_on_timeout: bool):
        ...

    @overload
    def __init__(self, name: str, sequence_command: GlobalSequenceCommand, wait_for_sequences_to_complete: bool, wait_timeout: float, abort_sequences_on_timeout: bool, group_number: int):
        ...

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.RealTimeSequenceCommand:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.RealTimeSequenceCommand(*_unwrap(None, *args))

    @property
    def sequence_command(self) -> GlobalSequenceCommand:
        """Gets or sets a value indicating the global command to apply to all running real-time sequences."""
        return _wrap(self._dotnet_instance.SequenceCommand)

    @sequence_command.setter
    def sequence_command(self, value: GlobalSequenceCommand):
        """Gets or sets a value indicating the global command to apply to all running real-time sequences."""
        self._dotnet_instance.SequenceCommand = next(_unwrap(None, value))

    @property
    def wait_for_sequences_to_complete(self) -> bool:
        """Gets or sets a value indicating whether to wait for all active sequences to complete execution."""
        return _wrap(self._dotnet_instance.WaitForSequencesToComplete)

    @wait_for_sequences_to_complete.setter
    def wait_for_sequences_to_complete(self, value: bool):
        """Gets or sets a value indicating whether to wait for all active sequences to complete execution."""
        self._dotnet_instance.WaitForSequencesToComplete = next(_unwrap(None, value))

    @property
    def abort_sequences_on_timeout(self) -> bool:
        """Gets or sets a value indicating whether to abort all active sequences if the sequence command times out waiting for them to complete."""
        return _wrap(self._dotnet_instance.AbortSequencesOnTimeout)

    @abort_sequences_on_timeout.setter
    def abort_sequences_on_timeout(self, value: bool):
        """Gets or sets a value indicating whether to abort all active sequences if the sequence command times out waiting for them to complete."""
        self._dotnet_instance.AbortSequencesOnTimeout = next(_unwrap(None, value))

    @property
    def wait_timeout(self) -> float:
        """Gets or sets a value indicating the maximum amount of time in seconds to wait for all active sequences to complete execution."""
        return _wrap(self._dotnet_instance.WaitTimeout)

    @wait_timeout.setter
    def wait_timeout(self, value: float):
        """Gets or sets a value indicating the maximum amount of time in seconds to wait for all active sequences to complete execution."""
        self._dotnet_instance.WaitTimeout = next(_unwrap(None, value))

    @property
    def group_number(self) -> int:
        """Gets or sets a value indicating the group number for the sequence to stop."""
        return _wrap(self._dotnet_instance.GroupNumber)

    @group_number.setter
    def group_number(self, value: int):
        """Gets or sets a value indicating the group number for the sequence to stop."""
        self._dotnet_instance.GroupNumber = next(_unwrap(None, value))


class ReceiveTime(Channel, IChannel):
    """Represents the <format type="bold">Receive Time</format> channel for an incoming NI-XNET CAN, LIN, or FlexRay frame. This channel contains the most recent timestamp at which the frame was received."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReceiveTime:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ReceiveTime")

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of the <format type="bold">Receive Time</format> channel."""
        return _wrap(self._dotnet_instance.InitialValue)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the <format type="bold">Receive Time</format> channel."""
        self._dotnet_instance.InitialValue = next(_unwrap(None, value))

    @overload
    def remove_node(self) -> bool:
        ...

    def remove_node(self, *args):
        return _wrap(self._dotnet_instance.RemoveNode(*_unwrap(None, *args)))


class ReflectiveMemory(Section):
    """Represents a reflective memory device under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataSharing" crefType="Unqualified" /> section of the system definition. A reflective memory device is a target on a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemory:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemory(*_unwrap(None, *args))

    @property
    def visa_resource(self) -> str:
        """Gets or sets the VISA resource name for the device as it appears in Measurement <entity value="amp" /> Automation Explorer (MAX)."""
        return _wrap(self._dotnet_instance.VISAResource)

    @visa_resource.setter
    def visa_resource(self, value: str):
        """Gets or sets the VISA resource name for the device as it appears in Measurement <entity value="amp" /> Automation Explorer (MAX)."""
        self._dotnet_instance.VISAResource = next(_unwrap(None, value))

    @property
    def generate_interrupt(self) -> bool:
        """Gets whether interrupts are enabled for the reflective memory device."""
        return _wrap(self._dotnet_instance.GenerateInterrupt)

    @property
    def interrupt_all_nodes(self) -> bool:
        """Gets whether the device sends interrupt signals to all nodes on the reflective memory network."""
        return _wrap(self._dotnet_instance.InterruptAllNodes)

    @property
    def interrupt_target_node(self) -> int:
        """Gets the decimal ID of the target node to which the reflective memory device sends interrupts."""
        return _wrap(self._dotnet_instance.InterruptTargetNode)

    @property
    def interrupt_type(self) -> int:
        """Gets the type of interrupt the reflective memory device generates."""
        return _wrap(self._dotnet_instance.InterruptType)

    @property
    def interrupt_data_constant(self) -> bool:
        """Gets whether the data included in the interrupt packet is a constant value."""
        return _wrap(self._dotnet_instance.InterruptDataConstant)

    @property
    def interrupt_constant_data(self) -> int:
        """Gets the constant value that is the data included in the interrupt packet."""
        return _wrap(self._dotnet_instance.InterruptConstantData)

    @property
    def interrupt_channel_data(self) -> BaseNode:
        """Gets the channel that provides the data included in the interrupt packet."""
        return _wrap(self._dotnet_instance.InterruptChannelData)

    @overload
    def disable_interrupt(self):
        ...

    def disable_interrupt(self, *args):
        return _wrap(self._dotnet_instance.DisableInterrupt(*_unwrap(None, *args)))

    @overload
    def enable_interrupt(self, type: ReflectiveMemoryInterruptType, interrupt_constant_value: int):
        ...

    @overload
    def enable_interrupt(self, type: ReflectiveMemoryInterruptType, interrupt_channel: BaseNode):
        ...

    @overload
    def enable_interrupt(self, interrupt_target_node: int, type: ReflectiveMemoryInterruptType, interrupt_constant_value: int):
        ...

    @overload
    def enable_interrupt(self, interrupt_target_node: int, type: ReflectiveMemoryInterruptType, interrupt_channel: BaseNode):
        ...

    def enable_interrupt(self, *args):
        return _wrap(self._dotnet_instance.EnableInterrupt(*_unwrap(None, *args)))

    @overload
    def get_information_channels(self) -> ReflectiveMemoryInformationChannels:
        ...

    def get_information_channels(self, *args):
        return _wrap(self._dotnet_instance.GetInformationChannels(*_unwrap(None, *args)))

    @overload
    def get_data_channels(self) -> ReflectiveMemoryDataChannels:
        ...

    def get_data_channels(self, *args):
        return _wrap(self._dotnet_instance.GetDataChannels(*_unwrap(None, *args)))


class ReflectiveMemoryDataChannel(Channel, IChannel):
    """Represents a data channel under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemory" crefType="Unqualified" /> device."""

    @overload
    def __init__(self, name: str, description: str, memory_address: int, data_type: ReflectiveMemoryDataChannelDataType, initial_value: float, type: ReflectiveMemoryDataChannelAccessType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannel:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannel(*_unwrap(None, *args))

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of a reflective memory data channel."""
        return _wrap(self._dotnet_instance.InitialValue)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of a reflective memory data channel."""
        self._dotnet_instance.InitialValue = next(_unwrap(None, value))

    @property
    def type(self) -> ReflectiveMemoryDataChannelAccessType:
        """Gets or sets the access type (<format type="monospace">Read</format> or <format type="monospace">Write</format>) of a reflective memory data channel."""
        return _wrap(self._dotnet_instance.Type)

    @type.setter
    def type(self, value: ReflectiveMemoryDataChannelAccessType):
        """Gets or sets the access type (<format type="monospace">Read</format> or <format type="monospace">Write</format>) of a reflective memory data channel."""
        self._dotnet_instance.Type = next(_unwrap(None, value))

    @property
    def data_type(self) -> ReflectiveMemoryDataChannelDataType:
        """Gets or sets the data type of a reflective memory data channel."""
        return _wrap(self._dotnet_instance.DataType)

    @data_type.setter
    def data_type(self, value: ReflectiveMemoryDataChannelDataType):
        """Gets or sets the data type of a reflective memory data channel."""
        self._dotnet_instance.DataType = next(_unwrap(None, value))

    @property
    def memory_address(self) -> int:
        """Gets or sets the address for the data channel in reflective memory."""
        return _wrap(self._dotnet_instance.MemoryAddress)

    @memory_address.setter
    def memory_address(self, value: int):
        """Gets or sets the address for the data channel in reflective memory."""
        self._dotnet_instance.MemoryAddress = next(_unwrap(None, value))


class ReflectiveMemoryDataChannels(Section):
    """Represents the top-level <format type="bold">Data Channels</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemory" crefType="Unqualified" /> device. This section contains all the data channels for the device, as well as sub-folders that you can use to organize the channels."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannels:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ReflectiveMemoryDataChannels")

    @overload
    def get_data_channels(self) -> Sequence[ReflectiveMemoryDataChannel]:
        ...

    def get_data_channels(self, *args):
        return _wrap(self._dotnet_instance.GetDataChannels(*_unwrap(None, *args)))

    @overload
    def get_folders(self) -> Sequence[ReflectiveMemoryFolder]:
        ...

    def get_folders(self, *args):
        return _wrap(self._dotnet_instance.GetFolders(*_unwrap(None, *args)))

    @overload
    def add_data_channel(self, reflective_memory_data_channel: ReflectiveMemoryDataChannel) -> bool:
        ...

    def add_data_channel(self, *args):
        return _wrap(self._dotnet_instance.AddDataChannel(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_folder(self, reflective_memory_folder: ReflectiveMemoryFolder) -> bool:
        ...

    def add_folder(self, *args):
        return _wrap(self._dotnet_instance.AddFolder(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class ReflectiveMemoryFolder(Section):
    """Represents a folder under a reflective memory device. Folders can contain data channels or additional sub-folders."""

    @overload
    def __init__(self, name: str, description: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryFolder:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryFolder(*_unwrap(None, *args))

    @overload
    def get_data_channels(self) -> Sequence[ReflectiveMemoryDataChannel]:
        ...

    def get_data_channels(self, *args):
        return _wrap(self._dotnet_instance.GetDataChannels(*_unwrap(None, *args)))

    @overload
    def get_folders(self) -> Sequence[ReflectiveMemoryFolder]:
        ...

    def get_folders(self, *args):
        return _wrap(self._dotnet_instance.GetFolders(*_unwrap(None, *args)))

    @overload
    def add_data_channel(self, reflective_memory_data_channel: ReflectiveMemoryDataChannel) -> bool:
        ...

    def add_data_channel(self, *args):
        return _wrap(self._dotnet_instance.AddDataChannel(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_folder(self, reflective_memory_folder: ReflectiveMemoryFolder) -> bool:
        ...

    def add_folder(self, *args):
        return _wrap(self._dotnet_instance.AddFolder(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class ReflectiveMemoryInformationChannels(Section):
    """Represents the <format type="bold">Information Channels</format> section under a reflective memory device."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInformationChannels:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ReflectiveMemoryInformationChannels")

    @overload
    def get_ring_read_late_count(self) -> ReflectiveMemoryRingReadLateCount:
        ...

    def get_ring_read_late_count(self, *args):
        return _wrap(self._dotnet_instance.GetRingReadLateCount(*_unwrap(None, *args)))

    @overload
    def get_write_late_count(self) -> ReflectiveMemoryWriteLateCount:
        ...

    def get_write_late_count(self, *args):
        return _wrap(self._dotnet_instance.GetWriteLateCount(*_unwrap(None, *args)))


class ReflectiveMemoryNetwork(Section):
    """Represents the reflective memory network that <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemory" crefType="Unqualified" /> devices use to share data. A single system definition can have only one reflective memory network."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ReflectiveMemoryNetwork")

    @property
    def start_memory_address(self) -> int:
        """Gets or sets the start address in reflective memory that NI VeriStand can use. Use this property together with <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.MaximumEndMemoryAddress" crefType="Unqualified" /> to specify the maximum amount of reflected memory allocated to NI VeriStand."""
        return _wrap(self._dotnet_instance.StartMemoryAddress)

    @start_memory_address.setter
    def start_memory_address(self, value: int):
        """Gets or sets the start address in reflective memory that NI VeriStand can use. Use this property together with <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.MaximumEndMemoryAddress" crefType="Unqualified" /> to specify the maximum amount of reflected memory allocated to NI VeriStand."""
        self._dotnet_instance.StartMemoryAddress = next(_unwrap(None, value))

    @property
    def maximum_end_memory_address(self) -> int:
        """Gets or sets the maximum end address in reflective memory that NI VeriStand can use. Use this property together with <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.StartMemoryAddress" crefType="Unqualified" /> to specify the maximum amount of reflected memory allocated to NI VeriStand."""
        return _wrap(self._dotnet_instance.MaximumEndMemoryAddress)

    @maximum_end_memory_address.setter
    def maximum_end_memory_address(self, value: int):
        """Gets or sets the maximum end address in reflective memory that NI VeriStand can use. Use this property together with <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.StartMemoryAddress" crefType="Unqualified" /> to specify the maximum amount of reflected memory allocated to NI VeriStand."""
        self._dotnet_instance.MaximumEndMemoryAddress = next(_unwrap(None, value))

    @property
    def export_memory_table(self) -> bool:
        """Gets or sets whether the memory table that NI VeriStand creates at compile time is exported to a text file."""
        return _wrap(self._dotnet_instance.ExportMemoryTable)

    @export_memory_table.setter
    def export_memory_table(self, value: bool):
        """Gets or sets whether the memory table that NI VeriStand creates at compile time is exported to a text file."""
        self._dotnet_instance.ExportMemoryTable = next(_unwrap(None, value))

    @property
    def export_memory_table_file(self) -> Sequence[int]:
        """Gets or sets the file path for the text file to export the memory table to at compile time if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.ExportMemoryTable" crefType="Unqualified" /> is <see langword="true" />."""
        return _wrap(self._dotnet_instance.ExportMemoryTableFile)

    @export_memory_table_file.setter
    def export_memory_table_file(self, value: Sequence[int]):
        """Gets or sets the file path for the text file to export the memory table to at compile time if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.ExportMemoryTable" crefType="Unqualified" /> is <see langword="true" />."""
        self._dotnet_instance.ExportMemoryTableFile = next(_unwrap(None, value))


class ReflectiveMemoryRingReadLateCount(Channel, IChannel):
    """Represents a <format type="bold">Ring Read Late Count</format> channel of a reflective memory device. This channel increments any time the device is not able to read a section of data from reflective memory because the section was still getting written to by another device. If this channel increments, the section of invalid data was not copied to the local channels."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryRingReadLateCount:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ReflectiveMemoryRingReadLateCount")


class ReflectiveMemoryWriteLateCount(Channel, IChannel):
    """Represents a <format type="bold">Node Write Late Count</format> channel of a reflective memory device. This channel increments any time the device is not able to write data to the reflective memory network because a new iteration of the Primary Control Loop started before the write operation was complete. In this situation, the PCL does not write or read any data for the iteration where the write operation failed to complete."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryWriteLateCount:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ReflectiveMemoryWriteLateCount")


class SCXIChassis(Section):
    """Represents an SCXI chassis under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SCXIChassis")

    @overload
    def get_scxi_modules(self) -> Sequence[SCXIModule]:
        ...

    def get_scxi_modules(self, *args):
        return _wrap(self._dotnet_instance.GetSCXIModules(*_unwrap(None, *args)))

    @overload
    def add_scxi_module(self, scxi_module: SCXIModule) -> bool:
        ...

    def add_scxi_module(self, *args):
        return _wrap(self._dotnet_instance.AddSCXIModule(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class SCXIModule(Section):
    """Represents an SCXI module under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str, type_guid: str, num_internal_channels: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIModule:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIModule(*_unwrap(None, *args))

    @property
    def scxi_module_type(self) -> str:
        """Gets the type of the SCXI module."""
        return _wrap(self._dotnet_instance.SCXIModuleType)

    @overload
    def get_analog_inputs(self) -> Sequence[DAQAnalogInput]:
        ...

    def get_analog_inputs(self, *args):
        return _wrap(self._dotnet_instance.GetAnalogInputs(*_unwrap(None, *args)))

    @overload
    def get_analog_outputs(self) -> Sequence[DAQAnalogOutput]:
        ...

    def get_analog_outputs(self, *args):
        return _wrap(self._dotnet_instance.GetAnalogOutputs(*_unwrap(None, *args)))

    @overload
    def get_dio_ports(self) -> Sequence[DAQDIOPort]:
        ...

    def get_dio_ports(self, *args):
        return _wrap(self._dotnet_instance.GetDIOPorts(*_unwrap(None, *args)))


class SLSC(Section):
    """Represents the <format type="bold">SLSC</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Hardware" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SLSC:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SLSC")

    @overload
    def get_slsc_chassis_list(self) -> Sequence[SLSCChassis]:
        ...

    def get_slsc_chassis_list(self, *args):
        return _wrap(self._dotnet_instance.GetSLSCChassisList(*_unwrap(None, *args)))

    @overload
    def export_configuration(self, filepath: str):
        ...

    def export_configuration(self, *args):
        return _wrap(self._dotnet_instance.ExportConfiguration(*_unwrap(None, *args)))

    @overload
    def import_configurations(self, filepath: str):
        ...

    def import_configurations(self, *args):
        return _wrap(self._dotnet_instance.ImportConfigurations(*_unwrap(None, *args)))

    @overload
    def add_slsc_chassis(self, slsc_chassis: SLSCChassis):
        ...

    def add_slsc_chassis(self, *args):
        return _wrap(self._dotnet_instance.AddSLSCChassis(*_unwrap(None, *args)))


class SLSCChassis(Section):
    """Represents the <format type="bold">SLSCChassis</format> section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SLSC" />."""

    @overload
    def __init__(self, name: str, chassis_type: SLSCChassis.SLSCChassisType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis(*_unwrap(None, *args))

    @property
    def chassis_id(self) -> str:
        """Gets or sets the name or the IP address of the SLSCChassis."""
        return _wrap(self._dotnet_instance.ChassisID)

    @chassis_id.setter
    def chassis_id(self, value: str):
        """Gets or sets the name or the IP address of the SLSCChassis."""
        self._dotnet_instance.ChassisID = next(_unwrap(None, value))

    @property
    def username(self) -> str:
        """Gets or sets the username for the SLSCChassis."""
        return _wrap(self._dotnet_instance.Username)

    @username.setter
    def username(self, value: str):
        """Gets or sets the username for the SLSCChassis."""
        self._dotnet_instance.Username = next(_unwrap(None, value))

    @property
    def password(self) -> str:
        """Gets or sets the password for the SLSCChassis."""
        return _wrap(self._dotnet_instance.Password)

    @password.setter
    def password(self, value: str):
        """Gets or sets the password for the SLSCChassis."""
        self._dotnet_instance.Password = next(_unwrap(None, value))

    @property
    def chassis_type(self) -> str:
        """Gets the type of the SLSCChassis."""
        return _wrap(self._dotnet_instance.ChassisType)

    @property
    def chassis_id_type(self) -> SLSCChassis.SLSCChassisIDType:
        """Gets or sets the mode how the cahssis is defined"""
        return _wrap(self._dotnet_instance.ChassisIDType)

    @chassis_id_type.setter
    def chassis_id_type(self, value: SLSCChassis.SLSCChassisIDType):
        """Gets or sets the mode how the cahssis is defined"""
        self._dotnet_instance.ChassisIDType = next(_unwrap(None, value))

    @overload
    def export_configuration(self, filepath: str):
        ...

    def export_configuration(self, *args):
        return _wrap(self._dotnet_instance.ExportConfiguration(*_unwrap(None, *args)))

    @overload
    def get_chassis_channels_section(self) -> SLSCChassisChannels:
        ...

    def get_chassis_channels_section(self, *args):
        return _wrap(self._dotnet_instance.GetChassisChannelsSection(*_unwrap(None, *args)))

    @overload
    def get_modules_section(self) -> SLSCModules:
        ...

    def get_modules_section(self, *args):
        return _wrap(self._dotnet_instance.GetModulesSection(*_unwrap(None, *args)))


    class SLSCChassisIDType(_DotNetEnum):
        """Represents an enum which contains the possibilityes used for connecting the SLSC Chassis."""

        def __init__(self, *args):
            """Create a new instance."""
            args_len = len(args)
            if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis.SLSCChassisIDType:
                self._dotnet_instance = args[0]
                self._py_field_name = args[1] if args_len == 2 else ""
            else:
                raise ValueError("No instance constructor for SLSCChassisIDType")

        @_staticproperty
        def CHASSIS_NAME() -> SLSCChassis.SLSCChassisIDType:
            return SLSCChassis.SLSCChassisIDType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis.SLSCChassisIDType, "ChassisName"), "CHASSIS_NAME")

        @_staticproperty
        def HOSTNAME_IP_ADDRESS() -> SLSCChassis.SLSCChassisIDType:
            return SLSCChassis.SLSCChassisIDType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis.SLSCChassisIDType, "HostnameIPAddress"), "HOSTNAME_IP_ADDRESS")


    class SLSCChassisType(_DotNetEnum):
        """Represents an enum which contains the predefined <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis" /> types (no need to read the chassis data from XML)."""

        def __init__(self, *args):
            """Create a new instance."""
            args_len = len(args)
            if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis.SLSCChassisType:
                self._dotnet_instance = args[0]
                self._py_field_name = args[1] if args_len == 2 else ""
            else:
                raise ValueError("No instance constructor for SLSCChassisType")

        @_staticproperty
        def E12001_CHASSIS_TYPE() -> SLSCChassis.SLSCChassisType:
            return SLSCChassis.SLSCChassisType(getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis.SLSCChassisType, "e12001_CHASSIS_TYPE"), "E12001_CHASSIS_TYPE")


class SLSCChassisChannel(Channel, IChannel):
    """Represents the <format type="bold">SLSC chassis channel</format> node of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassisChannelSection" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassisChannel:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SLSCChassisChannel")


class SLSCChassisChannelSection(Section):
    """Represents the <format type="bold">SLSC chassis channel category</format> section of an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassisChannelSection:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SLSCChassisChannelSection")

    @overload
    def get_slsc_chassis_channel_list(self) -> Sequence[SLSCChassisChannel]:
        ...

    def get_slsc_chassis_channel_list(self, *args):
        return _wrap(self._dotnet_instance.GetSLSCChassisChannelList(*_unwrap(None, *args)))


class SLSCChassisChannels(Section):
    """Represents the <format type="bold">SLSCChassisChannels</format> section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassisChannels:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SLSCChassisChannels")

    @overload
    def get_chassis_channel_sections(self) -> Sequence[SLSCChassisChannelSection]:
        ...

    def get_chassis_channel_sections(self, *args):
        return _wrap(self._dotnet_instance.GetChassisChannelSections(*_unwrap(None, *args)))


class SLSCModuleCustomDevice(CustomDevice):
    """Represents an SLSC module custom device."""

    @overload
    def __init__(self, name: str, guid: str, slot_number: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCModuleCustomDevice:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCModuleCustomDevice(*_unwrap(None, *args))

    @property
    def slot_number(self) -> int:
        """The slot number of the SLSC chassis with which the custom device is associated."""
        return _wrap(self._dotnet_instance.SlotNumber)

    @overload
    def remove_node(self) -> bool:
        ...

    def remove_node(self, *args):
        return _wrap(self._dotnet_instance.RemoveNode(*_unwrap(None, *args)))


class SLSCModules(Section):
    """Represents the <format type="bold">SLSCModules</format> section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCModules:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SLSCModules")

    @overload
    def get_module(self, slot_number: int) -> SLSCModuleCustomDevice:
        ...

    def get_module(self, *args):
        return _wrap(self._dotnet_instance.GetModule(*_unwrap(None, *args)))

    @overload
    def set_module(self, slot_number: int, custom_device: SLSCModuleCustomDevice) -> bool:
        ...

    def set_module(self, *args):
        return _wrap(self._dotnet_instance.SetModule(*_unwrap(None, *args)))


class Scale(Section):
    """Defines a base class for different types of scales allowed in system definition files. You can create scales to convert from the pre-scaled units measured by a hardware channel to the scaled units associated with a transducer or actuator."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Scale:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Scale")

    @property
    def scale_type(self) -> ScaleType:
        """Gets the scale type."""
        return _wrap(self._dotnet_instance.ScaleType)

    @property
    def scale_unit(self) -> str:
        """Gets or sets the scale unit. This can be any arbitrary string."""
        return _wrap(self._dotnet_instance.ScaleUnit)

    @scale_unit.setter
    def scale_unit(self, value: str):
        """Gets or sets the scale unit. This can be any arbitrary string."""
        self._dotnet_instance.ScaleUnit = next(_unwrap(None, value))


class ScaleFolder(Section):
    """Represents a folder under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Scales" /> section of the system definition. Folders simply organize scales into logical groups."""

    @overload
    def __init__(self, name: str, description: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ScaleFolder:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ScaleFolder(*_unwrap(None, *args))

    @overload
    def get_scale_list(self) -> Sequence[Scale]:
        ...

    @overload
    def get_scale_list(self, deep: bool) -> Sequence[Scale]:
        ...

    def get_scale_list(self, *args):
        return _wrap(self._dotnet_instance.GetScaleList(*_unwrap(None, *args)))

    @overload
    def get_scale_folder_list(self) -> Sequence[ScaleFolder]:
        ...

    @overload
    def get_scale_folder_list(self, deep: bool) -> Sequence[ScaleFolder]:
        ...

    def get_scale_folder_list(self, *args):
        return _wrap(self._dotnet_instance.GetScaleFolderList(*_unwrap(None, *args)))

    @overload
    def create_scale(self, name: str, type: ScaleType) -> Scale:
        ...

    def create_scale(self, *args):
        return _wrap(self._dotnet_instance.CreateScale(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_scale(self, scale: Scale) -> bool:
        ...

    def add_scale(self, *args):
        return _wrap(self._dotnet_instance.AddScale(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_scale_folder(self, folder: ScaleFolder) -> bool:
        ...

    def add_scale_folder(self, *args):
        return _wrap(self._dotnet_instance.AddScaleFolder(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_scale_folder(self, name: str, description: str) -> bool:
        ...

    def add_new_scale_folder(self, *args):
        return _wrap(self._dotnet_instance.AddNewScaleFolder(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class Scales(Section):
    """Represents the <format type="bold">Scales</format> section of the system definition, which contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Scale" /> objects. Use scales to convert from the pre-scaled units measured by a hardware channel to the scaled units associated with a transducer or actuator."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Scales:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Scales")

    @overload
    def get_scale_list(self) -> Sequence[Scale]:
        ...

    @overload
    def get_scale_list(self, deep: bool) -> Sequence[Scale]:
        ...

    def get_scale_list(self, *args):
        return _wrap(self._dotnet_instance.GetScaleList(*_unwrap(None, *args)))

    @overload
    def get_scale_folder_list(self) -> Sequence[ScaleFolder]:
        ...

    @overload
    def get_scale_folder_list(self, deep: bool) -> Sequence[ScaleFolder]:
        ...

    def get_scale_folder_list(self, *args):
        return _wrap(self._dotnet_instance.GetScaleFolderList(*_unwrap(None, *args)))

    @overload
    def create_scale(self, name: str, type: ScaleType) -> Scale:
        ...

    def create_scale(self, *args):
        return _wrap(self._dotnet_instance.CreateScale(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_scale(self, scale: Scale) -> bool:
        ...

    def add_scale(self, *args):
        return _wrap(self._dotnet_instance.AddScale(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_scale_folder(self, folder: ScaleFolder) -> bool:
        ...

    def add_scale_folder(self, *args):
        return _wrap(self._dotnet_instance.AddScaleFolder(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def add_new_scale_folder(self, name: str, description: str) -> bool:
        ...

    def add_new_scale_folder(self, *args):
        return _wrap(self._dotnet_instance.AddNewScaleFolder(*_unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)))


class SetMultipleVariables(Command):
    """Represents a <format type="bold">Set Multiple Variables</format> step that you can add to a procedure. This step sets the values of multiple channels to constant values."""

    @overload
    def __init__(self, name: str, description: str, channels: Sequence[BaseNode], values: Sequence[float]):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SetMultipleVariables:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SetMultipleVariables(*_unwrap(None, *args))

    @property
    def channels(self) -> Sequence[BaseNode]:
        """Gets or sets the channels to set to the specified values."""
        return _wrap(self._dotnet_instance.Channels)

    @property
    def values(self) -> Sequence[float]:
        """Gets the values to which this step sets the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetMultipleVariables.Channels" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.Values)

    @overload
    def set_channels_and_values(self, channels: Sequence[BaseNode], values: Sequence[float]):
        ...

    def set_channels_and_values(self, *args):
        return _wrap(self._dotnet_instance.SetChannelsAndValues(*_unwrap(None, *args)))


class SetVariable(Command):
    """Represents a <format type="bold">Set Variable</format> step that you can add to a procedure.  This step sets a channel, <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Variable" crefType="Unqualified" />, to a certain value. The value can be a constant or the result of a calculation using a <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> you specify."""

    @overload
    def __init__(self, name: str, description: str, variable: BaseNode, value: float):
        ...

    @overload
    def __init__(self, name: str, description: str, variable: BaseNode, value: BaseNode):
        ...

    @overload
    def __init__(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: float, value2: float):
        ...

    @overload
    def __init__(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: float, value2: BaseNode):
        ...

    @overload
    def __init__(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: BaseNode, value2: float):
        ...

    @overload
    def __init__(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: BaseNode, value2: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable(*_unwrap(None, *args))

    @property
    def function(self) -> SetVariableStepFunction:
        """Gets or sets the function (add, subtract, multiply, or divide) to use on the two values that determine the value to set on the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Variable" crefType="Unqualified" /> channel."""
        return _wrap(self._dotnet_instance.Function)

    @function.setter
    def function(self, value: SetVariableStepFunction):
        """Gets or sets the function (add, subtract, multiply, or divide) to use on the two values that determine the value to set on the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Variable" crefType="Unqualified" /> channel."""
        self._dotnet_instance.Function = next(_unwrap(None, value))

    @property
    def value1_constant(self) -> float:
        """Gets the constant value of <format type="italics">Value1</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation."""
        return _wrap(self._dotnet_instance.Value1Constant)

    @property
    def value2_constant(self) -> float:
        """Gets the constant value of <format type="italics">Value2</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation."""
        return _wrap(self._dotnet_instance.Value2Constant)

    @property
    def value1_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">Value1</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation is specified by a constant or a channel."""
        return _wrap(self._dotnet_instance.Value1IsConstant)

    @property
    def value2_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">Value2</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation is specified by a constant or a channel."""
        return _wrap(self._dotnet_instance.Value2IsConstant)

    @property
    def variable(self) -> BaseNode:
        """Gets or sets the channel in the system whose value the <format type="bold">Set Variable</format> step sets."""
        return _wrap(self._dotnet_instance.Variable)

    @variable.setter
    def variable(self, value: BaseNode):
        """Gets or sets the channel in the system whose value the <format type="bold">Set Variable</format> step sets."""
        self._dotnet_instance.Variable = next(_unwrap(None, value))

    @property
    def value1_channel(self) -> BaseNode:
        """Gets the channel that determines the value of <format type="italics">Value1</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation."""
        return _wrap(self._dotnet_instance.Value1Channel)

    @property
    def value2_channel(self) -> BaseNode:
        """Gets the channel that determines the value of <format type="italics">Value2</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation."""
        return _wrap(self._dotnet_instance.Value2Channel)

    @overload
    def set_value1(self, value1: float) -> bool:
        ...

    @overload
    def set_value1(self, value1: BaseNode) -> bool:
        ...

    def set_value1(self, *args):
        return _wrap(self._dotnet_instance.SetValue1(*_unwrap(None, *args)))

    @overload
    def set_value2(self, value2: float) -> bool:
        ...

    @overload
    def set_value2(self, value2: BaseNode) -> bool:
        ...

    def set_value2(self, *args):
        return _wrap(self._dotnet_instance.SetValue2(*_unwrap(None, *args)))


class SignalBasedSignal(Channel, IChannel):
    """Represents a signal format signal under an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedSignal:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SignalBasedSignal")

    @property
    def md5(self) -> Sequence[int]:
        """Gets the MD5 message-digest for the signal."""
        return _wrap(self._dotnet_instance.MD5)


class SkipCyclicFrames(Channel, IChannel):
    """Represents the <format type="bold">Skip Cyclic Frames</format> channel under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FrameFaulting" crefType="Unqualified" /> section of an outgoing cyclic frame of an NI-XNET CAN port. This channel specifies to skip transmission of a specified number of cyclic frames across the CAN bus when a specified trigger channel has a non-zero value."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SkipCyclicFrames:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SkipCyclicFrames")

    @property
    def skip_n_cycles(self) -> float:
        """Gets or sets the number cycles for which to skip transmission of the frame across the bus. For each skipped cycle, a frame value is dequeued and the skip count is decremented. When the skip count decrements to zero, subsequent cyclic transmissions resume."""
        return _wrap(self._dotnet_instance.SkipNCycles)

    @skip_n_cycles.setter
    def skip_n_cycles(self, value: float):
        """Gets or sets the number cycles for which to skip transmission of the frame across the bus. For each skipped cycle, a frame value is dequeued and the skip count is decremented. When the skip count decrements to zero, subsequent cyclic transmissions resume."""
        self._dotnet_instance.SkipNCycles = next(_unwrap(None, value))

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets or sets the trigger channel to watch for a non-zero value. Skipping frame transmission begins when this channel value becomes non-zero and stops when the skip count specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SkipCyclicFrames.SkipNCycles" crefType="Unqualified" /> decrements to zero."""
        return _wrap(self._dotnet_instance.TriggerChannel)

    @trigger_channel.setter
    def trigger_channel(self, value: BaseNode):
        """Gets or sets the trigger channel to watch for a non-zero value. Skipping frame transmission begins when this channel value becomes non-zero and stops when the skip count specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SkipCyclicFrames.SkipNCycles" crefType="Unqualified" /> decrements to zero."""
        self._dotnet_instance.TriggerChannel = next(_unwrap(None, value))


class SleepMode(Channel, IChannel):
    """Represents a <format type="bold">Transceiver State</format>, or Sleep Mode, channel under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANInterfaceChannels" crefType="Unqualified" /> section of an NI-XNET CAN port. This channel controls the sleep mode option on the CAN port. A port in sleep mode does not transmit data until you release sleep mode or until the port receives an incoming frame."""

    @overload
    def __init__(self, trigger_node: str):
        ...

    @overload
    def __init__(self, name: str, trigger_node: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SleepMode:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SleepMode(*_unwrap(None, *args))

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets or sets the channel that triggers sleep mode on an NI-XNET CAN port. If the value of this channel is non-zero, sleep mode is enabled. If the value is zero, sleep mode is disabled."""
        return _wrap(self._dotnet_instance.TriggerChannel)

    @trigger_channel.setter
    def trigger_channel(self, value: BaseNode):
        """Gets or sets the channel that triggers sleep mode on an NI-XNET CAN port. If the value of this channel is non-zero, sleep mode is enabled. If the value is zero, sleep mode is disabled."""
        self._dotnet_instance.TriggerChannel = next(_unwrap(None, value))


class StimulusChannel(Channel, IChannel):
    """Represents a stimulus channel of  a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Generator" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.StimulusChannel:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for StimulusChannel")

    @property
    def units(self) -> str:
        """Gets the units associated with the stimulus channel."""
        return _wrap(self._dotnet_instance.Units)


class SystemChannel(Channel, IChannel):
    """Represents a system channel under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SystemChannels" crefType="Unqualified" /> section. System channels monitor the state and condition of various aspects of the system."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SystemChannel:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SystemChannel")

    @property
    def units(self) -> str:
        """Gets the units associated with the channel."""
        return _wrap(self._dotnet_instance.Units)


class ThermocoupleScale(Scale):
    """Represents a thermocouple <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Scale" />, which converts raw values from a thermocouple to Kelvins or degrees Celsius, Fahrenheit, or Rankine."""

    @overload
    def __init__(self, name: str):
        ...

    @overload
    def __init__(self, name: str, thermocouple_type: ThermocoupleType, thermocouple_cjc_type: ThermocoupleCJCType, temperature_unit: TemperatureUnit, thermocouple_cjc_source: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleScale:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleScale(*_unwrap(None, *args))

    @property
    def thermocouple_type(self) -> ThermocoupleType:
        """Gets or sets the type of thermocouple in use."""
        return _wrap(self._dotnet_instance.ThermocoupleType)

    @thermocouple_type.setter
    def thermocouple_type(self, value: ThermocoupleType):
        """Gets or sets the type of thermocouple in use."""
        self._dotnet_instance.ThermocoupleType = next(_unwrap(None, value))

    @property
    def thermocouple_cjc_type(self) -> ThermocoupleCJCType:
        """Gets or sets the type of device the thermocouple uses to perform cold-junction compensation."""
        return _wrap(self._dotnet_instance.ThermocoupleCJCType)

    @thermocouple_cjc_type.setter
    def thermocouple_cjc_type(self, value: ThermocoupleCJCType):
        """Gets or sets the type of device the thermocouple uses to perform cold-junction compensation."""
        self._dotnet_instance.ThermocoupleCJCType = next(_unwrap(None, value))

    @property
    def temperature_unit(self) -> TemperatureUnit:
        """Gets or sets the units of the scaled temperature values: Kelvins or degrees Celsius, Fahrenheit, or Rankine."""
        return _wrap(self._dotnet_instance.TemperatureUnit)

    @temperature_unit.setter
    def temperature_unit(self, value: TemperatureUnit):
        """Gets or sets the units of the scaled temperature values: Kelvins or degrees Celsius, Fahrenheit, or Rankine."""
        self._dotnet_instance.TemperatureUnit = next(_unwrap(None, value))

    @property
    def thermocouple_cjc_source(self) -> BaseNode:
        """Gets or sets the channel that serves as the source of cold-junction compensation for the ThermocoupleScale."""
        return _wrap(self._dotnet_instance.ThermocoupleCJCSource)

    @thermocouple_cjc_source.setter
    def thermocouple_cjc_source(self, value: BaseNode):
        """Gets or sets the channel that serves as the source of cold-junction compensation for the ThermocoupleScale."""
        self._dotnet_instance.ThermocoupleCJCSource = next(_unwrap(None, value))


class TimeDifference(Channel, IChannel):
    """Represents the <format type="bold">Time Difference</format> channel for an incoming NI-XNET CAN, LIN, or FlexRay frame. This channel stores the difference between the two most recent <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReceiveTime" crefType="Unqualified" /> timestamps."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TimeDifference:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for TimeDifference")

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of the <format type="bold">Time Difference</format> channel. This property only represents an initial value for the channel, and does not actually enhance or delay frame transmission."""
        return _wrap(self._dotnet_instance.InitialValue)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the <format type="bold">Time Difference</format> channel. This property only represents an initial value for the channel, and does not actually enhance or delay frame transmission."""
        self._dotnet_instance.InitialValue = next(_unwrap(None, value))


class TimeStepDuration(Channel, IChannel):
    """Represents a <format type="bold">Time Step Duration</format> channel, which you can use to get information about the duration, in microseconds, of the last time step of the model running on the target."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TimeStepDuration:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for TimeStepDuration")


class TimingAndSyncDevice(CustomDevice):
    """Represents a timing and sync device, which is a custom device that can drive the RTSI 0 line and synchronize all the hardware I/O devices in the system."""

    @overload
    def __init__(self, name: str, guid: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TimingAndSyncDevice:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.TimingAndSyncDevice(*_unwrap(None, *args))

    @property
    def is_rtsi0_capable(self) -> bool:
        """Gets or sets whether the timing and sync device is capable of driving the RTSI 0 line, which is a digital line that sends a clock signal that synchronizes all hardware I/O devices in the system."""
        return _wrap(self._dotnet_instance.IsRTSI0Capable)

    @is_rtsi0_capable.setter
    def is_rtsi0_capable(self, value: bool):
        """Gets or sets whether the timing and sync device is capable of driving the RTSI 0 line, which is a digital line that sends a clock signal that synchronizes all hardware I/O devices in the system."""
        self._dotnet_instance.IsRTSI0Capable = next(_unwrap(None, value))


class TransmitTime(Channel, IChannel):
    """Represents a <format type="bold">Transmit Time</format> under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FrameFaulting" crefType="Unqualified" /> section of an outgoing cyclic frame of an NI-XNET CAN port. This channel specifies the amount of time that must elapse between subsequent transmissions of the cyclic frame."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.TransmitTime:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for TransmitTime")

    @property
    def transmit_time_value(self) -> float:
        """Gets or sets the constant value to use as the transmit time, in seconds."""
        return _wrap(self._dotnet_instance.TransmitTimeValue)

    @transmit_time_value.setter
    def transmit_time_value(self, value: float):
        """Gets or sets the constant value to use as the transmit time, in seconds."""
        self._dotnet_instance.TransmitTimeValue = next(_unwrap(None, value))

    @property
    def use_trigger_channel(self) -> bool:
        """Gets whether the <format type="bold">Transmit Time</format>  channel is using a trigger channel to get the transmit time value."""
        return _wrap(self._dotnet_instance.UseTriggerChannel)

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets a reference to the trigger channel the <format type="bold">Transmit Time</format> channel is using to get its value."""
        return _wrap(self._dotnet_instance.TriggerChannel)

    @overload
    def remove_trigger_channel(self):
        ...

    def remove_trigger_channel(self, *args):
        return _wrap(self._dotnet_instance.RemoveTriggerChannel(*_unwrap(None, *args)))

    @overload
    def set_trigger_channel(self, trigger_channel: BaseNode):
        ...

    def set_trigger_channel(self, *args):
        return _wrap(self._dotnet_instance.SetTriggerChannel(*_unwrap(None, *args)))


class UserChannel(Channel, IChannel):
    """Represents a user channel, which stores a single value. You can use user channels as variables in procedures, stimulus profiles, and so on."""

    @overload
    def __init__(self, name: str, description: str, units: str, default_value: float):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.UserChannel:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.UserChannel(*_unwrap(None, *args))

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of the user channel."""
        return _wrap(self._dotnet_instance.InitialValue)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the user channel."""
        self._dotnet_instance.InitialValue = next(_unwrap(None, value))


class AlarmStatus(Channel, IChannel):
    """A channel that indicates the current status of an alarm"""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmStatus:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for AlarmStatus")


class Alarming(Command):
    """Represents an <format type="bold">Alarm Command</format>, or Alarming, step that you can add to a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure" crefType="Unqualified" />. This step performs the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming.Function" crefType="Unqualified" /> on the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming.Alarm" crefType="Unqualified" /> when the step executes."""

    @overload
    def __init__(self, name: str, description: str, priority_number: int, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_source: BaseNode, upper_limit: ValueSource, lower_limit: ValueSource):
        ...

    @overload
    def __init__(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: float, lower_limit: float):
        ...

    @overload
    def __init__(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: float, lower_limit: BaseNode):
        ...

    @overload
    def __init__(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: BaseNode, lower_limit: float):
        ...

    @overload
    def __init__(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: BaseNode, lower_limit: BaseNode):
        ...

    @overload
    def __init__(self, name: str, description: str, function: AlarmingStepFunction, alarm: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming(*_unwrap(None, *args))

    @property
    def function(self) -> AlarmingStepFunction:
        """Gets or sets the function that the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming" crefType="Unqualified" /> step performs on the alarm."""
        return _wrap(self._dotnet_instance.Function)

    @function.setter
    def function(self, value: AlarmingStepFunction):
        """Gets or sets the function that the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming" crefType="Unqualified" /> step performs on the alarm."""
        self._dotnet_instance.Function = next(_unwrap(None, value))

    @property
    def priority_number(self) -> int:
        """Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31."""
        return _wrap(self._dotnet_instance.PriorityNumber)

    @priority_number.setter
    def priority_number(self, value: int):
        """Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31."""
        self._dotnet_instance.PriorityNumber = next(_unwrap(None, value))

    @property
    def priority(self) -> AlarmPriority:
        """This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>"""
        return _wrap(self._dotnet_instance.Priority)

    @priority.setter
    def priority(self, value: AlarmPriority):
        """This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>"""
        self._dotnet_instance.Priority = next(_unwrap(None, value))

    @property
    def default_state(self) -> AlarmState:
        """Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm."""
        return _wrap(self._dotnet_instance.DefaultState)

    @default_state.setter
    def default_state(self, value: AlarmState):
        """Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm."""
        self._dotnet_instance.DefaultState = next(_unwrap(None, value))

    @property
    def delay(self) -> float:
        """Gets or sets the amount of time to wait before triggering the alarm."""
        return _wrap(self._dotnet_instance.Delay)

    @delay.setter
    def delay(self, value: float):
        """Gets or sets the amount of time to wait before triggering the alarm."""
        self._dotnet_instance.Delay = next(_unwrap(None, value))

    @property
    def upper_limit_constant(self) -> float:
        """Gets the constant that determines the high limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered."""
        return _wrap(self._dotnet_instance.UpperLimitConstant)

    @property
    def lower_limit_constant(self) -> float:
        """Gets the constant that determines the low limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered."""
        return _wrap(self._dotnet_instance.LowerLimitConstant)

    @property
    def upper_limit_is_constant(self) -> bool:
        """Gets information about whether the high limit value of the alarm is determined by a channel or by a constant."""
        return _wrap(self._dotnet_instance.UpperLimitIsConstant)

    @property
    def lower_limit_is_constant(self) -> bool:
        """Gets information about whether the low limit value of the alarm is determined by a channel or by a constant."""
        return _wrap(self._dotnet_instance.LowerLimitIsConstant)

    @property
    def using_tripped_alarm(self) -> bool:
        """Gets information about whether the step is using the tripped alarm."""
        return _wrap(self._dotnet_instance.UsingTrippedAlarm)

    @property
    def alarm(self) -> BaseNode:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm" crefType="Unqualified" /> on which to perform the step <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming.Function" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.Alarm)

    @alarm.setter
    def alarm(self, value: BaseNode):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm" crefType="Unqualified" /> on which to perform the step <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming.Function" crefType="Unqualified" />."""
        self._dotnet_instance.Alarm = next(_unwrap(None, value))

    @property
    def alarm_channel(self) -> BaseNode:
        """Gets or sets the channel to monitor for alarm conditions."""
        return _wrap(self._dotnet_instance.AlarmChannel)

    @alarm_channel.setter
    def alarm_channel(self, value: BaseNode):
        """Gets or sets the channel to monitor for alarm conditions."""
        self._dotnet_instance.AlarmChannel = next(_unwrap(None, value))

    @property
    def procedure(self) -> BaseNode:
        """Gets or sets the procedure to initiate when the alarm conditions are met."""
        return _wrap(self._dotnet_instance.Procedure)

    @procedure.setter
    def procedure(self, value: BaseNode):
        """Gets or sets the procedure to initiate when the alarm conditions are met."""
        self._dotnet_instance.Procedure = next(_unwrap(None, value))

    @property
    def upper_limit_channel(self) -> BaseNode:
        """Gets the channel that determines the upper limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered."""
        return _wrap(self._dotnet_instance.UpperLimitChannel)

    @property
    def lower_limit_channel(self) -> BaseNode:
        """Gets the channel that determines the lower limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered."""
        return _wrap(self._dotnet_instance.LowerLimitChannel)

    @overload
    def set_upper_limit(self, upper_limit: float):
        ...

    @overload
    def set_upper_limit(self, upper_limit: BaseNode):
        ...

    @overload
    def set_upper_limit(self, upper_limit: ValueSource):
        ...

    def set_upper_limit(self, *args):
        return _wrap(self._dotnet_instance.SetUpperLimit(*_unwrap(None, *args)))

    @overload
    def set_lower_limit(self, lower_limit: float):
        ...

    @overload
    def set_lower_limit(self, lower_limit: BaseNode):
        ...

    @overload
    def set_lower_limit(self, lower_limit: ValueSource):
        ...

    def set_lower_limit(self, *args):
        return _wrap(self._dotnet_instance.SetLowerLimit(*_unwrap(None, *args)))

    @overload
    def use_tripped_alarm(self):
        ...

    def use_tripped_alarm(self, *args):
        return _wrap(self._dotnet_instance.UseTrippedAlarm(*_unwrap(None, *args)))


class CalculatedChannel(Channel, IChannel):
    """Represents a calculated channel, which produces new values based on calculations performed on other channels in the system definition."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for CalculatedChannel")

    @_staticproperty
    def formula() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Formula)

    @_staticproperty
    def maximum() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Maximum)

    @_staticproperty
    def minimum() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Minimum)

    @_staticproperty
    def lowpass_filter() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.LowpassFilter)

    @_staticproperty
    def peak_and_valley() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.PeakAndValley)

    @_staticproperty
    def acceleration() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Acceleration)

    @_staticproperty
    def average() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Average)

    @_staticproperty
    def conditional() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Conditional)

    @property
    def calculated_channel_type(self) -> int:
        """Gets the type of the calculated channel."""
        return _wrap(self._dotnet_instance.CalculatedChannelType)

    @overload
    def downcast(self) -> CalculatedChannel:
        ...

    def downcast(self, *args):
        return _wrap(self._dotnet_instance.Downcast(*_unwrap(None, *args)))


class CallProcedure(Command):
    """Represents a <format type="bold">Call Procedure</format> step that you can add to a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure" crefType="Unqualified" />. The <format type="bold">Call Procedure</format> step calls a procedure when the step executes."""

    @overload
    def __init__(self, name: str, description: str, procedure: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.CallProcedure:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CallProcedure(*_unwrap(None, *args))

    @property
    def procedure(self) -> BaseNode:
        """Gets or sets the procedure to call when this step executes."""
        return _wrap(self._dotnet_instance.Procedure)

    @procedure.setter
    def procedure(self, value: BaseNode):
        """Gets or sets the procedure to call when this step executes."""
        self._dotnet_instance.Procedure = next(_unwrap(None, value))


class Conditional(CalculatedChannel, IChannel):
    """Represents a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel" crefType="Unqualified" /> with the conditional function. The conditional function uses an if/else statement to check the channel you specify for the condition you specify and return the appropriate value."""

    @overload
    def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: float, w_value: float, z_value: float):
        ...

    @overload
    def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: float, w_value: float, z_value: BaseNode):
        ...

    @overload
    def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: float, w_value: BaseNode, z_value: float):
        ...

    @overload
    def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: float, w_value: BaseNode, z_value: BaseNode):
        ...

    @overload
    def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: BaseNode, w_value: float, z_value: float):
        ...

    @overload
    def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: BaseNode, w_value: float, z_value: BaseNode):
        ...

    @overload
    def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: BaseNode, w_value: BaseNode, z_value: float):
        ...

    @overload
    def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: BaseNode, w_value: BaseNode, z_value: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional(*_unwrap(None, *args))

    @_staticproperty
    def greater() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.Greater)

    @_staticproperty
    def less() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.Less)

    @_staticproperty
    def equal() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.Equal)

    @_staticproperty
    def not_equal() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.NotEqual)

    @_staticproperty
    def greater_or_equal() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.GreaterOrEqual)

    @_staticproperty
    def less_or_equal() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.LessOrEqual)

    @_staticproperty
    def and_() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.AND)

    @_staticproperty
    def or_() -> int:
        return _wrap(NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.OR)

    @property
    def y_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">Y</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        return _wrap(self._dotnet_instance.YConstantValue)

    @property
    def w_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">W</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        return _wrap(self._dotnet_instance.WConstantValue)

    @property
    def z_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">Z</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        return _wrap(self._dotnet_instance.ZConstantValue)

    @property
    def y_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">Y</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        return _wrap(self._dotnet_instance.YChannelValue)

    @property
    def w_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">W</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        return _wrap(self._dotnet_instance.WChannelValue)

    @property
    def z_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">Z</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        return _wrap(self._dotnet_instance.ZChannelValue)

    @property
    def comparison_mode(self) -> int:
        """Gets or sets the type of comparison to use for the condition."""
        return _wrap(self._dotnet_instance.ComparisonMode)

    @comparison_mode.setter
    def comparison_mode(self, value: int):
        """Gets or sets the type of comparison to use for the condition."""
        self._dotnet_instance.ComparisonMode = next(_unwrap(None, value))

    @property
    def x_channel(self) -> BaseNode:
        """Gets or sets the channel to check for the comparison condition. This channel is the value of <format type="italics">X</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        return _wrap(self._dotnet_instance.XChannel)

    @x_channel.setter
    def x_channel(self, value: BaseNode):
        """Gets or sets the channel to check for the comparison condition. This channel is the value of <format type="italics">X</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        self._dotnet_instance.XChannel = next(_unwrap(None, value))

    @overload
    def set_y_value(self, y_value: float):
        ...

    @overload
    def set_y_value(self, y_value: BaseNode):
        ...

    def set_y_value(self, *args):
        return _wrap(self._dotnet_instance.SetYValue(*_unwrap(None, *args)))

    @overload
    def set_w_value(self, w_value: float):
        ...

    @overload
    def set_w_value(self, w_value: BaseNode):
        ...

    def set_w_value(self, *args):
        return _wrap(self._dotnet_instance.SetWValue(*_unwrap(None, *args)))

    @overload
    def set_z_value(self, z_value: float):
        ...

    @overload
    def set_z_value(self, z_value: BaseNode):
        ...

    def set_z_value(self, *args):
        return _wrap(self._dotnet_instance.SetZValue(*_unwrap(None, *args)))


class DAQAnalogInput(DAQChannel, IChannel):
    """Represents a DAQ analog input channel."""

    @overload
    def __init__(self, name: str, channel: int, plugin_guid: str):
        ...

    @overload
    def __init__(self, name: str, channel: int, plugin_guid: str, initial_value: float):
        ...

    @overload
    def __init__(self, name: str, channel: int, measurement_type: DAQMeasurementType):
        ...

    @overload
    def __init__(self, name: str, channel: int, measurement_type: DAQMeasurementType, initial_value: float):
        ...

    @overload
    def __init__(self, name: str, units: str, initial_value: float, low_level: float, high_level: float, channel: int, channel_type: DAQAnalogChannelType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogInput:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogInput(*_unwrap(None, *args))

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of the analog input channel."""
        return _wrap(self._dotnet_instance.InitialValue)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the analog input channel."""
        self._dotnet_instance.InitialValue = next(_unwrap(None, value))

    @property
    def channel_type(self) -> DAQAnalogChannelType:
        """Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>)."""
        return _wrap(self._dotnet_instance.ChannelType)

    @channel_type.setter
    def channel_type(self, value: DAQAnalogChannelType):
        """Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>)."""
        self._dotnet_instance.ChannelType = next(_unwrap(None, value))

    @property
    def channel(self) -> int:
        """Gets or sets the channel number."""
        return _wrap(self._dotnet_instance.Channel)

    @channel.setter
    def channel(self, value: int):
        """Gets or sets the channel number."""
        self._dotnet_instance.Channel = next(_unwrap(None, value))

    @property
    def low_level(self) -> float:
        """Gets or sets the minimum value of the channel."""
        return _wrap(self._dotnet_instance.LowLevel)

    @low_level.setter
    def low_level(self, value: float):
        """Gets or sets the minimum value of the channel."""
        self._dotnet_instance.LowLevel = next(_unwrap(None, value))

    @property
    def high_level(self) -> float:
        """Gets or sets the maximum value of the channel."""
        return _wrap(self._dotnet_instance.HighLevel)

    @high_level.setter
    def high_level(self, value: float):
        """Gets or sets the maximum value of the channel."""
        self._dotnet_instance.HighLevel = next(_unwrap(None, value))

    @property
    def is_scxi(self) -> bool:
        """Gets whether the channel belongs to an SCXI module."""
        return _wrap(self._dotnet_instance.IsSCXI)

    @property
    def scxi_module_type(self) -> str:
        """Gets the specific type of SCXI module to which the channel belongs."""
        return _wrap(self._dotnet_instance.SCXIModuleType)


class DAQAnalogOutput(DAQChannel, IChannel):
    """Represents a DAQ analog output channel."""

    @overload
    def __init__(self, name: str, channel: int, plugin_guid: str):
        ...

    @overload
    def __init__(self, name: str, channel: int, plugin_guid: str, initial_value: float):
        ...

    @overload
    def __init__(self, name: str, channel: int, measurement_type: DAQMeasurementType):
        ...

    @overload
    def __init__(self, name: str, channel: int, measurement_type: DAQMeasurementType, initial_value: float):
        ...

    @overload
    def __init__(self, name: str, units: str, initial_value: float, low_level: float, high_level: float, channel: int, channel_type: DAQAnalogChannelType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogOutput:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogOutput(*_unwrap(None, *args))

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of the analog output channel."""
        return _wrap(self._dotnet_instance.InitialValue)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the analog output channel."""
        self._dotnet_instance.InitialValue = next(_unwrap(None, value))

    @property
    def channel_type(self) -> DAQAnalogChannelType:
        """Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>)."""
        return _wrap(self._dotnet_instance.ChannelType)

    @channel_type.setter
    def channel_type(self, value: DAQAnalogChannelType):
        """Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>)."""
        self._dotnet_instance.ChannelType = next(_unwrap(None, value))

    @property
    def channel(self) -> int:
        """Gets or sets the channel number."""
        return _wrap(self._dotnet_instance.Channel)

    @channel.setter
    def channel(self, value: int):
        """Gets or sets the channel number."""
        self._dotnet_instance.Channel = next(_unwrap(None, value))

    @property
    def low_level(self) -> float:
        """Gets or sets the minimum value of the channel."""
        return _wrap(self._dotnet_instance.LowLevel)

    @low_level.setter
    def low_level(self, value: float):
        """Gets or sets the minimum value of the channel."""
        self._dotnet_instance.LowLevel = next(_unwrap(None, value))

    @property
    def high_level(self) -> float:
        """Gets or sets the maximum value of the channel."""
        return _wrap(self._dotnet_instance.HighLevel)

    @high_level.setter
    def high_level(self, value: float):
        """Gets or sets the maximum value of the channel."""
        self._dotnet_instance.HighLevel = next(_unwrap(None, value))

    @property
    def is_scxi(self) -> bool:
        """Gets whether the channel belongs to an SCXI module."""
        return _wrap(self._dotnet_instance.IsSCXI)

    @property
    def scxi_module_type(self) -> str:
        """Gets the specific type of SCXI module to which the channel belongs."""
        return _wrap(self._dotnet_instance.SCXIModuleType)


class DAQCountUpDown(DAQCounter, IChannel):
    """Represents a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter" crefType="Unqualified" /> channel with the count up/down task type."""

    @overload
    def __init__(self, name: str, description: str, index: int, default_value: float, count_direction: DAQCounterCountMode, edge: DAQCounterEdge, reset_variable: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCountUpDown:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCountUpDown(*_unwrap(None, *args))

    @property
    def count_direction(self) -> DAQCounterCountMode:
        """Gets or sets the direction of the count (up, down, or externally controlled)."""
        return _wrap(self._dotnet_instance.CountDirection)

    @count_direction.setter
    def count_direction(self, value: DAQCounterCountMode):
        """Gets or sets the direction of the count (up, down, or externally controlled)."""
        self._dotnet_instance.CountDirection = next(_unwrap(None, value))

    @property
    def edge(self) -> DAQCounterEdge:
        """Gets or sets the edge on which to count (rising or falling)."""
        return _wrap(self._dotnet_instance.Edge)

    @edge.setter
    def edge(self, value: DAQCounterEdge):
        """Gets or sets the edge on which to count (rising or falling)."""
        self._dotnet_instance.Edge = next(_unwrap(None, value))

    @property
    def input_terminal(self) -> str:
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        return _wrap(self._dotnet_instance.InputTerminal)

    @input_terminal.setter
    def input_terminal(self, value: str):
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        self._dotnet_instance.InputTerminal = next(_unwrap(None, value))

    @property
    def reset_variable(self) -> BaseNode:
        """Gets or sets the channel whose value the counter must reach before it resets."""
        return _wrap(self._dotnet_instance.ResetVariable)

    @reset_variable.setter
    def reset_variable(self, value: BaseNode):
        """Gets or sets the channel whose value the counter must reach before it resets."""
        self._dotnet_instance.ResetVariable = next(_unwrap(None, value))


class DAQCounterInput(DAQSectionType):
    """Initializes a new instance of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterInput" /> class."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterInput:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQCounterInput")


class DAQCounterOutput(DAQSectionType):
    """Initializes a new instance of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterOutput" /> class."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterOutput:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for DAQCounterOutput")


class DAQPulseGeneration(DAQCounterOutput):
    """Represents a DAQ Counter measurement section of input channels."""

    @overload
    def __init__(self, name: str, description: str, index: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPulseGeneration:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPulseGeneration(*_unwrap(None, *args))

    @property
    def counter(self) -> str:
        """Gets the counter channel number."""
        return _wrap(self._dotnet_instance.Counter)

    @property
    def output_terminal(self) -> str:
        """Gets or sets the output terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        return _wrap(self._dotnet_instance.OutputTerminal)

    @output_terminal.setter
    def output_terminal(self, value: str):
        """Gets or sets the output terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        self._dotnet_instance.OutputTerminal = next(_unwrap(None, value))

    @overload
    def set_counter_index(self, index: int):
        ...

    def set_counter_index(self, *args):
        return _wrap(self._dotnet_instance.SetCounterIndex(*_unwrap(None, *args)))

    @overload
    def get_data_channel(self, type: DAQDataChannelType) -> Channel:
        ...

    def get_data_channel(self, *args):
        return _wrap(self._dotnet_instance.GetDataChannel(*_unwrap(None, *args)))


class DAQPulseMeasurement(DAQCounterInput):
    """Represents a DAQ Counter measurement section of input channels."""

    @overload
    def __init__(self, name: str, description: str, index: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPulseMeasurement:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPulseMeasurement(*_unwrap(None, *args))

    @property
    def counter(self) -> str:
        """Gets the counter channel number."""
        return _wrap(self._dotnet_instance.Counter)

    @property
    def input_terminal(self) -> str:
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        return _wrap(self._dotnet_instance.InputTerminal)

    @input_terminal.setter
    def input_terminal(self, value: str):
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        self._dotnet_instance.InputTerminal = next(_unwrap(None, value))

    @overload
    def set_counter_index(self, index: int):
        ...

    def set_counter_index(self, *args):
        return _wrap(self._dotnet_instance.SetCounterIndex(*_unwrap(None, *args)))

    @overload
    def get_data_channel(self, type: DAQDataChannelType) -> Channel:
        ...

    def get_data_channel(self, *args):
        return _wrap(self._dotnet_instance.GetDataChannel(*_unwrap(None, *args)))


class FPGAAICategory(FPGACategory):
    """Represents the <format type="bold">Input<entity value="raquo" />Analog</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGAAICategory:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGAAICategory")


class FPGAAOCategory(FPGACategory):
    """Represents the <format type="bold">Output<entity value="raquo" />Analog</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGAAOCategory:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGAAOCategory")


class FPGAAnalogInput(FPGAChannel, IChannel):
    """Represents an FPGA analog input channel."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGAAnalogInput:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGAAnalogInput")


class FPGAAnalogOutput(FPGAChannel, IChannel):
    """Represents an FPGA analog output channel."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.FPGAAnalogOutput:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for FPGAAnalogOutput")


class Formula(CalculatedChannel, IChannel):
    """Represents a calculated channel with the formula function. This function calculates the result of a formula you specify."""

    @overload
    def __init__(self, name: str, description: str, formula: str, variable_names: Sequence[str], variables: Sequence[BaseNode]):
        ...

    @overload
    def __init__(self, name: str, description: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Formula:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Formula(*_unwrap(None, *args))

    @property
    def formula_string(self) -> str:
        """Gets the formula for which the channel calculates the result."""
        return _wrap(self._dotnet_instance.FormulaString)

    @overload
    def set_formula(self, formula: str, variable_names: Sequence[str], variables: Sequence[BaseNode]):
        ...

    def set_formula(self, *args):
        return _wrap(self._dotnet_instance.SetFormula(*_unwrap(None, *args)))

    @overload
    def reset_formula(self):
        ...

    def reset_formula(self, *args):
        return _wrap(self._dotnet_instance.ResetFormula(*_unwrap(None, *args)))


class InportGroup(ModelDefaultGroup):
    """Represents a sub-section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Inports" crefType="Unqualified" /> section of a model. Inport groups provide organization within the model."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.InportGroup:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for InportGroup")

    @overload
    def get_inport_groups(self) -> Sequence[InportGroup]:
        ...

    def get_inport_groups(self, *args):
        return _wrap(self._dotnet_instance.GetInportGroups(*_unwrap(None, *args)))

    @overload
    def get_inports(self) -> Sequence[Inport]:
        ...

    @overload
    def get_inports(self, deep: bool) -> Sequence[Inport]:
        ...

    def get_inports(self, *args):
        return _wrap(self._dotnet_instance.GetInports(*_unwrap(None, *args)))


class LookupTable(Scale):
    """Represents a lookup table <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Scale" />, which maps an array of pre-scaled values to an array of corresponding scaled values."""

    @overload
    def __init__(self, name: str):
        ...

    @overload
    def __init__(self, name: str, lookup_table_values: Sequence[LUTValue], scale_unit: str):
        ...

    @overload
    def __init__(self, node: BaseNodeType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.LookupTable:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.LookupTable(*_unwrap(None, *args))

    @property
    def lookup_table_values(self) -> Sequence[LUTValue]:
        """Gets or sets the values of the LookupTable scale."""
        return _wrap(self._dotnet_instance.LookupTableValues)

    @lookup_table_values.setter
    def lookup_table_values(self, value: Sequence[LUTValue]):
        """Gets or sets the values of the LookupTable scale."""
        self._dotnet_instance.LookupTableValues = next(_unwrap(None, value))


class LowpassFilter(CalculatedChannel, IChannel):
    """Represents a calculated channel with the <format type="bold">Lowpass Filter</format> function. This function applies a lowpass Butterworth filter to the value of the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.LowpassFilter.ChannelToFilter" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str, description: str, channel_to_filter: Channel, low_cutoff_frequency: float, filter_order: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.LowpassFilter:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.LowpassFilter(*_unwrap(None, *args))

    @property
    def channel_to_filter(self) -> BaseNode:
        """Gets or sets the channel to which to apply the filter."""
        return _wrap(self._dotnet_instance.ChannelToFilter)

    @channel_to_filter.setter
    def channel_to_filter(self, value: BaseNode):
        """Gets or sets the channel to which to apply the filter."""
        self._dotnet_instance.ChannelToFilter = next(_unwrap(None, value))

    @property
    def filter_order(self) -> int:
        """Gets or sets the order of the filter. Increasing the value of this property causes the transition between the passband and the stopband to become steeper. However, as the filter order increases, the filter becomes more unstable."""
        return _wrap(self._dotnet_instance.FilterOrder)

    @filter_order.setter
    def filter_order(self, value: int):
        """Gets or sets the order of the filter. Increasing the value of this property causes the transition between the passband and the stopband to become steeper. However, as the filter order increases, the filter becomes more unstable."""
        self._dotnet_instance.FilterOrder = next(_unwrap(None, value))

    @property
    def low_cutoff_frequency(self) -> float:
        """Gets or sets the low cutoff frequency, in hertz."""
        return _wrap(self._dotnet_instance.LowCutoffFrequency)

    @low_cutoff_frequency.setter
    def low_cutoff_frequency(self, value: float):
        """Gets or sets the low cutoff frequency, in hertz."""
        self._dotnet_instance.LowCutoffFrequency = next(_unwrap(None, value))


class Maximum(CalculatedChannel, IChannel):
    """Represents a calculated channel with the <format type="bold">Maximum</format> function. This function compares two values (<format type="italics">x</format> and <format type="italics">y</format>) and returns the larger value."""

    @overload
    def __init__(self, name: str, description: str, x_value: float, y_value: float):
        ...

    @overload
    def __init__(self, name: str, description: str, x_value: float, y_value: BaseNode):
        ...

    @overload
    def __init__(self, name: str, description: str, x_value: BaseNode, y_value: float):
        ...

    @overload
    def __init__(self, name: str, description: str, x_value: BaseNode, y_value: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Maximum:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Maximum(*_unwrap(None, *args))

    @property
    def x_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel."""
        return _wrap(self._dotnet_instance.XIsConstant)

    @property
    def y_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel."""
        return _wrap(self._dotnet_instance.YIsConstant)

    @property
    def y_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>. regardless of whether <format type="italics">x</format> is a constant or a channel."""
        return _wrap(self._dotnet_instance.YConstantValue)

    @property
    def x_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>, regardless of whether <format type="italics">x</format> is a constant or a channel."""
        return _wrap(self._dotnet_instance.XConstantValue)

    @property
    def x_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>."""
        return _wrap(self._dotnet_instance.XChannelValue)

    @property
    def y_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>."""
        return _wrap(self._dotnet_instance.YChannelValue)

    @overload
    def set_x_value(self, x_value: float):
        ...

    @overload
    def set_x_value(self, x_value: BaseNode):
        ...

    def set_x_value(self, *args):
        return _wrap(self._dotnet_instance.SetXValue(*_unwrap(None, *args)))

    @overload
    def set_y_value(self, y_value: float):
        ...

    @overload
    def set_y_value(self, y_value: BaseNode):
        ...

    def set_y_value(self, *args):
        return _wrap(self._dotnet_instance.SetYValue(*_unwrap(None, *args)))


class Minimum(CalculatedChannel, IChannel):
    """Represents a calculated channel with the <format type="bold">Minimum</format> function. This function compares two values (<format type="italics">x</format> and <format type="italics">y</format>) and returns the smaller value."""

    @overload
    def __init__(self, name: str, description: str, x_value: float, y_value: float):
        ...

    @overload
    def __init__(self, name: str, description: str, x_value: float, y_value: BaseNode):
        ...

    @overload
    def __init__(self, name: str, description: str, x_value: BaseNode, y_value: float):
        ...

    @overload
    def __init__(self, name: str, description: str, x_value: BaseNode, y_value: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Minimum:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Minimum(*_unwrap(None, *args))

    @property
    def x_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel."""
        return _wrap(self._dotnet_instance.XIsConstant)

    @property
    def y_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel."""
        return _wrap(self._dotnet_instance.YIsConstant)

    @property
    def y_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>. regardless of whether <format type="italics">x</format> is a constant or a channel."""
        return _wrap(self._dotnet_instance.YConstantValue)

    @property
    def x_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>, regardless of whether <format type="italics">x</format> is a constant or a channel."""
        return _wrap(self._dotnet_instance.XConstantValue)

    @property
    def x_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>."""
        return _wrap(self._dotnet_instance.XChannelValue)

    @property
    def y_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>."""
        return _wrap(self._dotnet_instance.YChannelValue)

    @overload
    def set_x_value(self, x_value: float):
        ...

    @overload
    def set_x_value(self, x_value: BaseNode):
        ...

    def set_x_value(self, *args):
        return _wrap(self._dotnet_instance.SetXValue(*_unwrap(None, *args)))

    @overload
    def set_y_value(self, y_value: float):
        ...

    @overload
    def set_y_value(self, y_value: BaseNode):
        ...

    def set_y_value(self, *args):
        return _wrap(self._dotnet_instance.SetYValue(*_unwrap(None, *args)))


class PeakAndValley(CalculatedChannel, IChannel):
    """Represents a calculated channel with the <format type="bold">Peak <entity value="amp" /> Valley</format> function. This function calculates the peak, valley, and offset of a cyclical waveform on the channel you specify. The calculated channel stores the peak value, and the channels you specify when you configure the calculated channel store the valley and offset values."""

    @overload
    def __init__(self, name: str, description: str, channel_to_analyze: BaseNode, channel_for_valley: BaseNode, channel_for_offset: BaseNode, reset: int, hysteresis: float):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley(*_unwrap(None, *args))

    @property
    def channel_to_analyze(self) -> BaseNode:
        """Gets or sets the channel for which to calculate the peak, valley, and offset."""
        return _wrap(self._dotnet_instance.ChannelToAnalyze)

    @channel_to_analyze.setter
    def channel_to_analyze(self, value: BaseNode):
        """Gets or sets the channel for which to calculate the peak, valley, and offset."""
        self._dotnet_instance.ChannelToAnalyze = next(_unwrap(None, value))

    @property
    def channel_for_valley(self) -> BaseNode:
        """Gets or sets the channel on which to store the valley value."""
        return _wrap(self._dotnet_instance.ChannelForValley)

    @channel_for_valley.setter
    def channel_for_valley(self, value: BaseNode):
        """Gets or sets the channel on which to store the valley value."""
        self._dotnet_instance.ChannelForValley = next(_unwrap(None, value))

    @property
    def channel_for_offset(self) -> BaseNode:
        """Gets or sets the channel on which to store the offset value."""
        return _wrap(self._dotnet_instance.ChannelForOffset)

    @channel_for_offset.setter
    def channel_for_offset(self, value: BaseNode):
        """Gets or sets the channel on which to store the offset value."""
        self._dotnet_instance.ChannelForOffset = next(_unwrap(None, value))

    @property
    def hysteresis(self) -> float:
        """Gets or sets the amount by which the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> must exceed the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Reset" crefType="Unqualified" /> value for the calculation to reset."""
        return _wrap(self._dotnet_instance.Hysteresis)

    @hysteresis.setter
    def hysteresis(self, value: float):
        """Gets or sets the amount by which the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> must exceed the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Reset" crefType="Unqualified" /> value for the calculation to reset."""
        self._dotnet_instance.Hysteresis = next(_unwrap(None, value))

    @property
    def reset(self) -> int:
        """Gets or sets the value at which to reset the calculation. If the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> surpasses this value by more than the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Hysteresis" crefType="Unqualified" />, the calculation resets."""
        return _wrap(self._dotnet_instance.Reset)

    @reset.setter
    def reset(self, value: int):
        """Gets or sets the value at which to reset the calculation. If the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> surpasses this value by more than the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Hysteresis" crefType="Unqualified" />, the calculation resets."""
        self._dotnet_instance.Reset = next(_unwrap(None, value))


class PolynomialScale(Scale):
    """Represents a polynomial <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Scale" />, which converts values using a polynomial equation with up to ten coefficients."""

    @overload
    def __init__(self, name: str):
        ...

    @overload
    def __init__(self, name: str, polynomial_coeff: Sequence[float], reverse_polynomial_coeff: Sequence[float], scale_unit: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale(*_unwrap(None, *args))

    @property
    def polynomial_coeff(self) -> Sequence[float]:
        """Gets or sets the forward coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />."""
        return _wrap(self._dotnet_instance.PolynomialCoeff)

    @polynomial_coeff.setter
    def polynomial_coeff(self, value: Sequence[float]):
        """Gets or sets the forward coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />."""
        self._dotnet_instance.PolynomialCoeff = next(_unwrap(None, value))

    @property
    def reverse_polynomial_coeff(self) -> Sequence[float]:
        """Gets or sets the reverse coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />."""
        return _wrap(self._dotnet_instance.ReversePolynomialCoeff)

    @reverse_polynomial_coeff.setter
    def reverse_polynomial_coeff(self, value: Sequence[float]):
        """Gets or sets the reverse coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />."""
        self._dotnet_instance.ReversePolynomialCoeff = next(_unwrap(None, value))


class SCXI1100(SCXIModule):
    """Represents an SCXI-1100 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1100:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1100(*_unwrap(None, *args))


class SCXI1102(SCXIModule):
    """Represents an SCXI-1102 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1102:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1102(*_unwrap(None, *args))


class SCXI1102B(SCXIModule):
    """Represents an SCXI-1102B module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1102B:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1102B(*_unwrap(None, *args))


class SCXI1102C(SCXIModule):
    """Represents an SCXI-1102C module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1102C:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1102C(*_unwrap(None, *args))


class SCXI1104(SCXIModule):
    """Represents an SCXI-1104 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1104:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1104(*_unwrap(None, *args))


class SCXI1104C(SCXIModule):
    """Represents an SCXI-1104C module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1104C:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1104C(*_unwrap(None, *args))


class SCXI1112(SCXIModule):
    """Represents an SCXI-1112 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1112:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1112(*_unwrap(None, *args))


class SCXI1120(SCXIModule):
    """Represents an SCXI-1120 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1120:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1120(*_unwrap(None, *args))


class SCXI1120D(SCXIModule):
    """Represents an SCXI-1120D module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1120D:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1120D(*_unwrap(None, *args))


class SCXI1121(SCXIModule):
    """Represents an SCXI-1121 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1121:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1121(*_unwrap(None, *args))


class SCXI1122(SCXIModule):
    """Represents an SCXI-1122 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1122:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1122(*_unwrap(None, *args))


class SCXI1124(SCXIModule):
    """Represents an SCXI-1124 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1124:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1124(*_unwrap(None, *args))


class SCXI1125(SCXIModule):
    """Represents an SCXI-1125 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1125:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1125(*_unwrap(None, *args))


class SCXI1126(SCXIModule):
    """Represents an SCXI-1126 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1126:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1126(*_unwrap(None, *args))


class SCXI1127(SCXIModule):
    """Represents an SCXI-1127 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1127:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1127(*_unwrap(None, *args))


class SCXI1128(SCXIModule):
    """Represents an SCXI-1128 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1128:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1128(*_unwrap(None, *args))


class SCXI1140(SCXIModule):
    """Represents an SCXI-1140 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1140:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1140(*_unwrap(None, *args))


class SCXI1141(SCXIModule):
    """Represents an SCXI-1141 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1141:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1141(*_unwrap(None, *args))


class SCXI1142(SCXIModule):
    """Represents an SCXI-1142 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1142:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1142(*_unwrap(None, *args))


class SCXI1143(SCXIModule):
    """Represents an SCXI-1143 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1143:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1143(*_unwrap(None, *args))


class SCXI1160(SCXIModule):
    """Represents an SCXI-1160 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1160:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1160(*_unwrap(None, *args))


class SCXI1161(SCXIModule):
    """Represents an SCXI-1161 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1161:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1161(*_unwrap(None, *args))


class SCXI1162(SCXIModule):
    """Represents an SCXI-1162 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1162:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1162(*_unwrap(None, *args))


class SCXI1162HV(SCXIModule):
    """Represents an SCXI-1162HV module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1162HV:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1162HV(*_unwrap(None, *args))


class SCXI1163(SCXIModule):
    """Represents an SCXI-1163 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1163:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1163(*_unwrap(None, *args))


class SCXI1163R(SCXIModule):
    """Represents an SCXI-1163R module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1163R:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1163R(*_unwrap(None, *args))


class SCXI1190(SCXIModule):
    """Represents an SCXI-1190 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1190:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1190(*_unwrap(None, *args))


class SCXI1191(SCXIModule):
    """Represents an SCXI-1191 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1191:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1191(*_unwrap(None, *args))


class SCXI1192(SCXIModule):
    """Represents an SCXI-1192 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1192:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1192(*_unwrap(None, *args))


class SCXI1520(SCXIModule):
    """Represents an SCXI-1520 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1520:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1520(*_unwrap(None, *args))


class SCXI1530(SCXIModule):
    """Represents an SCXI-1530 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1530:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1530(*_unwrap(None, *args))


class SCXI1531(SCXIModule):
    """Represents an SCXI-1531 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1531:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1531(*_unwrap(None, *args))


class SCXI1540(SCXIModule):
    """Represents an SCXI-1540 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1540:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1540(*_unwrap(None, *args))


class SCXI1581(SCXIModule):
    """Represents an SCXI-1581 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />."""

    @overload
    def __init__(self, name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1581:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1581(*_unwrap(None, *args))


class Acceleration(CalculatedChannel, IChannel):
    """Represents a calculated channel with the acceleration function."""

    @overload
    def __init__(self, name: str, description: str, units: str, channel_to_analyze: BaseNode, channel_for_velocity: BaseNode):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Acceleration:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Acceleration(*_unwrap(None, *args))

    @property
    def velocity_channel(self) -> BaseNode:
        """Gets or sets the channel on which to store the velocity of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Acceleration.XChannel" crefType="Unqualified" />."""
        return _wrap(self._dotnet_instance.VelocityChannel)

    @velocity_channel.setter
    def velocity_channel(self, value: BaseNode):
        """Gets or sets the channel on which to store the velocity of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Acceleration.XChannel" crefType="Unqualified" />."""
        self._dotnet_instance.VelocityChannel = next(_unwrap(None, value))

    @property
    def x_channel(self) -> BaseNode:
        """Gets or sets the channel for which to calculate the acceleration."""
        return _wrap(self._dotnet_instance.XChannel)

    @x_channel.setter
    def x_channel(self, value: BaseNode):
        """Gets or sets the channel for which to calculate the acceleration."""
        self._dotnet_instance.XChannel = next(_unwrap(None, value))


class Average(CalculatedChannel, IChannel):
    """Represents a calculated channel with the average function. The average function calculates the average value of the channel you specify every <format type="italics">n</format> points."""

    @overload
    def __init__(self, name: str, description: str, number_of_points: int, channel_to_average: Channel):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.Average:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Average(*_unwrap(None, *args))

    @property
    def channel_to_average(self) -> BaseNode:
        """Gets or sets the channel for which to calculate the average value."""
        return _wrap(self._dotnet_instance.ChannelToAverage)

    @channel_to_average.setter
    def channel_to_average(self, value: BaseNode):
        """Gets or sets the channel for which to calculate the average value."""
        self._dotnet_instance.ChannelToAverage = next(_unwrap(None, value))

    @property
    def number_of_points(self) -> int:
        """Gets or sets the number of points of data to include in the average."""
        return _wrap(self._dotnet_instance.NumberOfPoints)

    @number_of_points.setter
    def number_of_points(self, value: int):
        """Gets or sets the number of points of data to include in the average."""
        self._dotnet_instance.NumberOfPoints = next(_unwrap(None, value))
