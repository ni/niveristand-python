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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AcquisitionMode, "Finite")
        return AcquisitionMode(dotnet_result, "FINITE")

    @_staticproperty
    def CONTINUOUS() -> AcquisitionMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AcquisitionMode, "Continuous")
        return AcquisitionMode(dotnet_result, "CONTINUOUS")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AcquisitionUnits, "Samples")
        return AcquisitionUnits(dotnet_result, "SAMPLES")

    @_staticproperty
    def SECONDS() -> AcquisitionUnits:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AcquisitionUnits, "Seconds")
        return AcquisitionUnits(dotnet_result, "SECONDS")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ActionOnNew, "NewGroup")
        return ActionOnNew(dotnet_result, "NEW_GROUP")

    @_staticproperty
    def NEW_FILE() -> ActionOnNew:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ActionOnNew, "NewFile")
        return ActionOnNew(dotnet_result, "NEW_FILE")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmMode, "Normal")
        return AlarmMode(dotnet_result, "NORMAL")

    @_staticproperty
    def INDICATE_ONLY() -> AlarmMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmMode, "IndicateOnly")
        return AlarmMode(dotnet_result, "INDICATE_ONLY")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmPriority, "Low")
        return AlarmPriority(dotnet_result, "LOW")

    @_staticproperty
    def MEDIUM() -> AlarmPriority:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmPriority, "Medium")
        return AlarmPriority(dotnet_result, "MEDIUM")

    @_staticproperty
    def HIGH() -> AlarmPriority:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmPriority, "High")
        return AlarmPriority(dotnet_result, "HIGH")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmState, "Disabled")
        return AlarmState(dotnet_result, "DISABLED")

    @_staticproperty
    def ENABLED() -> AlarmState:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmState, "Enabled")
        return AlarmState(dotnet_result, "ENABLED")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "AdjustSettings")
        return AlarmingStepFunction(dotnet_result, "ADJUST_SETTINGS")

    @_staticproperty
    def ENABLE_ALARM() -> AlarmingStepFunction:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "EnableAlarm")
        return AlarmingStepFunction(dotnet_result, "ENABLE_ALARM")

    @_staticproperty
    def DISABLE_ALARM() -> AlarmingStepFunction:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "DisableAlarm")
        return AlarmingStepFunction(dotnet_result, "DISABLE_ALARM")

    @_staticproperty
    def RESET_ALARM_EXIT_SUBROUTINE() -> AlarmingStepFunction:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "ResetAlarmExitSubroutine")
        return AlarmingStepFunction(dotnet_result, "RESET_ALARM_EXIT_SUBROUTINE")

    @_staticproperty
    def DISABLE_ALARM_EXIT_SUBROUTINE() -> AlarmingStepFunction:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "DisableAlarmExitSubroutine")
        return AlarmingStepFunction(dotnet_result, "DISABLE_ALARM_EXIT_SUBROUTINE")

    @_staticproperty
    def RESET_ALARM() -> AlarmingStepFunction:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunction, "ResetAlarm")
        return AlarmingStepFunction(dotnet_result, "RESET_ALARM")


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
        dotnet_result = self._dotnet_instance.BaseNodeType
        return _wrap(dotnet_result)

    @property
    def name(self) -> str:
        """Gets the name of this node. To rename a node, use the <see cref="M:NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode.RenameNode(System.String)" crefType="Unqualified" /> method."""
        dotnet_result = self._dotnet_instance.Name
        return _wrap(dotnet_result)

    @property
    def node_path(self) -> str:
        """Gets the path to the node within the system definition file."""
        dotnet_result = self._dotnet_instance.NodePath
        return _wrap(dotnet_result)

    @property
    def node_id(self) -> int:
        """Gets the ID of this node."""
        dotnet_result = self._dotnet_instance.NodeID
        return _wrap(dotnet_result)

    @property
    def log_file_producer(self) -> bool:
        """Gets a value indicating whether the node is a log file producer"""
        dotnet_result = self._dotnet_instance.LogFileProducer
        return _wrap(dotnet_result)

    @property
    def description(self) -> str:
        """Gets or sets the description of this node."""
        dotnet_result = self._dotnet_instance.Description
        return _wrap(dotnet_result)

    @description.setter
    def description(self, value: str):
        """Gets or sets the description of this node."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Description = next(unwrapped)

    @property
    def type_guid(self) -> str:
        """Gets the GUID associated with the node.
            Attempts to set the GUID of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode" crefType="Unqualified" /> will generate an exception."""
        dotnet_result = self._dotnet_instance.TypeGUID
        return _wrap(dotnet_result)

    @type_guid.setter
    def type_guid(self, value: str):
        """Gets the GUID associated with the node.
            Attempts to set the GUID of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode" crefType="Unqualified" /> will generate an exception."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TypeGUID = next(unwrapped)

    @overload
    def get_parent(self) -> Tuple[bool, BaseNode]:
        ...

    def get_parent(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetParent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_children(self) -> Sequence[BaseNode]:
        ...

    def get_children(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetChildren(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_children_by_guid(self, type_guid: str) -> Sequence[BaseNode]:
        ...

    def find_children_by_guid(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindChildrenByGUID(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_first_child_with_name(self, name: str, deep_hierarchy: bool) -> Tuple[bool, BaseNode]:
        ...

    def find_first_child_with_name(self, *args):
        unwrapped = _unwrap({None: (1, None)}, *args)
        dotnet_result = self._dotnet_instance.FindFirstChildWithName(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_node_by_path(self, nodepath: str) -> Tuple[bool, BaseNode]:
        ...

    def find_node_by_path(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindNodeByPath(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_document_root(self) -> Root:
        ...

    def get_document_root(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDocumentRoot(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_document_path(self) -> str:
        ...

    def get_document_path(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDocumentPath(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_node(self) -> bool:
        ...

    def remove_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def rename_node(self, new_name: str) -> bool:
        ...

    def rename_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RenameNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_node_errors(self):
        ...

    def get_node_errors(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetNodeErrors(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def equals(self, obj: Any) -> bool:
        ...

    def equals(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Equals(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_hash_code(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetHashCode(*unwrapped)
        return _wrap(dotnet_result)

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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType, "HS")
        return CANTransceiverType(dotnet_result, "HS")

    @_staticproperty
    def LS() -> CANTransceiverType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType, "LS")
        return CANTransceiverType(dotnet_result, "LS")

    @_staticproperty
    def SW() -> CANTransceiverType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType, "SW")
        return CANTransceiverType(dotnet_result, "SW")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransmitOrderType, "AsSubmitted")
        return CANTransmitOrderType(dotnet_result, "AS_SUBMITTED")

    @_staticproperty
    def BY_IDENTIFIER() -> CANTransmitOrderType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransmitOrderType, "ByIdentifier")
        return CANTransmitOrderType(dotnet_result, "BY_IDENTIFIER")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDChannel_Type, "Input")
        return CDChannel_Type(dotnet_result, "INPUT")

    @_staticproperty
    def OUTPUT() -> CDChannel_Type:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDChannel_Type, "Output")
        return CDChannel_Type(dotnet_result, "OUTPUT")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDDriverExecMode, "Asynchronous")
        return CDDriverExecMode(dotnet_result, "ASYNCHRONOUS")

    @_staticproperty
    def INLINE_HW_INTERFACE() -> CDDriverExecMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDDriverExecMode, "InlineHWInterface")
        return CDDriverExecMode(dotnet_result, "INLINE_HW_INTERFACE")

    @_staticproperty
    def INLINE_MODEL_INTERFACE() -> CDDriverExecMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDDriverExecMode, "InlineModelInterface")
        return CDDriverExecMode(dotnet_result, "INLINE_MODEL_INTERFACE")

    @_staticproperty
    def INLINE_TIMING_AND_SYNC() -> CDDriverExecMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDDriverExecMode, "InlineTimingAndSync")
        return CDDriverExecMode(dotnet_result, "INLINE_TIMING_AND_SYNC")

    @_staticproperty
    def ASYNCHRONOUS_TIMING_AND_SYNC() -> CDDriverExecMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDDriverExecMode, "AsynchronousTimingAndSync")
        return CDDriverExecMode(dotnet_result, "ASYNCHRONOUS_TIMING_AND_SYNC")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDLoopType, "WhileLoop")
        return CDLoopType(dotnet_result, "WHILE_LOOP")

    @_staticproperty
    def TIMED_LOOP() -> CDLoopType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDLoopType, "TimedLoop")
        return CDLoopType(dotnet_result, "TIMED_LOOP")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDTimeLoopPriority, "Low")
        return CDTimeLoopPriority(dotnet_result, "LOW")

    @_staticproperty
    def MEDIUM() -> CDTimeLoopPriority:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDTimeLoopPriority, "Medium")
        return CDTimeLoopPriority(dotnet_result, "MEDIUM")

    @_staticproperty
    def HIGH() -> CDTimeLoopPriority:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.CDTimeLoopPriority, "High")
        return CDTimeLoopPriority(dotnet_result, "HIGH")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ChannelNames, "PhysicalChannel")
        return ChannelNames(dotnet_result, "PHYSICAL_CHANNEL")

    @_staticproperty
    def SYSTEM_DEFINITION() -> ChannelNames:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ChannelNames, "SystemDefinition")
        return ChannelNames(dotnet_result, "SYSTEM_DEFINITION")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "Greater")
        return ConditionStepComparison(dotnet_result, "GREATER")

    @_staticproperty
    def LESS() -> ConditionStepComparison:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "Less")
        return ConditionStepComparison(dotnet_result, "LESS")

    @_staticproperty
    def EQUAL() -> ConditionStepComparison:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "Equal")
        return ConditionStepComparison(dotnet_result, "EQUAL")

    @_staticproperty
    def NOT_EQUAL() -> ConditionStepComparison:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "NotEqual")
        return ConditionStepComparison(dotnet_result, "NOT_EQUAL")

    @_staticproperty
    def GREATER_OR_EQUAL() -> ConditionStepComparison:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "GreaterOrEqual")
        return ConditionStepComparison(dotnet_result, "GREATER_OR_EQUAL")

    @_staticproperty
    def LESS_OR_EQUAL() -> ConditionStepComparison:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ConditionStepComparison, "LessOrEqual")
        return ConditionStepComparison(dotnet_result, "LESS_OR_EQUAL")


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RenameNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_boolean_property(self, name: str) -> Tuple[bool, bool]:
        ...

    def get_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_double_property(self, name: str) -> Tuple[bool, float]:
        ...

    def get_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_double_array_property(self, name: str) -> Tuple[bool, Sequence[float]]:
        ...

    def get_double_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDoubleArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string_property(self, name: str) -> Tuple[bool, str]:
        ...

    def get_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_binary_string_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_binary_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBinaryStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string_array_property(self, name: str) -> Tuple[bool, Sequence[str]]:
        ...

    def get_string_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStringArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

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
                dotnet_result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((dotnet_result, params_array[1]))

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
                dotnet_result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((dotnet_result, params_array[1]))

    @overload
    def get_dependent_file_property(self, name: str) -> Tuple[bool, DependentFile]:
        ...

    def get_dependent_file_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDependentFileProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_dictionary_property(self, name: str) -> Tuple[bool, Dictionary]:
        ...

    def get_dictionary_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDictionaryProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_dictionary_array_property(self, name: str) -> Tuple[bool, Sequence[Dictionary]]:
        ...

    def get_dictionary_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDictionaryArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_variant_property(self, name: str) -> Tuple[bool, Sequence[int], Sequence[int]]:
        ...

    def get_variant_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetVariantProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_boolean_property(self, name: str, value: bool) -> bool:
        ...

    def set_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u16_property(self, name: str, value: int) -> bool:
        ...

    def set_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u32_property(self, name: str, value: int) -> bool:
        ...

    def set_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u32_array_property(self, name: str, value: Sequence[int]) -> bool:
        ...

    def set_u32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u64_property(self, name: str, value: int) -> bool:
        ...

    def set_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i32_property(self, name: str, value: int) -> bool:
        ...

    def set_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i32_array_property(self, name: str, value: Sequence[int]) -> bool:
        ...

    def set_i32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_double_property(self, name: str, value: float) -> bool:
        ...

    def set_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_double_array_property(self, name: str, value: Sequence[float]) -> bool:
        ...

    def set_double_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDoubleArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_string_property(self, name: str, value: str) -> bool:
        ...

    def set_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_binary_string_property(self, name: str, value: Sequence[int]) -> bool:
        ...

    def set_binary_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetBinaryStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_string_array_property(self, name: str, value: Sequence[str]) -> bool:
        ...

    def set_string_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetStringArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dependent_node_property(self, name: str, value: BaseNode) -> bool:
        ...

    @overload
    def set_dependent_node_property(self, name: str, dep_node_path: str) -> bool:
        ...

    def set_dependent_node_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDependentNodeProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dependent_file_property(self, name: str, value: DependentFile) -> bool:
        ...

    def set_dependent_file_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDependentFileProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dictionary_property(self, name: str, value: Dictionary) -> bool:
        ...

    def set_dictionary_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDictionaryProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dictionary_array_property(self, name: str, value: Sequence[Dictionary]) -> bool:
        ...

    def set_dictionary_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDictionaryArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_variant_property(self, name: str, type: Sequence[int], value: Sequence[int]) -> bool:
        ...

    def set_variant_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetVariantProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_property_names(self) -> Sequence[str]:
        ...

    def get_property_names(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetPropertyNames(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_property_type(self, property_name: str) -> Tuple[bool, PropertyContent]:
        ...

    def get_property_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetPropertyType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_property(self, name: str) -> bool:
        ...

    def remove_property(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.RemoveProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def move_node_to(self, parent_type: CustomDeviceBase) -> bool:
        ...

    def move_node_to(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.MoveNodeTo(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_error(self, error_id: str):
        ...

    def remove_error(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveError(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def report_error(self, error_id: str, is_error: bool, err_code: int, message: str):
        ...

    def report_error(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReportError(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_log_file_producer_flag(self, is_log_file_producer: bool):
        ...

    def set_log_file_producer_flag(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetLogFileProducerFlag(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceSection(*unwrapped)

    @overload
    def add_custom_device_section_if_not_found(self, name: str, guid: str) -> Tuple[CustomDeviceSection, bool]:
        ...

    def add_custom_device_section_if_not_found(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddCustomDeviceSectionIfNotFound(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_custom_device_channel_if_not_found(self, name: str, guid: str) -> Tuple[CustomDeviceChannel, bool]:
        ...

    def add_custom_device_channel_if_not_found(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddCustomDeviceChannelIfNotFound(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_custom_device_waveform_if_not_found(self, name: str, guid: str, data_type: WaveformTypeDataType) -> Tuple[CustomDeviceWaveform, bool]:
        ...

    def add_custom_device_waveform_if_not_found(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddCustomDeviceWaveformIfNotFound(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_output_underflow_count_channel(self, name: str) -> CustomDeviceChannel:
        ...

    def add_output_underflow_count_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddOutputUnderflowCountChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_input_overflow_count_channel(self, name: str) -> CustomDeviceChannel:
        ...

    def add_input_overflow_count_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddInputOverflowCountChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_error_channel(self, name: str) -> CustomDeviceChannel:
        ...

    def add_error_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddErrorChannel(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceWaveform(*unwrapped)

    @property
    def units(self) -> str:
        """Gets or sets the units associated with a CustomDeviceWaveform. Units can be any string that makes sense for your custom device."""
        dotnet_result = self._dotnet_instance.Units
        return _wrap(dotnet_result)

    @units.setter
    def units(self, value: str):
        """Gets or sets the units associated with a CustomDeviceWaveform. Units can be any string that makes sense for your custom device."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Units = next(unwrapped)

    @property
    def data_type(self) -> WaveformTypeDataType:
        """Gets or sets the data type associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceWaveform" /> class."""
        dotnet_result = self._dotnet_instance.DataType
        return _wrap(dotnet_result)

    @data_type.setter
    def data_type(self, value: WaveformTypeDataType):
        """Gets or sets the data type associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceWaveform" /> class."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DataType = next(unwrapped)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogChannelType, "Voltage")
        return DAQAnalogChannelType(dotnet_result, "VOLTAGE")

    @_staticproperty
    def CURRENT() -> DAQAnalogChannelType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogChannelType, "Current")
        return DAQAnalogChannelType(dotnet_result, "CURRENT")

    @_staticproperty
    def OTHER() -> DAQAnalogChannelType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogChannelType, "Other")
        return DAQAnalogChannelType(dotnet_result, "OTHER")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Active_Edge, "Rising")
        return DAQCM_Active_Edge(dotnet_result, "RISING")

    @_staticproperty
    def FALLING() -> DAQCM_Active_Edge:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Active_Edge, "Falling")
        return DAQCM_Active_Edge(dotnet_result, "FALLING")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "Onboard10MHzClock")
        return DAQCM_Clock_Source(dotnet_result, "ONBOARD10_M_HZ_CLOCK")

    @_staticproperty
    def PFI_0() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_0")
        return DAQCM_Clock_Source(dotnet_result, "PFI_0")

    @_staticproperty
    def PFI_1() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_1")
        return DAQCM_Clock_Source(dotnet_result, "PFI_1")

    @_staticproperty
    def PFI_2() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_2")
        return DAQCM_Clock_Source(dotnet_result, "PFI_2")

    @_staticproperty
    def PFI_3() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_3")
        return DAQCM_Clock_Source(dotnet_result, "PFI_3")

    @_staticproperty
    def PFI_4() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_4")
        return DAQCM_Clock_Source(dotnet_result, "PFI_4")

    @_staticproperty
    def PFI_5() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_5")
        return DAQCM_Clock_Source(dotnet_result, "PFI_5")

    @_staticproperty
    def PFI_6() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_6")
        return DAQCM_Clock_Source(dotnet_result, "PFI_6")

    @_staticproperty
    def PFI_7() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_7")
        return DAQCM_Clock_Source(dotnet_result, "PFI_7")

    @_staticproperty
    def PFI_8() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_8")
        return DAQCM_Clock_Source(dotnet_result, "PFI_8")

    @_staticproperty
    def PFI_9() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_9")
        return DAQCM_Clock_Source(dotnet_result, "PFI_9")

    @_staticproperty
    def PFI_10() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_10")
        return DAQCM_Clock_Source(dotnet_result, "PFI_10")

    @_staticproperty
    def PFI_11() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_11")
        return DAQCM_Clock_Source(dotnet_result, "PFI_11")

    @_staticproperty
    def PFI_12() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_12")
        return DAQCM_Clock_Source(dotnet_result, "PFI_12")

    @_staticproperty
    def PFI_13() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_13")
        return DAQCM_Clock_Source(dotnet_result, "PFI_13")

    @_staticproperty
    def PFI_14() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_14")
        return DAQCM_Clock_Source(dotnet_result, "PFI_14")

    @_staticproperty
    def PFI_15() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "PFI_15")
        return DAQCM_Clock_Source(dotnet_result, "PFI_15")

    @_staticproperty
    def RTSI_PXI_TRIG_0() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_0")
        return DAQCM_Clock_Source(dotnet_result, "RTSI_PXI_TRIG_0")

    @_staticproperty
    def RTSI_PXI_TRIG_1() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_1")
        return DAQCM_Clock_Source(dotnet_result, "RTSI_PXI_TRIG_1")

    @_staticproperty
    def RTSI_PXI_TRIG_2() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_2")
        return DAQCM_Clock_Source(dotnet_result, "RTSI_PXI_TRIG_2")

    @_staticproperty
    def RTSI_PXI_TRIG_3() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_3")
        return DAQCM_Clock_Source(dotnet_result, "RTSI_PXI_TRIG_3")

    @_staticproperty
    def RTSI_PXI_TRIG_4() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_4")
        return DAQCM_Clock_Source(dotnet_result, "RTSI_PXI_TRIG_4")

    @_staticproperty
    def RTSI_PXI_TRIG_5() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_5")
        return DAQCM_Clock_Source(dotnet_result, "RTSI_PXI_TRIG_5")

    @_staticproperty
    def RTSI_PXI_TRIG_6() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_6")
        return DAQCM_Clock_Source(dotnet_result, "RTSI_PXI_TRIG_6")

    @_staticproperty
    def RTSI_PXI_TRIG_7() -> DAQCM_Clock_Source:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Clock_Source, "RTSI_PXI_TRIG_7")
        return DAQCM_Clock_Source(dotnet_result, "RTSI_PXI_TRIG_7")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "Default_RTSI_PXI_TRIG_0")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "DEFAULT_RTSI_PXI_TRIG_0")

    @_staticproperty
    def PFI_0() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_0")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_0")

    @_staticproperty
    def PFI_1() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_1")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_1")

    @_staticproperty
    def PFI_2() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_2")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_2")

    @_staticproperty
    def PFI_3() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_3")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_3")

    @_staticproperty
    def PFI_4() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_4")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_4")

    @_staticproperty
    def PFI_5() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_5")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_5")

    @_staticproperty
    def PFI_6() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_6")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_6")

    @_staticproperty
    def PFI_7() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_7")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_7")

    @_staticproperty
    def PFI_8() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_8")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_8")

    @_staticproperty
    def PFI_9() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_9")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_9")

    @_staticproperty
    def PFI_10() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_10")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_10")

    @_staticproperty
    def PFI_11() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_11")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_11")

    @_staticproperty
    def PFI_12() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_12")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_12")

    @_staticproperty
    def PFI_13() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_13")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_13")

    @_staticproperty
    def PFI_14() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_14")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_14")

    @_staticproperty
    def PFI_15() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "PFI_15")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "PFI_15")

    @_staticproperty
    def RTSI_PXI_TRIG_0() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_0")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "RTSI_PXI_TRIG_0")

    @_staticproperty
    def RTSI_PXI_TRIG_1() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_1")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "RTSI_PXI_TRIG_1")

    @_staticproperty
    def RTSI_PXI_TRIG_2() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_2")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "RTSI_PXI_TRIG_2")

    @_staticproperty
    def RTSI_PXI_TRIG_3() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_3")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "RTSI_PXI_TRIG_3")

    @_staticproperty
    def RTSI_PXI_TRIG_4() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_4")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "RTSI_PXI_TRIG_4")

    @_staticproperty
    def RTSI_PXI_TRIG_5() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_5")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "RTSI_PXI_TRIG_5")

    @_staticproperty
    def RTSI_PXI_TRIG_6() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_6")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "RTSI_PXI_TRIG_6")

    @_staticproperty
    def RTSI_PXI_TRIG_7() -> DAQCM_Export_Clk_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Clk_On_Line, "RTSI_PXI_TRIG_7")
        return DAQCM_Export_Clk_On_Line(dotnet_result, "RTSI_PXI_TRIG_7")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Sample_Clock, "aiSampleClock")
        return DAQCM_Export_Sample_Clock(dotnet_result, "AI_SAMPLE_CLOCK")

    @_staticproperty
    def AO_SAMPLE_CLOCK() -> DAQCM_Export_Sample_Clock:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Sample_Clock, "aoSampleClock")
        return DAQCM_Export_Sample_Clock(dotnet_result, "AO_SAMPLE_CLOCK")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "None")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "NONE")

    @_staticproperty
    def PFI_0() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_0")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_0")

    @_staticproperty
    def PFI_1() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_1")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_1")

    @_staticproperty
    def PFI_2() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_2")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_2")

    @_staticproperty
    def PFI_3() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_3")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_3")

    @_staticproperty
    def PFI_4() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_4")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_4")

    @_staticproperty
    def PFI_5() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_5")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_5")

    @_staticproperty
    def PFI_6() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_6")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_6")

    @_staticproperty
    def PFI_7() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_7")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_7")

    @_staticproperty
    def PFI_8() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_8")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_8")

    @_staticproperty
    def PFI_9() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_9")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_9")

    @_staticproperty
    def PFI_10() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_10")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_10")

    @_staticproperty
    def PFI_11() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_11")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_11")

    @_staticproperty
    def PFI_12() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_12")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_12")

    @_staticproperty
    def PFI_13() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_13")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_13")

    @_staticproperty
    def PFI_14() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_14")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_14")

    @_staticproperty
    def PFI_15() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "PFI_15")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "PFI_15")

    @_staticproperty
    def RTSI_PXI_TRIG_0() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_0")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "RTSI_PXI_TRIG_0")

    @_staticproperty
    def RTSI_PXI_TRIG_1() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_1")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "RTSI_PXI_TRIG_1")

    @_staticproperty
    def RTSI_PXI_TRIG_2() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_2")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "RTSI_PXI_TRIG_2")

    @_staticproperty
    def RTSI_PXI_TRIG_3() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_3")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "RTSI_PXI_TRIG_3")

    @_staticproperty
    def RTSI_PXI_TRIG_4() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_4")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "RTSI_PXI_TRIG_4")

    @_staticproperty
    def RTSI_PXI_TRIG_5() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_5")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "RTSI_PXI_TRIG_5")

    @_staticproperty
    def RTSI_PXI_TRIG_6() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_6")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "RTSI_PXI_TRIG_6")

    @_staticproperty
    def RTSI_PXI_TRIG_7() -> DAQCM_Export_StartTrigger_On_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_StartTrigger_On_Line, "RTSI_PXI_TRIG_7")
        return DAQCM_Export_StartTrigger_On_Line(dotnet_result, "RTSI_PXI_TRIG_7")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Start_Trigger, "aiStartTrigger")
        return DAQCM_Export_Start_Trigger(dotnet_result, "AI_START_TRIGGER")

    @_staticproperty
    def AO_START_TRIGGER() -> DAQCM_Export_Start_Trigger:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Export_Start_Trigger, "aoStartTrigger")
        return DAQCM_Export_Start_Trigger(dotnet_result, "AO_START_TRIGGER")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Slope, "Rising")
        return DAQCM_Slope(dotnet_result, "RISING")

    @_staticproperty
    def FALLING() -> DAQCM_Slope:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Slope, "Falling")
        return DAQCM_Slope(dotnet_result, "FALLING")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "None")
        return DAQCM_Trigger_Line(dotnet_result, "NONE")

    @_staticproperty
    def PFI_0() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_0")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_0")

    @_staticproperty
    def PFI_1() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_1")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_1")

    @_staticproperty
    def PFI_2() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_2")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_2")

    @_staticproperty
    def PFI_3() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_3")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_3")

    @_staticproperty
    def PFI_4() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_4")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_4")

    @_staticproperty
    def PFI_5() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_5")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_5")

    @_staticproperty
    def PFI_6() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_6")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_6")

    @_staticproperty
    def PFI_7() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_7")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_7")

    @_staticproperty
    def PFI_8() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_8")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_8")

    @_staticproperty
    def PFI_9() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_9")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_9")

    @_staticproperty
    def PFI_10() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_10")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_10")

    @_staticproperty
    def PFI_11() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_11")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_11")

    @_staticproperty
    def PFI_12() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_12")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_12")

    @_staticproperty
    def PFI_13() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_13")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_13")

    @_staticproperty
    def PFI_14() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_14")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_14")

    @_staticproperty
    def PFI_15() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "PFI_15")
        return DAQCM_Trigger_Line(dotnet_result, "PFI_15")

    @_staticproperty
    def RTSI_PXI_TRIG_0() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_0")
        return DAQCM_Trigger_Line(dotnet_result, "RTSI_PXI_TRIG_0")

    @_staticproperty
    def RTSI_PXI_TRIG_1() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_1")
        return DAQCM_Trigger_Line(dotnet_result, "RTSI_PXI_TRIG_1")

    @_staticproperty
    def RTSI_PXI_TRIG_2() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_2")
        return DAQCM_Trigger_Line(dotnet_result, "RTSI_PXI_TRIG_2")

    @_staticproperty
    def RTSI_PXI_TRIG_3() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_3")
        return DAQCM_Trigger_Line(dotnet_result, "RTSI_PXI_TRIG_3")

    @_staticproperty
    def RTSI_PXI_TRIG_4() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_4")
        return DAQCM_Trigger_Line(dotnet_result, "RTSI_PXI_TRIG_4")

    @_staticproperty
    def RTSI_PXI_TRIG_5() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_5")
        return DAQCM_Trigger_Line(dotnet_result, "RTSI_PXI_TRIG_5")

    @_staticproperty
    def RTSI_PXI_TRIG_6() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_6")
        return DAQCM_Trigger_Line(dotnet_result, "RTSI_PXI_TRIG_6")

    @_staticproperty
    def RTSI_PXI_TRIG_7() -> DAQCM_Trigger_Line:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCM_Trigger_Line, "RTSI_PXI_TRIG_7")
        return DAQCM_Trigger_Line(dotnet_result, "RTSI_PXI_TRIG_7")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQConversionRate, "Default")
        return DAQConversionRate(dotnet_result, "DEFAULT")

    @_staticproperty
    def MAXIMUM() -> DAQConversionRate:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQConversionRate, "Maximum")
        return DAQConversionRate(dotnet_result, "MAXIMUM")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterCountMode, "Up")
        return DAQCounterCountMode(dotnet_result, "UP")

    @_staticproperty
    def DOWN() -> DAQCounterCountMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterCountMode, "Down")
        return DAQCounterCountMode(dotnet_result, "DOWN")

    @_staticproperty
    def EXTERNALLY_CONTROLLED() -> DAQCounterCountMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterCountMode, "ExternallyControlled")
        return DAQCounterCountMode(dotnet_result, "EXTERNALLY_CONTROLLED")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterDecoding, "Decoding1X")
        return DAQCounterDecoding(dotnet_result, "DECODING1_X")

    @_staticproperty
    def DECODING2_X() -> DAQCounterDecoding:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterDecoding, "Decoding2X")
        return DAQCounterDecoding(dotnet_result, "DECODING2_X")

    @_staticproperty
    def DECODING4_X() -> DAQCounterDecoding:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterDecoding, "Decoding4X")
        return DAQCounterDecoding(dotnet_result, "DECODING4_X")

    @_staticproperty
    def DECODING_PULSE_COUNTING() -> DAQCounterDecoding:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterDecoding, "DecodingPulseCounting")
        return DAQCounterDecoding(dotnet_result, "DECODING_PULSE_COUNTING")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterEdge, "Falling")
        return DAQCounterEdge(dotnet_result, "FALLING")

    @_staticproperty
    def RISING() -> DAQCounterEdge:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterEdge, "Rising")
        return DAQCounterEdge(dotnet_result, "RISING")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterType, "FrequencyMeasurement")
        return DAQCounterType(dotnet_result, "FREQUENCY_MEASUREMENT")

    @_staticproperty
    def PERIOD_MEASUREMENT() -> DAQCounterType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterType, "PeriodMeasurement")
        return DAQCounterType(dotnet_result, "PERIOD_MEASUREMENT")

    @_staticproperty
    def COUNT_UP_DOWN() -> DAQCounterType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterType, "CountUpDown")
        return DAQCounterType(dotnet_result, "COUNT_UP_DOWN")

    @_staticproperty
    def POSITION_MEASUREMENT() -> DAQCounterType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterType, "PositionMeasurement")
        return DAQCounterType(dotnet_result, "POSITION_MEASUREMENT")

    @_staticproperty
    def OTHER() -> DAQCounterType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterType, "Other")
        return DAQCounterType(dotnet_result, "OTHER")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterZIndexMode, "AHighBHigh")
        return DAQCounterZIndexMode(dotnet_result, "A_HIGH_B_HIGH")

    @_staticproperty
    def A_HIGH_B_LOW() -> DAQCounterZIndexMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterZIndexMode, "AHighBLow")
        return DAQCounterZIndexMode(dotnet_result, "A_HIGH_B_LOW")

    @_staticproperty
    def A_LOW_B_HIGH() -> DAQCounterZIndexMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterZIndexMode, "ALowBHigh")
        return DAQCounterZIndexMode(dotnet_result, "A_LOW_B_HIGH")

    @_staticproperty
    def A_LOW_B_LOW() -> DAQCounterZIndexMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterZIndexMode, "ALowBLow")
        return DAQCounterZIndexMode(dotnet_result, "A_LOW_B_LOW")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDataChannelType, "Frequency")
        return DAQDataChannelType(dotnet_result, "FREQUENCY")

    @_staticproperty
    def DUTY_CYCLE() -> DAQDataChannelType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDataChannelType, "DutyCycle")
        return DAQDataChannelType(dotnet_result, "DUTY_CYCLE")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfiguration, "Default")
        return DAQDeviceInputConfiguration(dotnet_result, "DEFAULT")

    @_staticproperty
    def RSE() -> DAQDeviceInputConfiguration:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfiguration, "RSE")
        return DAQDeviceInputConfiguration(dotnet_result, "RSE")

    @_staticproperty
    def NRSE() -> DAQDeviceInputConfiguration:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfiguration, "NRSE")
        return DAQDeviceInputConfiguration(dotnet_result, "NRSE")

    @_staticproperty
    def DIFFERENTIAL() -> DAQDeviceInputConfiguration:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfiguration, "Differential")
        return DAQDeviceInputConfiguration(dotnet_result, "DIFFERENTIAL")

    @_staticproperty
    def PSEUDODIFFERENTIAL() -> DAQDeviceInputConfiguration:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfiguration, "Pseudodifferential")
        return DAQDeviceInputConfiguration(dotnet_result, "PSEUDODIFFERENTIAL")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputVoltage")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_VOLTAGE")

    @_staticproperty
    def ANALOG_INPUT_CURRENT() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputCurrent")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_CURRENT")

    @_staticproperty
    def ANALOG_INPUT_TEMPERATURE_THERMOCOUPLE() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputTemperatureThermocouple")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_TEMPERATURE_THERMOCOUPLE")

    @_staticproperty
    def ANALOG_INPUT_TEMPERATURE_THERMISTOR_VEX() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputTemperatureThermistorVex")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_TEMPERATURE_THERMISTOR_VEX")

    @_staticproperty
    def ANALOG_INPUT_TEMPERATURE_THERMISTOR_IEX() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputTemperatureThermistorIex")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_TEMPERATURE_THERMISTOR_IEX")

    @_staticproperty
    def ANALOG_INPUT_TEMPERATURE_RTD() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputTemperatureRTD")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_TEMPERATURE_RTD")

    @_staticproperty
    def ANALOG_INPUT_STRAIN_GAGE() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputStrainGage")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_STRAIN_GAGE")

    @_staticproperty
    def ANALOG_INPUT_ACCELEROMETER() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputAccelerometer")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_ACCELEROMETER")

    @_staticproperty
    def ANALOG_INPUT_BRIDGE() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputBridge")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_BRIDGE")

    @_staticproperty
    def ANALOG_INPUT_FORCE() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputForce")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_FORCE")

    @_staticproperty
    def ANALOG_INPUT_PRESSURE() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputPressure")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_PRESSURE")

    @_staticproperty
    def ANALOG_INPUT_TORQUE() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputTorque")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_TORQUE")

    @_staticproperty
    def ANALOG_INPUT_POSITION_LVDT() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputPositionLVDT")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_POSITION_LVDT")

    @_staticproperty
    def ANALOG_INPUT_POSITION_RVDT() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogInputPositionRVDT")
        return DAQMeasurementType(dotnet_result, "ANALOG_INPUT_POSITION_RVDT")

    @_staticproperty
    def ANALOG_OUTPUT_VOLTAGE() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogOutputVoltage")
        return DAQMeasurementType(dotnet_result, "ANALOG_OUTPUT_VOLTAGE")

    @_staticproperty
    def ANALOG_OUTPUT_CURRENT() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "AnalogOutputCurrent")
        return DAQMeasurementType(dotnet_result, "ANALOG_OUTPUT_CURRENT")

    @_staticproperty
    def DIGITAL_INPUT() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "DigitalInput")
        return DAQMeasurementType(dotnet_result, "DIGITAL_INPUT")

    @_staticproperty
    def DIGITAL_OUTPUT() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "DigitalOutput")
        return DAQMeasurementType(dotnet_result, "DIGITAL_OUTPUT")

    @_staticproperty
    def COUNTER_INPUT_COUNT_EDGES() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterInputCountEdges")
        return DAQMeasurementType(dotnet_result, "COUNTER_INPUT_COUNT_EDGES")

    @_staticproperty
    def COUNTER_INPUT_FREQUENCY() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterInputFrequency")
        return DAQMeasurementType(dotnet_result, "COUNTER_INPUT_FREQUENCY")

    @_staticproperty
    def COUNTER_INPUT_PERIOD() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterInputPeriod")
        return DAQMeasurementType(dotnet_result, "COUNTER_INPUT_PERIOD")

    @_staticproperty
    def COUNTER_INPUT_POSITION_LINEAR_ENCODER() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterInputPositionLinearEncoder")
        return DAQMeasurementType(dotnet_result, "COUNTER_INPUT_POSITION_LINEAR_ENCODER")

    @_staticproperty
    def COUNTER_INPUT_PULSE_MEASUREMENT() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterInputPulseMeasurement")
        return DAQMeasurementType(dotnet_result, "COUNTER_INPUT_PULSE_MEASUREMENT")

    @_staticproperty
    def COUNTER_OUTPUT_PULSE_GENERATION() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "CounterOutputPulseGeneration")
        return DAQMeasurementType(dotnet_result, "COUNTER_OUTPUT_PULSE_GENERATION")

    @_staticproperty
    def USER_DEFINED() -> DAQMeasurementType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementType, "UserDefined")
        return DAQMeasurementType(dotnet_result, "USER_DEFINED")


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
        dotnet_result = self._dotnet_instance.TriggerType
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge(*unwrapped)

    @property
    def source(self) -> str:
        """Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger."""
        dotnet_result = self._dotnet_instance.Source
        return _wrap(dotnet_result)

    @source.setter
    def source(self, value: str):
        """Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Source = next(unwrapped)

    @property
    def slope(self) -> DirectionType:
        """Gets or sets the direction of a signal slope that causes a trigger when the signal crosses the threshold <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Level" />."""
        dotnet_result = self._dotnet_instance.Slope
        return _wrap(dotnet_result)

    @slope.setter
    def slope(self, value: DirectionType):
        """Gets or sets the direction of a signal slope that causes a trigger when the signal crosses the threshold <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Level" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Slope = next(unwrapped)

    @property
    def level(self) -> float:
        """Gets or sets the threshold value, in the units of the measurement, at which to start acquiring samples. Set the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Slope" /> to specify on which type of slope this level causes the task to start acquiring data."""
        dotnet_result = self._dotnet_instance.Level
        return _wrap(dotnet_result)

    @level.setter
    def level(self, value: float):
        """Gets or sets the threshold value, in the units of the measurement, at which to start acquiring samples. Set the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Slope" /> to specify on which type of slope this level causes the task to start acquiring data."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Level = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow(*unwrapped)

    @property
    def source(self) -> str:
        """Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger."""
        dotnet_result = self._dotnet_instance.Source
        return _wrap(dotnet_result)

    @source.setter
    def source(self, value: str):
        """Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Source = next(unwrapped)

    @property
    def window_condition(self) -> WindowConditionType:
        """Gets or sets whether the task starts acquiring samples when the signal enters the window between <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowBottom" /> and <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowTop" /> or when it leaves the window."""
        dotnet_result = self._dotnet_instance.WindowCondition
        return _wrap(dotnet_result)

    @window_condition.setter
    def window_condition(self, value: WindowConditionType):
        """Gets or sets whether the task starts acquiring samples when the signal enters the window between <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowBottom" /> and <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowTop" /> or when it leaves the window."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.WindowCondition = next(unwrapped)

    @property
    def window_top(self) -> float:
        """Gets or sets the upper limit of the window, in the units of the measurement."""
        dotnet_result = self._dotnet_instance.WindowTop
        return _wrap(dotnet_result)

    @window_top.setter
    def window_top(self, value: float):
        """Gets or sets the upper limit of the window, in the units of the measurement."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.WindowTop = next(unwrapped)

    @property
    def window_bottom(self) -> float:
        """Gets or sets the lower limit of the window, in the units of the measurement."""
        dotnet_result = self._dotnet_instance.WindowBottom
        return _wrap(dotnet_result)

    @window_bottom.setter
    def window_bottom(self, value: float):
        """Gets or sets the lower limit of the window, in the units of the measurement."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.WindowBottom = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerDigitalEdge(*unwrapped)

    @property
    def source(self) -> str:
        """Gets or sets the name of a terminal that is the source of the digital signal used as the trigger."""
        dotnet_result = self._dotnet_instance.Source
        return _wrap(dotnet_result)

    @source.setter
    def source(self, value: str):
        """Gets or sets the name of a terminal that is the source of the digital signal used as the trigger."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Source = next(unwrapped)

    @property
    def edge(self) -> DirectionType:
        """Gets or sets on which type of edge of the digital signal to start acquiring samples."""
        dotnet_result = self._dotnet_instance.Edge
        return _wrap(dotnet_result)

    @edge.setter
    def edge(self, value: DirectionType):
        """Gets or sets on which type of edge of the digital signal to start acquiring samples."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Edge = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerNone(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerSoftware(*unwrapped)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFilterType, "LogEntireBusTraffic")
        return DataLoggingFilterType(dotnet_result, "LOG_ENTIRE_BUS_TRAFFIC")

    @_staticproperty
    def EXCLUDE_FRAME_I_DS() -> DataLoggingFilterType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFilterType, "ExcludeFrameIDs")
        return DataLoggingFilterType(dotnet_result, "EXCLUDE_FRAME_I_DS")

    @_staticproperty
    def INCLUDE_FRAME_I_DS() -> DataLoggingFilterType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFilterType, "IncludeFrameIDs")
        return DataLoggingFilterType(dotnet_result, "INCLUDE_FRAME_I_DS")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingOperationType, "ContinueLoggingInNewFile")
        return DataLoggingOperationType(dotnet_result, "CONTINUE_LOGGING_IN_NEW_FILE")

    @_staticproperty
    def STOP_LOGGING() -> DataLoggingOperationType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingOperationType, "StopLogging")
        return DataLoggingOperationType(dotnet_result, "STOP_LOGGING")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingTriggerType, "StartLoggingOnNonZero")
        return DataLoggingTriggerType(dotnet_result, "START_LOGGING_ON_NON_ZERO")

    @_staticproperty
    def START_LOGGING_ON_ZERO() -> DataLoggingTriggerType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingTriggerType, "StartLoggingOnZero")
        return DataLoggingTriggerType(dotnet_result, "START_LOGGING_ON_ZERO")

    @_staticproperty
    def ENABLE_LOGGING_WHEN_TRIGGER_IS_ZERO() -> DataLoggingTriggerType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingTriggerType, "EnableLoggingWhenTriggerIsZero")
        return DataLoggingTriggerType(dotnet_result, "ENABLE_LOGGING_WHEN_TRIGGER_IS_ZERO")

    @_staticproperty
    def ENABLE_LOGGING_WHEN_TRIGGER_IS_NON_ZERO() -> DataLoggingTriggerType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingTriggerType, "EnableLoggingWhenTriggerIsNonZero")
        return DataLoggingTriggerType(dotnet_result, "ENABLE_LOGGING_WHEN_TRIGGER_IS_NON_ZERO")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.Delimiter, "Tab")
        return Delimiter(dotnet_result, "TAB")

    @_staticproperty
    def EQUALS() -> Delimiter:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.Delimiter, "Equals")
        return Delimiter(dotnet_result, "EQUALS")

    @_staticproperty
    def COMMA() -> Delimiter:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.Delimiter, "Comma")
        return Delimiter(dotnet_result, "COMMA")


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFile(*unwrapped)

    @property
    def path(self) -> str:
        """Gets the path to the file on the host computer."""
        dotnet_result = self._dotnet_instance.Path
        return _wrap(dotnet_result)

    @property
    def type(self) -> DependentFileType:
        """Gets whether the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFile.Path" crefType="Unqualified" /> to the dependent file is absolute or relative to another directory."""
        dotnet_result = self._dotnet_instance.Type
        return _wrap(dotnet_result)

    @property
    def version(self) -> str:
        """Gets or sets version information for the dependent file."""
        dotnet_result = self._dotnet_instance.Version
        return _wrap(dotnet_result)

    @version.setter
    def version(self, value: str):
        """Gets or sets version information for the dependent file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Version = next(unwrapped)

    @property
    def force_download(self) -> bool:
        """Gets or sets whether the file is set to force-download to the target."""
        dotnet_result = self._dotnet_instance.ForceDownload
        return _wrap(dotnet_result)

    @force_download.setter
    def force_download(self, value: bool):
        """Gets or sets whether the file is set to force-download to the target."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ForceDownload = next(unwrapped)

    @property
    def rt_destination(self) -> str:
        """Gets or sets the destination path, including the filename, for the file on the target. This property must be an absolute path."""
        dotnet_result = self._dotnet_instance.RTDestination
        return _wrap(dotnet_result)

    @rt_destination.setter
    def rt_destination(self, value: str):
        """Gets or sets the destination path, including the filename, for the file on the target. This property must be an absolute path."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.RTDestination = next(unwrapped)

    @property
    def supported_target(self) -> str:
        """Gets or sets the target operating system(s) to which the file is deployed."""
        dotnet_result = self._dotnet_instance.SupportedTarget
        return _wrap(dotnet_result)

    @supported_target.setter
    def supported_target(self, value: str):
        """Gets or sets the target operating system(s) to which the file is deployed."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SupportedTarget = next(unwrapped)

    @property
    def md5(self) -> str:
        """Gets or sets the MD5 message-digest for the file."""
        dotnet_result = self._dotnet_instance.MD5
        return _wrap(dotnet_result)

    @md5.setter
    def md5(self, value: str):
        """Gets or sets the MD5 message-digest for the file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.MD5 = next(unwrapped)

    @overload
    def set_path(self, file_path: str, sdf_path: str):
        ...

    def set_path(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetPath(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_absolute_path(self, base_absolute_path: str) -> str:
        ...

    def get_absolute_path(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAbsolutePath(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFileType, "Absolute")
        return DependentFileType(dotnet_result, "ABSOLUTE")

    @_staticproperty
    def RELATIVE() -> DependentFileType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFileType, "Relative")
        return DependentFileType(dotnet_result, "RELATIVE")

    @_staticproperty
    def TO_COMMON_DOC_DIR() -> DependentFileType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFileType, "ToCommonDocDir")
        return DependentFileType(dotnet_result, "TO_COMMON_DOC_DIR")

    @_staticproperty
    def TO_APP_DATA_DIR() -> DependentFileType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFileType, "ToAppDataDir")
        return DependentFileType(dotnet_result, "TO_APP_DATA_DIR")


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary(*unwrapped)

    @property
    def count(self) -> int:
        """Gets the total number of key/value pairs in a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.Count
        return _wrap(dotnet_result)

    @property
    def elem(self) -> Sequence[DictionaryElement]:
        """Gets all the elements in the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.Elem
        return _wrap(dotnet_result)

    @overload
    def add_boolean(self, name: str, value: bool) -> bool:
        ...

    def add_boolean(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddBoolean(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_boolean_array(self, name: str, value: Sequence[bool]) -> bool:
        ...

    def add_boolean_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddBooleanArray(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u16(self, name: str, value: int) -> bool:
        ...

    def add_u16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u16_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_u16_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU16Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u32(self, name: str, value: int) -> bool:
        ...

    def add_u32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u32_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_u32_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU32Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u64(self, name: str, value: int) -> bool:
        ...

    def add_u64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u64_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_u64_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU64Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i16(self, name: str, value: int) -> bool:
        ...

    def add_i16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i16_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_i16_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI16Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i32(self, name: str, value: int) -> bool:
        ...

    def add_i32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i32_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_i32_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI32Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i64(self, name: str, value: int) -> bool:
        ...

    def add_i64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i64_array(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_i64_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI64Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_double(self, name: str, value: float) -> bool:
        ...

    def add_double(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddDouble(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_double_array(self, name: str, value: Sequence[float]) -> bool:
        ...

    def add_double_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddDoubleArray(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_string(self, name: str, value: str) -> bool:
        ...

    def add_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_string_array(self, name: str, value: Sequence[str]) -> bool:
        ...

    def add_string_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddStringArray(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def clear(self):
        ...

    def clear(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clear(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_boolean(self, name: str) -> Tuple[bool, bool]:
        ...

    def get_boolean(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBoolean(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_boolean_array(self, name: str) -> Tuple[bool, Sequence[bool]]:
        ...

    def get_boolean_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBooleanArray(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u16_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u32_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u64_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i16(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i16_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i16_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI16Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i32_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i64(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i64_array(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i64_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI64Array(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_double(self, name: str) -> Tuple[bool, float]:
        ...

    def get_double(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDouble(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_double_array(self, name: str) -> Tuple[bool, Sequence[float]]:
        ...

    def get_double_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDoubleArray(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string(self, name: str) -> Tuple[bool, str]:
        ...

    def get_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string_array(self, name: str) -> Tuple[bool, Sequence[str]]:
        ...

    def get_string_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStringArray(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_element(self, key: str) -> bool:
        ...

    def remove_element(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveElement(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DictionaryElement(*unwrapped)

    @property
    def item(self) -> Any:
        """Gets or sets a reference to a value of a dictionary element."""
        dotnet_result = self._dotnet_instance.Item
        return _wrap(dotnet_result)

    @item.setter
    def item(self, value: Any):
        """Gets or sets a reference to a value of a dictionary element."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Item = next(unwrapped)

    @property
    def key(self) -> str:
        """Gets or sets the key, or name, of a dictionary element."""
        dotnet_result = self._dotnet_instance.Key
        return _wrap(dotnet_result)

    @key.setter
    def key(self, value: str):
        """Gets or sets the key, or name, of a dictionary element."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Key = next(unwrapped)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DirectionType, "Rising")
        return DirectionType(dotnet_result, "RISING")

    @_staticproperty
    def FALLING() -> DirectionType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.DirectionType, "Falling")
        return DirectionType(dotnet_result, "FALLING")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.EdgeType, "Rising")
        return EdgeType(dotnet_result, "RISING")

    @_staticproperty
    def FALLING() -> EdgeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.EdgeType, "Falling")
        return EdgeType(dotnet_result, "FALLING")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FDISOMode, "ISO")
        return FDISOMode(dotnet_result, "ISO")

    @_staticproperty
    def NON_ISO() -> FDISOMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FDISOMode, "NonISO")
        return FDISOMode(dotnet_result, "NON_ISO")

    @_staticproperty
    def ISO_LEGACY() -> FDISOMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FDISOMode, "ISOLegacy")
        return FDISOMode(dotnet_result, "ISO_LEGACY")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FileLimitationType, "Footprint")
        return FileLimitationType(dotnet_result, "FOOTPRINT")

    @_staticproperty
    def TIME() -> FileLimitationType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FileLimitationType, "Time")
        return FileLimitationType(dotnet_result, "TIME")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FileType, "TDMS")
        return FileType(dotnet_result, "TDMS")

    @_staticproperty
    def NCL() -> FileType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FileType, "NCL")
        return FileType(dotnet_result, "NCL")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FramePhaseType, "Unchanged")
        return FramePhaseType(dotnet_result, "UNCHANGED")

    @_staticproperty
    def RESET() -> FramePhaseType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FramePhaseType, "Reset")
        return FramePhaseType(dotnet_result, "RESET")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameTriggerType, "ChannelValueChange")
        return FrameTriggerType(dotnet_result, "CHANNEL_VALUE_CHANGE")

    @_staticproperty
    def TRIGGER_CHANNEL_NOT_ZERO() -> FrameTriggerType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameTriggerType, "TriggerChannelNotZero")
        return FrameTriggerType(dotnet_result, "TRIGGER_CHANNEL_NOT_ZERO")

    @_staticproperty
    def CHANNEL_VALUE_CHANGE_OR_TRIGGER_CHANNEL_NOT_ZERO() -> FrameTriggerType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameTriggerType, "ChannelValueChangeOrTriggerChannelNotZero")
        return FrameTriggerType(dotnet_result, "CHANNEL_VALUE_CHANGE_OR_TRIGGER_CHANNEL_NOT_ZERO")

    @_staticproperty
    def TRIGGER_CHANNEL_ANY_VALUE_CHANGE() -> FrameTriggerType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameTriggerType, "TriggerChannelAnyValueChange")
        return FrameTriggerType(dotnet_result, "TRIGGER_CHANNEL_ANY_VALUE_CHANGE")

    @_staticproperty
    def CHANNEL_VALUE_CHANGE_OR_TRIGGER_CHANNEL_ANY_VALUE_CHANGE() -> FrameTriggerType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameTriggerType, "ChannelValueChangeOrTriggerChannelAnyValueChange")
        return FrameTriggerType(dotnet_result, "CHANNEL_VALUE_CHANGE_OR_TRIGGER_CHANNEL_ANY_VALUE_CHANGE")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameType, "CANDataFrame")
        return FrameType(dotnet_result, "CAN_DATA_FRAME")

    @_staticproperty
    def CAN_REMOTE_FRAME() -> FrameType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameType, "CANRemoteFrame")
        return FrameType(dotnet_result, "CAN_REMOTE_FRAME")

    @_staticproperty
    def FLEX_RAY_DATA_FRAME() -> FrameType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameType, "FlexRayDataFrame")
        return FrameType(dotnet_result, "FLEX_RAY_DATA_FRAME")

    @_staticproperty
    def FLEX_RAY_NULL_FRAME() -> FrameType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.FrameType, "FlexRayNullFrame")
        return FrameType(dotnet_result, "FLEX_RAY_NULL_FRAME")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalParameterScopes, "Target")
        return GlobalParameterScopes(dotnet_result, "TARGET")

    @_staticproperty
    def MODEL() -> GlobalParameterScopes:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalParameterScopes, "Model")
        return GlobalParameterScopes(dotnet_result, "MODEL")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalSequenceCommand, "StopAll")
        return GlobalSequenceCommand(dotnet_result, "STOP_ALL")

    @_staticproperty
    def ABORT_ALL() -> GlobalSequenceCommand:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalSequenceCommand, "AbortAll")
        return GlobalSequenceCommand(dotnet_result, "ABORT_ALL")

    @_staticproperty
    def STOP_GROUP() -> GlobalSequenceCommand:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalSequenceCommand, "StopGroup")
        return GlobalSequenceCommand(dotnet_result, "STOP_GROUP")


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
        dotnet_result = self._dotnet_instance.DataSource
        return _wrap(dotnet_result)

    @data_source.setter
    def data_source(self, value: BaseNode):
        """Gets or sets the source channel that maps to the current channel and provides it data."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DataSource = next(unwrapped)

    @property
    def column_dimensions(self) -> int:
        """Gets the number of columns in the channel value."""
        dotnet_result = self._dotnet_instance.ColumnDimensions
        return _wrap(dotnet_result)

    @property
    def row_dimensions(self) -> int:
        """Gets the number of rows in the channel value."""
        dotnet_result = self._dotnet_instance.RowDimensions
        return _wrap(dotnet_result)

    @property
    def units(self) -> str:
        """Gets or sets the units associated with the channel. This can be any arbitrary string."""
        dotnet_result = self._dotnet_instance.Units
        return _wrap(dotnet_result)

    @units.setter
    def units(self, value: str):
        """Gets or sets the units associated with the channel. This can be any arbitrary string."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Units = next(unwrapped)

    @property
    def is_readable(self) -> bool:
        """Gets a value indicating whether the channel is readable."""
        dotnet_result = self._dotnet_instance.IsReadable
        return _wrap(dotnet_result)

    @property
    def is_writable(self) -> bool:
        """Gets a value indicating whether the channel is writable."""
        dotnet_result = self._dotnet_instance.IsWritable
        return _wrap(dotnet_result)

    @property
    def scale_units(self) -> str:
        """Gets the units of the scale associated with the channel."""
        dotnet_result = self._dotnet_instance.ScaleUnits
        return _wrap(dotnet_result)

    @overload
    def remove_data_source(self):
        ...

    def remove_data_source(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveDataSource(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_value_table(self) -> Tuple[bool, Sequence[str], Sequence[float]]:
        ...

    def get_value_table(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetValueTable(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.LUTValue(*unwrapped)

    @property
    def pre_scaled(self) -> float:
        """Gets or sets the pre-scaled LUTValue."""
        dotnet_result = self._dotnet_instance.PreScaled
        return _wrap(dotnet_result)

    @pre_scaled.setter
    def pre_scaled(self, value: float):
        """Gets or sets the pre-scaled LUTValue."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PreScaled = next(unwrapped)

    @property
    def scaled(self) -> float:
        """Gets or sets the scaled LUTValue."""
        dotnet_result = self._dotnet_instance.Scaled
        return _wrap(dotnet_result)

    @scaled.setter
    def scaled(self, value: float):
        """Gets or sets the scaled LUTValue."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Scaled = next(unwrapped)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.LogMode, "Log")
        return LogMode(dotnet_result, "LOG")

    @_staticproperty
    def LOG_AND_READ() -> LogMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.LogMode, "LogAndRead")
        return LogMode(dotnet_result, "LOG_AND_READ")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommandState, "Start")
        return ModelCommandState(dotnet_result, "START")

    @_staticproperty
    def PAUSE() -> ModelCommandState:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommandState, "Pause")
        return ModelCommandState(dotnet_result, "PAUSE")

    @_staticproperty
    def RESET() -> ModelCommandState:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommandState, "Reset")
        return ModelCommandState(dotnet_result, "RESET")

    @_staticproperty
    def SAVE() -> ModelCommandState:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommandState, "Save")
        return ModelCommandState(dotnet_result, "SAVE")

    @_staticproperty
    def RESTORE() -> ModelCommandState:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ModelCommandState, "Restore")
        return ModelCommandState(dotnet_result, "RESTORE")


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil(*unwrapped)

    @staticmethod
    @overload
    def id_to_base_node(node_id: int) -> BaseNode:
        ...

    def id_to_base_node(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToBaseNode(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def id_to_custom_device_base(node_id: int) -> CustomDeviceBase:
        ...

    def id_to_custom_device_base(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToCustomDeviceBase(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def id_to_custom_device_channel(node_id: int) -> CustomDeviceChannel:
        ...

    def id_to_custom_device_channel(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToCustomDeviceChannel(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def id_to_custom_device_waveform(node_id: int) -> CustomDeviceWaveform:
        ...

    def id_to_custom_device_waveform(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToCustomDeviceWaveform(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def id_to_custom_device_section(node_id: int) -> CustomDeviceSection:
        ...

    def id_to_custom_device_section(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToCustomDeviceSection(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def id_to_custom_device(node_id: int) -> CustomDevice:
        ...

    def id_to_custom_device(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToCustomDevice(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def id_to_timing_sync_device(node_id: int) -> TimingAndSyncDevice:
        ...

    def id_to_timing_sync_device(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.NodeIDUtil.IDToTimingSyncDevice(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.PXIBackplaneReferenceClock, "Automatic")
        return PXIBackplaneReferenceClock(dotnet_result, "AUTOMATIC")

    @_staticproperty
    def NONE() -> PXIBackplaneReferenceClock:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.PXIBackplaneReferenceClock, "None")
        return PXIBackplaneReferenceClock(dotnet_result, "NONE")

    @_staticproperty
    def CLK10() -> PXIBackplaneReferenceClock:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.PXIBackplaneReferenceClock, "Clk10")
        return PXIBackplaneReferenceClock(dotnet_result, "CLK10")

    @_staticproperty
    def CLK100() -> PXIBackplaneReferenceClock:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.PXIBackplaneReferenceClock, "Clk100")
        return PXIBackplaneReferenceClock(dotnet_result, "CLK100")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ParameterAccess, "OnlyImportedParameters")
        return ParameterAccess(dotnet_result, "ONLY_IMPORTED_PARAMETERS")

    @_staticproperty
    def ANY_PARAMETER() -> ParameterAccess:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ParameterAccess, "AnyParameter")
        return ParameterAccess(dotnet_result, "ANY_PARAMETER")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelAccessType, "Read")
        return ReflectiveMemoryDataChannelAccessType(dotnet_result, "READ")

    @_staticproperty
    def WRITE() -> ReflectiveMemoryDataChannelAccessType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelAccessType, "Write")
        return ReflectiveMemoryDataChannelAccessType(dotnet_result, "WRITE")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "UInt8")
        return ReflectiveMemoryDataChannelDataType(dotnet_result, "U_INT8")

    @_staticproperty
    def INT8() -> ReflectiveMemoryDataChannelDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "Int8")
        return ReflectiveMemoryDataChannelDataType(dotnet_result, "INT8")

    @_staticproperty
    def U_INT16() -> ReflectiveMemoryDataChannelDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "UInt16")
        return ReflectiveMemoryDataChannelDataType(dotnet_result, "U_INT16")

    @_staticproperty
    def INT16() -> ReflectiveMemoryDataChannelDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "Int16")
        return ReflectiveMemoryDataChannelDataType(dotnet_result, "INT16")

    @_staticproperty
    def U_INT32() -> ReflectiveMemoryDataChannelDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "UInt32")
        return ReflectiveMemoryDataChannelDataType(dotnet_result, "U_INT32")

    @_staticproperty
    def INT32() -> ReflectiveMemoryDataChannelDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "Int32")
        return ReflectiveMemoryDataChannelDataType(dotnet_result, "INT32")

    @_staticproperty
    def U_INT64() -> ReflectiveMemoryDataChannelDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "UInt64")
        return ReflectiveMemoryDataChannelDataType(dotnet_result, "U_INT64")

    @_staticproperty
    def INT64() -> ReflectiveMemoryDataChannelDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "Int64")
        return ReflectiveMemoryDataChannelDataType(dotnet_result, "INT64")

    @_staticproperty
    def DOUBLE() -> ReflectiveMemoryDataChannelDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelDataType, "Double")
        return ReflectiveMemoryDataChannelDataType(dotnet_result, "DOUBLE")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptType, "LinkResetInterrupt")
        return ReflectiveMemoryInterruptType(dotnet_result, "LINK_RESET_INTERRUPT")

    @_staticproperty
    def NETWORK_INTERRUPT1() -> ReflectiveMemoryInterruptType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptType, "NetworkInterrupt1")
        return ReflectiveMemoryInterruptType(dotnet_result, "NETWORK_INTERRUPT1")

    @_staticproperty
    def NETWORK_INTERRUPT2() -> ReflectiveMemoryInterruptType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptType, "NetworkInterrupt2")
        return ReflectiveMemoryInterruptType(dotnet_result, "NETWORK_INTERRUPT2")

    @_staticproperty
    def NETWORK_INTERRUPT3() -> ReflectiveMemoryInterruptType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptType, "NetworkInterrupt3")
        return ReflectiveMemoryInterruptType(dotnet_result, "NETWORK_INTERRUPT3")

    @_staticproperty
    def NETWORK_INIT_INTERRUPT() -> ReflectiveMemoryInterruptType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptType, "NetworkInitInterrupt")
        return ReflectiveMemoryInterruptType(dotnet_result, "NETWORK_INIT_INTERRUPT")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior, "ReplayEntireFile")
        return ReplayBehavior(dotnet_result, "REPLAY_ENTIRE_FILE")

    @_staticproperty
    def EXCLUDE_FRAME_I_DS() -> ReplayBehavior:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior, "ExcludeFrameIDs")
        return ReplayBehavior(dotnet_result, "EXCLUDE_FRAME_I_DS")

    @_staticproperty
    def INCLUDE_FRAME_I_DS() -> ReplayBehavior:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior, "IncludeFrameIDs")
        return ReplayBehavior(dotnet_result, "INCLUDE_FRAME_I_DS")


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
        dotnet_result = self._dotnet_instance.Version
        return _wrap(dotnet_result)

    @version.setter
    def version(self, value: str):
        """Gets or sets the system definition file version number."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Version = next(unwrapped)

    @property
    def creator(self) -> str:
        """Gets or sets the user account name of the system definition file creator."""
        dotnet_result = self._dotnet_instance.Creator
        return _wrap(dotnet_result)

    @creator.setter
    def creator(self, value: str):
        """Gets or sets the user account name of the system definition file creator."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Creator = next(unwrapped)

    @property
    def creation_date(self) -> float:
        """Gets or sets the creation date of the system definition file."""
        dotnet_result = self._dotnet_instance.CreationDate
        return _wrap(dotnet_result)

    @creation_date.setter
    def creation_date(self, value: float):
        """Gets or sets the creation date of the system definition file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.CreationDate = next(unwrapped)

    @overload
    def delete_channel_mappings(self, channel_path_destinations: Sequence[str]):
        ...

    def delete_channel_mappings(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DeleteChannelMappings(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_channel_mappings(self, channel_path_sources: Sequence[str], channel_path_destinations: Sequence[str]) -> bool:
        ...

    def add_channel_mappings(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddChannelMappings(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_channel_mappings(self) -> Tuple[Sequence[str], Sequence[str]]:
        ...

    def get_channel_mappings(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetChannelMappings(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def clear_channel_mappings(self):
        ...

    def clear_channel_mappings(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ClearChannelMappings(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_targets(self) -> Targets:
        ...

    def get_targets(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTargets(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def refresh_node_dependencies(self):
        ...

    def refresh_node_dependencies(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RefreshNodeDependencies(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_aliases(self) -> Aliases:
        ...

    def get_aliases(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAliases(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_scales(self) -> Scales:
        ...

    def get_scales(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetScales(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_system_mappings(self) -> SystemMappings:
        ...

    def get_system_mappings(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSystemMappings(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_data_sharing_network(self) -> DataSharingNetwork:
        ...

    def get_data_sharing_network(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataSharingNetwork(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_system_initialization(self) -> SystemInitialization:
        ...

    def get_system_initialization(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSystemInitialization(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SampleMode, "SinglePoint")
        return SampleMode(dotnet_result, "SINGLE_POINT")

    @_staticproperty
    def WAVEFORM() -> SampleMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SampleMode, "Waveform")
        return SampleMode(dotnet_result, "WAVEFORM")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ScaleType, "Polynomial")
        return ScaleType(dotnet_result, "POLYNOMIAL")

    @_staticproperty
    def THERMOCOUPLE() -> ScaleType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ScaleType, "Thermocouple")
        return ScaleType(dotnet_result, "THERMOCOUPLE")

    @_staticproperty
    def LOOKUP_TABLE() -> ScaleType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ScaleType, "LookupTable")
        return ScaleType(dotnet_result, "LOOKUP_TABLE")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariableStepFunction, "None")
        return SetVariableStepFunction(dotnet_result, "NONE")

    @_staticproperty
    def ADD() -> SetVariableStepFunction:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariableStepFunction, "Add")
        return SetVariableStepFunction(dotnet_result, "ADD")

    @_staticproperty
    def SUBTRACT() -> SetVariableStepFunction:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariableStepFunction, "Subtract")
        return SetVariableStepFunction(dotnet_result, "SUBTRACT")

    @_staticproperty
    def MULTIPLY() -> SetVariableStepFunction:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariableStepFunction, "Multiply")
        return SetVariableStepFunction(dotnet_result, "MULTIPLY")

    @_staticproperty
    def DIVIDE() -> SetVariableStepFunction:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariableStepFunction, "Divide")
        return SetVariableStepFunction(dotnet_result, "DIVIDE")


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame(*unwrapped)

    @property
    def transmit_trigger(self) -> FrameTriggerType:
        """Gets the trigger type (channel value change, trigger channel not zero, and so on) specified for an event-triggered frame."""
        dotnet_result = self._dotnet_instance.TransmitTrigger
        return _wrap(dotnet_result)

    @property
    def phase(self) -> FramePhaseType:
        """Gets or sets whether to reset the timer after <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        dotnet_result = self._dotnet_instance.Phase
        return _wrap(dotnet_result)

    @phase.setter
    def phase(self, value: FramePhaseType):
        """Gets or sets whether to reset the timer after <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Phase = next(unwrapped)

    @property
    def frame_type(self) -> FrameType:
        """Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port."""
        dotnet_result = self._dotnet_instance.FrameType
        return _wrap(dotnet_result)

    @frame_type.setter
    def frame_type(self, value: FrameType):
        """Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FrameType = next(unwrapped)

    @property
    def id(self) -> int:
        """Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent."""
        dotnet_result = self._dotnet_instance.ID
        return _wrap(dotnet_result)

    @id.setter
    def id(self, value: int):
        """Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ID = next(unwrapped)

    @property
    def payload_length(self) -> int:
        """Gets or sets the number of bytes in the payload of the frame."""
        dotnet_result = self._dotnet_instance.PayloadLength
        return _wrap(dotnet_result)

    @payload_length.setter
    def payload_length(self, value: int):
        """Gets or sets the number of bytes in the payload of the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PayloadLength = next(unwrapped)

    @property
    def md5(self) -> Sequence[int]:
        """Gets the MD5 message digest for the frame."""
        dotnet_result = self._dotnet_instance.MD5
        return _wrap(dotnet_result)

    @property
    def start_time_offset(self) -> float:
        """Gets or sets the amount of time that elapses between the session start and the transmission of the first frame."""
        dotnet_result = self._dotnet_instance.StartTimeOffset
        return _wrap(dotnet_result)

    @start_time_offset.setter
    def start_time_offset(self, value: float):
        """Gets or sets the amount of time that elapses between the session start and the transmission of the first frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.StartTimeOffset = next(unwrapped)

    @property
    def enable64_bit(self) -> bool:
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        dotnet_result = self._dotnet_instance.Enable64Bit
        return _wrap(dotnet_result)

    @enable64_bit.setter
    def enable64_bit(self, value: bool):
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Enable64Bit = next(unwrapped)

    @property
    def owning_database(self) -> BaseNode:
        """Gets or sets a reference to the XNET database that contains the frame."""
        dotnet_result = self._dotnet_instance.OwningDatabase
        return _wrap(dotnet_result)

    @owning_database.setter
    def owning_database(self, value: BaseNode):
        """Gets or sets a reference to the XNET database that contains the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.OwningDatabase = next(unwrapped)

    @property
    def cluster_name(self) -> str:
        """Gets or sets the name of the cluster in the XNET database that contains the frame."""
        dotnet_result = self._dotnet_instance.ClusterName
        return _wrap(dotnet_result)

    @cluster_name.setter
    def cluster_name(self, value: str):
        """Gets or sets the name of the cluster in the XNET database that contains the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ClusterName = next(unwrapped)

    @property
    def database_alias(self) -> str:
        """Gets or sets the alias for the XNET database that contains the frame."""
        dotnet_result = self._dotnet_instance.DatabaseAlias
        return _wrap(dotnet_result)

    @database_alias.setter
    def database_alias(self, value: str):
        """Gets or sets the alias for the XNET database that contains the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DatabaseAlias = next(unwrapped)

    @property
    def disabled(self) -> bool:
        """Gets whether transmission of the outgoing frame is disabled."""
        dotnet_result = self._dotnet_instance.Disabled
        return _wrap(dotnet_result)

    @property
    def disable_channel(self) -> BaseNode:
        """Gets a reference to the disable channel for the frame. A disable channel disables transmission of an outgoing frame when the value of the disable channel is non-zero."""
        dotnet_result = self._dotnet_instance.DisableChannel
        return _wrap(dotnet_result)

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets a reference to the channel that is checked for a non-zero value when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableFrameCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        dotnet_result = self._dotnet_instance.TriggerChannel
        return _wrap(dotnet_result)

    @property
    def enable_software_cyclic_trigger(self) -> bool:
        """Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame."""
        dotnet_result = self._dotnet_instance.EnableSoftwareCyclicTrigger
        return _wrap(dotnet_result)

    @enable_software_cyclic_trigger.setter
    def enable_software_cyclic_trigger(self, value: bool):
        """Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnableSoftwareCyclicTrigger = next(unwrapped)

    @property
    def enable_frame_cyclic_trigger(self) -> bool:
        """Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame."""
        dotnet_result = self._dotnet_instance.EnableFrameCyclicTrigger
        return _wrap(dotnet_result)

    @enable_frame_cyclic_trigger.setter
    def enable_frame_cyclic_trigger(self, value: bool):
        """Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnableFrameCyclicTrigger = next(unwrapped)

    @property
    def transmit_time(self) -> float:
        """Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        dotnet_result = self._dotnet_instance.TransmitTime
        return _wrap(dotnet_result)

    @transmit_time.setter
    def transmit_time(self, value: float):
        """Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TransmitTime = next(unwrapped)

    @overload
    def create_multiplexer(self, multiplexer_value: int) -> Multiplexer:
        ...

    @overload
    def create_multiplexer(self, multiplexer_value: int, signal_name: str) -> Multiplexer:
        ...

    def create_multiplexer(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateMultiplexer(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_mode(self, multiplexer_value: int, signal_name: str, description: str, units: str, default_value: float) -> Mode:
        ...

    def create_mode(self, *args):
        unwrapped = _unwrap({None: (5, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateMode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_signal_based_signal(self, name: str, description: str, units: str, default_value: float) -> SignalBasedSignal:
        ...

    def create_signal_based_signal(self, *args):
        unwrapped = _unwrap({None: (4, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateSignalBasedSignal(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_frame_information(self) -> FrameInformation:
        ...

    def create_frame_information(self, *args):
        unwrapped = _unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateFrameInformation(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_frame_faulting(self, create_skip_cyclic_frames: bool, create_transmit_time: bool) -> FrameFaulting:
        ...

    def create_frame_faulting(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateFrameFaulting(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_automatic_frame_processing(self) -> AutomaticFrameProcessing:
        ...

    def create_automatic_frame_processing(self, *args):
        unwrapped = _unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateAutomaticFrameProcessing(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def enable_transmission(self):
        ...

    def enable_transmission(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.EnableTransmission(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def disable_transmission(self, disable_channel: BaseNode):
        ...

    def disable_transmission(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DisableTransmission(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_transmit_trigger(self, trigger_type: FrameTriggerType, trigger_channel: BaseNode):
        ...

    def set_transmit_trigger(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetTransmitTrigger(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_multiplexer(self) -> Multiplexer:
        ...

    def get_multiplexer(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetMultiplexer(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_mode_list(self) -> Sequence[Mode]:
        ...

    def get_mode_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModeList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_signal_based_signal_list(self) -> Sequence[SignalBasedSignal]:
        ...

    def get_signal_based_signal_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSignalBasedSignalList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_frame_information(self) -> FrameInformation:
        ...

    def get_frame_information(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFrameInformation(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_frame_faulting(self) -> FrameFaulting:
        ...

    def get_frame_faulting(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFrameFaulting(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_automatic_frame_processing(self) -> AutomaticFrameProcessing:
        ...

    def get_automatic_frame_processing(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAutomaticFrameProcessing(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.ApplyParameterFile
        return _wrap(dotnet_result)

    @apply_parameter_file.setter
    def apply_parameter_file(self, value: bool):
        """Gets or sets a value indicating whether to apply the parameter values defined in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" /> when you deploy a system definition file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ApplyParameterFile = next(unwrapped)

    @property
    def parameter_file_delimiter(self) -> Delimiter:
        """Gets or sets the delimiter used to separate parameter-value pairs in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />."""
        dotnet_result = self._dotnet_instance.ParameterFileDelimiter
        return _wrap(dotnet_result)

    @parameter_file_delimiter.setter
    def parameter_file_delimiter(self, value: Delimiter):
        """Gets or sets the delimiter used to separate parameter-value pairs in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ParameterFileDelimiter = next(unwrapped)

    @property
    def parameter_access(self) -> ParameterAccess:
        """Gets or sets the flag used to allow or deny reading and writing non-imported parameters."""
        dotnet_result = self._dotnet_instance.ParameterAccess
        return _wrap(dotnet_result)

    @parameter_access.setter
    def parameter_access(self, value: ParameterAccess):
        """Gets or sets the flag used to allow or deny reading and writing non-imported parameters."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ParameterAccess = next(unwrapped)

    @property
    def parameter_file_allow_temp_variable(self) -> bool:
        """Gets or sets a value indicating whether the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" /> allows temporary variables. Temporary variables are always local to the file in which you define them."""
        dotnet_result = self._dotnet_instance.ParameterFileAllowTempVariable
        return _wrap(dotnet_result)

    @parameter_file_allow_temp_variable.setter
    def parameter_file_allow_temp_variable(self, value: bool):
        """Gets or sets a value indicating whether the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" /> allows temporary variables. Temporary variables are always local to the file in which you define them."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ParameterFileAllowTempVariable = next(unwrapped)

    @property
    def parameter_file(self) -> str:
        """Gets or sets the parameter calibration <format type="monospace">.txt</format> file to apply when you deploy a system definition file."""
        dotnet_result = self._dotnet_instance.ParameterFile
        return _wrap(dotnet_result)

    @parameter_file.setter
    def parameter_file(self, value: str):
        """Gets or sets the parameter calibration <format type="monospace">.txt</format> file to apply when you deploy a system definition file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ParameterFile = next(unwrapped)

    @property
    def parameter_alias_file(self) -> str:
        """Gets or sets the parameter alias file to use with the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />."""
        dotnet_result = self._dotnet_instance.ParameterAliasFile
        return _wrap(dotnet_result)

    @parameter_alias_file.setter
    def parameter_alias_file(self, value: str):
        """Gets or sets the parameter alias file to use with the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ParameterAliasFile = next(unwrapped)

    @overload
    def remove_parameter_alias_file(self):
        ...

    def remove_parameter_alias_file(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveParameterAliasFile(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_models(self) -> Models:
        ...

    def get_models(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModels(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_execution_order(self) -> ExecutionOrder:
        ...

    def get_execution_order(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetExecutionOrder(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSignalBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetRawDataBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddSignalBasedFrame(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddRawDataBasedFrame(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSignalBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetRawDataBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddSignalBasedFrame(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddRawDataBasedFrame(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.MaxGenMaps
        return _wrap(dotnet_result)

    @max_gen_maps.setter
    def max_gen_maps(self, value: int):
        """Gets or sets the maximum number of stimulus generator mappings across the entire system."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.MaxGenMaps = next(unwrapped)

    @property
    def max_steps(self) -> int:
        """Gets or sets the maximum number of steps a stimulus generator can contain. Set this value to a number that is larger than the number of steps in the longest generator script."""
        dotnet_result = self._dotnet_instance.MaxSteps
        return _wrap(dotnet_result)

    @max_steps.setter
    def max_steps(self, value: int):
        """Gets or sets the maximum number of steps a stimulus generator can contain. Set this value to a number that is larger than the number of steps in the longest generator script."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.MaxSteps = next(unwrapped)

    @property
    def auxilliary_buffer_size(self) -> int:
        """Gets or sets the size of the auxiliary buffer. The auxiliary buffer stores multi-point playback data in comma-separated value (CSV), files. Set this buffer size to a number that matches or exceeds the number of data points in the CSV file you want to play back. The auxiliary buffer size is shared by all active stimulus generators, so all generators can have up to Auxiliary Buffer Size total in data points for playback."""
        dotnet_result = self._dotnet_instance.AuxilliaryBufferSize
        return _wrap(dotnet_result)

    @auxilliary_buffer_size.setter
    def auxilliary_buffer_size(self, value: int):
        """Gets or sets the size of the auxiliary buffer. The auxiliary buffer stores multi-point playback data in comma-separated value (CSV), files. Set this buffer size to a number that matches or exceeds the number of data points in the CSV file you want to play back. The auxiliary buffer size is shared by all active stimulus generators, so all generators can have up to Auxiliary Buffer Size total in data points for playback."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AuxilliaryBufferSize = next(unwrapped)

    @property
    def analysis_buffer_size(self) -> int:
        """Gets or sets the size of the analysis buffer. The analysis buffer stores the expected result values for a table test. Set this value to a number that matches or exceeds the number of expected result values in a given table test."""
        dotnet_result = self._dotnet_instance.AnalysisBufferSize
        return _wrap(dotnet_result)

    @analysis_buffer_size.setter
    def analysis_buffer_size(self, value: int):
        """Gets or sets the size of the analysis buffer. The analysis buffer stores the expected result values for a table test. Set this value to a number that matches or exceeds the number of expected result values in a given table test."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AnalysisBufferSize = next(unwrapped)

    @property
    def analysis_result_size(self) -> int:
        """Gets or sets the size of the analysis failure result buffer. The analysis failure result buffer stores the failure results for a table test. Set this value to a number that meets or exceeds the maximum number of failures you expect to occur in the table test."""
        dotnet_result = self._dotnet_instance.AnalysisResultSize
        return _wrap(dotnet_result)

    @analysis_result_size.setter
    def analysis_result_size(self, value: int):
        """Gets or sets the size of the analysis failure result buffer. The analysis failure result buffer stores the failure results for a table test. Set this value to a number that meets or exceeds the maximum number of failures you expect to occur in the table test."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AnalysisResultSize = next(unwrapped)

    @overload
    def set_generator_count(self, count: int) -> bool:
        ...

    def set_generator_count(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetGeneratorCount(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_generator_list(self) -> Sequence[Generator]:
        ...

    def get_generator_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetGeneratorList(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSystemChannels(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinition(*unwrapped)

    @property
    def version(self) -> Tuple[int, int, int, int]:
        """Gets the version number of the system definition file."""
        dotnet_result = self._dotnet_instance.Version
        return _wrap(dotnet_result)

    @property
    def document_type(self) -> DocumentType:
        """The DocumentType for this SystemDefinition"""
        dotnet_result = self._dotnet_instance.DocumentType
        return _wrap(dotnet_result)

    @property
    def root(self) -> Root:
        """Gets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Root" crefType="Unqualified" /> node of the system definition file."""
        dotnet_result = self._dotnet_instance.Root
        return _wrap(dotnet_result)

    @overload
    def save_system_definition_file(self, filepath: str) -> Tuple[bool, str]:
        ...

    @overload
    def save_system_definition_file(self) -> Tuple[bool, str]:
        ...

    def save_system_definition_file(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SaveSystemDefinitionFile(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinitionExtensions.GetParent(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def is_self_or_ancestor_of(base_node: BaseNode, potential_child: BaseNode) -> bool:
        ...

    @staticmethod
    @overload
    def is_self_or_ancestor_of(base_node_type: BaseNodeType, potential_child: BaseNodeType) -> bool:
        ...

    def is_self_or_ancestor_of(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinitionExtensions.IsSelfOrAncestorOf(*unwrapped)
        return _wrap(dotnet_result)

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
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinitionExtensions.GetDescendantChannels(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def is_deprecated(node: BaseNode) -> bool:
        ...

    @staticmethod
    @overload
    def is_deprecated(base_node_type: BaseNodeType) -> bool:
        ...

    def is_deprecated(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.SystemDefinitionExtensions.IsDeprecated(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.AutoStart
        return _wrap(dotnet_result)

    @auto_start.setter
    def auto_start(self, value: bool):
        """Gets or sets whether the system runs the system definition file automatically after a target reboots or waits for a user to redeploy the file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AutoStart = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Target(*unwrapped)

    @_staticproperty
    def username_property_string() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Target.UsernamePropertyString
        return _wrap(dotnet_result)

    @_staticproperty
    def password_property_string() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Target.PasswordPropertyString
        return _wrap(dotnet_result)

    @property
    def timing_source_daq_settings(self) -> TimingSourceSettingsOptions:
        """Gets or sets the timing source setting for the DAQ device that is timing the Primary Control Loop. This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.TimingSourceDAQSettings
        return _wrap(dotnet_result)

    @timing_source_daq_settings.setter
    def timing_source_daq_settings(self, value: TimingSourceSettingsOptions):
        """Gets or sets the timing source setting for the DAQ device that is timing the Primary Control Loop. This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TimingSourceDAQSettings = next(unwrapped)

    @property
    def execution_mode(self) -> TargetExecutionMode:
        """Gets or sets the execution mode (parallel or low latency) of the loops of the VeriStand Engine."""
        dotnet_result = self._dotnet_instance.ExecutionMode
        return _wrap(dotnet_result)

    @execution_mode.setter
    def execution_mode(self, value: TargetExecutionMode):
        """Gets or sets the execution mode (parallel or low latency) of the loops of the VeriStand Engine."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ExecutionMode = next(unwrapped)

    @property
    def control_loop_timing_source(self) -> TargetControlLoopTimingSource:
        """Gets the timing source for the Primary Control Loop."""
        dotnet_result = self._dotnet_instance.ControlLoopTimingSource
        return _wrap(dotnet_result)

    @property
    def daq_timing_device(self) -> DAQDevice:
        """Gets or sets the DAQ device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.DAQTimingDevice
        return _wrap(dotnet_result)

    @property
    def custom_timing_device(self) -> CustomDevice:
        """Gets or sets the custom device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.CustomDeviceTiming" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.CustomTimingDevice
        return _wrap(dotnet_result)

    @property
    def daq_digital_lines_decimation(self) -> int:
        """Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at a rate of 100Hz. If you set the PCL to execute at a rate faster than 100Hz, use this property to specify a higher decimation value and reduce the frequency with which the PCL reads and writes the digital line values."""
        dotnet_result = self._dotnet_instance.DAQDigitalLinesDecimation
        return _wrap(dotnet_result)

    @daq_digital_lines_decimation.setter
    def daq_digital_lines_decimation(self, value: int):
        """Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at a rate of 100Hz. If you set the PCL to execute at a rate faster than 100Hz, use this property to specify a higher decimation value and reduce the frequency with which the PCL reads and writes the digital line values."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DAQDigitalLinesDecimation = next(unwrapped)

    @property
    def daq_digital_lines_rate(self) -> float:
        """Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values.
            The DIO Loop, which receives and sends these values from and to the PCL, executes at this rate and cannot be faster than the PCL loop."""
        dotnet_result = self._dotnet_instance.DAQDigitalLinesRate
        return _wrap(dotnet_result)

    @daq_digital_lines_rate.setter
    def daq_digital_lines_rate(self, value: float):
        """Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values.
            The DIO Loop, which receives and sends these values from and to the PCL, executes at this rate and cannot be faster than the PCL loop."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DAQDigitalLinesRate = next(unwrapped)

    @property
    def disable_target(self) -> bool:
        """Gets or sets the Boolean flag indicating whether a target is disabled."""
        dotnet_result = self._dotnet_instance.DisableTarget
        return _wrap(dotnet_result)

    @disable_target.setter
    def disable_target(self, value: bool):
        """Gets or sets the Boolean flag indicating whether a target is disabled."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DisableTarget = next(unwrapped)

    @property
    def operating_system(self) -> str:
        """Gets or sets the operating system of the target."""
        dotnet_result = self._dotnet_instance.OperatingSystem
        return _wrap(dotnet_result)

    @operating_system.setter
    def operating_system(self, value: str):
        """Gets or sets the operating system of the target."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.OperatingSystem = next(unwrapped)

    @property
    def ip_address(self) -> str:
        """Gets or sets the IP address of the target."""
        dotnet_result = self._dotnet_instance.IPAddress
        return _wrap(dotnet_result)

    @ip_address.setter
    def ip_address(self, value: str):
        """Gets or sets the IP address of the target."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IPAddress = next(unwrapped)

    @property
    def username(self) -> str:
        """Gets or sets the username for the target."""
        dotnet_result = self._dotnet_instance.Username
        return _wrap(dotnet_result)

    @username.setter
    def username(self, value: str):
        """Gets or sets the username for the target."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Username = next(unwrapped)

    @property
    def password(self) -> str:
        """Gets or sets the password for the target."""
        dotnet_result = self._dotnet_instance.Password
        return _wrap(dotnet_result)

    @password.setter
    def password(self, value: str):
        """Gets or sets the password for the target."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Password = next(unwrapped)

    @property
    def fpga_scan_interface_mode(self) -> int:
        """Gets or sets the interface mode for the NI Scan Engine on RT targets. You can use this property to override the current settings of the NI Scan Engine, which can be useful for certain C Series modules, such as NI 986x series devices. <format type="bold">(Windows)</format> This setting has no effect on Windows targets."""
        dotnet_result = self._dotnet_instance.FPGAScanInterfaceMode
        return _wrap(dotnet_result)

    @fpga_scan_interface_mode.setter
    def fpga_scan_interface_mode(self, value: int):
        """Gets or sets the interface mode for the NI Scan Engine on RT targets. You can use this property to override the current settings of the NI Scan Engine, which can be useful for certain C Series modules, such as NI 986x series devices. <format type="bold">(Windows)</format> This setting has no effect on Windows targets."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FPGAScanInterfaceMode = next(unwrapped)

    @property
    def target_timing_mode(self) -> TargetTimingMode:
        """Gets or sets the timing mode for the target.  When an FPGA serves as the Primary Control Loop timing source, the mode affects certain performance characteristics of the system."""
        dotnet_result = self._dotnet_instance.TargetTimingMode
        return _wrap(dotnet_result)

    @target_timing_mode.setter
    def target_timing_mode(self, value: TargetTimingMode):
        """Gets or sets the timing mode for the target.  When an FPGA serves as the Primary Control Loop timing source, the mode affects certain performance characteristics of the system."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TargetTimingMode = next(unwrapped)

    @property
    def primary_control_loop_processor(self) -> int:
        """Gets or sets the processor on which to execute the Primary Control Loop (PCL)."""
        dotnet_result = self._dotnet_instance.PrimaryControlLoopProcessor
        return _wrap(dotnet_result)

    @primary_control_loop_processor.setter
    def primary_control_loop_processor(self, value: int):
        """Gets or sets the processor on which to execute the Primary Control Loop (PCL)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PrimaryControlLoopProcessor = next(unwrapped)

    @property
    def data_processing_loop_processor(self) -> int:
        """Gets or sets the processor on which to execute the Data Processing Loop. -2 is any available processor. If you specify an invalid processor, the loop executes on the first available processor."""
        dotnet_result = self._dotnet_instance.DataProcessingLoopProcessor
        return _wrap(dotnet_result)

    @data_processing_loop_processor.setter
    def data_processing_loop_processor(self, value: int):
        """Gets or sets the processor on which to execute the Data Processing Loop. -2 is any available processor. If you specify an invalid processor, the loop executes on the first available processor."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DataProcessingLoopProcessor = next(unwrapped)

    @property
    def data_processing_loop_decimation(self) -> int:
        """Gets or sets the execution rate of the Data Processing Loop (DPL). A value of 1 specifies that the DPL reads values on every iteration of the Primary Control Loop (PCL). You can specify a value higher than 1 to read PCL values less frequently and increase system execution."""
        dotnet_result = self._dotnet_instance.DataProcessingLoopDecimation
        return _wrap(dotnet_result)

    @data_processing_loop_decimation.setter
    def data_processing_loop_decimation(self, value: int):
        """Gets or sets the execution rate of the Data Processing Loop (DPL). A value of 1 specifies that the DPL reads values on every iteration of the Primary Control Loop (PCL). You can specify a value higher than 1 to read PCL values less frequently and increase system execution."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DataProcessingLoopDecimation = next(unwrapped)

    @property
    def maximum_streamed_channels(self) -> int:
        """Gets or sets the maximum number of channels that the VeriStand Engine can stream to the host."""
        dotnet_result = self._dotnet_instance.MaximumStreamedChannels
        return _wrap(dotnet_result)

    @maximum_streamed_channels.setter
    def maximum_streamed_channels(self, value: int):
        """Gets or sets the maximum number of channels that the VeriStand Engine can stream to the host."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.MaximumStreamedChannels = next(unwrapped)

    @property
    def filter_daq_errors(self) -> bool:
        """Gets or sets whether to filter errors from NI-DAQmx function calls. Set this property to <see langword="true" /> if you do not want the system to shut down when an NI-DAQ device reports an error."""
        dotnet_result = self._dotnet_instance.FilterDAQErrors
        return _wrap(dotnet_result)

    @filter_daq_errors.setter
    def filter_daq_errors(self, value: bool):
        """Gets or sets whether to filter errors from NI-DAQmx function calls. Set this property to <see langword="true" /> if you do not want the system to shut down when an NI-DAQ device reports an error."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FilterDAQErrors = next(unwrapped)

    @property
    def filter_watchdog_errors(self) -> bool:
        """Gets or sets whether to filter errors reported by the timing watchdog. For example, if you set the Primary Control Loop to execute at a high rate and your system contains large or complex models, the watchdog reports an error if the models cannot execute quickly enough to keep up with the Primary Control Loop. Set this property to <see langword="true" /> if you want NI VeriStand to ignore these errors."""
        dotnet_result = self._dotnet_instance.FilterWatchdogErrors
        return _wrap(dotnet_result)

    @filter_watchdog_errors.setter
    def filter_watchdog_errors(self, value: bool):
        """Gets or sets whether to filter errors reported by the timing watchdog. For example, if you set the Primary Control Loop to execute at a high rate and your system contains large or complex models, the watchdog reports an error if the models cannot execute quickly enough to keep up with the Primary Control Loop. Set this property to <see langword="true" /> if you want NI VeriStand to ignore these errors."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FilterWatchdogErrors = next(unwrapped)

    @property
    def target_rate(self) -> float:
        """Gets or sets the execution rate of the target in hertz."""
        dotnet_result = self._dotnet_instance.TargetRate
        return _wrap(dotnet_result)

    @target_rate.setter
    def target_rate(self, value: float):
        """Gets or sets the execution rate of the target in hertz."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TargetRate = next(unwrapped)

    @property
    def timeout(self) -> float:
        """Gets or sets the amount of time to wait for a start trigger from the DAQ device before timing out. This property is only valid if the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.Timeout
        return _wrap(dotnet_result)

    @timeout.setter
    def timeout(self, value: float):
        """Gets or sets the amount of time to wait for a start trigger from the DAQ device before timing out. This property is only valid if the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Timeout = next(unwrapped)

    @property
    def daq_timeout(self) -> int:
        """Gets the amount of time to wait for a DAQ device to transfer data before timing out. This property is only valid of the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.DAQTimeout
        return _wrap(dotnet_result)

    @property
    def timed_loop_sleep_time(self) -> int:
        """Gets the amount of time in microseconds the Primary Control Loop (PCL) sleeps after each tick. NI VeriStand ignores this value if the master timing device has an external timing source."""
        dotnet_result = self._dotnet_instance.TimedLoopSleepTime
        return _wrap(dotnet_result)

    @property
    def deployment_group(self) -> int:
        """Gets or sets the deployment group to which a target belongs."""
        dotnet_result = self._dotnet_instance.DeploymentGroup
        return _wrap(dotnet_result)

    @deployment_group.setter
    def deployment_group(self, value: int):
        """Gets or sets the deployment group to which a target belongs."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DeploymentGroup = next(unwrapped)

    @property
    def warmup_time_ms(self) -> int:
        """Gets or sets the amount of time the system waits before considering late flags. You can set a warm-up time to give the system time to allocate and manage resources."""
        dotnet_result = self._dotnet_instance.WarmupTime_ms
        return _wrap(dotnet_result)

    @warmup_time_ms.setter
    def warmup_time_ms(self, value: int):
        """Gets or sets the amount of time the system waits before considering late flags. You can set a warm-up time to give the system time to allocate and manage resources."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.WarmupTime_ms = next(unwrapped)

    @property
    def data_rate(self) -> float:
        """Gets or sets the rate for updating channel values in the Send Communication Loop."""
        dotnet_result = self._dotnet_instance.DataRate
        return _wrap(dotnet_result)

    @data_rate.setter
    def data_rate(self, value: float):
        """Gets or sets the rate for updating channel values in the Send Communication Loop."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DataRate = next(unwrapped)

    @overload
    def set_control_loop_timing_source_to_automatic(self) -> bool:
        ...

    def set_control_loop_timing_source_to_automatic(self, *args):
        unwrapped = _unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.SetControlLoopTimingSourceToAutomatic(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_control_loop_timing_source_to_daq(self, daq_device_name: str, daq_timeout: int, timed_loop_sleep_time: int) -> bool:
        ...

    def set_control_loop_timing_source_to_daq(self, *args):
        unwrapped = _unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.SetControlLoopTimingSourceToDAQ(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_control_loop_timing_source_to_custom_device(self, custom_device_name: str) -> bool:
        ...

    def set_control_loop_timing_source_to_custom_device(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.SetControlLoopTimingSourceToCustomDevice(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_system_channels(self) -> SystemChannels:
        ...

    def get_system_channels(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSystemChannels(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_hardware(self) -> Hardware:
        ...

    def get_hardware(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetHardware(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_stimulus(self) -> Stimulus:
        ...

    def get_stimulus(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStimulus(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_simulation_models(self) -> SimulationModels:
        ...

    def get_simulation_models(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSimulationModels(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_alarms(self) -> Alarms:
        ...

    def get_alarms(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAlarms(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_procedures(self) -> Procedures:
        ...

    def get_procedures(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetProcedures(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_custom_devices(self) -> CustomDevices:
        ...

    def get_custom_devices(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCustomDevices(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_user_channels(self) -> UserChannels:
        ...

    def get_user_channels(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetUserChannels(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_calculated_channels(self) -> CalculatedChannels:
        ...

    def get_calculated_channels(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCalculatedChannels(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_xnet_databases(self) -> XNETDatabases:
        ...

    def get_xnet_databases(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetXNETDatabases(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource, "AutomaticTiming")
        return TargetControlLoopTimingSource(dotnet_result, "AUTOMATIC_TIMING")

    @_staticproperty
    def DAQ_TIMING() -> TargetControlLoopTimingSource:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource, "DAQTiming")
        return TargetControlLoopTimingSource(dotnet_result, "DAQ_TIMING")

    @_staticproperty
    def CUSTOM_DEVICE_TIMING() -> TargetControlLoopTimingSource:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource, "CustomDeviceTiming")
        return TargetControlLoopTimingSource(dotnet_result, "CUSTOM_DEVICE_TIMING")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetExecutionMode, "Parallel")
        return TargetExecutionMode(dotnet_result, "PARALLEL")

    @_staticproperty
    def LOW_LATENCY() -> TargetExecutionMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetExecutionMode, "LowLatency")
        return TargetExecutionMode(dotnet_result, "LOW_LATENCY")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetTimingMode, "Auto")
        return TargetTimingMode(dotnet_result, "AUTO")

    @_staticproperty
    def WAIT_ON_INTERRUPT() -> TargetTimingMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetTimingMode, "WaitOnInterrupt")
        return TargetTimingMode(dotnet_result, "WAIT_ON_INTERRUPT")

    @_staticproperty
    def WAIT_ON_DMA_READ() -> TargetTimingMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TargetTimingMode, "WaitOnDmaRead")
        return TargetTimingMode(dotnet_result, "WAIT_ON_DMA_READ")


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTargetList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_target(self, target: Target) -> bool:
        ...

    def add_target(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddTarget(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TaskType, "AnalogInput")
        return TaskType(dotnet_result, "ANALOG_INPUT")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TemperatureUnit, "Celsius")
        return TemperatureUnit(dotnet_result, "CELSIUS")

    @_staticproperty
    def FAHRENHEIT() -> TemperatureUnit:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TemperatureUnit, "Fahrenheit")
        return TemperatureUnit(dotnet_result, "FAHRENHEIT")

    @_staticproperty
    def KELVIN() -> TemperatureUnit:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TemperatureUnit, "Kelvin")
        return TemperatureUnit(dotnet_result, "KELVIN")

    @_staticproperty
    def RANKINE() -> TemperatureUnit:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TemperatureUnit, "Rankine")
        return TemperatureUnit(dotnet_result, "RANKINE")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "ICSensor")
        return ThermocoupleCJCType(dotnet_result, "IC_SENSOR")

    @_staticproperty
    def THERMISTOR() -> ThermocoupleCJCType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "Thermistor")
        return ThermocoupleCJCType(dotnet_result, "THERMISTOR")

    @_staticproperty
    def TEMPERATURE() -> ThermocoupleCJCType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "Temperature")
        return ThermocoupleCJCType(dotnet_result, "TEMPERATURE")

    @_staticproperty
    def NI9211() -> ThermocoupleCJCType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "NI9211")
        return ThermocoupleCJCType(dotnet_result, "NI9211")

    @_staticproperty
    def NI9213() -> ThermocoupleCJCType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "NI9213")
        return ThermocoupleCJCType(dotnet_result, "NI9213")

    @_staticproperty
    def NI9219() -> ThermocoupleCJCType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "NI9219")
        return ThermocoupleCJCType(dotnet_result, "NI9219")

    @_staticproperty
    def NI9214() -> ThermocoupleCJCType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleCJCType, "NI9214")
        return ThermocoupleCJCType(dotnet_result, "NI9214")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "B")
        return ThermocoupleType(dotnet_result, "B")

    @_staticproperty
    def E() -> ThermocoupleType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "E")
        return ThermocoupleType(dotnet_result, "E")

    @_staticproperty
    def J() -> ThermocoupleType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "J")
        return ThermocoupleType(dotnet_result, "J")

    @_staticproperty
    def K() -> ThermocoupleType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "K")
        return ThermocoupleType(dotnet_result, "K")

    @_staticproperty
    def R() -> ThermocoupleType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "R")
        return ThermocoupleType(dotnet_result, "R")

    @_staticproperty
    def S() -> ThermocoupleType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "S")
        return ThermocoupleType(dotnet_result, "S")

    @_staticproperty
    def T() -> ThermocoupleType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "T")
        return ThermocoupleType(dotnet_result, "T")

    @_staticproperty
    def N() -> ThermocoupleType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleType, "N")
        return ThermocoupleType(dotnet_result, "N")


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTimingAndSyncDeviceList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_timing_and_sync_device(self, timing_and_sync_device: TimingAndSyncDevice) -> bool:
        ...

    def add_timing_and_sync_device(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddTimingAndSyncDevice(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TimingSourceSettingsOptions, "ControlLoopFromTask")
        return TimingSourceSettingsOptions(dotnet_result, "CONTROL_LOOP_FROM_TASK")

    @_staticproperty
    def SIGNAL_FROM_TASK__SAMPLE_COMPLETE() -> TimingSourceSettingsOptions:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TimingSourceSettingsOptions, "SignalFromTask_SampleComplete")
        return TimingSourceSettingsOptions(dotnet_result, "SIGNAL_FROM_TASK__SAMPLE_COMPLETE")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TriggerType, "None")
        return TriggerType(dotnet_result, "NONE")

    @_staticproperty
    def ANALOG_EDGE() -> TriggerType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TriggerType, "AnalogEdge")
        return TriggerType(dotnet_result, "ANALOG_EDGE")

    @_staticproperty
    def ANALOG_WINDOW() -> TriggerType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TriggerType, "AnalogWindow")
        return TriggerType(dotnet_result, "ANALOG_WINDOW")

    @_staticproperty
    def DIGITAL_EDGE() -> TriggerType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TriggerType, "DigitalEdge")
        return TriggerType(dotnet_result, "DIGITAL_EDGE")

    @_staticproperty
    def SOFTWARE() -> TriggerType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.TriggerType, "Software")
        return TriggerType(dotnet_result, "SOFTWARE")


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSignalBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetRawDataBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddSignalBasedFrame(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddRawDataBasedFrame(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetUserChannelList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_user_channel_folder_list(self) -> Sequence[UserChannelsFolder]:
        ...

    @overload
    def get_user_channel_folder_list(self, deep: bool) -> Sequence[UserChannelsFolder]:
        ...

    def get_user_channel_folder_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetUserChannelFolderList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_user_channel(self, channel: UserChannel) -> bool:
        ...

    def add_user_channel(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddUserChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_user_channels_folder(self, folder: UserChannelsFolder) -> bool:
        ...

    def add_user_channels_folder(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddUserChannelsFolder(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_user_channel(self, name: str, description: str, units: str, default_value: float) -> UserChannel:
        ...

    def add_new_user_channel(self, *args):
        unwrapped = _unwrap({None: (4, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewUserChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_user_channels_folder(self, name: str, description: str) -> UserChannelsFolder:
        ...

    def add_new_user_channels_folder(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewUserChannelsFolder(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.UserChannelsFolder(*unwrapped)

    @overload
    def get_user_channel_list(self) -> Sequence[UserChannel]:
        ...

    @overload
    def get_user_channel_list(self, deep: bool) -> Sequence[UserChannel]:
        ...

    def get_user_channel_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetUserChannelList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_user_channel_folder_list(self) -> Sequence[UserChannelsFolder]:
        ...

    @overload
    def get_user_channel_folder_list(self, deep: bool) -> Sequence[UserChannelsFolder]:
        ...

    def get_user_channel_folder_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetUserChannelFolderList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_user_channel(self, channel: UserChannel) -> bool:
        ...

    def add_user_channel(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddUserChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_user_channels_folder(self, folder: UserChannelsFolder) -> bool:
        ...

    def add_user_channels_folder(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddUserChannelsFolder(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_user_channel(self, name: str, description: str, units: str, default_value: float) -> UserChannel:
        ...

    def add_new_user_channel(self, *args):
        unwrapped = _unwrap({None: (4, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewUserChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_user_channels_folder(self, name: str, description: str) -> UserChannelsFolder:
        ...

    def add_new_user_channels_folder(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewUserChannelsFolder(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities(*unwrapped)

    @_staticproperty
    def current_version() -> VersionType:
        """Gets the current version information for the system definition file."""
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.CurrentVersion
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def serialize_slsc(filepath: str, node: BaseNodeType):
        ...

    def serialize_slsc(*args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.SerializeSLSC(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def deserialize_slsc(filepath: str, base_node: BaseNodeType):
        ...

    def deserialize_slsc(*args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.DeserializeSLSC(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def reset_all_identifiers(base_node_type: BaseNodeType):
        ...

    def reset_all_identifiers(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.ResetAllIdentifiers(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def date_time_to_double(date_time: System.DateTime) -> float:
        ...

    def date_time_to_double(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.DateTimeToDouble(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def double_to_date_time(total_seconds: float) -> System.DateTime:
        ...

    def double_to_date_time(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.DoubleToDateTime(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def version_type_to_version(versiontype: VersionType) -> Tuple[int, int, int, int]:
        ...

    def version_type_to_version(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.VersionTypeToVersion(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def get_localized_name_by_guid(guid: str) -> str:
        ...

    def get_localized_name_by_guid(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.GetLocalizedNameByGUID(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def resolve_path_type(root_path: str, file_path: str) -> DependentFileType:
        ...

    def resolve_path_type(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.ResolvePathType(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def strip_path(path: str) -> Tuple[str, str]:
        ...

    def strip_path(*args):
        unwrapped = _unwrap({None: (1, "")}, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.StripPath(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def get_filename(path: str) -> str:
        ...

    def get_filename(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.GetFilename(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def build_path(path: str, relative: str) -> str:
        ...

    def build_path(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.BuildPath(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def rt_main_path() -> str:
        ...

    def rt_main_path(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.RtMainPath(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def data_replay_rt_path() -> str:
        ...

    def data_replay_rt_path(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.DataReplayRTPath(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def relative_afp_ini_path() -> str:
        ...

    def relative_afp_ini_path(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.RelativeAfpIniPath(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def afp_rt_path() -> str:
        ...

    def afp_rt_path(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.AfpRtPath(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def path_type_pair_to_absolute_path(path: str, type: PathType) -> str:
        ...

    @staticmethod
    @overload
    def path_type_pair_to_absolute_path(path: str, type: DependentFilePropertyType, base_path: str) -> str:
        ...

    def path_type_pair_to_absolute_path(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.PathTypePairToAbsolutePath(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def strip_path_if_in_llb(file_path: str) -> str:
        ...

    def strip_path_if_in_llb(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.StripPathIfInLLB(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def add_mapping(source: Channel, destination: Channel):
        ...

    def add_mapping(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.AddMapping(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def clear_mapping(destination: Channel):
        ...

    def clear_mapping(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.ClearMapping(*unwrapped)
        return _wrap(dotnet_result)

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
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.AutoMapChannels(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def default_auto_map_recursion_filter(node: BaseNode) -> bool:
        ...

    def default_auto_map_recursion_filter(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.DefaultAutoMapRecursionFilter(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def find_name_matches(source_channels: Iterable[IChannel], destination_channels: Iterable[IChannel], comparer: System.IEqualityComparer) -> Iterable[System.Collections.Generic.KeyValuePair[NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel,NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel]]:
        ...

    def find_name_matches(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.FindNameMatches(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def create_base_node_from_system_storage_node(storage_node: BaseNodeType) -> BaseNode:
        ...

    def create_base_node_from_system_storage_node(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Utilities.CreateBaseNodeFromSystemStorageNode(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ValueSource(*unwrapped)

    @property
    def is_constant(self) -> bool:
        dotnet_result = self._dotnet_instance.isConstant
        return _wrap(dotnet_result)

    @property
    def channel(self) -> BaseNode:
        dotnet_result = self._dotnet_instance.Channel
        return _wrap(dotnet_result)

    @property
    def constant(self) -> float:
        dotnet_result = self._dotnet_instance.Constant
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.Units
        return _wrap(dotnet_result)

    @units.setter
    def units(self, value: str):
        """Gets or sets the units associated with the waveform. This can be any arbitrary string."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Units = next(unwrapped)

    @property
    def data_type(self) -> WaveformTypeDataType:
        """Gets or sets the data type associated with the waveform."""
        dotnet_result = self._dotnet_instance.DataType
        return _wrap(dotnet_result)

    @data_type.setter
    def data_type(self, value: WaveformTypeDataType):
        """Gets or sets the data type associated with the waveform."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DataType = next(unwrapped)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.WindowConditionType, "EnteringWindow")
        return WindowConditionType(dotnet_result, "ENTERING_WINDOW")

    @_staticproperty
    def LEAVING_WINDOW() -> WindowConditionType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.WindowConditionType, "LeavingWindow")
        return WindowConditionType(dotnet_result, "LEAVING_WINDOW")


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
        dotnet_result = self._dotnet_instance.Decimation
        return _wrap(dotnet_result)

    @decimation.setter
    def decimation(self, value: int):
        """Gets or sets the processing rate for inline incoming and outgoing frames of an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> device, which NI VeriStand uses to calculate the decimation factor (decimation factor = Primary Control Loop rate/processing rate). This value determines how many iterations of the Primary Control Loop occur between calls to the device."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Decimation = next(unwrapped)

    @overload
    def enable_xnet(self):
        ...

    def enable_xnet(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.EnableXNET(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def disable_xnet(self):
        ...

    def disable_xnet(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DisableXNET(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_can(self) -> CAN:
        ...

    def get_can(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCAN(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_flex_ray(self) -> FlexRay:
        ...

    def get_flex_ray(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFlexRay(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_lin(self) -> LIN:
        ...

    def get_lin(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLIN(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDatabaseList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_database(self, database: Database) -> bool:
        ...

    def add_database(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddDatabase(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination, "Off")
        return XNETTermination(dotnet_result, "OFF")

    @_staticproperty
    def ON() -> XNETTermination:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination, "On")
        return XNETTermination(dotnet_result, "ON")


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm(*unwrapped)

    @property
    def mode(self) -> AlarmMode:
        """Gets or sets the mode of the alarm (<format type="monospace">Normal</format> or <format type="monospace">IndicateOnly</format>)."""
        dotnet_result = self._dotnet_instance.Mode
        return _wrap(dotnet_result)

    @mode.setter
    def mode(self, value: AlarmMode):
        """Gets or sets the mode of the alarm (<format type="monospace">Normal</format> or <format type="monospace">IndicateOnly</format>)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Mode = next(unwrapped)

    @property
    def priority_number(self) -> int:
        """Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31."""
        dotnet_result = self._dotnet_instance.PriorityNumber
        return _wrap(dotnet_result)

    @priority_number.setter
    def priority_number(self, value: int):
        """Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PriorityNumber = next(unwrapped)

    @property
    def group_number(self) -> int:
        """Gets or sets the number of the group to which an alarm belongs."""
        dotnet_result = self._dotnet_instance.GroupNumber
        return _wrap(dotnet_result)

    @group_number.setter
    def group_number(self, value: int):
        """Gets or sets the number of the group to which an alarm belongs."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.GroupNumber = next(unwrapped)

    @property
    def priority(self) -> AlarmPriority:
        """This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>"""
        dotnet_result = self._dotnet_instance.Priority
        return _wrap(dotnet_result)

    @priority.setter
    def priority(self, value: AlarmPriority):
        """This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Priority = next(unwrapped)

    @property
    def default_state(self) -> AlarmState:
        """Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm."""
        dotnet_result = self._dotnet_instance.DefaultState
        return _wrap(dotnet_result)

    @default_state.setter
    def default_state(self, value: AlarmState):
        """Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DefaultState = next(unwrapped)

    @property
    def auto_reset_alarm(self) -> bool:
        """Gets or sets the reset behavior of the alarm. This property defines whether the alarm automatically resets when the channel is back in range, as opposed to being reset by a procedure."""
        dotnet_result = self._dotnet_instance.AutoResetAlarm
        return _wrap(dotnet_result)

    @auto_reset_alarm.setter
    def auto_reset_alarm(self, value: bool):
        """Gets or sets the reset behavior of the alarm. This property defines whether the alarm automatically resets when the channel is back in range, as opposed to being reset by a procedure."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AutoResetAlarm = next(unwrapped)

    @property
    def require_alarm_acknowledgement(self) -> bool:
        """Gets or sets the acknowledgement behavior of the alarm. This property defines whether the alarm must be manually acknowledged before it can reset. Otherwise, alarm is automatically acknowledged when the channel is back in range."""
        dotnet_result = self._dotnet_instance.RequireAlarmAcknowledgement
        return _wrap(dotnet_result)

    @require_alarm_acknowledgement.setter
    def require_alarm_acknowledgement(self, value: bool):
        """Gets or sets the acknowledgement behavior of the alarm. This property defines whether the alarm must be manually acknowledged before it can reset. Otherwise, alarm is automatically acknowledged when the channel is back in range."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.RequireAlarmAcknowledgement = next(unwrapped)

    @property
    def delay(self) -> float:
        """Gets or sets the amount of time to wait before triggering the alarm."""
        dotnet_result = self._dotnet_instance.Delay
        return _wrap(dotnet_result)

    @delay.setter
    def delay(self, value: float):
        """Gets or sets the amount of time to wait before triggering the alarm."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Delay = next(unwrapped)

    @property
    def alarm_source(self) -> BaseNode:
        """Gets or sets the channel to monitor for alarm conditions."""
        dotnet_result = self._dotnet_instance.AlarmSource
        return _wrap(dotnet_result)

    @alarm_source.setter
    def alarm_source(self, value: BaseNode):
        """Gets or sets the channel to monitor for alarm conditions."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AlarmSource = next(unwrapped)

    @property
    def upper_limit_is_constant(self) -> int:
        """Gets whether the upper limit value of the alarm is specified by a constant or a channel."""
        dotnet_result = self._dotnet_instance.UpperLimitIsConstant
        return _wrap(dotnet_result)

    @property
    def upper_limit_constant(self) -> float:
        """Gets the constant that determines the upper limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered."""
        dotnet_result = self._dotnet_instance.UpperLimitConstant
        return _wrap(dotnet_result)

    @property
    def lower_limit_is_constant(self) -> int:
        """Gets whether the lower limit value of the alarm is specified by a constant or a channel."""
        dotnet_result = self._dotnet_instance.LowerLimitIsConstant
        return _wrap(dotnet_result)

    @property
    def lower_limit_constant(self) -> float:
        """Gets the constant value that determines the lower limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered."""
        dotnet_result = self._dotnet_instance.LowerLimitConstant
        return _wrap(dotnet_result)

    @property
    def upper_limit_channel(self) -> BaseNode:
        """Gets the channel that determines the upper limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered."""
        dotnet_result = self._dotnet_instance.UpperLimitChannel
        return _wrap(dotnet_result)

    @property
    def lower_limit_channel(self) -> BaseNode:
        """Gets the channel that determines the lower limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered."""
        dotnet_result = self._dotnet_instance.LowerLimitChannel
        return _wrap(dotnet_result)

    @property
    def alarm_action(self) -> BaseNode:
        """Gets or sets the procedure to initiate when the alarm conditions are met."""
        dotnet_result = self._dotnet_instance.AlarmAction
        return _wrap(dotnet_result)

    @alarm_action.setter
    def alarm_action(self, value: BaseNode):
        """Gets or sets the procedure to initiate when the alarm conditions are met."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AlarmAction = next(unwrapped)

    @property
    def trip_message(self) -> str:
        """Gets or sets the message to display when the alarm is tripped."""
        dotnet_result = self._dotnet_instance.TripMessage
        return _wrap(dotnet_result)

    @trip_message.setter
    def trip_message(self, value: str):
        """Gets or sets the message to display when the alarm is tripped."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TripMessage = next(unwrapped)

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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetUpperLimit(*unwrapped)
        return _wrap(dotnet_result)

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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetLowerLimit(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_alarm_status_channel(self) -> bool:
        ...

    def add_alarm_status_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddAlarmStatusChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_alarm_status_channel(self) -> AlarmStatus:
        ...

    def get_alarm_status_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAlarmStatusChannel(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmFolder(*unwrapped)

    @overload
    def get_alarm_list(self) -> Sequence[Alarm]:
        ...

    @overload
    def get_alarm_list(self, deep: bool) -> Sequence[Alarm]:
        ...

    def get_alarm_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAlarmList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_alarm_folder_list(self) -> Sequence[AlarmFolder]:
        ...

    @overload
    def get_alarm_folder_list(self, deep: bool) -> Sequence[AlarmFolder]:
        ...

    def get_alarm_folder_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAlarmFolderList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_alarm(self, alarm: Alarm) -> bool:
        ...

    def add_alarm(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAlarm(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_alarm_folder(self, folder: AlarmFolder) -> bool:
        ...

    def add_alarm_folder(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAlarmFolder(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: ValueSource, lower_limit: ValueSource, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, group_number: int, priority_number: int, delay: float, trip_message: str) -> Alarm:
        ...

    def add_new_alarm(self, *args):
        unwrapped = _unwrap({None: (12, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewAlarm(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_alarm_folder(self, name: str, description: str) -> AlarmFolder:
        ...

    def add_new_alarm_folder(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewAlarmFolder(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAlarmList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_alarm_folder_list(self) -> Sequence[AlarmFolder]:
        ...

    @overload
    def get_alarm_folder_list(self, deep: bool) -> Sequence[AlarmFolder]:
        ...

    def get_alarm_folder_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAlarmFolderList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_alarm(self, alarm: Alarm) -> bool:
        ...

    def add_alarm(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAlarm(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_alarm_folder(self, folder: AlarmFolder) -> bool:
        ...

    def add_alarm_folder(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAlarmFolder(*unwrapped)
        return _wrap(dotnet_result)

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
        unwrapped = _unwrap({(str, str, Channel, (float, int), (float, int), Procedure, AlarmMode, AlarmState, AlarmPriority, (float, int), str): (11, NationalInstruments.VeriStand.Error.NoError), (str, str, Channel, (float, int), BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, (float, int), str): (11, NationalInstruments.VeriStand.Error.NoError), (str, str, Channel, BaseNode, (float, int), Procedure, AlarmMode, AlarmState, AlarmPriority, (float, int), str): (11, NationalInstruments.VeriStand.Error.NoError), (str, str, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, (float, int), str): (11, NationalInstruments.VeriStand.Error.NoError), (str, str, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, int, int, (float, int), str): (12, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewAlarm(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_alarm_folder(self, name: str, description: str) -> AlarmFolder:
        ...

    def add_new_alarm_folder(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewAlarmFolder(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Alias(*unwrapped)

    @property
    def linked_channel(self) -> BaseNode:
        """Gets or sets the channel that the alias represents."""
        dotnet_result = self._dotnet_instance.LinkedChannel
        return _wrap(dotnet_result)

    @linked_channel.setter
    def linked_channel(self, value: BaseNode):
        """Gets or sets the channel that the alias represents."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LinkedChannel = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.AliasFolder(*unwrapped)

    @overload
    def get_aliases_list(self) -> Sequence[Alias]:
        ...

    @overload
    def get_aliases_list(self, deep: bool) -> Sequence[Alias]:
        ...

    def get_aliases_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAliasesList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_alias_folder_list(self) -> Sequence[AliasFolder]:
        ...

    @overload
    def get_alias_folder_list(self, deep: bool) -> Sequence[AliasFolder]:
        ...

    def get_alias_folder_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAliasFolderList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_alias(self, alias: Alias) -> bool:
        ...

    def add_alias(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAlias(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_alias_folder(self, folder: AliasFolder) -> bool:
        ...

    def add_alias_folder(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAliasFolder(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_alias_by_path(self, name: str, description: str, linked_channel_path: str) -> Alias:
        ...

    def add_new_alias_by_path(self, *args):
        unwrapped = _unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewAliasByPath(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_alias_by_reference(self, name: str, description: str, linked_channel_reference: Channel) -> Alias:
        ...

    def add_new_alias_by_reference(self, *args):
        unwrapped = _unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewAliasByReference(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_alias_folder(self, name: str, description: str) -> AliasFolder:
        ...

    def add_new_alias_folder(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewAliasFolder(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DeleteUnmappedAliases(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def import_aliases_from_file(self, file_path: str, inclusion_filter: Callable[[str], bool]):
        ...

    def import_aliases_from_file(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ImportAliasesFromFile(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def export_aliases_to_file(self, file_path: str, inclusion_filter: Callable[[IChannel], bool], recurse_predicate: Callable[[BaseNode], bool]):
        ...

    def export_aliases_to_file(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ExportAliasesToFile(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_aliases_list(self) -> Sequence[Alias]:
        ...

    @overload
    def get_aliases_list(self, deep: bool) -> Sequence[Alias]:
        ...

    def get_aliases_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAliasesList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_alias_folder_list(self) -> Sequence[AliasFolder]:
        ...

    @overload
    def get_alias_folder_list(self, deep: bool) -> Sequence[AliasFolder]:
        ...

    def get_alias_folder_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAliasFolderList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_alias(self, alias: Alias) -> bool:
        ...

    def add_alias(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAlias(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_alias_folder(self, folder: AliasFolder) -> bool:
        ...

    def add_alias_folder(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAliasFolder(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_alias_by_path(self, name: str, description: str, linked_channel_path: str) -> Alias:
        ...

    def add_new_alias_by_path(self, *args):
        unwrapped = _unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewAliasByPath(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_alias_by_reference(self, name: str, description: str, linked_channel_reference: Channel) -> Alias:
        ...

    def add_new_alias_by_reference(self, *args):
        unwrapped = _unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewAliasByReference(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_alias_folder(self, name: str, description: str) -> AliasFolder:
        ...

    def add_new_alias_folder(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewAliasFolder(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCRC(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_counter(self) -> Counter:
        ...

    def get_counter(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCounter(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCANPortList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_can_port(self, can_port: CANPort) -> bool:
        ...

    def add_can_port(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddCANPort(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCommunicationStateChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_fault_channel(self) -> Channel:
        ...

    def get_fault_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFaultChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_last_error_channel(self) -> Channel:
        ...

    def get_last_error_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLastErrorChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_last_error_timestamp_channel(self) -> Channel:
        ...

    def get_last_error_timestamp_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLastErrorTimestampChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_receive_error_counter_channel(self) -> Channel:
        ...

    def get_receive_error_counter_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetReceiveErrorCounterChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_sleep_mode_channel(self) -> SleepMode:
        ...

    def get_sleep_mode_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSleepModeChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_transceiver_error_channel(self) -> Channel:
        ...

    def get_transceiver_error_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTransceiverErrorChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_transmit_error_counter_channel(self) -> Channel:
        ...

    def get_transmit_error_counter_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTransmitErrorCounterChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_sleep_mode_channel(self, sleep_mode: SleepMode) -> bool:
        ...

    def add_sleep_mode_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddSleepModeChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_communication_state_channel(self) -> Channel:
        ...

    def create_communication_state_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateCommunicationStateChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_fault_channel(self) -> Channel:
        ...

    def create_fault_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateFaultChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_last_error_channel(self) -> Channel:
        ...

    def create_last_error_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateLastErrorChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_last_error_timestamp_channel(self) -> Channel:
        ...

    def create_last_error_timestamp_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateLastErrorTimestampChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_receive_error_counter_channel(self) -> Channel:
        ...

    def create_receive_error_counter_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateReceiveErrorCounterChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_transceiver_error_channel(self) -> Channel:
        ...

    def create_transceiver_error_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateTransceiverErrorChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_transmit_error_counter_channel(self) -> Channel:
        ...

    def create_transmit_error_counter_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateTransmitErrorCounterChannel(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort(*unwrapped)

    @property
    def port_number(self) -> int:
        """Gets or sets the physical address of the CAN port."""
        dotnet_result = self._dotnet_instance.PortNumber
        return _wrap(dotnet_result)

    @port_number.setter
    def port_number(self, value: int):
        """Gets or sets the physical address of the CAN port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PortNumber = next(unwrapped)

    @property
    def linked_database(self) -> BaseNode:
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.LinkedDatabase
        return _wrap(dotnet_result)

    @linked_database.setter
    def linked_database(self, value: BaseNode):
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LinkedDatabase = next(unwrapped)

    @property
    def baud_rate_bitfield(self) -> int:
        """Gets or sets the baud rate bitfield of the CAN port."""
        dotnet_result = self._dotnet_instance.BaudRateBitfield
        return _wrap(dotnet_result)

    @baud_rate_bitfield.setter
    def baud_rate_bitfield(self, value: int):
        """Gets or sets the baud rate bitfield of the CAN port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BaudRateBitfield = next(unwrapped)

    @property
    def baud_rate(self) -> int:
        """Gets or sets the baud rate of the CAN port."""
        dotnet_result = self._dotnet_instance.BaudRate
        return _wrap(dotnet_result)

    @baud_rate.setter
    def baud_rate(self, value: int):
        """Gets or sets the baud rate of the CAN port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BaudRate = next(unwrapped)

    @property
    def fd_baud_rate_bitfield(self) -> int:
        """Gets or sets the FD baud rate bitfield of the CAN port."""
        dotnet_result = self._dotnet_instance.FDBaudRateBitfield
        return _wrap(dotnet_result)

    @fd_baud_rate_bitfield.setter
    def fd_baud_rate_bitfield(self, value: int):
        """Gets or sets the FD baud rate bitfield of the CAN port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FDBaudRateBitfield = next(unwrapped)

    @property
    def fd_baud_rate(self) -> int:
        """Gets or sets the FD baud rate of the CAN port."""
        dotnet_result = self._dotnet_instance.FDBaudRate
        return _wrap(dotnet_result)

    @fd_baud_rate.setter
    def fd_baud_rate(self, value: int):
        """Gets or sets the FD baud rate of the CAN port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FDBaudRate = next(unwrapped)

    @property
    def fdiso_mode(self) -> FDISOMode:
        """Gets or sets the FD ISO mode of the CAN port."""
        dotnet_result = self._dotnet_instance.FDISOMode
        return _wrap(dotnet_result)

    @fdiso_mode.setter
    def fdiso_mode(self, value: FDISOMode):
        """Gets or sets the FD ISO mode of the CAN port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FDISOMode = next(unwrapped)

    @property
    def cluster_name(self) -> str:
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.ClusterName
        return _wrap(dotnet_result)

    @cluster_name.setter
    def cluster_name(self, value: str):
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ClusterName = next(unwrapped)

    @property
    def incoming_rate(self) -> int:
        """Gets or sets the processing rate for incoming frames in hertz."""
        dotnet_result = self._dotnet_instance.IncomingRate
        return _wrap(dotnet_result)

    @incoming_rate.setter
    def incoming_rate(self, value: int):
        """Gets or sets the processing rate for incoming frames in hertz."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IncomingRate = next(unwrapped)

    @property
    def outgoing_rate(self) -> int:
        """Gets or sets the processing rate for outgoing frames in hertz."""
        dotnet_result = self._dotnet_instance.OutgoingRate
        return _wrap(dotnet_result)

    @outgoing_rate.setter
    def outgoing_rate(self, value: int):
        """Gets or sets the processing rate for outgoing frames in hertz."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.OutgoingRate = next(unwrapped)

    @property
    def echo(self) -> bool:
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        dotnet_result = self._dotnet_instance.Echo
        return _wrap(dotnet_result)

    @echo.setter
    def echo(self, value: bool):
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Echo = next(unwrapped)

    @property
    def input_stream_queue_size(self) -> int:
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        dotnet_result = self._dotnet_instance.InputStreamQueueSize
        return _wrap(dotnet_result)

    @input_stream_queue_size.setter
    def input_stream_queue_size(self, value: int):
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InputStreamQueueSize = next(unwrapped)

    @property
    def can_bus_off(self) -> bool:
        """Gets or sets whether the CAN bus is recovered if it switches off due to a physical fault on the bus."""
        dotnet_result = self._dotnet_instance.CANBusOff
        return _wrap(dotnet_result)

    @can_bus_off.setter
    def can_bus_off(self, value: bool):
        """Gets or sets whether the CAN bus is recovered if it switches off due to a physical fault on the bus."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.CANBusOff = next(unwrapped)

    @property
    def can_bus_off_rate(self) -> int:
        """Gets or sets the bit rate at which to check the state of the CAN bus (active or off)."""
        dotnet_result = self._dotnet_instance.CANBusOffRate
        return _wrap(dotnet_result)

    @can_bus_off_rate.setter
    def can_bus_off_rate(self, value: int):
        """Gets or sets the bit rate at which to check the state of the CAN bus (active or off)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.CANBusOffRate = next(unwrapped)

    @property
    def afpini_file(self) -> str:
        """Gets the name of the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort.AFPBinaryFile" crefType="Unqualified" /> used for automatic frame processing."""
        dotnet_result = self._dotnet_instance.AFPINIFile
        return _wrap(dotnet_result)

    @property
    def afp_binary_file(self) -> DependentFile:
        """Gets the binary (<format type="monospace">.ini</format>) file used for automatic frame processing."""
        dotnet_result = self._dotnet_instance.AFPBinaryFile
        return _wrap(dotnet_result)

    @property
    def afp_global_data(self) -> Sequence[int]:
        """Gets the global data used for automatic frame processing."""
        dotnet_result = self._dotnet_instance.AFPGlobalData
        return _wrap(dotnet_result)

    @property
    def inline_incoming(self) -> bool:
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        dotnet_result = self._dotnet_instance.InlineIncoming
        return _wrap(dotnet_result)

    @inline_incoming.setter
    def inline_incoming(self, value: bool):
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InlineIncoming = next(unwrapped)

    @property
    def inline_outgoing(self) -> bool:
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        dotnet_result = self._dotnet_instance.InlineOutgoing
        return _wrap(dotnet_result)

    @inline_outgoing.setter
    def inline_outgoing(self, value: bool):
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InlineOutgoing = next(unwrapped)

    @property
    def disabled(self) -> bool:
        """Gets or sets whether the port is disabled."""
        dotnet_result = self._dotnet_instance.Disabled
        return _wrap(dotnet_result)

    @disabled.setter
    def disabled(self, value: bool):
        """Gets or sets whether the port is disabled."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Disabled = next(unwrapped)

    @property
    def termination(self) -> XNETTermination:
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.Termination
        return _wrap(dotnet_result)

    @termination.setter
    def termination(self, value: XNETTermination):
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Termination = next(unwrapped)

    @property
    def transceiver_type(self) -> CANTransceiverType:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType" crefType="Unqualified" /> for the port. Transceivers can be high-speed (<format type="monospace">HS</format>), low-speed (<format type="monospace">LS</format>), or single wire (<format type="monospace">SW</format>)."""
        dotnet_result = self._dotnet_instance.TransceiverType
        return _wrap(dotnet_result)

    @transceiver_type.setter
    def transceiver_type(self, value: CANTransceiverType):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType" crefType="Unqualified" /> for the port. Transceivers can be high-speed (<format type="monospace">HS</format>), low-speed (<format type="monospace">LS</format>), or single wire (<format type="monospace">SW</format>)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TransceiverType = next(unwrapped)

    @property
    def transmit_order_type(self) -> CANTransmitOrderType:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransmitOrderType" crefType="Unqualified" /> for the port. You can transmit frames to the CAN bus <format type="monospace">AsSubmitted</format> or <format type="monospace">ByIdentifier</format>."""
        dotnet_result = self._dotnet_instance.TransmitOrderType
        return _wrap(dotnet_result)

    @transmit_order_type.setter
    def transmit_order_type(self, value: CANTransmitOrderType):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransmitOrderType" crefType="Unqualified" /> for the port. You can transmit frames to the CAN bus <format type="monospace">AsSubmitted</format> or <format type="monospace">ByIdentifier</format>."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TransmitOrderType = next(unwrapped)

    @property
    def input_stream_read_time(self) -> float:
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        dotnet_result = self._dotnet_instance.InputStreamReadTime
        return _wrap(dotnet_result)

    @input_stream_read_time.setter
    def input_stream_read_time(self, value: float):
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InputStreamReadTime = next(unwrapped)

    @overload
    def get_incoming(self) -> Incoming:
        ...

    def get_incoming(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetIncoming(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_outgoing(self) -> Outgoing:
        ...

    def get_outgoing(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetOutgoing(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_interface_section(self) -> CANInterfaceChannels:
        ...

    def get_interface_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetInterfaceSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_interface_section(self) -> CANInterfaceChannels:
        ...

    def create_interface_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateInterfaceSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_automatic_frame_processing(self):
        ...

    def remove_automatic_frame_processing(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveAutomaticFrameProcessing(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove986x_support(self):
        ...

    def remove986x_support(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Remove986xSupport(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set986x_support(self, file: DependentFile, rio_port_number: int):
        ...

    def set986x_support(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Set986xSupport(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_automatic_frame_processing(self, ini_file_name: str, binary_file_path: str, global_data: Sequence[int]):
        ...

    def set_automatic_frame_processing(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetAutomaticFrameProcessing(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.MaxAFPLength
        return _wrap(dotnet_result)

    @max_afp_length.setter
    def max_afp_length(self, value: int):
        """Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.MaxAFPLength = next(unwrapped)

    @property
    def index_crc(self) -> int:
        """Gets or sets the index of the CRC within the frame."""
        dotnet_result = self._dotnet_instance.IndexCRC
        return _wrap(dotnet_result)

    @index_crc.setter
    def index_crc(self, value: int):
        """Gets or sets the index of the CRC within the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IndexCRC = next(unwrapped)

    @property
    def afp_data(self) -> Sequence[int]:
        """Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.AFPData
        return _wrap(dotnet_result)

    @afp_data.setter
    def afp_data(self, value: Sequence[int]):
        """Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AFPData = next(unwrapped)

    @property
    def use_alternate_channel(self) -> bool:
        """Gets whether the <format type="italics">AlternateChannel</format> specified by <see cref="M:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC.SetAlternateChannel(NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode)" crefType="Unqualified" /> is used to trigger writing data."""
        dotnet_result = self._dotnet_instance.UseAlternateChannel
        return _wrap(dotnet_result)

    @property
    def alternate_channel(self) -> BaseNode:
        """Gets the channel used to trigger writing data when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC.UseAlternateChannel" crefType="Unqualified" /> is <see langword="true" />."""
        dotnet_result = self._dotnet_instance.AlternateChannel
        return _wrap(dotnet_result)

    @overload
    def remove_alternate_channel(self):
        ...

    def remove_alternate_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveAlternateChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_alternate_channel(self, alternate_channel: BaseNode):
        ...

    def set_alternate_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetAlternateChannel(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannelFolder(*unwrapped)

    @overload
    def get_calculated_channels_list(self) -> Sequence[CalculatedChannel]:
        ...

    @overload
    def get_calculated_channels_list(self, deep: bool) -> Sequence[CalculatedChannel]:
        ...

    def get_calculated_channels_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCalculatedChannelsList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_calculated_channel_folder_list(self) -> Sequence[CalculatedChannelFolder]:
        ...

    @overload
    def get_calculated_channel_folder_list(self, deep: bool) -> Sequence[CalculatedChannelFolder]:
        ...

    def get_calculated_channel_folder_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCalculatedChannelFolderList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_calculated_channel(self, calculated_channel: CalculatedChannel) -> bool:
        ...

    def add_calculated_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddCalculatedChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_calculated_channel_folder(self, folder: CalculatedChannelFolder) -> bool:
        ...

    def add_calculated_channel_folder(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddCalculatedChannelFolder(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.ReorderChannelList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_ordered_channel_list(self) -> Sequence[CalculatedChannel]:
        ...

    def get_ordered_channel_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetOrderedChannelList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_calculated_channel_folder_list(self) -> Sequence[CalculatedChannelFolder]:
        ...

    @overload
    def get_calculated_channel_folder_list(self, deep: bool) -> Sequence[CalculatedChannelFolder]:
        ...

    def get_calculated_channel_folder_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCalculatedChannelFolderList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_calculated_channel_folder(self, folder: CalculatedChannelFolder) -> bool:
        ...

    def add_calculated_channel_folder(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddCalculatedChannelFolder(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_calculated_channel_list(self) -> Sequence[CalculatedChannel]:
        ...

    def get_calculated_channel_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCalculatedChannelList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_calculated_channel(self, calculated_channel: CalculatedChannel) -> bool:
        ...

    def add_calculated_channel(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddCalculatedChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_formula(self, formula: Formula) -> bool:
        ...

    def add_formula(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddFormula(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_maximum(self, maximum: Maximum) -> bool:
        ...

    def add_maximum(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddMaximum(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_minimum(self, minimum: Minimum) -> bool:
        ...

    def add_minimum(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddMinimum(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_lowpass_filter(self, lowpass_filter: LowpassFilter) -> bool:
        ...

    def add_lowpass_filter(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddLowpassFilter(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_peak_and_valley(self, peak_and_valley: PeakAndValley) -> bool:
        ...

    def add_peak_and_valley(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddPeakAndValley(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_acceleration(self, acceleration: Acceleration) -> bool:
        ...

    def add_acceleration(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAcceleration(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_average(self, average: Average) -> bool:
        ...

    def add_average(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAverage(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_conditional(self, conditional: Conditional) -> bool:
        ...

    def add_conditional(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddConditional(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Channel(*unwrapped)

    @_staticproperty
    def k_readable() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Channel.K_READABLE
        return _wrap(dotnet_result)

    @_staticproperty
    def k_writable() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Channel.K_WRITABLE
        return _wrap(dotnet_result)

    @_staticproperty
    def k_faultable() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Channel.K_FAULTABLE
        return _wrap(dotnet_result)

    @_staticproperty
    def k_scalable() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Channel.K_SCALABLE
        return _wrap(dotnet_result)

    @property
    def scale(self) -> Scale:
        """Gets or sets the value of the scale property on the channel."""
        dotnet_result = self._dotnet_instance.Scale
        return _wrap(dotnet_result)

    @scale.setter
    def scale(self, value: Scale):
        """Gets or sets the value of the scale property on the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Scale = next(unwrapped)

    @property
    def bit_fields(self) -> int:
        """Gets a bitfield mask that is set on the channel."""
        dotnet_result = self._dotnet_instance.BitFields
        return _wrap(dotnet_result)

    @property
    def default_value(self) -> Sequence[float]:
        """Gets the default value of the channel."""
        dotnet_result = self._dotnet_instance.DefaultValue
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis(*unwrapped)

    @overload
    def clear_chassis_master_device(self):
        ...

    def clear_chassis_master_device(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ClearChassisMasterDevice(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_chassis_master_to_daq(self, daq_name: str, clk_src: DAQCM_Clock_Source, active_edge: DAQCM_Active_Edge, export_clk: DAQCM_Export_Sample_Clock, export_clk_to_line: DAQCM_Export_Clk_On_Line, trigger_line: DAQCM_Trigger_Line, trigger_slope: DAQCM_Slope, start_trigger: DAQCM_Export_Start_Trigger, start_trigger_line: DAQCM_Export_StartTrigger_On_Line) -> bool:
        ...

    def set_chassis_master_to_daq(self, *args):
        unwrapped = _unwrap({None: (9, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.SetChassisMasterToDAQ(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_chassis_master_to_fpga(self, fpga_name: str) -> bool:
        ...

    def set_chassis_master_to_fpga(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.SetChassisMasterToFPGA(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_chassis_master_to_timing_and_sync(self, timing_and_sync_name: str) -> bool:
        ...

    def set_chassis_master_to_timing_and_sync(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.SetChassisMasterToTimingAndSync(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_timing_and_sync(self) -> TimingAndSync:
        ...

    def get_timing_and_sync(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTimingAndSync(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_daq(self) -> DAQ:
        ...

    def get_daq(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDAQ(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_fpga(self) -> FPGA:
        ...

    def get_fpga(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFPGA(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_xnet(self) -> XNET:
        ...

    def get_xnet(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetXNET(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_data_sharing(self) -> DataSharing:
        ...

    def get_data_sharing(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataSharing(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Condition(*unwrapped)

    @property
    def comparison(self) -> ConditionStepComparison:
        """Gets or sets the condition to use when comparing <format type="italics">Variable</format> and <format type="italics">Value</format>."""
        dotnet_result = self._dotnet_instance.Comparison
        return _wrap(dotnet_result)

    @comparison.setter
    def comparison(self, value: ConditionStepComparison):
        """Gets or sets the condition to use when comparing <format type="italics">Variable</format> and <format type="italics">Value</format>."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Comparison = next(unwrapped)

    @property
    def value_constant(self) -> float:
        """Gets the constant value that is compared to <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Condition.Variable" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.ValueConstant
        return _wrap(dotnet_result)

    @property
    def value_is_constant(self) -> bool:
        """Gets whether the value compared to <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Condition.Variable" crefType="Unqualified" /> is determined by a channel or by a constant."""
        dotnet_result = self._dotnet_instance.ValueIsConstant
        return _wrap(dotnet_result)

    @property
    def goto_label(self) -> BaseNode:
        """Gets or sets the procedure step to go to if the condition is met."""
        dotnet_result = self._dotnet_instance.GotoLabel
        return _wrap(dotnet_result)

    @goto_label.setter
    def goto_label(self, value: BaseNode):
        """Gets or sets the procedure step to go to if the condition is met."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.GotoLabel = next(unwrapped)

    @property
    def variable(self) -> BaseNode:
        """Gets or sets the channel against which to test the condition."""
        dotnet_result = self._dotnet_instance.Variable
        return _wrap(dotnet_result)

    @variable.setter
    def variable(self, value: BaseNode):
        """Gets or sets the channel against which to test the condition."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Variable = next(unwrapped)

    @property
    def value_channel(self) -> BaseNode:
        """Gets the channel that specifies the value that is compared to <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Condition.Variable" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.ValueChannel
        return _wrap(dotnet_result)

    @overload
    def set_value(self, value: float):
        ...

    @overload
    def set_value(self, value: BaseNode):
        ...

    def set_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetValue(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.MaxAFPLength
        return _wrap(dotnet_result)

    @max_afp_length.setter
    def max_afp_length(self, value: int):
        """Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.MaxAFPLength = next(unwrapped)

    @property
    def index_counter(self) -> int:
        """Gets or sets the index of the counter within the frame."""
        dotnet_result = self._dotnet_instance.IndexCounter
        return _wrap(dotnet_result)

    @index_counter.setter
    def index_counter(self, value: int):
        """Gets or sets the index of the counter within the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IndexCounter = next(unwrapped)

    @property
    def afp_data(self) -> Sequence[int]:
        """Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.AFPData
        return _wrap(dotnet_result)

    @afp_data.setter
    def afp_data(self, value: Sequence[int]):
        """Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AFPData = next(unwrapped)

    @property
    def use_alternate_channel(self) -> bool:
        """Gets whether the <format type="italics">AlternateChannel</format> specified by <see cref="M:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter.SetAlternateChannel(NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode)" crefType="Unqualified" /> is used to trigger writing data."""
        dotnet_result = self._dotnet_instance.UseAlternateChannel
        return _wrap(dotnet_result)

    @property
    def alternate_channel(self) -> BaseNode:
        """Gets the channel used to trigger writing data when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter.UseAlternateChannel" crefType="Unqualified" /> is <see langword="true" />."""
        dotnet_result = self._dotnet_instance.AlternateChannel
        return _wrap(dotnet_result)

    @overload
    def remove_alternate_channel(self):
        ...

    def remove_alternate_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveAlternateChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_alternate_channel(self, alternate_channel: BaseNode):
        ...

    def set_alternate_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetAlternateChannel(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDevice(*unwrapped)

    @property
    def timed_loop_priority(self) -> CDTimeLoopPriority:
        """Gets or sets the priority (<format type="monospace">High</format>, <format type="monospace">Low</format>, or <format type="monospace">Medium</format>) of the Timed Loop in which an asynchronous custom device runs. This property only applies to asynchronous custom devices that run in Timed Loops."""
        dotnet_result = self._dotnet_instance.TimedLoopPriority
        return _wrap(dotnet_result)

    @timed_loop_priority.setter
    def timed_loop_priority(self, value: CDTimeLoopPriority):
        """Gets or sets the priority (<format type="monospace">High</format>, <format type="monospace">Low</format>, or <format type="monospace">Medium</format>) of the Timed Loop in which an asynchronous custom device runs. This property only applies to asynchronous custom devices that run in Timed Loops."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TimedLoopPriority = next(unwrapped)

    @property
    def loop_type(self) -> CDLoopType:
        """Gets or sets the type of loop (<format type="monospace">TimedLoop</format> or <format type="monospace">WhileLoop</format>) in which the custom device runs. This property only applies to asynchronous custom devices."""
        dotnet_result = self._dotnet_instance.LoopType
        return _wrap(dotnet_result)

    @loop_type.setter
    def loop_type(self, value: CDLoopType):
        """Gets or sets the type of loop (<format type="monospace">TimedLoop</format> or <format type="monospace">WhileLoop</format>) in which the custom device runs. This property only applies to asynchronous custom devices."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LoopType = next(unwrapped)

    @property
    def driver_vi_execution_mode(self) -> CDDriverExecMode:
        """Gets or sets the execution mode of the custom device, such as if it runs inline with the Primary Control Loop or asynchronously."""
        dotnet_result = self._dotnet_instance.DriverVIExecutionMode
        return _wrap(dotnet_result)

    @driver_vi_execution_mode.setter
    def driver_vi_execution_mode(self, value: CDDriverExecMode):
        """Gets or sets the execution mode of the custom device, such as if it runs inline with the Primary Control Loop or asynchronously."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DriverVIExecutionMode = next(unwrapped)

    @property
    def device_enabled_state(self) -> bool:
        """Gets or sets the state (enabled or disabled) of the custom device.
            
             The effect of setting this property will not be visible in System Explorer. Many custom devices provide an alternate TypeGUID and associated glyph to indicate whether the custom device is disabled."""
        dotnet_result = self._dotnet_instance.DeviceEnabledState
        return _wrap(dotnet_result)

    @device_enabled_state.setter
    def device_enabled_state(self, value: bool):
        """Gets or sets the state (enabled or disabled) of the custom device.
            
             The effect of setting this property will not be visible in System Explorer. Many custom devices provide an alternate TypeGUID and associated glyph to indicate whether the custom device is disabled."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DeviceEnabledState = next(unwrapped)

    @property
    def version(self) -> str:
        """Gets or sets information stored with a custom device, such as version information. You can read this string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code."""
        dotnet_result = self._dotnet_instance.Version
        return _wrap(dotnet_result)

    @version.setter
    def version(self, value: str):
        """Gets or sets information stored with a custom device, such as version information. You can read this string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Version = next(unwrapped)

    @property
    def use_device_clock(self) -> bool:
        """Gets or sets whether the Timed Loop in which an asynchronous custom device runs is synchronized with the Primary Control Loop (PCL) timing source. This property only applies to asynchronous custom devices that run in Timed Loops."""
        dotnet_result = self._dotnet_instance.UseDeviceClock
        return _wrap(dotnet_result)

    @use_device_clock.setter
    def use_device_clock(self, value: bool):
        """Gets or sets whether the Timed Loop in which an asynchronous custom device runs is synchronized with the Primary Control Loop (PCL) timing source. This property only applies to asynchronous custom devices that run in Timed Loops."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.UseDeviceClock = next(unwrapped)

    @property
    def decimation(self) -> int:
        """Gets or sets the decimation factor for the custom device, which determines how many iterations of the Primary Control Loop (PCL) occur between calls to the custom device."""
        dotnet_result = self._dotnet_instance.Decimation
        return _wrap(dotnet_result)

    @decimation.setter
    def decimation(self, value: int):
        """Gets or sets the decimation factor for the custom device, which determines how many iterations of the Primary Control Loop (PCL) occur between calls to the custom device."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Decimation = next(unwrapped)

    @property
    def fifo_source_depth(self) -> int:
        """Gets or sets the depth of the FIFO at the source. This property defines the size of the buffer for incoming data. This property only applies to asynchronous custom devices."""
        dotnet_result = self._dotnet_instance.FIFOSourceDepth
        return _wrap(dotnet_result)

    @fifo_source_depth.setter
    def fifo_source_depth(self, value: int):
        """Gets or sets the depth of the FIFO at the source. This property defines the size of the buffer for incoming data. This property only applies to asynchronous custom devices."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FIFOSourceDepth = next(unwrapped)

    @property
    def fifo_sink_depth(self) -> int:
        """Gets or sets the depth of the FIFO at the sink. This property defines the size of the buffer for outgoing data. This property only applies to asynchronous custom devices."""
        dotnet_result = self._dotnet_instance.FIFOSinkDepth
        return _wrap(dotnet_result)

    @fifo_sink_depth.setter
    def fifo_sink_depth(self, value: int):
        """Gets or sets the depth of the FIFO at the sink. This property defines the size of the buffer for outgoing data. This property only applies to asynchronous custom devices."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FIFOSinkDepth = next(unwrapped)

    @overload
    def get_custom_device_channel_list(self) -> Sequence[CustomDeviceChannel]:
        ...

    def get_custom_device_channel_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCustomDeviceChannelList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_custom_device_waveform_list(self) -> Sequence[CustomDeviceWaveform]:
        ...

    def get_custom_device_waveform_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCustomDeviceWaveformList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_custom_device_section_list(self) -> Sequence[CustomDeviceSection]:
        ...

    def get_custom_device_section_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCustomDeviceSectionList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_dependencies(self) -> Sequence[DependentFile]:
        ...

    def get_dependencies(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDependencies(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_driver_vi_for_owner_target_type(self) -> DependentFile:
        ...

    def get_driver_vi_for_owner_target_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDriverVIForOwnerTargetType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_driver_v_is(self) -> Sequence[DependentFile]:
        ...

    def get_driver_v_is(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDriverVIs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_timing_source_init_v_is(self) -> Sequence[DependentFile]:
        ...

    def get_timing_source_init_v_is(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTimingSourceInitVIs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_dependencies(self, dependencies: Sequence[DependentFile]):
        ...

    def add_dependencies(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddDependencies(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_driver_v_is(self, driver_v_is: Sequence[DependentFile]):
        ...

    def set_driver_v_is(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDriverVIs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_timing_source_init_v_is(self, timing_source_init_v_is: Sequence[DependentFile]):
        ...

    def set_timing_source_init_v_is(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetTimingSourceInitVIs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reset_dependencies(self):
        ...

    def reset_dependencies(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ResetDependencies(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel(*unwrapped)

    @property
    def type(self) -> CDChannel_Type:
        """Gets or sets whether a custom device channel is an input or output channel. Only input channels are writable."""
        dotnet_result = self._dotnet_instance.Type
        return _wrap(dotnet_result)

    @type.setter
    def type(self, value: CDChannel_Type):
        """Gets or sets whether a custom device channel is an input or output channel. Only input channels are writable."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Type = next(unwrapped)

    @property
    def faultable(self) -> bool:
        """Gets or sets whether a custom device channel is faultable, meaning the VeriStand Engine can fault the channel using software fault insertion."""
        dotnet_result = self._dotnet_instance.Faultable
        return _wrap(dotnet_result)

    @faultable.setter
    def faultable(self, value: bool):
        """Gets or sets whether a custom device channel is faultable, meaning the VeriStand Engine can fault the channel using software fault insertion."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Faultable = next(unwrapped)

    @property
    def scalable(self) -> bool:
        """Gets or sets whether a custom device channel can be calibrated or scaled into specific engineering units."""
        dotnet_result = self._dotnet_instance.Scalable
        return _wrap(dotnet_result)

    @scalable.setter
    def scalable(self, value: bool):
        """Gets or sets whether a custom device channel can be calibrated or scaled into specific engineering units."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Scalable = next(unwrapped)

    @property
    def default_value(self) -> float:
        """Gets or sets the default value for a custom device channel."""
        dotnet_result = self._dotnet_instance.DefaultValue
        return _wrap(dotnet_result)

    @default_value.setter
    def default_value(self, value: float):
        """Gets or sets the default value for a custom device channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DefaultValue = next(unwrapped)

    @property
    def scale(self) -> Scale:
        """Gets or sets the value of the scale property on the channel."""
        dotnet_result = self._dotnet_instance.Scale
        return _wrap(dotnet_result)

    @scale.setter
    def scale(self, value: Scale):
        """Gets or sets the value of the scale property on the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Scale = next(unwrapped)

    @property
    def bit_fields(self) -> int:
        """For internal use only. Stores various channel settings, such as its type, default value, whether it is faultable or scalable, and so on. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.DefaultValue" crefType="Unqualified" />, <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.Faultable" crefType="Unqualified" />, <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.Scalable" crefType="Unqualified" />, and <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.Type" crefType="Unqualified" /> properties to get the information the bit field contains."""
        dotnet_result = self._dotnet_instance.BitFields
        return _wrap(dotnet_result)

    @overload
    def set_value_table(self, names: Sequence[str], values: Sequence[float]):
        ...

    def set_value_table(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetValueTable(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCustomDeviceList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_custom_device(self, custom_device: CustomDevice) -> bool:
        ...

    def add_custom_device(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddCustomDevice(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSignalBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetRawDataBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddSignalBasedFrame(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddRawDataBasedFrame(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSignalBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetRawDataBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddSignalBasedFrame(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddRawDataBasedFrame(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDeviceList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_tasks(self) -> DAQTasks:
        ...

    def get_tasks(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTasks(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_device(self, device: DAQDevice) -> bool:
        ...

    def add_device(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddDevice(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.SampleMode
        return _wrap(dotnet_result)

    @sample_mode.setter
    def sample_mode(self, value: SampleMode):
        """Gets or sets whether the acquisition is single-point or buffered."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SampleMode = next(unwrapped)

    @property
    def waveform_analog_input_task(self) -> DAQTaskAI:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> associated with the buffered acquisition."""
        dotnet_result = self._dotnet_instance.WaveformAnalogInputTask
        return _wrap(dotnet_result)

    @waveform_analog_input_task.setter
    def waveform_analog_input_task(self, value: DAQTaskAI):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> associated with the buffered acquisition."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.WaveformAnalogInputTask = next(unwrapped)

    @property
    def is_slow_background_convert_enabled(self) -> bool:
        """Gets whether the Slow Background Convert configuration is enabled."""
        dotnet_result = self._dotnet_instance.IsSlowBackgroundConvertEnabled
        return _wrap(dotnet_result)

    @property
    def slow_background_convert_rate(self) -> float:
        """Gets the Slow Background Convert sample rate."""
        dotnet_result = self._dotnet_instance.SlowBackgroundConvertRate
        return _wrap(dotnet_result)

    @overload
    def get_analog_input_list(self) -> Sequence[DAQAnalogInput]:
        ...

    def get_analog_input_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAnalogInputList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_waveform_analog_input_list(self) -> Sequence[DAQWaveformAnalogInput]:
        ...

    def get_waveform_analog_input_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetWaveformAnalogInputList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_analog_input(self, analog_input: DAQAnalogInput) -> bool:
        ...

    def add_analog_input(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAnalogInput(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_waveform_analog_input(self, waveform_analog_input: DAQWaveformAnalogInput) -> bool:
        ...

    def add_waveform_analog_input(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddWaveformAnalogInput(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def slow_background_convert_mode(self, enable: bool, rate: float):
        ...

    def slow_background_convert_mode(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SlowBackgroundConvertMode(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAnalogOutputList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_analog_output(self, analog_output: DAQAnalogOutput) -> bool:
        ...

    def add_analog_output(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddAnalogOutput(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.PluginGUID
        return _wrap(dotnet_result)

    @property
    def measurement_type(self) -> DAQMeasurementType:
        """Gets the type of measurement or generation the DAQ channel performs."""
        dotnet_result = self._dotnet_instance.MeasurementType
        return _wrap(dotnet_result)

    @overload
    def get_double_property(self, property_name: str) -> float:
        ...

    def get_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64_property(self, property_name: str) -> int:
        ...

    def get_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32_property(self, property_name: str) -> int:
        ...

    def get_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16_property(self, property_name: str) -> int:
        ...

    def get_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i64_property(self, property_name: str) -> int:
        ...

    def get_i64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32_property(self, property_name: str) -> int:
        ...

    def get_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i16_property(self, property_name: str) -> int:
        ...

    def get_i16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_boolean_property(self, property_name: str) -> bool:
        ...

    def get_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string_property(self, property_name: str) -> str:
        ...

    def get_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_enum_property(self, property_name: str) -> Tuple[str, int]:
        ...

    def get_enum_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetEnumProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_properties(self) -> Tuple[Sequence[str], Sequence[ValueDataType]]:
        ...

    def get_properties(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetProperties(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reset_property_values(self):
        ...

    def reset_property_values(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ResetPropertyValues(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_double_property(self, property_name: str, value: float):
        ...

    def set_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u64_property(self, property_name: str, value: int):
        ...

    def set_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u32_property(self, property_name: str, value: int):
        ...

    def set_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u16_property(self, property_name: str, value: int):
        ...

    def set_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i64_property(self, property_name: str, value: int):
        ...

    def set_i64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i32_property(self, property_name: str, value: int):
        ...

    def set_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i16_property(self, property_name: str, value: int):
        ...

    def set_i16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_boolean_property(self, property_name: str, value: bool):
        ...

    def set_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_string_property(self, property_name: str, value: str):
        ...

    def set_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_enum_property(self, property_name: str, enum_string: str):
        ...

    @overload
    def set_enum_property(self, property_name: str, value: int):
        ...

    def set_enum_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetEnumProperty(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter(*unwrapped)

    @_staticproperty
    def default_terminal() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal
        return _wrap(dotnet_result)

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of the counter channel."""
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the counter channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialValue = next(unwrapped)

    @property
    def data_task(self) -> DAQCounterType:
        """Gets the type of task the counter performs (frequency measurement, period measurement, count up/down, or position measurement)."""
        dotnet_result = self._dotnet_instance.DataTask
        return _wrap(dotnet_result)

    @property
    def counter(self) -> str:
        """Gets the counter channel number."""
        dotnet_result = self._dotnet_instance.Counter
        return _wrap(dotnet_result)

    @overload
    def downcast(self) -> DAQCounter:
        ...

    def downcast(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Downcast(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_counter_index(self, index: int) -> bool:
        ...

    def set_counter_index(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetCounterIndex(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCounterList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_counter_outputs(self) -> Sequence[DAQCounterOutput]:
        ...

    def get_counter_outputs(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCounterOutputs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_counter_inputs(self) -> Sequence[DAQCounterInput]:
        ...

    def get_counter_inputs(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCounterInputs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_counter(self, counter: DAQCounter) -> bool:
        ...

    def add_counter(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddCounter(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_counter_input(self, counter: DAQCounterInput) -> bool:
        ...

    def add_counter_input(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddCounterInput(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_counter_output(self, counter: DAQCounterOutput) -> bool:
        ...

    def add_counter_output(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddCounterOutput(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDIOPort(*unwrapped)

    @property
    def inverted(self) -> bool:
        """Gets or sets whether the digital lines are inverted."""
        dotnet_result = self._dotnet_instance.Inverted
        return _wrap(dotnet_result)

    @inverted.setter
    def inverted(self, value: bool):
        """Gets or sets whether the digital lines are inverted."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Inverted = next(unwrapped)

    @overload
    def get_digital_inputs(self) -> Sequence[DAQDigitalInput]:
        ...

    def get_digital_inputs(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDigitalInputs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_digital_outputs(self) -> Sequence[DAQDigitalOutput]:
        ...

    def get_digital_outputs(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDigitalOutputs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_digital_input(self, digital_input: DAQDigitalInput) -> bool:
        ...

    def add_digital_input(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddDigitalInput(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_digital_output(self, digital_output: DAQDigitalOutput) -> bool:
        ...

    def add_digital_output(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddDigitalOutput(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice(*unwrapped)

    @property
    def backplane_reference_clock(self) -> PXIBackplaneReferenceClock:
        """Sets or gets the reference clock on the PXI/PXIe chassis backplane to which the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" /> synchronizes its timing."""
        dotnet_result = self._dotnet_instance.BackplaneReferenceClock
        return _wrap(dotnet_result)

    @backplane_reference_clock.setter
    def backplane_reference_clock(self, value: PXIBackplaneReferenceClock):
        """Sets or gets the reference clock on the PXI/PXIe chassis backplane to which the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" /> synchronizes its timing."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BackplaneReferenceClock = next(unwrapped)

    @property
    def product_id(self) -> int:
        """Public, always writable version of DAQ Product ID
            DAQ Product ID is the unique numeric identifier for a DAQ device."""
        dotnet_result = self._dotnet_instance.ProductID
        return _wrap(dotnet_result)

    @product_id.setter
    def product_id(self, value: int):
        """Public, always writable version of DAQ Product ID
            DAQ Product ID is the unique numeric identifier for a DAQ device."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ProductID = next(unwrapped)

    @property
    def product_category(self) -> int:
        """Public, always writable version of DAQ Product Category.
            Unique identifier for each DAQ Product category."""
        dotnet_result = self._dotnet_instance.ProductCategory
        return _wrap(dotnet_result)

    @product_category.setter
    def product_category(self, value: int):
        """Public, always writable version of DAQ Product Category.
            Unique identifier for each DAQ Product category."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ProductCategory = next(unwrapped)

    @property
    def product_name(self) -> str:
        """Public, always writable version of DAQ Product Name."""
        dotnet_result = self._dotnet_instance.ProductName
        return _wrap(dotnet_result)

    @product_name.setter
    def product_name(self, value: str):
        """Public, always writable version of DAQ Product Name."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ProductName = next(unwrapped)

    @property
    def input_configuration(self) -> DAQDeviceInputConfiguration:
        """Gets or sets the input terminal configuration applied to device channels."""
        dotnet_result = self._dotnet_instance.InputConfiguration
        return _wrap(dotnet_result)

    @input_configuration.setter
    def input_configuration(self, value: DAQDeviceInputConfiguration):
        """Gets or sets the input terminal configuration applied to device channels."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InputConfiguration = next(unwrapped)

    @property
    def daq_conversion_rate_option(self) -> DAQConversionRate:
        """Gets or sets the rate used to run the analog-digital converters on the DAQ device."""
        dotnet_result = self._dotnet_instance.DAQConversionRateOption
        return _wrap(dotnet_result)

    @daq_conversion_rate_option.setter
    def daq_conversion_rate_option(self, value: DAQConversionRate):
        """Gets or sets the rate used to run the analog-digital converters on the DAQ device."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DAQConversionRateOption = next(unwrapped)

    @property
    def turn_off_hw_timed_single_point_ai(self) -> bool:
        """Gets or sets whether hardware-timed single-point support is disabled for analog input tasks."""
        dotnet_result = self._dotnet_instance.TurnOffHWTimedSinglePointAI
        return _wrap(dotnet_result)

    @turn_off_hw_timed_single_point_ai.setter
    def turn_off_hw_timed_single_point_ai(self, value: bool):
        """Gets or sets whether hardware-timed single-point support is disabled for analog input tasks."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TurnOffHWTimedSinglePointAI = next(unwrapped)

    @property
    def port_width(self) -> int:
        """Gets or sets the total number of lines per port."""
        dotnet_result = self._dotnet_instance.PortWidth
        return _wrap(dotnet_result)

    @port_width.setter
    def port_width(self, value: int):
        """Gets or sets the total number of lines per port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PortWidth = next(unwrapped)

    @property
    def turn_off_hw_timed_single_point_ao(self) -> bool:
        """Gets or sets whether hardware-timed single-point support is disabled for analog output tasks."""
        dotnet_result = self._dotnet_instance.TurnOffHWTimedSinglePointAO
        return _wrap(dotnet_result)

    @turn_off_hw_timed_single_point_ao.setter
    def turn_off_hw_timed_single_point_ao(self, value: bool):
        """Gets or sets whether hardware-timed single-point support is disabled for analog output tasks."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TurnOffHWTimedSinglePointAO = next(unwrapped)

    @overload
    def create_analog_inputs(self) -> DAQAnalogInputs:
        ...

    @overload
    def create_analog_inputs(self, mode: SampleMode) -> DAQAnalogInputs:
        ...

    def create_analog_inputs(self, *args):
        unwrapped = _unwrap({(): (0, NationalInstruments.VeriStand.Error.NoError), (SampleMode,): (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateAnalogInputs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_analog_outputs(self) -> DAQAnalogOutputs:
        ...

    def create_analog_outputs(self, *args):
        unwrapped = _unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateAnalogOutputs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_counters(self) -> DAQCounters:
        ...

    def create_counters(self, *args):
        unwrapped = _unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateCounters(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_digital_inputs(self) -> DAQDigitalInputs:
        ...

    def create_digital_inputs(self, *args):
        unwrapped = _unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateDigitalInputs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_digital_outputs(self) -> DAQDigitalOutputs:
        ...

    def create_digital_outputs(self, *args):
        unwrapped = _unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateDigitalOutputs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_scxi_chassis(self) -> SCXIChassis:
        ...

    def create_scxi_chassis(self, *args):
        unwrapped = _unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateSCXIChassis(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_internal_channels(self) -> DAQInternalChannels:
        ...

    def create_internal_channels(self, *args):
        unwrapped = _unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateInternalChannels(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def populate_device(self, num_ai_channels: int, num_ao_channels: int, num_di_channels: int, num_do_channels: int, port_width: int):
        ...

    @overload
    def populate_device(self, num_ai_channels: int, num_ao_channels: int, num_di_channels: int, num_do_channels: int, port_width: int, counter_types: Sequence[DAQCounterType], num_internal_channels: int):
        ...

    def populate_device(self, *args):
        unwrapped = _unwrap({None: (7, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.PopulateDevice(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_analog_input_section(self) -> DAQAnalogInputs:
        ...

    def get_analog_input_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAnalogInputSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_analog_output_section(self) -> DAQAnalogOutputs:
        ...

    def get_analog_output_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAnalogOutputSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_counter_section(self) -> DAQCounters:
        ...

    def get_counter_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCounterSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_digital_input_section(self) -> DAQDigitalInputs:
        ...

    def get_digital_input_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDigitalInputSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_digital_output_section(self) -> DAQDigitalOutputs:
        ...

    def get_digital_output_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDigitalOutputSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_scxi_chassis_section(self) -> SCXIChassis:
        ...

    def get_scxi_chassis_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSCXIChassisSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_internal_channels_section(self) -> DAQInternalChannels:
        ...

    def get_internal_channels_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetInternalChannelsSection(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalInput(*unwrapped)

    @property
    def inital_value(self) -> bool:
        """Gets or sets the initial value of the digital input channel."""
        dotnet_result = self._dotnet_instance.InitalValue
        return _wrap(dotnet_result)

    @inital_value.setter
    def inital_value(self, value: bool):
        """Gets or sets the initial value of the digital input channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitalValue = next(unwrapped)

    @property
    def digital_line(self) -> int:
        """Gets or sets the digital line for the channel."""
        dotnet_result = self._dotnet_instance.DigitalLine
        return _wrap(dotnet_result)

    @digital_line.setter
    def digital_line(self, value: int):
        """Gets or sets the digital line for the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DigitalLine = next(unwrapped)

    @property
    def port_number(self) -> int:
        """Gets or sets the port to which the channel belongs."""
        dotnet_result = self._dotnet_instance.PortNumber
        return _wrap(dotnet_result)

    @port_number.setter
    def port_number(self, value: int):
        """Gets or sets the port to which the channel belongs."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PortNumber = next(unwrapped)

    @property
    def is_scxi(self) -> bool:
        """Gets whether the channel belongs to an SCXI module."""
        dotnet_result = self._dotnet_instance.IsSCXI
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDIOPorts(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_dio_port(self, dio_port: DAQDIOPort) -> bool:
        ...

    def add_dio_port(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddDIOPort(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalOutput(*unwrapped)

    @property
    def inital_value(self) -> bool:
        """Gets or sets the initial value of the digital output channel."""
        dotnet_result = self._dotnet_instance.InitalValue
        return _wrap(dotnet_result)

    @inital_value.setter
    def inital_value(self, value: bool):
        """Gets or sets the initial value of the digital output channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitalValue = next(unwrapped)

    @property
    def digital_line(self) -> int:
        """Gets or sets the digital line for the channel."""
        dotnet_result = self._dotnet_instance.DigitalLine
        return _wrap(dotnet_result)

    @digital_line.setter
    def digital_line(self, value: int):
        """Gets or sets the digital line for the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DigitalLine = next(unwrapped)

    @property
    def port_number(self) -> int:
        """Gets or sets the port to which the channel belongs."""
        dotnet_result = self._dotnet_instance.PortNumber
        return _wrap(dotnet_result)

    @port_number.setter
    def port_number(self, value: int):
        """Gets or sets the port to which the channel belongs."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PortNumber = next(unwrapped)

    @property
    def is_scxi(self) -> bool:
        """Gets whether the channel belongs to an SCXI module."""
        dotnet_result = self._dotnet_instance.IsSCXI
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDIOPorts(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_dio_port(self, dio_port: DAQDIOPort) -> bool:
        ...

    def add_dio_port(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddDIOPort(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQFrequencyMeasurement(*unwrapped)

    @property
    def edge(self) -> DAQCounterEdge:
        """Gets or sets the edge on which to count (rising or falling)."""
        dotnet_result = self._dotnet_instance.Edge
        return _wrap(dotnet_result)

    @edge.setter
    def edge(self, value: DAQCounterEdge):
        """Gets or sets the edge on which to count (rising or falling)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Edge = next(unwrapped)

    @property
    def input_terminal(self) -> str:
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        dotnet_result = self._dotnet_instance.InputTerminal
        return _wrap(dotnet_result)

    @input_terminal.setter
    def input_terminal(self, value: str):
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InputTerminal = next(unwrapped)

    @property
    def max(self) -> float:
        """Gets or sets the maximum value of the channel in hertz."""
        dotnet_result = self._dotnet_instance.Max
        return _wrap(dotnet_result)

    @max.setter
    def max(self, value: float):
        """Gets or sets the maximum value of the channel in hertz."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Max = next(unwrapped)

    @property
    def min(self) -> float:
        """Gets or sets the minimum value of the channel in hertz."""
        dotnet_result = self._dotnet_instance.Min
        return _wrap(dotnet_result)

    @min.setter
    def min(self, value: float):
        """Gets or sets the minimum value of the channel in hertz."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Min = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQInternalChannel(*unwrapped)

    @property
    def low_level(self) -> float:
        """Gets or sets the minimum value of the channel."""
        dotnet_result = self._dotnet_instance.LowLevel
        return _wrap(dotnet_result)

    @low_level.setter
    def low_level(self, value: float):
        """Gets or sets the minimum value of the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LowLevel = next(unwrapped)

    @property
    def high_level(self) -> float:
        """Gets or sets the maximum value of the channel."""
        dotnet_result = self._dotnet_instance.HighLevel
        return _wrap(dotnet_result)

    @high_level.setter
    def high_level(self, value: float):
        """Gets or sets the maximum value of the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.HighLevel = next(unwrapped)

    @property
    def channel(self) -> str:
        """Gets or sets the physical name for the channel."""
        dotnet_result = self._dotnet_instance.Channel
        return _wrap(dotnet_result)

    @channel.setter
    def channel(self, value: str):
        """Gets or sets the physical name for the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Channel = next(unwrapped)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetInternalChannelList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_internal_channel(self, internal_channel: DAQInternalChannel) -> bool:
        ...

    def add_internal_channel(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddInternalChannel(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.UseTaskAsFilename
        return _wrap(dotnet_result)

    @use_task_as_filename.setter
    def use_task_as_filename(self, value: bool):
        """Gets or sets a value indicating whether to use the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> name from the system definition as the base of log filenames."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.UseTaskAsFilename = next(unwrapped)

    @property
    def filename_base(self) -> str:
        """Gets or sets the base string used in log filenames. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsFilename" /> is <see langword="false" /> to specify a filename base other than the task name."""
        dotnet_result = self._dotnet_instance.FilenameBase
        return _wrap(dotnet_result)

    @filename_base.setter
    def filename_base(self, value: str):
        """Gets or sets the base string used in log filenames. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsFilename" /> is <see langword="false" /> to specify a filename base other than the task name."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FilenameBase = next(unwrapped)

    @property
    def log_directory(self) -> str:
        """Gets or sets the directory in which to save log files on the target."""
        dotnet_result = self._dotnet_instance.LogDirectory
        return _wrap(dotnet_result)

    @log_directory.setter
    def log_directory(self, value: str):
        """Gets or sets the directory in which to save log files on the target."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LogDirectory = next(unwrapped)

    @property
    def timestamp_filename(self) -> bool:
        """Gets or sets a value indicating whether to append timestamps to the log filenames."""
        dotnet_result = self._dotnet_instance.TimestampFilename
        return _wrap(dotnet_result)

    @timestamp_filename.setter
    def timestamp_filename(self, value: bool):
        """Gets or sets a value indicating whether to append timestamps to the log filenames."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TimestampFilename = next(unwrapped)

    @property
    def action_on_new(self) -> ActionOnNew:
        """Gets or sets the location to log data when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> begins a new acquisition."""
        dotnet_result = self._dotnet_instance.ActionOnNew
        return _wrap(dotnet_result)

    @action_on_new.setter
    def action_on_new(self, value: ActionOnNew):
        """Gets or sets the location to log data when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> begins a new acquisition."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ActionOnNew = next(unwrapped)

    @property
    def use_task_as_group_name(self) -> bool:
        """Gets or sets a value indicating whether to use the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> name from the system definition as the group name under which data is logged in the TDMS file."""
        dotnet_result = self._dotnet_instance.UseTaskAsGroupName
        return _wrap(dotnet_result)

    @use_task_as_group_name.setter
    def use_task_as_group_name(self, value: bool):
        """Gets or sets a value indicating whether to use the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> name from the system definition as the group name under which data is logged in the TDMS file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.UseTaskAsGroupName = next(unwrapped)

    @property
    def group_name(self) -> str:
        """Gets or sets the group name to which the task logs data in the TDMS file. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsGroupName" /> is <see langword="false" /> to specify a group name other than the task name."""
        dotnet_result = self._dotnet_instance.GroupName
        return _wrap(dotnet_result)

    @group_name.setter
    def group_name(self, value: str):
        """Gets or sets the group name to which the task logs data in the TDMS file. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsGroupName" /> is <see langword="false" /> to specify a group name other than the task name."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.GroupName = next(unwrapped)

    @property
    def logging_enabled(self) -> bool:
        """Gets or sets a value indicating whether the Logging Enabled <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskCommand" /> channel is allowed to start and stop logging. Note that this property does not toggle logging; the Logging Enabled channel toggles logging."""
        dotnet_result = self._dotnet_instance.LoggingEnabled
        return _wrap(dotnet_result)

    @logging_enabled.setter
    def logging_enabled(self, value: bool):
        """Gets or sets a value indicating whether the Logging Enabled <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskCommand" /> channel is allowed to start and stop logging. Note that this property does not toggle logging; the Logging Enabled channel toggles logging."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LoggingEnabled = next(unwrapped)

    @property
    def logging_mode(self) -> LogMode:
        """Gets or sets whether data is available to components in the NI VeriStand system while you log it.  This property valid only if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.LoggingEnabled" /> is <see langword="true" />."""
        dotnet_result = self._dotnet_instance.LoggingMode
        return _wrap(dotnet_result)

    @logging_mode.setter
    def logging_mode(self, value: LogMode):
        """Gets or sets whether data is available to components in the NI VeriStand system while you log it.  This property valid only if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.LoggingEnabled" /> is <see langword="true" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LoggingMode = next(unwrapped)

    @property
    def span_multiple_files(self) -> bool:
        """Gets or sets a value indicating whether to create a new log file when you reach the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SamplesPerFile" /> limit."""
        dotnet_result = self._dotnet_instance.SpanMultipleFiles
        return _wrap(dotnet_result)

    @span_multiple_files.setter
    def span_multiple_files(self, value: bool):
        """Gets or sets a value indicating whether to create a new log file when you reach the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SamplesPerFile" /> limit."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SpanMultipleFiles = next(unwrapped)

    @property
    def samples_per_file(self) -> int:
        """Gets or sets a limit to the number of samples per channel to log to the current file when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="true" />. This property not active if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="false" /> because NI VeriStand logs to the current file without limiting the number of samples."""
        dotnet_result = self._dotnet_instance.SamplesPerFile
        return _wrap(dotnet_result)

    @samples_per_file.setter
    def samples_per_file(self, value: int):
        """Gets or sets a limit to the number of samples per channel to log to the current file when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="true" />. This property not active if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="false" /> because NI VeriStand logs to the current file without limiting the number of samples."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SamplesPerFile = next(unwrapped)

    @overload
    def get_logging_enabled_channel(self) -> DAQTaskCommand:
        ...

    def get_logging_enabled_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLoggingEnabledChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_start_new_file_channel(self) -> DAQTaskCommand:
        ...

    def get_start_new_file_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStartNewFileChannel(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPeriodMeasurement(*unwrapped)

    @property
    def edge(self) -> DAQCounterEdge:
        """Gets or sets the edge on which to count (rising or falling)."""
        dotnet_result = self._dotnet_instance.Edge
        return _wrap(dotnet_result)

    @edge.setter
    def edge(self, value: DAQCounterEdge):
        """Gets or sets the edge on which to count (rising or falling)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Edge = next(unwrapped)

    @property
    def input_terminal(self) -> str:
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        dotnet_result = self._dotnet_instance.InputTerminal
        return _wrap(dotnet_result)

    @input_terminal.setter
    def input_terminal(self, value: str):
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InputTerminal = next(unwrapped)

    @property
    def max(self) -> float:
        """Gets or sets the maximum value of the channel in seconds."""
        dotnet_result = self._dotnet_instance.Max
        return _wrap(dotnet_result)

    @max.setter
    def max(self, value: float):
        """Gets or sets the maximum value of the channel in seconds."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Max = next(unwrapped)

    @property
    def min(self) -> float:
        """Gets or sets the minimum value of the channel in seconds."""
        dotnet_result = self._dotnet_instance.Min
        return _wrap(dotnet_result)

    @min.setter
    def min(self, value: float):
        """Gets or sets the minimum value of the channel in seconds."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Min = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPositionMeasurement(*unwrapped)

    @property
    def decoding(self) -> DAQCounterDecoding:
        """Gets or sets the method used to count and interpret the pulses the encoder generates on signal A and signal B."""
        dotnet_result = self._dotnet_instance.Decoding
        return _wrap(dotnet_result)

    @decoding.setter
    def decoding(self, value: DAQCounterDecoding):
        """Gets or sets the method used to count and interpret the pulses the encoder generates on signal A and signal B."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Decoding = next(unwrapped)

    @property
    def z_index_mode(self) -> DAQCounterZIndexMode:
        """Gets or sets the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement."""
        dotnet_result = self._dotnet_instance.ZIndexMode
        return _wrap(dotnet_result)

    @z_index_mode.setter
    def z_index_mode(self, value: DAQCounterZIndexMode):
        """Gets or sets the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ZIndexMode = next(unwrapped)

    @property
    def a_input_terminal(self) -> str:
        """Gets or sets the A input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        dotnet_result = self._dotnet_instance.AInputTerminal
        return _wrap(dotnet_result)

    @a_input_terminal.setter
    def a_input_terminal(self, value: str):
        """Gets or sets the A input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AInputTerminal = next(unwrapped)

    @property
    def b_input_terminal(self) -> str:
        """Gets or sets the B input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        dotnet_result = self._dotnet_instance.BInputTerminal
        return _wrap(dotnet_result)

    @b_input_terminal.setter
    def b_input_terminal(self, value: str):
        """Gets or sets the B input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BInputTerminal = next(unwrapped)

    @property
    def z_input_terminal(self) -> str:
        """Gets or sets the Z input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        dotnet_result = self._dotnet_instance.ZInputTerminal
        return _wrap(dotnet_result)

    @z_input_terminal.setter
    def z_input_terminal(self, value: str):
        """Gets or sets the Z input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ZInputTerminal = next(unwrapped)


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
        dotnet_result = self._dotnet_instance.PluginGUID
        return _wrap(dotnet_result)

    @property
    def measurement_type(self) -> DAQMeasurementType:
        """Gets the enum specifying DAQ Measurement Type."""
        dotnet_result = self._dotnet_instance.MeasurementType
        return _wrap(dotnet_result)

    @property
    def data_channels(self) -> Sequence[Channel]:
        """Gets all registered data channels for a measurement type."""
        dotnet_result = self._dotnet_instance.DataChannels
        return _wrap(dotnet_result)

    @overload
    def get_double_property(self, property_name: str) -> float:
        ...

    def get_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64_property(self, property_name: str) -> int:
        ...

    def get_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32_property(self, property_name: str) -> int:
        ...

    def get_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16_property(self, property_name: str) -> int:
        ...

    def get_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i64_property(self, property_name: str) -> int:
        ...

    def get_i64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32_property(self, property_name: str) -> int:
        ...

    def get_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i16_property(self, property_name: str) -> int:
        ...

    def get_i16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_boolean_property(self, property_name: str) -> bool:
        ...

    def get_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string_property(self, property_name: str) -> str:
        ...

    def get_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_enum_property(self, property_name: str) -> Tuple[str, int]:
        ...

    def get_enum_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetEnumProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_properties(self) -> Tuple[Sequence[str], Sequence[ValueDataType]]:
        ...

    def get_properties(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetProperties(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reset_property_values(self):
        ...

    def reset_property_values(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ResetPropertyValues(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_double_property(self, property_name: str, value: float):
        ...

    def set_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u64_property(self, property_name: str, value: int):
        ...

    def set_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u32_property(self, property_name: str, value: int):
        ...

    def set_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u16_property(self, property_name: str, value: int):
        ...

    def set_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i64_property(self, property_name: str, value: int):
        ...

    def set_i64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i32_property(self, property_name: str, value: int):
        ...

    def set_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i16_property(self, property_name: str, value: int):
        ...

    def set_i16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_boolean_property(self, property_name: str, value: bool):
        ...

    def set_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_string_property(self, property_name: str, value: str):
        ...

    def set_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_enum_property(self, property_name: str, enum_string: str):
        ...

    @overload
    def set_enum_property(self, property_name: str, value: int):
        ...

    def set_enum_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetEnumProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_data_channel(self, type: DAQDataChannelType) -> Channel:
        ...

    def get_data_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataChannel(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.TaskType
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI(*unwrapped)

    @property
    def rate(self) -> float:
        """Gets or sets the sampling rate, in samples per channel per second, or Hz."""
        dotnet_result = self._dotnet_instance.Rate
        return _wrap(dotnet_result)

    @rate.setter
    def rate(self, value: float):
        """Gets or sets the sampling rate, in samples per channel per second, or Hz."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Rate = next(unwrapped)

    @property
    def acquisition_mode(self) -> AcquisitionMode:
        """Gets or sets the type of acquisition the task performs."""
        dotnet_result = self._dotnet_instance.AcquisitionMode
        return _wrap(dotnet_result)

    @acquisition_mode.setter
    def acquisition_mode(self, value: AcquisitionMode):
        """Gets or sets the type of acquisition the task performs."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AcquisitionMode = next(unwrapped)

    @property
    def automatic_read_size(self) -> bool:
        """Gets or sets a value indicating whether to automatically determine the size of read operations that make up an acquisition."""
        dotnet_result = self._dotnet_instance.AutomaticReadSize
        return _wrap(dotnet_result)

    @automatic_read_size.setter
    def automatic_read_size(self, value: bool):
        """Gets or sets a value indicating whether to automatically determine the size of read operations that make up an acquisition."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AutomaticReadSize = next(unwrapped)

    @property
    def read_samples(self) -> int:
        """Gets or sets the requested number of samples per channel to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />."""
        dotnet_result = self._dotnet_instance.ReadSamples
        return _wrap(dotnet_result)

    @read_samples.setter
    def read_samples(self, value: int):
        """Gets or sets the requested number of samples per channel to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ReadSamples = next(unwrapped)

    @property
    def read_time(self) -> float:
        """Gets or sets the number of seconds to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />."""
        dotnet_result = self._dotnet_instance.ReadTime
        return _wrap(dotnet_result)

    @read_time.setter
    def read_time(self, value: float):
        """Gets or sets the number of seconds to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ReadTime = next(unwrapped)

    @property
    def read_units(self) -> AcquisitionUnits:
        """Gets or sets whether the task uses <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadTime" /> or <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadSamples" /> as the read size. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that do not automatically determine the read size."""
        dotnet_result = self._dotnet_instance.ReadUnits
        return _wrap(dotnet_result)

    @read_units.setter
    def read_units(self, value: AcquisitionUnits):
        """Gets or sets whether the task uses <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadTime" /> or <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadSamples" /> as the read size. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that do not automatically determine the read size."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ReadUnits = next(unwrapped)

    @property
    def acquisition_samples(self) -> int:
        """Gets or sets the total number of samples per channel to acquire. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        dotnet_result = self._dotnet_instance.AcquisitionSamples
        return _wrap(dotnet_result)

    @acquisition_samples.setter
    def acquisition_samples(self, value: int):
        """Gets or sets the total number of samples per channel to acquire. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AcquisitionSamples = next(unwrapped)

    @property
    def acquisition_time(self) -> float:
        """Gets or sets the total number of seconds to acquire data. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        dotnet_result = self._dotnet_instance.AcquisitionTime
        return _wrap(dotnet_result)

    @acquisition_time.setter
    def acquisition_time(self, value: float):
        """Gets or sets the total number of seconds to acquire data. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AcquisitionTime = next(unwrapped)

    @property
    def acquisition_units(self) -> AcquisitionUnits:
        """Gets or sets whether the task uses time in seconds or number of samples as the size of the acquisitions it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        dotnet_result = self._dotnet_instance.AcquisitionUnits
        return _wrap(dotnet_result)

    @acquisition_units.setter
    def acquisition_units(self, value: AcquisitionUnits):
        """Gets or sets whether the task uses time in seconds or number of samples as the size of the acquisitions it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AcquisitionUnits = next(unwrapped)

    @property
    def clock_source(self) -> str:
        """Gets or sets the source terminal of the sample clock that you want to control acquisition timing.  An empty string corresponds to the default onboard clock of the device."""
        dotnet_result = self._dotnet_instance.ClockSource
        return _wrap(dotnet_result)

    @clock_source.setter
    def clock_source(self, value: str):
        """Gets or sets the source terminal of the sample clock that you want to control acquisition timing.  An empty string corresponds to the default onboard clock of the device."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ClockSource = next(unwrapped)

    @property
    def active_edge(self) -> EdgeType:
        """Gets or sets the type of edge in the pulses of the sample clock that cause the task to acquire samples: rising or falling."""
        dotnet_result = self._dotnet_instance.ActiveEdge
        return _wrap(dotnet_result)

    @active_edge.setter
    def active_edge(self, value: EdgeType):
        """Gets or sets the type of edge in the pulses of the sample clock that cause the task to acquire samples: rising or falling."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ActiveEdge = next(unwrapped)

    @property
    def channel_names(self) -> ChannelNames:
        """Gets or sets a value that indicates how the names of AI channels appear in log files that this task creates."""
        dotnet_result = self._dotnet_instance.ChannelNames
        return _wrap(dotnet_result)

    @channel_names.setter
    def channel_names(self, value: ChannelNames):
        """Gets or sets a value that indicates how the names of AI channels appear in log files that this task creates."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ChannelNames = next(unwrapped)

    @overload
    def get_logging(self) -> DAQLogging:
        ...

    def get_logging(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLogging(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_triggers(self) -> DAQTriggers:
        ...

    def get_triggers(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTriggers(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_task_enabled_channel(self) -> DAQTaskCommand:
        ...

    def get_task_enabled_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTaskEnabledChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_devices(self) -> Sequence[DAQDevice]:
        ...

    def get_devices(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDevices(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @initial_value.setter
    def initial_value(self, value: bool):
        """Gets or sets a value indicating whether the channel is initially enabled or disabled."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialValue = next(unwrapped)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTaskList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_task(self, task: DAQTask) -> bool:
        ...

    def add_task(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddTask(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_task_list(self, tasks: Sequence[DAQTask]) -> bool:
        ...

    def reorder_task_list(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.ReorderTaskList(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers(*unwrapped)

    @property
    def start_trigger(self) -> DAQTrigger:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the start trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />."""
        dotnet_result = self._dotnet_instance.StartTrigger
        return _wrap(dotnet_result)

    @start_trigger.setter
    def start_trigger(self, value: DAQTrigger):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the start trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.StartTrigger = next(unwrapped)

    @property
    def reference_trigger(self) -> DAQTrigger:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the reference trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />."""
        dotnet_result = self._dotnet_instance.ReferenceTrigger
        return _wrap(dotnet_result)

    @reference_trigger.setter
    def reference_trigger(self, value: DAQTrigger):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the reference trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ReferenceTrigger = next(unwrapped)

    @property
    def pretrigger_samples(self) -> int:
        """Gets or sets the number of samples per channel prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs."""
        dotnet_result = self._dotnet_instance.PretriggerSamples
        return _wrap(dotnet_result)

    @pretrigger_samples.setter
    def pretrigger_samples(self, value: int):
        """Gets or sets the number of samples per channel prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PretriggerSamples = next(unwrapped)

    @property
    def pretrigger_time(self) -> float:
        """Gets or sets the length of time, in seconds, prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs."""
        dotnet_result = self._dotnet_instance.PretriggerTime
        return _wrap(dotnet_result)

    @pretrigger_time.setter
    def pretrigger_time(self, value: float):
        """Gets or sets the length of time, in seconds, prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PretriggerTime = next(unwrapped)

    @property
    def pretrigger_units(self) -> AcquisitionUnits:
        """Gets or sets whether the task uses samples or seconds of time as the size of the pre-trigger acquisition it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serve as the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> for the task."""
        dotnet_result = self._dotnet_instance.PretriggerUnits
        return _wrap(dotnet_result)

    @pretrigger_units.setter
    def pretrigger_units(self, value: AcquisitionUnits):
        """Gets or sets whether the task uses samples or seconds of time as the size of the pre-trigger acquisition it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serve as the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> for the task."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PretriggerUnits = next(unwrapped)

    @overload
    def get_retriggerable_channel(self) -> DAQTaskCommand:
        ...

    def get_retriggerable_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetRetriggerableChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_start_trigger_channel(self) -> DAQTaskCommand:
        ...

    def get_start_trigger_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStartTriggerChannel(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.PluginGUID
        return _wrap(dotnet_result)

    @property
    def measurement_type(self) -> DAQMeasurementType:
        """Gets the enum specifying DAQ Measurement Type."""
        dotnet_result = self._dotnet_instance.MeasurementType
        return _wrap(dotnet_result)

    @overload
    def get_double_property(self, property_name: str) -> float:
        ...

    def get_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64_property(self, property_name: str) -> int:
        ...

    def get_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32_property(self, property_name: str) -> int:
        ...

    def get_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16_property(self, property_name: str) -> int:
        ...

    def get_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i64_property(self, property_name: str) -> int:
        ...

    def get_i64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32_property(self, property_name: str) -> int:
        ...

    def get_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i16_property(self, property_name: str) -> int:
        ...

    def get_i16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_boolean_property(self, property_name: str) -> bool:
        ...

    def get_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string_property(self, property_name: str) -> str:
        ...

    def get_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_enum_property(self, property_name: str) -> Tuple[str, int]:
        ...

    def get_enum_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetEnumProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_properties(self) -> Tuple[Sequence[str], Sequence[ValueDataType]]:
        ...

    def get_properties(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetProperties(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reset_property_values(self):
        ...

    def reset_property_values(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ResetPropertyValues(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_double_property(self, property_name: str, value: float):
        ...

    def set_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u64_property(self, property_name: str, value: int):
        ...

    def set_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u32_property(self, property_name: str, value: int):
        ...

    def set_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u16_property(self, property_name: str, value: int):
        ...

    def set_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i64_property(self, property_name: str, value: int):
        ...

    def set_i64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i32_property(self, property_name: str, value: int):
        ...

    def set_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i16_property(self, property_name: str, value: int):
        ...

    def set_i16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_boolean_property(self, property_name: str, value: bool):
        ...

    def set_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_string_property(self, property_name: str, value: str):
        ...

    def set_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_enum_property(self, property_name: str, enum_string: str):
        ...

    @overload
    def set_enum_property(self, property_name: str, value: int):
        ...

    def set_enum_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetEnumProperty(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQWaveformAnalogInput(*unwrapped)

    @property
    def channel(self) -> int:
        """Gets or sets the channel number."""
        dotnet_result = self._dotnet_instance.Channel
        return _wrap(dotnet_result)

    @channel.setter
    def channel(self, value: int):
        """Gets or sets the channel number."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Channel = next(unwrapped)

    @property
    def low_level(self) -> float:
        """Gets or sets the minimum value of the channel."""
        dotnet_result = self._dotnet_instance.LowLevel
        return _wrap(dotnet_result)

    @low_level.setter
    def low_level(self, value: float):
        """Gets or sets the minimum value of the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LowLevel = next(unwrapped)

    @property
    def high_level(self) -> float:
        """Gets or sets the maximum value of the channel."""
        dotnet_result = self._dotnet_instance.HighLevel
        return _wrap(dotnet_result)

    @high_level.setter
    def high_level(self, value: float):
        """Gets or sets the maximum value of the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.HighLevel = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay(*unwrapped)

    @property
    def behavior(self) -> ReplayBehavior:
        """Gets or sets whether and how frames in the data replay file are filtered."""
        dotnet_result = self._dotnet_instance.Behavior
        return _wrap(dotnet_result)

    @behavior.setter
    def behavior(self, value: ReplayBehavior):
        """Gets or sets whether and how frames in the data replay file are filtered."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Behavior = next(unwrapped)

    @property
    def tdms_group_name(self) -> str:
        """Gets or sets the name of the group in a TDMS file that contains the logged data for replay."""
        dotnet_result = self._dotnet_instance.TDMSGroupName
        return _wrap(dotnet_result)

    @tdms_group_name.setter
    def tdms_group_name(self, value: str):
        """Gets or sets the name of the group in a TDMS file that contains the logged data for replay."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TDMSGroupName = next(unwrapped)

    @property
    def tdms_channel_name(self) -> str:
        """Gets or sets the name of the channel in a TDMS file that contains the logged data for replay."""
        dotnet_result = self._dotnet_instance.TDMSChannelName
        return _wrap(dotnet_result)

    @tdms_channel_name.setter
    def tdms_channel_name(self, value: str):
        """Gets or sets the name of the channel in a TDMS file that contains the logged data for replay."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TDMSChannelName = next(unwrapped)

    @property
    def path(self) -> DependentFile:
        """Gets or sets the path to the replay file on disk."""
        dotnet_result = self._dotnet_instance.Path
        return _wrap(dotnet_result)

    @path.setter
    def path(self, value: DependentFile):
        """Gets or sets the path to the replay file on disk."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Path = next(unwrapped)

    @property
    def frame_cache_size(self) -> int:
        """Gets or sets the number of frames cached during replay."""
        dotnet_result = self._dotnet_instance.FrameCacheSize
        return _wrap(dotnet_result)

    @frame_cache_size.setter
    def frame_cache_size(self, value: int):
        """Gets or sets the number of frames cached during replay."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FrameCacheSize = next(unwrapped)

    @property
    def loop_rate(self) -> int:
        """Gets or sets the rate in hertz at which the frames to send in the outgoing queue are updated. This property does not affect the actual update rate of frames on the CAN bus."""
        dotnet_result = self._dotnet_instance.LoopRate
        return _wrap(dotnet_result)

    @loop_rate.setter
    def loop_rate(self, value: int):
        """Gets or sets the rate in hertz at which the frames to send in the outgoing queue are updated. This property does not affect the actual update rate of frames on the CAN bus."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LoopRate = next(unwrapped)

    @property
    def frame_i_ds(self) -> Sequence[str]:
        """Gets or sets the IDs of the frames in the log file that are included or excluded from the file replay when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay.Behavior" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.ExcludeFrameIDs" crefType="Unqualified" /> or <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.IncludeFrameIDs" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.FrameIDs
        return _wrap(dotnet_result)

    @frame_i_ds.setter
    def frame_i_ds(self, value: Sequence[str]):
        """Gets or sets the IDs of the frames in the log file that are included or excluded from the file replay when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay.Behavior" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.ExcludeFrameIDs" crefType="Unqualified" /> or <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.IncludeFrameIDs" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FrameIDs = next(unwrapped)

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets or sets the channel used to trigger replay. Replay begins as soon as the value of this channel becomes non-zero. If desired, you can select or configure a channel that triggers multiple replays of the file."""
        dotnet_result = self._dotnet_instance.TriggerChannel
        return _wrap(dotnet_result)

    @trigger_channel.setter
    def trigger_channel(self, value: BaseNode):
        """Gets or sets the channel used to trigger replay. Replay begins as soon as the value of this channel becomes non-zero. If desired, you can select or configure a channel that triggers multiple replays of the file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TriggerChannel = next(unwrapped)

    @overload
    def get_data_file_error(self) -> DataFileError:
        ...

    def get_data_file_error(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataFileError(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_data_file_status(self) -> DataFileStatus:
        ...

    def get_data_file_status(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataFileStatus(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile(*unwrapped)

    @property
    def data_logging_file_type(self) -> FileType:
        """Gets or sets the file type of an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />. Log files can be TDMS or NCL files."""
        dotnet_result = self._dotnet_instance.DataLoggingFileType
        return _wrap(dotnet_result)

    @data_logging_file_type.setter
    def data_logging_file_type(self, value: FileType):
        """Gets or sets the file type of an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />. Log files can be TDMS or NCL files."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DataLoggingFileType = next(unwrapped)

    @property
    def tdms_group_name(self) -> str:
        """Gets or sets the name of the group in the TDMS file to log data to."""
        dotnet_result = self._dotnet_instance.TDMSGroupName
        return _wrap(dotnet_result)

    @tdms_group_name.setter
    def tdms_group_name(self, value: str):
        """Gets or sets the name of the group in the TDMS file to log data to."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TDMSGroupName = next(unwrapped)

    @property
    def tdms_channel_name(self) -> str:
        """Gets or sets the name of the channel in the TDMS file to log data to."""
        dotnet_result = self._dotnet_instance.TDMSChannelName
        return _wrap(dotnet_result)

    @tdms_channel_name.setter
    def tdms_channel_name(self, value: str):
        """Gets or sets the name of the channel in the TDMS file to log data to."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TDMSChannelName = next(unwrapped)

    @property
    def limit_type(self) -> FileLimitationType:
        """Gets or sets the criteria to use to stop logging data to the current file. When the limit you specify occurs, NI VeriStand either stops logging completely or continues logging in a new file, depending on the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Operation" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.LimitType
        return _wrap(dotnet_result)

    @limit_type.setter
    def limit_type(self, value: FileLimitationType):
        """Gets or sets the criteria to use to stop logging data to the current file. When the limit you specify occurs, NI VeriStand either stops logging completely or continues logging in a new file, depending on the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Operation" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LimitType = next(unwrapped)

    @property
    def trigger_type(self) -> DataLoggingTriggerType:
        """Gets or sets the type of trigger to use to start or stop data logging."""
        dotnet_result = self._dotnet_instance.TriggerType
        return _wrap(dotnet_result)

    @trigger_type.setter
    def trigger_type(self, value: DataLoggingTriggerType):
        """Gets or sets the type of trigger to use to start or stop data logging."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TriggerType = next(unwrapped)

    @property
    def filter(self) -> DataLoggingFilterType:
        """Gets or sets whether and how to filter the logged frames."""
        dotnet_result = self._dotnet_instance.Filter
        return _wrap(dotnet_result)

    @filter.setter
    def filter(self, value: DataLoggingFilterType):
        """Gets or sets whether and how to filter the logged frames."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Filter = next(unwrapped)

    @property
    def operation(self) -> DataLoggingOperationType:
        """Gets or sets the action to take when a trigger condition is met."""
        dotnet_result = self._dotnet_instance.Operation
        return _wrap(dotnet_result)

    @operation.setter
    def operation(self, value: DataLoggingOperationType):
        """Gets or sets the action to take when a trigger condition is met."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Operation = next(unwrapped)

    @property
    def buffer_time(self) -> float:
        """Gets or sets the buffer time of the log file in seconds. Frames read will be added to the buffer until the specified amount of time has elapsed, at which point all buffered data will be written to the file.  If the buffer is partially full when a file is finished, the remaining data in the buffer will be written to the file.  If the buffer time is set to 0, data will be immediately written to the file when read."""
        dotnet_result = self._dotnet_instance.BufferTime
        return _wrap(dotnet_result)

    @buffer_time.setter
    def buffer_time(self, value: float):
        """Gets or sets the buffer time of the log file in seconds. Frames read will be added to the buffer until the specified amount of time has elapsed, at which point all buffered data will be written to the file.  If the buffer is partially full when a file is finished, the remaining data in the buffer will be written to the file.  If the buffer time is set to 0, data will be immediately written to the file when read."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BufferTime = next(unwrapped)

    @property
    def destination(self) -> str:
        """Gets or sets the destination for a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" /> on disk."""
        dotnet_result = self._dotnet_instance.Destination
        return _wrap(dotnet_result)

    @destination.setter
    def destination(self, value: str):
        """Gets or sets the destination for a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" /> on disk."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Destination = next(unwrapped)

    @property
    def filename(self) -> str:
        """Gets or sets the filename of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.Filename
        return _wrap(dotnet_result)

    @filename.setter
    def filename(self, value: str):
        """Gets or sets the filename of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Filename = next(unwrapped)

    @property
    def retriggerable(self) -> bool:
        """Gets or sets whether logging can be retriggered after a stop. If <see langword="true" />, logging begins again when the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerChannel" crefType="Unqualified" /> reaches the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.Retriggerable
        return _wrap(dotnet_result)

    @retriggerable.setter
    def retriggerable(self, value: bool):
        """Gets or sets whether logging can be retriggered after a stop. If <see langword="true" />, logging begins again when the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerChannel" crefType="Unqualified" /> reaches the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Retriggerable = next(unwrapped)

    @property
    def limit_value(self) -> int:
        """Gets or sets the value used to determine when to stop logging data to the current log file. This property can represent a size in kilobytes or a time in seconds, depending on the file's <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.LimitType" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.LimitValue
        return _wrap(dotnet_result)

    @limit_value.setter
    def limit_value(self, value: int):
        """Gets or sets the value used to determine when to stop logging data to the current log file. This property can represent a size in kilobytes or a time in seconds, depending on the file's <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.LimitType" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LimitValue = next(unwrapped)

    @property
    def number_of_bytes_to_read(self) -> int:
        """Gets or sets the maximum number of raw bytes to read. This number does not represent the number of frames to read. CAN and LIN frames are always 24 bytes long. FlexRay frames vary in length."""
        dotnet_result = self._dotnet_instance.NumberOfBytesToRead
        return _wrap(dotnet_result)

    @number_of_bytes_to_read.setter
    def number_of_bytes_to_read(self, value: int):
        """Gets or sets the maximum number of raw bytes to read. This number does not represent the number of frames to read. CAN and LIN frames are always 24 bytes long. FlexRay frames vary in length."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.NumberOfBytesToRead = next(unwrapped)

    @property
    def trigger_channel(self) -> BaseNode:
        """The channel to watch for the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.TriggerChannel
        return _wrap(dotnet_result)

    @trigger_channel.setter
    def trigger_channel(self, value: BaseNode):
        """The channel to watch for the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TriggerChannel = next(unwrapped)

    @property
    def frame_i_ds(self) -> Sequence[str]:
        """Gets or sets the frame IDs in the XNET database cluster to either include in or exclude from data logging. Use this property when you configure a <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Filter" crefType="Unqualified" /> for the data logging file."""
        dotnet_result = self._dotnet_instance.FrameIDs
        return _wrap(dotnet_result)

    @frame_i_ds.setter
    def frame_i_ds(self, value: Sequence[str]):
        """Gets or sets the frame IDs in the XNET database cluster to either include in or exclude from data logging. Use this property when you configure a <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Filter" crefType="Unqualified" /> for the data logging file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FrameIDs = next(unwrapped)

    @overload
    def get_data_file_error(self) -> DataFileError:
        ...

    def get_data_file_error(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataFileError(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_data_file_status(self) -> DataFileStatus:
        ...

    def get_data_file_status(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataFileStatus(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataFileReplayList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_data_file_replay(self, data_file_replay: DataFileReplay) -> bool:
        ...

    def add_data_file_replay(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddDataFileReplay(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetReflectiveMemory(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_reflective_memory(self, name: str) -> bool:
        ...

    def add_reflective_memory(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddReflectiveMemory(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.DynamicDataSize
        return _wrap(dotnet_result)

    @dynamic_data_size.setter
    def dynamic_data_size(self, value: int):
        """Gets or sets the number of channels in reflective memory to reserve for dynamically mapping channel data at run-time. For example, in a distributed system, if target A needs to access data provided by a channel on target B at run-time, the targets require a channel in reflective memory that target B can copy data to and target A can read data from."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DynamicDataSize = next(unwrapped)

    @overload
    def get_reflective_memory_network(self) -> ReflectiveMemoryNetwork:
        ...

    def get_reflective_memory_network(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetReflectiveMemoryNetwork(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_reflective_memory_network(self, name: str) -> bool:
        ...

    def add_reflective_memory_network(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddReflectiveMemoryNetwork(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Database(*unwrapped)

    @property
    def md5(self) -> Sequence[int]:
        """Gets the MD5 message-digest for the database as a byte array."""
        dotnet_result = self._dotnet_instance.MD5
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Dwell(*unwrapped)

    @property
    def dwell_time_constant(self) -> float:
        """Gets the constant value that determines the amount of time to suspend the procedure."""
        dotnet_result = self._dotnet_instance.DwellTimeConstant
        return _wrap(dotnet_result)

    @property
    def dwell_time_channel(self) -> BaseNode:
        """Gets the channel whose value determines the amount of time to suspend the procedure."""
        dotnet_result = self._dotnet_instance.DwellTimeChannel
        return _wrap(dotnet_result)

    @property
    def dwell_time_is_constant(self) -> int:
        """Gets whether the amount of time to suspend the procedure is determined by a constant value or by a channel value."""
        dotnet_result = self._dotnet_instance.DwellTimeIsConstant
        return _wrap(dotnet_result)

    @overload
    def set_dwell_time(self, dwell_time: float):
        ...

    @overload
    def set_dwell_time(self, dwell_time: BaseNode):
        ...

    def set_dwell_time(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDwellTime(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.MD5
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.End(*unwrapped)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSignalBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]:
        ...

    def get_raw_data_based_frame_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetRawDataBasedFrameList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool:
        ...

    def add_signal_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddSignalBasedFrame(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool:
        ...

    def add_raw_data_based_frame(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddRawDataBasedFrame(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModelCommand(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_model_status(self) -> ModelStatus:
        ...

    def get_model_status(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModelStatus(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_model_time(self) -> ModelTime:
        ...

    def get_model_time(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModelTime(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ExitSubroutine(*unwrapped)


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
        unwrapped = _unwrap({(str,): (1, NationalInstruments.VeriStand.Error.NoError), (): (0, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddFPGADevice(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_fpga_device_list(self) -> Sequence[FPGADevice]:
        ...

    def get_fpga_device_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFPGADeviceList(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCategoryList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_channel_list(self) -> Sequence[FPGAChannel]:
        ...

    def get_channel_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetChannelList(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the FPGA channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialValue = next(unwrapped)

    @property
    def channel_bit_offset(self) -> int:
        """Gets the bit offset of the FPGA channel in the DMA packet."""
        dotnet_result = self._dotnet_instance.ChannelBitOffset
        return _wrap(dotnet_result)

    @property
    def fxpiwl(self) -> int:
        """Gets the integer word length of a fixed-point FPGA channel."""
        dotnet_result = self._dotnet_instance.FXPIWL
        return _wrap(dotnet_result)

    @property
    def fxpwl(self) -> int:
        """Gets the word length of a fixed-point FPGA channel."""
        dotnet_result = self._dotnet_instance.FXPWL
        return _wrap(dotnet_result)

    @property
    def offset(self) -> float:
        """Gets or sets the offset of the FPGA channel."""
        dotnet_result = self._dotnet_instance.Offset
        return _wrap(dotnet_result)

    @offset.setter
    def offset(self, value: float):
        """Gets or sets the offset of the FPGA channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Offset = next(unwrapped)

    @property
    def packet_index(self) -> int:
        """Gets the index of the packet in the DMA FIFO that defines the channel."""
        dotnet_result = self._dotnet_instance.PacketIndex
        return _wrap(dotnet_result)

    @property
    def period_pwm(self) -> int:
        """Gets or sets the pulse width modulation (PWM) period for an output channel."""
        dotnet_result = self._dotnet_instance.PeriodPWM
        return _wrap(dotnet_result)

    @period_pwm.setter
    def period_pwm(self, value: int):
        """Gets or sets the pulse width modulation (PWM) period for an output channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PeriodPWM = next(unwrapped)

    @property
    def representation(self) -> int:
        """Gets the data type of the FPGA channel as it is represented in the DMA packet."""
        dotnet_result = self._dotnet_instance.Representation
        return _wrap(dotnet_result)

    @property
    def scaling(self) -> float:
        """Gets or sets the scaling value applied to a channel."""
        dotnet_result = self._dotnet_instance.Scaling
        return _wrap(dotnet_result)

    @scaling.setter
    def scaling(self, value: float):
        """Gets or sets the scaling value applied to a channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Scaling = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice(*unwrapped)

    @property
    def read_packets(self) -> int:
        """Gets the number of DMA read packets."""
        dotnet_result = self._dotnet_instance.ReadPackets
        return _wrap(dotnet_result)

    @property
    def write_packets(self) -> int:
        """Gets the number of DMA write packets."""
        dotnet_result = self._dotnet_instance.WritePackets
        return _wrap(dotnet_result)

    @property
    def fpga_config_file(self) -> DependentFile:
        """Gets the FPGA configuration file used to define the FPGA target."""
        dotnet_result = self._dotnet_instance.FPGAConfigFile
        return _wrap(dotnet_result)

    @property
    def fpga_bitfile(self) -> DependentFile:
        """Gets the name of the FPGA bitfile used for the FPGA target."""
        dotnet_result = self._dotnet_instance.FPGABitfile
        return _wrap(dotnet_result)

    @property
    def latest_refresh(self) -> str:
        """Gets a timestamp indicating the last date and time that the FPGA configuration file, which specifies the content of the DMA FIFOs and how the device appears in System Explorer, was refreshed. Refreshing the configuration file essentially re-creates the device."""
        dotnet_result = self._dotnet_instance.LatestRefresh
        return _wrap(dotnet_result)

    @overload
    def change_rio_address(self, address_number: int) -> bool:
        ...

    def change_rio_address(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.ChangeRIOAddress(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_category_list(self) -> Sequence[FPGACategory]:
        ...

    def get_category_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCategoryList(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFlexRayPortList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_flex_ray_port(self, flex_ray_port: FlexRayPort) -> bool:
        ...

    def add_flex_ray_port(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddFlexRayPort(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetPOCStateChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_clock_correction_failed_channel(self) -> Channel:
        ...

    def get_clock_correction_failed_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetClockCorrectionFailedChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_passive_to_active_count_channel(self) -> Channel:
        ...

    def get_passive_to_active_count_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetPassiveToActiveCountChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_channel_a_sleep_channel(self) -> Channel:
        ...

    def get_channel_a_sleep_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetChannelASleepChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_channel_b_sleep_channel(self) -> Channel:
        ...

    def get_channel_b_sleep_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetChannelBSleepChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_fault_channel(self) -> Channel:
        ...

    def get_fault_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFaultChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_fault_code_channel(self) -> Channel:
        ...

    def get_fault_code_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFaultCodeChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_poc_state_channel(self) -> Channel:
        ...

    def create_poc_state_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreatePOCStateChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_clock_correction_failed_channel(self) -> Channel:
        ...

    def create_clock_correction_failed_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateClockCorrectionFailedChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_passive_to_active_count_channel(self) -> Channel:
        ...

    def create_passive_to_active_count_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreatePassiveToActiveCountChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_channel_a_sleep_channel(self) -> Channel:
        ...

    def create_channel_a_sleep_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateChannelASleepChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_channel_b_sleep_channel(self) -> Channel:
        ...

    def create_channel_b_sleep_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateChannelBSleepChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_fault_channel(self) -> Channel:
        ...

    def create_fault_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateFaultChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_fault_code_channel(self) -> Channel:
        ...

    def create_fault_code_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateFaultCodeChannel(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort(*unwrapped)

    @property
    def disabled(self) -> bool:
        """Gets or sets whether the port is disabled."""
        dotnet_result = self._dotnet_instance.Disabled
        return _wrap(dotnet_result)

    @disabled.setter
    def disabled(self, value: bool):
        """Gets or sets whether the port is disabled."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Disabled = next(unwrapped)

    @property
    def termination(self) -> XNETTermination:
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. This setting applies to both FlexRay communication channels (A and B) on each FlexRay interface."""
        dotnet_result = self._dotnet_instance.Termination
        return _wrap(dotnet_result)

    @termination.setter
    def termination(self, value: XNETTermination):
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. This setting applies to both FlexRay communication channels (A and B) on each FlexRay interface."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Termination = next(unwrapped)

    @property
    def input_stream_read_time(self) -> float:
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        dotnet_result = self._dotnet_instance.InputStreamReadTime
        return _wrap(dotnet_result)

    @input_stream_read_time.setter
    def input_stream_read_time(self, value: float):
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InputStreamReadTime = next(unwrapped)

    @property
    def enable_passive_to_active(self) -> int:
        """Corresponds to the `Interface:FlexRay:Allow Passive to Active` property for the FlexRay port."""
        dotnet_result = self._dotnet_instance.EnablePassiveToActive
        return _wrap(dotnet_result)

    @enable_passive_to_active.setter
    def enable_passive_to_active(self, value: int):
        """Corresponds to the `Interface:FlexRay:Allow Passive to Active` property for the FlexRay port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnablePassiveToActive = next(unwrapped)

    @property
    def port_number(self) -> int:
        """Gets or sets the physical address of the FlexRay port."""
        dotnet_result = self._dotnet_instance.PortNumber
        return _wrap(dotnet_result)

    @port_number.setter
    def port_number(self, value: int):
        """Gets or sets the physical address of the FlexRay port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PortNumber = next(unwrapped)

    @property
    def linked_database(self) -> BaseNode:
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.LinkedDatabase
        return _wrap(dotnet_result)

    @linked_database.setter
    def linked_database(self, value: BaseNode):
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LinkedDatabase = next(unwrapped)

    @property
    def baud_rate(self) -> int:
        """Gets or sets the baud rate that all cluster nodes use."""
        dotnet_result = self._dotnet_instance.BaudRate
        return _wrap(dotnet_result)

    @baud_rate.setter
    def baud_rate(self, value: int):
        """Gets or sets the baud rate that all cluster nodes use."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BaudRate = next(unwrapped)

    @property
    def cluster_name(self) -> str:
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.ClusterName
        return _wrap(dotnet_result)

    @cluster_name.setter
    def cluster_name(self, value: str):
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ClusterName = next(unwrapped)

    @property
    def enable_cold_start(self) -> bool:
        """Gets or sets whether the FlexRay interface operates as a cold-start node on the cluster."""
        dotnet_result = self._dotnet_instance.EnableColdStart
        return _wrap(dotnet_result)

    @enable_cold_start.setter
    def enable_cold_start(self, value: bool):
        """Gets or sets whether the FlexRay interface operates as a cold-start node on the cluster."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnableColdStart = next(unwrapped)

    @property
    def key_slot(self) -> int:
        """Gets or sets the FlexRay slot number from which the XNET FlexRay interface transmits a startup frame during the process of integration with other cluster nodes."""
        dotnet_result = self._dotnet_instance.KeySlot
        return _wrap(dotnet_result)

    @key_slot.setter
    def key_slot(self, value: int):
        """Gets or sets the FlexRay slot number from which the XNET FlexRay interface transmits a startup frame during the process of integration with other cluster nodes."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.KeySlot = next(unwrapped)

    @property
    def incoming_rate(self) -> int:
        """Gets or sets the processing rate for incoming frames in hertz."""
        dotnet_result = self._dotnet_instance.IncomingRate
        return _wrap(dotnet_result)

    @incoming_rate.setter
    def incoming_rate(self, value: int):
        """Gets or sets the processing rate for incoming frames in hertz."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IncomingRate = next(unwrapped)

    @property
    def outgoing_rate(self) -> int:
        """Gets or sets the processing rate for outgoing frames in hertz."""
        dotnet_result = self._dotnet_instance.OutgoingRate
        return _wrap(dotnet_result)

    @outgoing_rate.setter
    def outgoing_rate(self, value: int):
        """Gets or sets the processing rate for outgoing frames in hertz."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.OutgoingRate = next(unwrapped)

    @property
    def echo(self) -> bool:
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        dotnet_result = self._dotnet_instance.Echo
        return _wrap(dotnet_result)

    @echo.setter
    def echo(self, value: bool):
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Echo = next(unwrapped)

    @property
    def input_stream_queue_size(self) -> int:
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        dotnet_result = self._dotnet_instance.InputStreamQueueSize
        return _wrap(dotnet_result)

    @input_stream_queue_size.setter
    def input_stream_queue_size(self, value: int):
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InputStreamQueueSize = next(unwrapped)

    @property
    def inline_incoming(self) -> bool:
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        dotnet_result = self._dotnet_instance.InlineIncoming
        return _wrap(dotnet_result)

    @inline_incoming.setter
    def inline_incoming(self, value: bool):
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InlineIncoming = next(unwrapped)

    @property
    def inline_outgoing(self) -> bool:
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        dotnet_result = self._dotnet_instance.InlineOutgoing
        return _wrap(dotnet_result)

    @inline_outgoing.setter
    def inline_outgoing(self, value: bool):
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InlineOutgoing = next(unwrapped)

    @overload
    def get_interface_section(self) -> FlexRayInterfaceChannels:
        ...

    def get_interface_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetInterfaceSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_interface_section(self) -> FlexRayInterfaceChannels:
        ...

    def create_interface_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateInterfaceSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_incoming(self) -> Incoming:
        ...

    def get_incoming(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetIncoming(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_outgoing(self) -> Outgoing:
        ...

    def get_outgoing(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetOutgoing(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSkipCyclicFrames(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_transmit_time(self) -> TransmitTime:
        ...

    def get_transmit_time(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTransmitTime(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.ID
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetReceiveTime(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_time_difference(self) -> TimeDifference:
        ...

    def get_time_difference(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTimeDifference(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_frame_id(self) -> FrameID:
        ...

    def get_frame_id(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFrameID(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStimulusChannelList(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel(*unwrapped)

    @property
    def label(self) -> BaseNode:
        """Gets or sets the procedure step to execute when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel" crefType="Unqualified" /> step is executed."""
        dotnet_result = self._dotnet_instance.Label
        return _wrap(dotnet_result)

    @label.setter
    def label(self, value: BaseNode):
        """Gets or sets the procedure step to execute when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel" crefType="Unqualified" /> step is executed."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Label = next(unwrapped)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetChassisList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_slsc(self) -> SLSC:
        ...

    def get_slsc(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSLSC(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_chassis(self, chassis: Chassis) -> bool:
        ...

    def add_chassis(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddChassis(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_chassis(self, name: str) -> Chassis:
        ...

    def add_new_chassis(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewChassis(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSinglePoint(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_raw_frame_data_logging(self) -> RawFrameDataLogging:
        ...

    def get_raw_frame_data_logging(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetRawFrameDataLogging(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @initial_value.setter
    def initial_value(self, value: Union[System.Array[System.Double], Sequence[Sequence[float]]]):
        """Gets or sets the initial value of the model inport."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialValue = next(unwrapped)

    @property
    def index(self) -> int:
        """Gets the index of the inport in the inport vector (array)."""
        dotnet_result = self._dotnet_instance.Index
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetInports(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_inport_groups(self) -> Sequence[InportGroup]:
        ...

    def get_inport_groups(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetInportGroups(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.InputOverflowChannel(*unwrapped)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLINPortList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_lin_port(self, lin_port: LINPort) -> bool:
        ...

    def add_lin_port(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddLINPort(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCommunicationStateChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_fault_channel(self) -> Channel:
        ...

    def get_fault_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFaultChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_fault_code_channel(self) -> Channel:
        ...

    def get_fault_code_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFaultCodeChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_last_error_channel(self) -> Channel:
        ...

    def get_last_error_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLastErrorChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_last_error_expected_channel(self) -> Channel:
        ...

    def get_last_error_expected_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLastErrorExpectedChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_last_error_identifier_channel(self) -> Channel:
        ...

    def get_last_error_identifier_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLastErrorIdentifierChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_last_error_received_channel(self) -> Channel:
        ...

    def get_last_error_received_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLastErrorReceivedChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_last_error_timestamp_channel(self) -> Channel:
        ...

    def get_last_error_timestamp_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLastErrorTimestampChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_sleep_channel(self) -> Channel:
        ...

    def get_sleep_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSleepChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_transceiver_ready_channel(self) -> Channel:
        ...

    def get_transceiver_ready_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTransceiverReadyChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_communication_state_channel(self) -> Channel:
        ...

    def create_communication_state_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateCommunicationStateChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_fault_channel(self) -> Channel:
        ...

    def create_fault_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateFaultChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_fault_code_channel(self) -> Channel:
        ...

    def create_fault_code_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateFaultCodeChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_last_error_channel(self) -> Channel:
        ...

    def create_last_error_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateLastErrorChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_last_error_expected_channel(self) -> Channel:
        ...

    def create_last_error_expected_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateLastErrorExpectedChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_last_error_identifier_channel(self) -> Channel:
        ...

    def create_last_error_identifier_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateLastErrorIdentifierChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_last_error_received_channel(self) -> Channel:
        ...

    def create_last_error_received_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateLastErrorReceivedChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_last_error_timestamp_channel(self) -> Channel:
        ...

    def create_last_error_timestamp_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateLastErrorTimestampChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_sleep_channel(self) -> Channel:
        ...

    def create_sleep_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateSleepChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_transceiver_state_channel(self) -> Channel:
        ...

    def create_transceiver_state_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateTransceiverStateChannel(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort(*unwrapped)

    @property
    def disabled(self) -> bool:
        """Gets or sets whether the port is disabled."""
        dotnet_result = self._dotnet_instance.Disabled
        return _wrap(dotnet_result)

    @disabled.setter
    def disabled(self, value: bool):
        """Gets or sets whether the port is disabled."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Disabled = next(unwrapped)

    @property
    def termination(self) -> XNETTermination:
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. You can select <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.Off" crefType="Unqualified" /> (disabled) and <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.On" crefType="Unqualified" /> (enabled)."""
        dotnet_result = self._dotnet_instance.Termination
        return _wrap(dotnet_result)

    @termination.setter
    def termination(self, value: XNETTermination):
        """Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. You can select <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.Off" crefType="Unqualified" /> (disabled) and <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.On" crefType="Unqualified" /> (enabled)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Termination = next(unwrapped)

    @property
    def input_stream_read_time(self) -> float:
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        dotnet_result = self._dotnet_instance.InputStreamReadTime
        return _wrap(dotnet_result)

    @input_stream_read_time.setter
    def input_stream_read_time(self, value: float):
        """Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InputStreamReadTime = next(unwrapped)

    @property
    def port_number(self) -> int:
        """Gets or sets the physical address of the LIN port."""
        dotnet_result = self._dotnet_instance.PortNumber
        return _wrap(dotnet_result)

    @port_number.setter
    def port_number(self, value: int):
        """Gets or sets the physical address of the LIN port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PortNumber = next(unwrapped)

    @property
    def linked_database(self) -> BaseNode:
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.LinkedDatabase
        return _wrap(dotnet_result)

    @linked_database.setter
    def linked_database(self, value: BaseNode):
        """Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LinkedDatabase = next(unwrapped)

    @property
    def baud_rate(self) -> int:
        """Gets or sets the baud rate that all cluster nodes use."""
        dotnet_result = self._dotnet_instance.BaudRate
        return _wrap(dotnet_result)

    @baud_rate.setter
    def baud_rate(self, value: int):
        """Gets or sets the baud rate that all cluster nodes use."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BaudRate = next(unwrapped)

    @property
    def cluster_name(self) -> str:
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.ClusterName
        return _wrap(dotnet_result)

    @cluster_name.setter
    def cluster_name(self, value: str):
        """Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ClusterName = next(unwrapped)

    @property
    def lin_schedules(self) -> str:
        """Gets or sets the names of all the available LIN schedules."""
        dotnet_result = self._dotnet_instance.LINSchedules
        return _wrap(dotnet_result)

    @lin_schedules.setter
    def lin_schedules(self, value: str):
        """Gets or sets the names of all the available LIN schedules."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LINSchedules = next(unwrapped)

    @property
    def incoming_rate(self) -> int:
        """Gets or sets the processing rate for outgoing frames in hertz."""
        dotnet_result = self._dotnet_instance.IncomingRate
        return _wrap(dotnet_result)

    @incoming_rate.setter
    def incoming_rate(self, value: int):
        """Gets or sets the processing rate for outgoing frames in hertz."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IncomingRate = next(unwrapped)

    @property
    def outgoing_rate(self) -> int:
        """Gets or sets the processing rate for outgoing frames in hertz."""
        dotnet_result = self._dotnet_instance.OutgoingRate
        return _wrap(dotnet_result)

    @outgoing_rate.setter
    def outgoing_rate(self, value: int):
        """Gets or sets the processing rate for outgoing frames in hertz."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.OutgoingRate = next(unwrapped)

    @property
    def echo(self) -> bool:
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        dotnet_result = self._dotnet_instance.Echo
        return _wrap(dotnet_result)

    @echo.setter
    def echo(self, value: bool):
        """Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Echo = next(unwrapped)

    @property
    def input_stream_queue_size(self) -> int:
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        dotnet_result = self._dotnet_instance.InputStreamQueueSize
        return _wrap(dotnet_result)

    @input_stream_queue_size.setter
    def input_stream_queue_size(self, value: int):
        """Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InputStreamQueueSize = next(unwrapped)

    @property
    def is_master(self) -> bool:
        """Gets or sets whether the port is the master for the network. A LIN network always consists of one master and several slaves. The master transmits the schedule for frame headers, which are remote requests for specific frame IDs."""
        dotnet_result = self._dotnet_instance.IsMaster
        return _wrap(dotnet_result)

    @is_master.setter
    def is_master(self, value: bool):
        """Gets or sets whether the port is the master for the network. A LIN network always consists of one master and several slaves. The master transmits the schedule for frame headers, which are remote requests for specific frame IDs."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IsMaster = next(unwrapped)

    @property
    def inline_incoming(self) -> bool:
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        dotnet_result = self._dotnet_instance.InlineIncoming
        return _wrap(dotnet_result)

    @inline_incoming.setter
    def inline_incoming(self, value: bool):
        """Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InlineIncoming = next(unwrapped)

    @property
    def inline_outgoing(self) -> bool:
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        dotnet_result = self._dotnet_instance.InlineOutgoing
        return _wrap(dotnet_result)

    @inline_outgoing.setter
    def inline_outgoing(self, value: bool):
        """Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InlineOutgoing = next(unwrapped)

    @overload
    def get_interface_section(self) -> LINInterfaceChannels:
        ...

    def get_interface_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetInterfaceSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_interface_section(self) -> LINInterfaceChannels:
        ...

    def create_interface_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateInterfaceSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_incoming(self) -> Incoming:
        ...

    def get_incoming(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetIncoming(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_outgoing(self) -> Outgoing:
        ...

    def get_outgoing(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetOutgoing(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_lin_scheduler(self) -> LINScheduler:
        ...

    def get_lin_scheduler(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetLINScheduler(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.Units
        return _wrap(dotnet_result)

    @property
    def active_schedule(self) -> str:
        """Gets or sets the name of the active LIN schedule."""
        dotnet_result = self._dotnet_instance.ActiveSchedule
        return _wrap(dotnet_result)

    @active_schedule.setter
    def active_schedule(self, value: str):
        """Gets or sets the name of the active LIN schedule."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ActiveSchedule = next(unwrapped)

    @overload
    def set_active_schedule(self, lin_schedules: Sequence[str], active_schedule_index: int) -> bool:
        ...

    @overload
    def set_active_schedule(self, lin_schedules: Sequence[str], active_schedule: str) -> bool:
        ...

    def set_active_schedule(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetActiveSchedule(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDynamicSignal(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_all_dynamic_signals(self) -> Sequence[DynamicSignal]:
        ...

    def get_all_dynamic_signals(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAllDynamicSignals(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_mode_information(self) -> ModeInformation:
        ...

    def get_mode_information(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModeInformation(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_mode_information(self) -> ModeInformation:
        ...

    def create_mode_information(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CreateModeInformation(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_dynamic_signal(self, signal_name: str, description: str, units: str, default_value: float) -> bool:
        ...

    def add_dynamic_signal(self, *args):
        unwrapped = _unwrap({None: (4, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddDynamicSignal(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetReceiveTime(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_time_difference(self) -> ModeTimeDifference:
        ...

    def get_time_difference(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTimeDifference(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveNode(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Model(*unwrapped)

    @_staticproperty
    def automatic_processor_value() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Model.AutomaticProcessorValue
        return _wrap(dotnet_result)

    @property
    def load_success(self) -> bool:
        """Gets whether NI VeriStand loaded the model successfully."""
        dotnet_result = self._dotnet_instance.LoadSuccess
        return _wrap(dotnet_result)

    @property
    def global_parameter_scope(self) -> GlobalParameterScopes:
        """Gets or sets whether global parameters in the current model share their values with other models on the same target."""
        dotnet_result = self._dotnet_instance.GlobalParameterScope
        return _wrap(dotnet_result)

    @global_parameter_scope.setter
    def global_parameter_scope(self, value: GlobalParameterScopes):
        """Gets or sets whether global parameters in the current model share their values with other models on the same target."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.GlobalParameterScope = next(unwrapped)

    @property
    def model_execution_group(self) -> int:
        """Gets or sets the model execution group"""
        dotnet_result = self._dotnet_instance.ModelExecutionGroup
        return _wrap(dotnet_result)

    @model_execution_group.setter
    def model_execution_group(self, value: int):
        """Gets or sets the model execution group"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ModelExecutionGroup = next(unwrapped)

    @property
    def model_descriptor(self) -> IModelDescriptor:
        """Gets the model descriptor"""
        dotnet_result = self._dotnet_instance.ModelDescriptor
        return _wrap(dotnet_result)

    @property
    def base_rate(self) -> float:
        """Gets the base rate of the model in microseconds."""
        dotnet_result = self._dotnet_instance.BaseRate
        return _wrap(dotnet_result)

    @property
    def dll_size(self) -> int:
        """Gets the size, in bytes, of the compiled version of the model (<format type="monospace">.dll</format> file)."""
        dotnet_result = self._dotnet_instance.DLLSize
        return _wrap(dotnet_result)

    @property
    def dll_timestamp(self) -> float:
        """Gets the time at which the model DLL was compiled."""
        dotnet_result = self._dotnet_instance.DLLTimestamp
        return _wrap(dotnet_result)

    @property
    def model_bitness(self) -> int:
        """Gets the bitness of the compiled model (32- or 64-bit)."""
        dotnet_result = self._dotnet_instance.ModelBitness
        return _wrap(dotnet_result)

    @property
    def decimation(self) -> int:
        """Gets or sets the decimation applied to the Primary Control Loop rate to determine the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Model.BaseRate" crefType="Unqualified" /> of the model."""
        dotnet_result = self._dotnet_instance.Decimation
        return _wrap(dotnet_result)

    @decimation.setter
    def decimation(self, value: int):
        """Gets or sets the decimation applied to the Primary Control Loop rate to determine the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Model.BaseRate" crefType="Unqualified" /> of the model."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Decimation = next(unwrapped)

    @property
    def model_timestamp(self) -> float:
        """Gets the time at which the model was last saved."""
        dotnet_result = self._dotnet_instance.ModelTimestamp
        return _wrap(dotnet_result)

    @property
    def processor(self) -> int:
        """Gets or sets the processor on which the Model Execution Loop executes. -2 (AutomaticProcessorValue) automatically assigns the processor to <entity value="quot" />any available<entity value="quot" />."""
        dotnet_result = self._dotnet_instance.Processor
        return _wrap(dotnet_result)

    @processor.setter
    def processor(self, value: int):
        """Gets or sets the processor on which the Model Execution Loop executes. -2 (AutomaticProcessorValue) automatically assigns the processor to <entity value="quot" />any available<entity value="quot" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Processor = next(unwrapped)

    @property
    def show_unnamed_signals(self) -> bool:
        """Gets whether signals without names are visible."""
        dotnet_result = self._dotnet_instance.ShowUnnamedSignals
        return _wrap(dotnet_result)

    @property
    def user_rate(self) -> float:
        """<para>THIS PROPERTY IS OBSOLETE in NI VeriStand 2011 SP1 and later. Use <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Model.BaseRate" crefType="Unqualified" /> instead.</para>
            Gets the user rate of the model."""
        dotnet_result = self._dotnet_instance.UserRate
        return _wrap(dotnet_result)

    @property
    def segment_vectors(self) -> bool:
        """Gets information about whether or not vector inputs, outputs, parameters, and signals were split up into scalar channels when the model was loaded."""
        dotnet_result = self._dotnet_instance.SegmentVectors
        return _wrap(dotnet_result)

    @property
    def md5(self) -> str:
        """Gets the MD5 message-digest for the model."""
        dotnet_result = self._dotnet_instance.MD5
        return _wrap(dotnet_result)

    @property
    def ni_veri_stand_server_port(self) -> int:
        """Gets or sets the network port that the model uses for communication via TCP. This property only applies to uncompiled models from The MathWorks, Inc. Simulink<entity value="reg" /> software. DLLs and <format type="monospace">.lvmodel</format> files do not require a network port."""
        dotnet_result = self._dotnet_instance.NIVeriStandServerPort
        return _wrap(dotnet_result)

    @ni_veri_stand_server_port.setter
    def ni_veri_stand_server_port(self, value: int):
        """Gets or sets the network port that the model uses for communication via TCP. This property only applies to uncompiled models from The MathWorks, Inc. Simulink<entity value="reg" /> software. DLLs and <format type="monospace">.lvmodel</format> files do not require a network port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.NIVeriStandServerPort = next(unwrapped)

    @property
    def dll_path(self) -> DependentFile:
        """Gets a reference to the compiled version of the model (<format type="monospace">.dll</format> file)."""
        dotnet_result = self._dotnet_instance.DLLPath
        return _wrap(dotnet_result)

    @property
    def model_path(self) -> DependentFile:
        """Gets a reference to the uncompiled model file."""
        dotnet_result = self._dotnet_instance.ModelPath
        return _wrap(dotnet_result)

    @property
    def file_version(self) -> str:
        """Gets the model version"""
        dotnet_result = self._dotnet_instance.FileVersion
        return _wrap(dotnet_result)

    @property
    def model_generation_toolchain_version(self) -> str:
        """Version of the tool that was used to generate the model"""
        dotnet_result = self._dotnet_instance.ModelGenerationToolchainVersion
        return _wrap(dotnet_result)

    @property
    def model_author(self) -> str:
        """Author of the model"""
        dotnet_result = self._dotnet_instance.ModelAuthor
        return _wrap(dotnet_result)

    @property
    def target_platforms(self) -> Sequence[str]:
        """Target platforms supported by the model"""
        dotnet_result = self._dotnet_instance.TargetPlatforms
        return _wrap(dotnet_result)

    @property
    def product_name(self) -> str:
        """Gets the product name"""
        dotnet_result = self._dotnet_instance.ProductName
        return _wrap(dotnet_result)

    @property
    def internal_name(self) -> str:
        """Gets the internal name"""
        dotnet_result = self._dotnet_instance.InternalName
        return _wrap(dotnet_result)

    @property
    def company_name(self) -> str:
        """Gets the company name"""
        dotnet_result = self._dotnet_instance.CompanyName
        return _wrap(dotnet_result)

    @property
    def legal_copyright(self) -> str:
        """Gets the legal copyright"""
        dotnet_result = self._dotnet_instance.LegalCopyright
        return _wrap(dotnet_result)

    @property
    def file_description(self) -> str:
        """Gets the file description"""
        dotnet_result = self._dotnet_instance.FileDescription
        return _wrap(dotnet_result)

    @overload
    def get_section_with_all_parameters(self) -> ModelParameters:
        ...

    def get_section_with_all_parameters(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSectionWithAllParameters(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_section_with_all_signals(self) -> ModelSignals:
        ...

    def get_section_with_all_signals(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSectionWithAllSignals(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reload_model_from_path(self, new_path: str, segment_vectors: bool) -> Sequence[str]:
        ...

    @overload
    def reload_model_from_path(self, new_path: str) -> Sequence[str]:
        ...

    def reload_model_from_path(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReloadModelFromPath(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def rename_node(self, new_name: str) -> bool:
        ...

    def rename_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RenameNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_model_details(self) -> System.Collections.Generic.Dictionary[System.String,System.String]:
        ...

    def get_model_details(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModelDetails(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def import_parameters(self, parameters: Iterable[ModelParameter]) -> bool:
        ...

    def import_parameters(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ImportParameters(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def import_signals(self, signals: Iterable[ModelSignal]) -> bool:
        ...

    def import_signals(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ImportSignals(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_parameters(self, parameters: Iterable[ModelParameter]):
        ...

    def remove_parameters(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveParameters(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_signals(self, signals: Iterable[ModelSignal]):
        ...

    def remove_signals(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveSignals(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_execution_section(self) -> Execution:
        ...

    def get_execution_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetExecutionSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_inports_section(self) -> Inports:
        ...

    def get_inports_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetInportsSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_outports_section(self) -> Outports:
        ...

    def get_outports_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetOutportsSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_parameters_section(self) -> ModelParameters:
        ...

    def get_parameters_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetParametersSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_signals_section(self) -> ModelSignals:
        ...

    def get_signals_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSignalsSection(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.InitialState
        return _wrap(dotnet_result)

    @initial_state.setter
    def initial_state(self, value: ModelCommandState):
        """Gets or sets the initial execution state of the model."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialState = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameter(*unwrapped)

    @property
    def model_path(self) -> str:
        """Gets the symbolic path to the parameter within the model."""
        dotnet_result = self._dotnet_instance.ModelPath
        return _wrap(dotnet_result)

    @property
    def expression(self) -> str:
        """Gets the expression of the model parameter."""
        dotnet_result = self._dotnet_instance.Expression
        return _wrap(dotnet_result)

    @property
    def index(self) -> int:
        """Gets the index of the model parameter."""
        dotnet_result = self._dotnet_instance.Index
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameterGroup(*unwrapped)

    @overload
    def get_model_parameter_groups(self) -> Sequence[ModelParameterGroup]:
        ...

    def get_model_parameter_groups(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModelParameterGroups(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_parameters(self) -> Sequence[ModelParameter]:
        ...

    @overload
    def get_parameters(self, deep: bool) -> Sequence[ModelParameter]:
        ...

    def get_parameters(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetParameters(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_model_parameter_group(self, model_parameter_group: ModelParameterGroup) -> bool:
        ...

    def add_model_parameter_group(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddModelParameterGroup(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_model_parameter(self, model_parameter: ModelParameter) -> bool:
        ...

    def add_model_parameter(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddModelParameter(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_model_parameters(self, model_parameters: Sequence[ModelParameter]) -> bool:
        ...

    def add_model_parameters(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddModelParameters(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetParameters(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_model_parameter_groups(self) -> Sequence[ModelParameterGroup]:
        ...

    def get_model_parameter_groups(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModelParameterGroups(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_parameter(self, parameter: ModelParameter) -> bool:
        ...

    def add_parameter(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddParameter(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_parameters(self, model_parameters: Sequence[ModelParameter]) -> bool:
        ...

    def add_parameters(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddParameters(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_model_parameter_group(self, model_parameter_group: ModelParameterGroup) -> bool:
        ...

    def add_model_parameter_group(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddModelParameterGroup(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignal(*unwrapped)

    @property
    def index(self) -> int:
        """Gets the index of the model signal."""
        dotnet_result = self._dotnet_instance.Index
        return _wrap(dotnet_result)

    @property
    def model_path(self) -> str:
        """Gets the symbolic path to the parameter within the model."""
        dotnet_result = self._dotnet_instance.ModelPath
        return _wrap(dotnet_result)

    @property
    def path(self) -> str:
        """Gets the path to the model that contains the signal."""
        dotnet_result = self._dotnet_instance.Path
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignalGroup(*unwrapped)

    @overload
    def get_model_signal_groups(self) -> Sequence[ModelSignalGroup]:
        ...

    def get_model_signal_groups(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModelSignalGroups(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_signals(self) -> Sequence[ModelSignal]:
        ...

    @overload
    def get_signals(self, deep: bool) -> Sequence[ModelSignal]:
        ...

    def get_signals(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSignals(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_model_signal_group(self, model_signal_group: ModelSignalGroup) -> bool:
        ...

    def add_model_signal_group(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddModelSignalGroup(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_model_signal(self, model_signal: ModelSignal) -> bool:
        ...

    def add_model_signal(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddModelSignal(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSignals(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_model_signal_groups(self) -> Sequence[ModelSignalGroup]:
        ...

    def get_model_signal_groups(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModelSignalGroups(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_signal(self, signal: ModelSignal) -> bool:
        ...

    def add_signal(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddSignal(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_model_signal_group(self, model_signal_group: ModelSignalGroup) -> bool:
        ...

    def add_model_signal_group(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddModelSignalGroup(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModels(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_model(self, model: Model) -> bool:
        ...

    def add_model(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddModel(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.MultiplexerValue
        return _wrap(dotnet_result)

    @multiplexer_value.setter
    def multiplexer_value(self, value: int):
        """Gets or sets the value of a multiplexer signal, which defines the dynamic signals to transmit in a given frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.MultiplexerValue = next(unwrapped)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetEventTriggered(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_cyclic(self) -> Cyclic:
        ...

    def get_cyclic(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCyclic(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_cyclic_event(self) -> CyclicEvent:
        ...

    def get_cyclic_event(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCyclicEvent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_data_replay(self) -> DataReplay:
        ...

    def get_data_replay(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataReplay(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_sporadic(self) -> Sporadic:
        ...

    def get_sporadic(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSporadic(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_unconditional(self) -> Unconditional:
        ...

    def get_unconditional(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetUnconditional(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @initial_value.setter
    def initial_value(self, value: Union[System.Array[System.Double], Sequence[Sequence[float]]]):
        """Gets or sets the initial value of the model outport."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialValue = next(unwrapped)

    @property
    def index(self) -> int:
        """Gets the index number of the outport in the outport vector (array)."""
        dotnet_result = self._dotnet_instance.Index
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetOutportGroups(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_outports(self) -> Sequence[Outport]:
        ...

    @overload
    def get_outports(self, deep: bool) -> Sequence[Outport]:
        ...

    def get_outports(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetOutports(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetOutports(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_outport_groups(self) -> Sequence[OutportGroup]:
        ...

    def get_outport_groups(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetOutportGroups(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.OutputUnderflowChannel(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure(*unwrapped)

    @overload
    def reorder_command_list(self, commands: Sequence[Command]) -> bool:
        ...

    def reorder_command_list(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.ReorderCommandList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_command_list(self) -> Sequence[Command]:
        ...

    def get_command_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetCommandList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_command(self, command: Command) -> bool:
        ...

    def add_command(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddCommand(*unwrapped)
        return _wrap(dotnet_result)

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
        unwrapped = _unwrap({(str, str, AlarmPriority, AlarmState, BaseNode, (float, int), BaseNode, BaseNode, (float, int), (float, int)): (10, NationalInstruments.VeriStand.Error.NoError), (str, str, AlarmPriority, AlarmState, BaseNode, (float, int), BaseNode, BaseNode, (float, int), BaseNode): (10, NationalInstruments.VeriStand.Error.NoError), (str, str, AlarmPriority, AlarmState, BaseNode, (float, int), BaseNode, BaseNode, BaseNode, (float, int)): (10, NationalInstruments.VeriStand.Error.NoError), (str, str, AlarmPriority, AlarmState, BaseNode, (float, int), BaseNode, BaseNode, BaseNode, BaseNode): (10, NationalInstruments.VeriStand.Error.NoError), (str, str, AlarmingStepFunction, BaseNode): (4, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewAlarming(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_call_procedure(self, name: str, description: str, procedure: Procedure) -> bool:
        ...

    def add_new_call_procedure(self, *args):
        unwrapped = _unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewCallProcedure(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_condition(self, name: str, description: str, variable: BaseNode, comparison: ConditionStepComparison, value: float, goto_label: Command) -> bool:
        ...

    @overload
    def add_new_condition(self, name: str, description: str, variable: BaseNode, comparison: ConditionStepComparison, value: BaseNode, goto_label: Command) -> bool:
        ...

    def add_new_condition(self, *args):
        unwrapped = _unwrap({(str, str, BaseNode, ConditionStepComparison, (float, int), Command): (6, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, ConditionStepComparison, BaseNode, Command): (6, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewCondition(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_dwell(self, name: str, description: str, dwell_time: float) -> bool:
        ...

    @overload
    def add_new_dwell(self, name: str, description: str, dwell_time: BaseNode) -> bool:
        ...

    def add_new_dwell(self, *args):
        unwrapped = _unwrap({(str, str, (float, int)): (3, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode): (3, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewDwell(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_end(self, name: str, description: str) -> bool:
        ...

    def add_new_end(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewEnd(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_exit_subroutine(self, name: str, description: str) -> bool:
        ...

    def add_new_exit_subroutine(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewExitSubroutine(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_goto_label(self, name: str, description: str, label: Command) -> bool:
        ...

    def add_new_goto_label(self, *args):
        unwrapped = _unwrap({None: (3, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewGotoLabel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_set_multiple_variables(self, name: str, description: str, channels: Sequence[BaseNode], values: Sequence[float]) -> bool:
        ...

    def add_new_set_multiple_variables(self, *args):
        unwrapped = _unwrap({None: (4, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewSetMultipleVariables(*unwrapped)
        return _wrap(dotnet_result)

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
        unwrapped = _unwrap({(str, str, BaseNode, (float, int)): (4, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, BaseNode): (4, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, SetVariableStepFunction, (float, int), (float, int)): (6, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, SetVariableStepFunction, (float, int), BaseNode): (6, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, SetVariableStepFunction, BaseNode, (float, int)): (6, NationalInstruments.VeriStand.Error.NoError), (str, str, BaseNode, SetVariableStepFunction, BaseNode, BaseNode): (6, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewSetVariable(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_real_time_sequence_command(self, name: str, description: str, sequence_command: GlobalSequenceCommand, wait_for_sequences_to_complete: bool, wait_timeout: float, abort_sequences_on_timeout: bool) -> RealTimeSequenceCommand:
        ...

    @overload
    def add_new_real_time_sequence_command(self, name: str, description: str, sequence_command: GlobalSequenceCommand, wait_for_sequences_to_complete: bool, wait_timeout: float, abort_sequences_on_timeout: bool, group_number: int) -> RealTimeSequenceCommand:
        ...

    def add_new_real_time_sequence_command(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddNewRealTimeSequenceCommand(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.StartupProcedure
        return _wrap(dotnet_result)

    @startup_procedure.setter
    def startup_procedure(self, value: Procedure):
        """Gets or sets a value indicating the procedure that runs on startup."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.StartupProcedure = next(unwrapped)

    @overload
    def reorder_procedure_list(self, procedures: Sequence[Procedure]) -> bool:
        ...

    def reorder_procedure_list(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.ReorderProcedureList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_procedures_list(self) -> Sequence[Procedure]:
        ...

    def get_procedures_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetProceduresList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_procedure(self, procedure: Procedure) -> bool:
        ...

    def add_procedure(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddProcedure(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.DefaultValue
        return _wrap(dotnet_result)

    @default_value.setter
    def default_value(self, value: float):
        """Gets or sets the default value of the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DefaultValue = next(unwrapped)

    @property
    def start_bit(self) -> int:
        """Gets or sets the start bit, or the least significant signal bit position in the frame payload. This value determines the signal starting point in the frame."""
        dotnet_result = self._dotnet_instance.StartBit
        return _wrap(dotnet_result)

    @start_bit.setter
    def start_bit(self, value: int):
        """Gets or sets the start bit, or the least significant signal bit position in the frame payload. This value determines the signal starting point in the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.StartBit = next(unwrapped)

    @property
    def number_of_bits(self) -> int:
        """Gets or sets the number of bits the signal uses in the frame payload."""
        dotnet_result = self._dotnet_instance.NumberOfBits
        return _wrap(dotnet_result)

    @number_of_bits.setter
    def number_of_bits(self, value: int):
        """Gets or sets the number of bits the signal uses in the frame payload."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.NumberOfBits = next(unwrapped)

    @property
    def enable64_bit(self) -> bool:
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        dotnet_result = self._dotnet_instance.Enable64Bit
        return _wrap(dotnet_result)

    @enable64_bit.setter
    def enable64_bit(self, value: bool):
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Enable64Bit = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame(*unwrapped)

    @property
    def transmit_trigger(self) -> FrameTriggerType:
        """Gets the trigger type (channel value change, trigger channel not zero, and so on) specified for an event-triggered frame."""
        dotnet_result = self._dotnet_instance.TransmitTrigger
        return _wrap(dotnet_result)

    @property
    def phase(self) -> FramePhaseType:
        """Gets or sets whether to reset the timer after the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        dotnet_result = self._dotnet_instance.Phase
        return _wrap(dotnet_result)

    @phase.setter
    def phase(self, value: FramePhaseType):
        """Gets or sets whether to reset the timer after the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Phase = next(unwrapped)

    @property
    def frame_type(self) -> FrameType:
        """Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port."""
        dotnet_result = self._dotnet_instance.FrameType
        return _wrap(dotnet_result)

    @frame_type.setter
    def frame_type(self, value: FrameType):
        """Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FrameType = next(unwrapped)

    @property
    def id(self) -> int:
        """Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent."""
        dotnet_result = self._dotnet_instance.ID
        return _wrap(dotnet_result)

    @id.setter
    def id(self, value: int):
        """Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ID = next(unwrapped)

    @property
    def payload_length(self) -> int:
        """Gets or sets the number of bytes in the payload of the frame."""
        dotnet_result = self._dotnet_instance.PayloadLength
        return _wrap(dotnet_result)

    @payload_length.setter
    def payload_length(self, value: int):
        """Gets or sets the number of bytes in the payload of the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PayloadLength = next(unwrapped)

    @property
    def md5(self) -> Sequence[int]:
        """Gets the MD5 message digest for the frame."""
        dotnet_result = self._dotnet_instance.MD5
        return _wrap(dotnet_result)

    @property
    def start_time_offset(self) -> float:
        """Gets or sets the amount of time that elapses between the session start and the transmission of the first frame."""
        dotnet_result = self._dotnet_instance.StartTimeOffset
        return _wrap(dotnet_result)

    @start_time_offset.setter
    def start_time_offset(self, value: float):
        """Gets or sets the amount of time that elapses between the session start and the transmission of the first frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.StartTimeOffset = next(unwrapped)

    @property
    def enable64_bit(self) -> bool:
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        dotnet_result = self._dotnet_instance.Enable64Bit
        return _wrap(dotnet_result)

    @enable64_bit.setter
    def enable64_bit(self, value: bool):
        """Gets or sets whether U64 bitfield representation is enabled for the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Enable64Bit = next(unwrapped)

    @property
    def owning_database(self) -> BaseNode:
        """Gets or sets a reference to the XNET database that contains the frame."""
        dotnet_result = self._dotnet_instance.OwningDatabase
        return _wrap(dotnet_result)

    @owning_database.setter
    def owning_database(self, value: BaseNode):
        """Gets or sets a reference to the XNET database that contains the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.OwningDatabase = next(unwrapped)

    @property
    def cluster_name(self) -> str:
        """Gets or sets the name of the cluster in the XNET database that contains the frame."""
        dotnet_result = self._dotnet_instance.ClusterName
        return _wrap(dotnet_result)

    @cluster_name.setter
    def cluster_name(self, value: str):
        """Gets or sets the name of the cluster in the XNET database that contains the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ClusterName = next(unwrapped)

    @property
    def database_alias(self) -> str:
        """Gets or sets the alias for the XNET database that contains the frame."""
        dotnet_result = self._dotnet_instance.DatabaseAlias
        return _wrap(dotnet_result)

    @database_alias.setter
    def database_alias(self, value: str):
        """Gets or sets the alias for the XNET database that contains the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DatabaseAlias = next(unwrapped)

    @property
    def disabled(self) -> bool:
        """Gets whether transmission of the outgoing frame is disabled."""
        dotnet_result = self._dotnet_instance.Disabled
        return _wrap(dotnet_result)

    @property
    def enable_software_cyclic_trigger(self) -> bool:
        """Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame."""
        dotnet_result = self._dotnet_instance.EnableSoftwareCyclicTrigger
        return _wrap(dotnet_result)

    @enable_software_cyclic_trigger.setter
    def enable_software_cyclic_trigger(self, value: bool):
        """Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnableSoftwareCyclicTrigger = next(unwrapped)

    @property
    def enable_frame_cyclic_trigger(self) -> bool:
        """Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame."""
        dotnet_result = self._dotnet_instance.EnableFrameCyclicTrigger
        return _wrap(dotnet_result)

    @enable_frame_cyclic_trigger.setter
    def enable_frame_cyclic_trigger(self, value: bool):
        """Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnableFrameCyclicTrigger = next(unwrapped)

    @property
    def disable_channel(self) -> BaseNode:
        """Gets a reference to the disable channel for the frame. A disable channel disables transmission of an outgoing frame when the value of the disable channel is non-zero."""
        dotnet_result = self._dotnet_instance.DisableChannel
        return _wrap(dotnet_result)

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets a reference to the channel that is checked for a non-zero value when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableFrameCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        dotnet_result = self._dotnet_instance.TriggerChannel
        return _wrap(dotnet_result)

    @property
    def transmit_time(self) -> float:
        """Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        dotnet_result = self._dotnet_instance.TransmitTime
        return _wrap(dotnet_result)

    @transmit_time.setter
    def transmit_time(self, value: float):
        """Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TransmitTime = next(unwrapped)

    @overload
    def create_raw_data_based_channel(self, start_bit: int, number_of_bits: int) -> RawDataBasedChannel:
        ...

    def create_raw_data_based_channel(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateRawDataBasedChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_frame_information(self, create_time_information_channels: bool, create_frame_id: bool) -> FrameInformation:
        ...

    def create_frame_information(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateFrameInformation(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_frame_faulting(self, create_skip_cyclic_frames: bool, create_transmit_time: bool) -> FrameFaulting:
        ...

    def create_frame_faulting(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateFrameFaulting(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_automatic_frame_processing(self) -> AutomaticFrameProcessing:
        ...

    def create_automatic_frame_processing(self, *args):
        unwrapped = _unwrap({None: (0, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateAutomaticFrameProcessing(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def disable_transmission_trigger(self):
        ...

    def disable_transmission_trigger(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DisableTransmissionTrigger(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def enable_transmission_trigger(self, disable_channel: BaseNode):
        ...

    def enable_transmission_trigger(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.EnableTransmissionTrigger(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_transmit_trigger(self, trigger_type: FrameTriggerType, trigger_channel: BaseNode):
        ...

    def set_transmit_trigger(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetTransmitTrigger(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_raw_data_based_channel_list(self) -> Sequence[RawDataBasedChannel]:
        ...

    def get_raw_data_based_channel_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetRawDataBasedChannelList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_frame_information(self) -> FrameInformation:
        ...

    def get_frame_information(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFrameInformation(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_frame_faulting(self) -> FrameFaulting:
        ...

    def get_frame_faulting(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFrameFaulting(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_automatic_frame_processing(self) -> AutomaticFrameProcessing:
        ...

    def get_automatic_frame_processing(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAutomaticFrameProcessing(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataLoggingFileList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_data_logging_file(self, data_logging_file: DataLoggingFile) -> bool:
        ...

    def add_data_logging_file(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddDataLoggingFile(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.RealTimeSequenceCommand(*unwrapped)

    @property
    def sequence_command(self) -> GlobalSequenceCommand:
        """Gets or sets a value indicating the global command to apply to all running real-time sequences."""
        dotnet_result = self._dotnet_instance.SequenceCommand
        return _wrap(dotnet_result)

    @sequence_command.setter
    def sequence_command(self, value: GlobalSequenceCommand):
        """Gets or sets a value indicating the global command to apply to all running real-time sequences."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SequenceCommand = next(unwrapped)

    @property
    def wait_for_sequences_to_complete(self) -> bool:
        """Gets or sets a value indicating whether to wait for all active sequences to complete execution."""
        dotnet_result = self._dotnet_instance.WaitForSequencesToComplete
        return _wrap(dotnet_result)

    @wait_for_sequences_to_complete.setter
    def wait_for_sequences_to_complete(self, value: bool):
        """Gets or sets a value indicating whether to wait for all active sequences to complete execution."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.WaitForSequencesToComplete = next(unwrapped)

    @property
    def abort_sequences_on_timeout(self) -> bool:
        """Gets or sets a value indicating whether to abort all active sequences if the sequence command times out waiting for them to complete."""
        dotnet_result = self._dotnet_instance.AbortSequencesOnTimeout
        return _wrap(dotnet_result)

    @abort_sequences_on_timeout.setter
    def abort_sequences_on_timeout(self, value: bool):
        """Gets or sets a value indicating whether to abort all active sequences if the sequence command times out waiting for them to complete."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AbortSequencesOnTimeout = next(unwrapped)

    @property
    def wait_timeout(self) -> float:
        """Gets or sets a value indicating the maximum amount of time in seconds to wait for all active sequences to complete execution."""
        dotnet_result = self._dotnet_instance.WaitTimeout
        return _wrap(dotnet_result)

    @wait_timeout.setter
    def wait_timeout(self, value: float):
        """Gets or sets a value indicating the maximum amount of time in seconds to wait for all active sequences to complete execution."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.WaitTimeout = next(unwrapped)

    @property
    def group_number(self) -> int:
        """Gets or sets a value indicating the group number for the sequence to stop."""
        dotnet_result = self._dotnet_instance.GroupNumber
        return _wrap(dotnet_result)

    @group_number.setter
    def group_number(self, value: int):
        """Gets or sets a value indicating the group number for the sequence to stop."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.GroupNumber = next(unwrapped)


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
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the <format type="bold">Receive Time</format> channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialValue = next(unwrapped)

    @overload
    def remove_node(self) -> bool:
        ...

    def remove_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveNode(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemory(*unwrapped)

    @property
    def visa_resource(self) -> str:
        """Gets or sets the VISA resource name for the device as it appears in Measurement <entity value="amp" /> Automation Explorer (MAX)."""
        dotnet_result = self._dotnet_instance.VISAResource
        return _wrap(dotnet_result)

    @visa_resource.setter
    def visa_resource(self, value: str):
        """Gets or sets the VISA resource name for the device as it appears in Measurement <entity value="amp" /> Automation Explorer (MAX)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.VISAResource = next(unwrapped)

    @property
    def generate_interrupt(self) -> bool:
        """Gets whether interrupts are enabled for the reflective memory device."""
        dotnet_result = self._dotnet_instance.GenerateInterrupt
        return _wrap(dotnet_result)

    @property
    def interrupt_all_nodes(self) -> bool:
        """Gets whether the device sends interrupt signals to all nodes on the reflective memory network."""
        dotnet_result = self._dotnet_instance.InterruptAllNodes
        return _wrap(dotnet_result)

    @property
    def interrupt_target_node(self) -> int:
        """Gets the decimal ID of the target node to which the reflective memory device sends interrupts."""
        dotnet_result = self._dotnet_instance.InterruptTargetNode
        return _wrap(dotnet_result)

    @property
    def interrupt_type(self) -> int:
        """Gets the type of interrupt the reflective memory device generates."""
        dotnet_result = self._dotnet_instance.InterruptType
        return _wrap(dotnet_result)

    @property
    def interrupt_data_constant(self) -> bool:
        """Gets whether the data included in the interrupt packet is a constant value."""
        dotnet_result = self._dotnet_instance.InterruptDataConstant
        return _wrap(dotnet_result)

    @property
    def interrupt_constant_data(self) -> int:
        """Gets the constant value that is the data included in the interrupt packet."""
        dotnet_result = self._dotnet_instance.InterruptConstantData
        return _wrap(dotnet_result)

    @property
    def interrupt_channel_data(self) -> BaseNode:
        """Gets the channel that provides the data included in the interrupt packet."""
        dotnet_result = self._dotnet_instance.InterruptChannelData
        return _wrap(dotnet_result)

    @overload
    def disable_interrupt(self):
        ...

    def disable_interrupt(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DisableInterrupt(*unwrapped)
        return _wrap(dotnet_result)

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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.EnableInterrupt(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_information_channels(self) -> ReflectiveMemoryInformationChannels:
        ...

    def get_information_channels(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetInformationChannels(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_data_channels(self) -> ReflectiveMemoryDataChannels:
        ...

    def get_data_channels(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataChannels(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannel(*unwrapped)

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of a reflective memory data channel."""
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of a reflective memory data channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialValue = next(unwrapped)

    @property
    def type(self) -> ReflectiveMemoryDataChannelAccessType:
        """Gets or sets the access type (<format type="monospace">Read</format> or <format type="monospace">Write</format>) of a reflective memory data channel."""
        dotnet_result = self._dotnet_instance.Type
        return _wrap(dotnet_result)

    @type.setter
    def type(self, value: ReflectiveMemoryDataChannelAccessType):
        """Gets or sets the access type (<format type="monospace">Read</format> or <format type="monospace">Write</format>) of a reflective memory data channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Type = next(unwrapped)

    @property
    def data_type(self) -> ReflectiveMemoryDataChannelDataType:
        """Gets or sets the data type of a reflective memory data channel."""
        dotnet_result = self._dotnet_instance.DataType
        return _wrap(dotnet_result)

    @data_type.setter
    def data_type(self, value: ReflectiveMemoryDataChannelDataType):
        """Gets or sets the data type of a reflective memory data channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DataType = next(unwrapped)

    @property
    def memory_address(self) -> int:
        """Gets or sets the address for the data channel in reflective memory."""
        dotnet_result = self._dotnet_instance.MemoryAddress
        return _wrap(dotnet_result)

    @memory_address.setter
    def memory_address(self, value: int):
        """Gets or sets the address for the data channel in reflective memory."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.MemoryAddress = next(unwrapped)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataChannels(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_folders(self) -> Sequence[ReflectiveMemoryFolder]:
        ...

    def get_folders(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFolders(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_data_channel(self, reflective_memory_data_channel: ReflectiveMemoryDataChannel) -> bool:
        ...

    def add_data_channel(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddDataChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_folder(self, reflective_memory_folder: ReflectiveMemoryFolder) -> bool:
        ...

    def add_folder(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddFolder(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryFolder(*unwrapped)

    @overload
    def get_data_channels(self) -> Sequence[ReflectiveMemoryDataChannel]:
        ...

    def get_data_channels(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataChannels(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_folders(self) -> Sequence[ReflectiveMemoryFolder]:
        ...

    def get_folders(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetFolders(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_data_channel(self, reflective_memory_data_channel: ReflectiveMemoryDataChannel) -> bool:
        ...

    def add_data_channel(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddDataChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_folder(self, reflective_memory_folder: ReflectiveMemoryFolder) -> bool:
        ...

    def add_folder(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddFolder(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetRingReadLateCount(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_write_late_count(self) -> ReflectiveMemoryWriteLateCount:
        ...

    def get_write_late_count(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetWriteLateCount(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.StartMemoryAddress
        return _wrap(dotnet_result)

    @start_memory_address.setter
    def start_memory_address(self, value: int):
        """Gets or sets the start address in reflective memory that NI VeriStand can use. Use this property together with <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.MaximumEndMemoryAddress" crefType="Unqualified" /> to specify the maximum amount of reflected memory allocated to NI VeriStand."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.StartMemoryAddress = next(unwrapped)

    @property
    def maximum_end_memory_address(self) -> int:
        """Gets or sets the maximum end address in reflective memory that NI VeriStand can use. Use this property together with <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.StartMemoryAddress" crefType="Unqualified" /> to specify the maximum amount of reflected memory allocated to NI VeriStand."""
        dotnet_result = self._dotnet_instance.MaximumEndMemoryAddress
        return _wrap(dotnet_result)

    @maximum_end_memory_address.setter
    def maximum_end_memory_address(self, value: int):
        """Gets or sets the maximum end address in reflective memory that NI VeriStand can use. Use this property together with <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.StartMemoryAddress" crefType="Unqualified" /> to specify the maximum amount of reflected memory allocated to NI VeriStand."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.MaximumEndMemoryAddress = next(unwrapped)

    @property
    def export_memory_table(self) -> bool:
        """Gets or sets whether the memory table that NI VeriStand creates at compile time is exported to a text file."""
        dotnet_result = self._dotnet_instance.ExportMemoryTable
        return _wrap(dotnet_result)

    @export_memory_table.setter
    def export_memory_table(self, value: bool):
        """Gets or sets whether the memory table that NI VeriStand creates at compile time is exported to a text file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ExportMemoryTable = next(unwrapped)

    @property
    def export_memory_table_file(self) -> Sequence[int]:
        """Gets or sets the file path for the text file to export the memory table to at compile time if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.ExportMemoryTable" crefType="Unqualified" /> is <see langword="true" />."""
        dotnet_result = self._dotnet_instance.ExportMemoryTableFile
        return _wrap(dotnet_result)

    @export_memory_table_file.setter
    def export_memory_table_file(self, value: Sequence[int]):
        """Gets or sets the file path for the text file to export the memory table to at compile time if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.ExportMemoryTable" crefType="Unqualified" /> is <see langword="true" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ExportMemoryTableFile = next(unwrapped)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSCXIModules(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_scxi_module(self, scxi_module: SCXIModule) -> bool:
        ...

    def add_scxi_module(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddSCXIModule(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIModule(*unwrapped)

    @property
    def scxi_module_type(self) -> str:
        """Gets the type of the SCXI module."""
        dotnet_result = self._dotnet_instance.SCXIModuleType
        return _wrap(dotnet_result)

    @overload
    def get_analog_inputs(self) -> Sequence[DAQAnalogInput]:
        ...

    def get_analog_inputs(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAnalogInputs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_analog_outputs(self) -> Sequence[DAQAnalogOutput]:
        ...

    def get_analog_outputs(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAnalogOutputs(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_dio_ports(self) -> Sequence[DAQDIOPort]:
        ...

    def get_dio_ports(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDIOPorts(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSLSCChassisList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def export_configuration(self, filepath: str):
        ...

    def export_configuration(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ExportConfiguration(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def import_configurations(self, filepath: str):
        ...

    def import_configurations(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ImportConfigurations(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_slsc_chassis(self, slsc_chassis: SLSCChassis):
        ...

    def add_slsc_chassis(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddSLSCChassis(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis(*unwrapped)

    @property
    def chassis_id(self) -> str:
        """Gets or sets the name or the IP address of the SLSCChassis."""
        dotnet_result = self._dotnet_instance.ChassisID
        return _wrap(dotnet_result)

    @chassis_id.setter
    def chassis_id(self, value: str):
        """Gets or sets the name or the IP address of the SLSCChassis."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ChassisID = next(unwrapped)

    @property
    def username(self) -> str:
        """Gets or sets the username for the SLSCChassis."""
        dotnet_result = self._dotnet_instance.Username
        return _wrap(dotnet_result)

    @username.setter
    def username(self, value: str):
        """Gets or sets the username for the SLSCChassis."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Username = next(unwrapped)

    @property
    def password(self) -> str:
        """Gets or sets the password for the SLSCChassis."""
        dotnet_result = self._dotnet_instance.Password
        return _wrap(dotnet_result)

    @password.setter
    def password(self, value: str):
        """Gets or sets the password for the SLSCChassis."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Password = next(unwrapped)

    @property
    def chassis_type(self) -> str:
        """Gets the type of the SLSCChassis."""
        dotnet_result = self._dotnet_instance.ChassisType
        return _wrap(dotnet_result)

    @property
    def chassis_id_type(self) -> SLSCChassis.SLSCChassisIDType:
        """Gets or sets the mode how the cahssis is defined"""
        dotnet_result = self._dotnet_instance.ChassisIDType
        return _wrap(dotnet_result)

    @chassis_id_type.setter
    def chassis_id_type(self, value: SLSCChassis.SLSCChassisIDType):
        """Gets or sets the mode how the cahssis is defined"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ChassisIDType = next(unwrapped)

    @overload
    def export_configuration(self, filepath: str):
        ...

    def export_configuration(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ExportConfiguration(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_chassis_channels_section(self) -> SLSCChassisChannels:
        ...

    def get_chassis_channels_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetChassisChannelsSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_modules_section(self) -> SLSCModules:
        ...

    def get_modules_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModulesSection(*unwrapped)
        return _wrap(dotnet_result)


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
            dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis.SLSCChassisIDType, "ChassisName")
            return SLSCChassis.SLSCChassisIDType(dotnet_result, "CHASSIS_NAME")

        @_staticproperty
        def HOSTNAME_IP_ADDRESS() -> SLSCChassis.SLSCChassisIDType:
            dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis.SLSCChassisIDType, "HostnameIPAddress")
            return SLSCChassis.SLSCChassisIDType(dotnet_result, "HOSTNAME_IP_ADDRESS")


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
            dotnet_result = getattr(NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis.SLSCChassisType, "e12001_CHASSIS_TYPE")
            return SLSCChassis.SLSCChassisType(dotnet_result, "E12001_CHASSIS_TYPE")


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSLSCChassisChannelList(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetChassisChannelSections(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCModuleCustomDevice(*unwrapped)

    @property
    def slot_number(self) -> int:
        """The slot number of the SLSC chassis with which the custom device is associated."""
        dotnet_result = self._dotnet_instance.SlotNumber
        return _wrap(dotnet_result)

    @overload
    def remove_node(self) -> bool:
        ...

    def remove_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveNode(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetModule(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_module(self, slot_number: int, custom_device: SLSCModuleCustomDevice) -> bool:
        ...

    def set_module(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetModule(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.ScaleType
        return _wrap(dotnet_result)

    @property
    def scale_unit(self) -> str:
        """Gets or sets the scale unit. This can be any arbitrary string."""
        dotnet_result = self._dotnet_instance.ScaleUnit
        return _wrap(dotnet_result)

    @scale_unit.setter
    def scale_unit(self, value: str):
        """Gets or sets the scale unit. This can be any arbitrary string."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ScaleUnit = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ScaleFolder(*unwrapped)

    @overload
    def get_scale_list(self) -> Sequence[Scale]:
        ...

    @overload
    def get_scale_list(self, deep: bool) -> Sequence[Scale]:
        ...

    def get_scale_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetScaleList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_scale_folder_list(self) -> Sequence[ScaleFolder]:
        ...

    @overload
    def get_scale_folder_list(self, deep: bool) -> Sequence[ScaleFolder]:
        ...

    def get_scale_folder_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetScaleFolderList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_scale(self, name: str, type: ScaleType) -> Scale:
        ...

    def create_scale(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateScale(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_scale(self, scale: Scale) -> bool:
        ...

    def add_scale(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddScale(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_scale_folder(self, folder: ScaleFolder) -> bool:
        ...

    def add_scale_folder(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddScaleFolder(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_scale_folder(self, name: str, description: str) -> bool:
        ...

    def add_new_scale_folder(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewScaleFolder(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetScaleList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_scale_folder_list(self) -> Sequence[ScaleFolder]:
        ...

    @overload
    def get_scale_folder_list(self, deep: bool) -> Sequence[ScaleFolder]:
        ...

    def get_scale_folder_list(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetScaleFolderList(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def create_scale(self, name: str, type: ScaleType) -> Scale:
        ...

    def create_scale(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.CreateScale(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_scale(self, scale: Scale) -> bool:
        ...

    def add_scale(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddScale(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_scale_folder(self, folder: ScaleFolder) -> bool:
        ...

    def add_scale_folder(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddScaleFolder(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_new_scale_folder(self, name: str, description: str) -> bool:
        ...

    def add_new_scale_folder(self, *args):
        unwrapped = _unwrap({None: (2, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.AddNewScaleFolder(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SetMultipleVariables(*unwrapped)

    @property
    def channels(self) -> Sequence[BaseNode]:
        """Gets or sets the channels to set to the specified values."""
        dotnet_result = self._dotnet_instance.Channels
        return _wrap(dotnet_result)

    @property
    def values(self) -> Sequence[float]:
        """Gets the values to which this step sets the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetMultipleVariables.Channels" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.Values
        return _wrap(dotnet_result)

    @overload
    def set_channels_and_values(self, channels: Sequence[BaseNode], values: Sequence[float]):
        ...

    def set_channels_and_values(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetChannelsAndValues(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable(*unwrapped)

    @property
    def function(self) -> SetVariableStepFunction:
        """Gets or sets the function (add, subtract, multiply, or divide) to use on the two values that determine the value to set on the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Variable" crefType="Unqualified" /> channel."""
        dotnet_result = self._dotnet_instance.Function
        return _wrap(dotnet_result)

    @function.setter
    def function(self, value: SetVariableStepFunction):
        """Gets or sets the function (add, subtract, multiply, or divide) to use on the two values that determine the value to set on the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Variable" crefType="Unqualified" /> channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Function = next(unwrapped)

    @property
    def value1_constant(self) -> float:
        """Gets the constant value of <format type="italics">Value1</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation."""
        dotnet_result = self._dotnet_instance.Value1Constant
        return _wrap(dotnet_result)

    @property
    def value2_constant(self) -> float:
        """Gets the constant value of <format type="italics">Value2</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation."""
        dotnet_result = self._dotnet_instance.Value2Constant
        return _wrap(dotnet_result)

    @property
    def value1_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">Value1</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation is specified by a constant or a channel."""
        dotnet_result = self._dotnet_instance.Value1IsConstant
        return _wrap(dotnet_result)

    @property
    def value2_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">Value2</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation is specified by a constant or a channel."""
        dotnet_result = self._dotnet_instance.Value2IsConstant
        return _wrap(dotnet_result)

    @property
    def variable(self) -> BaseNode:
        """Gets or sets the channel in the system whose value the <format type="bold">Set Variable</format> step sets."""
        dotnet_result = self._dotnet_instance.Variable
        return _wrap(dotnet_result)

    @variable.setter
    def variable(self, value: BaseNode):
        """Gets or sets the channel in the system whose value the <format type="bold">Set Variable</format> step sets."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Variable = next(unwrapped)

    @property
    def value1_channel(self) -> BaseNode:
        """Gets the channel that determines the value of <format type="italics">Value1</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation."""
        dotnet_result = self._dotnet_instance.Value1Channel
        return _wrap(dotnet_result)

    @property
    def value2_channel(self) -> BaseNode:
        """Gets the channel that determines the value of <format type="italics">Value2</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation."""
        dotnet_result = self._dotnet_instance.Value2Channel
        return _wrap(dotnet_result)

    @overload
    def set_value1(self, value1: float) -> bool:
        ...

    @overload
    def set_value1(self, value1: BaseNode) -> bool:
        ...

    def set_value1(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetValue1(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_value2(self, value2: float) -> bool:
        ...

    @overload
    def set_value2(self, value2: BaseNode) -> bool:
        ...

    def set_value2(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetValue2(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.MD5
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.SkipNCycles
        return _wrap(dotnet_result)

    @skip_n_cycles.setter
    def skip_n_cycles(self, value: float):
        """Gets or sets the number cycles for which to skip transmission of the frame across the bus. For each skipped cycle, a frame value is dequeued and the skip count is decremented. When the skip count decrements to zero, subsequent cyclic transmissions resume."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SkipNCycles = next(unwrapped)

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets or sets the trigger channel to watch for a non-zero value. Skipping frame transmission begins when this channel value becomes non-zero and stops when the skip count specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SkipCyclicFrames.SkipNCycles" crefType="Unqualified" /> decrements to zero."""
        dotnet_result = self._dotnet_instance.TriggerChannel
        return _wrap(dotnet_result)

    @trigger_channel.setter
    def trigger_channel(self, value: BaseNode):
        """Gets or sets the trigger channel to watch for a non-zero value. Skipping frame transmission begins when this channel value becomes non-zero and stops when the skip count specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SkipCyclicFrames.SkipNCycles" crefType="Unqualified" /> decrements to zero."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TriggerChannel = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SleepMode(*unwrapped)

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets or sets the channel that triggers sleep mode on an NI-XNET CAN port. If the value of this channel is non-zero, sleep mode is enabled. If the value is zero, sleep mode is disabled."""
        dotnet_result = self._dotnet_instance.TriggerChannel
        return _wrap(dotnet_result)

    @trigger_channel.setter
    def trigger_channel(self, value: BaseNode):
        """Gets or sets the channel that triggers sleep mode on an NI-XNET CAN port. If the value of this channel is non-zero, sleep mode is enabled. If the value is zero, sleep mode is disabled."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TriggerChannel = next(unwrapped)


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
        dotnet_result = self._dotnet_instance.Units
        return _wrap(dotnet_result)


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
        dotnet_result = self._dotnet_instance.Units
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ThermocoupleScale(*unwrapped)

    @property
    def thermocouple_type(self) -> ThermocoupleType:
        """Gets or sets the type of thermocouple in use."""
        dotnet_result = self._dotnet_instance.ThermocoupleType
        return _wrap(dotnet_result)

    @thermocouple_type.setter
    def thermocouple_type(self, value: ThermocoupleType):
        """Gets or sets the type of thermocouple in use."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ThermocoupleType = next(unwrapped)

    @property
    def thermocouple_cjc_type(self) -> ThermocoupleCJCType:
        """Gets or sets the type of device the thermocouple uses to perform cold-junction compensation."""
        dotnet_result = self._dotnet_instance.ThermocoupleCJCType
        return _wrap(dotnet_result)

    @thermocouple_cjc_type.setter
    def thermocouple_cjc_type(self, value: ThermocoupleCJCType):
        """Gets or sets the type of device the thermocouple uses to perform cold-junction compensation."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ThermocoupleCJCType = next(unwrapped)

    @property
    def temperature_unit(self) -> TemperatureUnit:
        """Gets or sets the units of the scaled temperature values: Kelvins or degrees Celsius, Fahrenheit, or Rankine."""
        dotnet_result = self._dotnet_instance.TemperatureUnit
        return _wrap(dotnet_result)

    @temperature_unit.setter
    def temperature_unit(self, value: TemperatureUnit):
        """Gets or sets the units of the scaled temperature values: Kelvins or degrees Celsius, Fahrenheit, or Rankine."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TemperatureUnit = next(unwrapped)

    @property
    def thermocouple_cjc_source(self) -> BaseNode:
        """Gets or sets the channel that serves as the source of cold-junction compensation for the ThermocoupleScale."""
        dotnet_result = self._dotnet_instance.ThermocoupleCJCSource
        return _wrap(dotnet_result)

    @thermocouple_cjc_source.setter
    def thermocouple_cjc_source(self, value: BaseNode):
        """Gets or sets the channel that serves as the source of cold-junction compensation for the ThermocoupleScale."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ThermocoupleCJCSource = next(unwrapped)


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
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the <format type="bold">Time Difference</format> channel. This property only represents an initial value for the channel, and does not actually enhance or delay frame transmission."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialValue = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.TimingAndSyncDevice(*unwrapped)

    @property
    def is_rtsi0_capable(self) -> bool:
        """Gets or sets whether the timing and sync device is capable of driving the RTSI 0 line, which is a digital line that sends a clock signal that synchronizes all hardware I/O devices in the system."""
        dotnet_result = self._dotnet_instance.IsRTSI0Capable
        return _wrap(dotnet_result)

    @is_rtsi0_capable.setter
    def is_rtsi0_capable(self, value: bool):
        """Gets or sets whether the timing and sync device is capable of driving the RTSI 0 line, which is a digital line that sends a clock signal that synchronizes all hardware I/O devices in the system."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IsRTSI0Capable = next(unwrapped)


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
        dotnet_result = self._dotnet_instance.TransmitTimeValue
        return _wrap(dotnet_result)

    @transmit_time_value.setter
    def transmit_time_value(self, value: float):
        """Gets or sets the constant value to use as the transmit time, in seconds."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TransmitTimeValue = next(unwrapped)

    @property
    def use_trigger_channel(self) -> bool:
        """Gets whether the <format type="bold">Transmit Time</format>  channel is using a trigger channel to get the transmit time value."""
        dotnet_result = self._dotnet_instance.UseTriggerChannel
        return _wrap(dotnet_result)

    @property
    def trigger_channel(self) -> BaseNode:
        """Gets a reference to the trigger channel the <format type="bold">Transmit Time</format> channel is using to get its value."""
        dotnet_result = self._dotnet_instance.TriggerChannel
        return _wrap(dotnet_result)

    @overload
    def remove_trigger_channel(self):
        ...

    def remove_trigger_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveTriggerChannel(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_trigger_channel(self, trigger_channel: BaseNode):
        ...

    def set_trigger_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetTriggerChannel(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.UserChannel(*unwrapped)

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of the user channel."""
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the user channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialValue = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming(*unwrapped)

    @property
    def function(self) -> AlarmingStepFunction:
        """Gets or sets the function that the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming" crefType="Unqualified" /> step performs on the alarm."""
        dotnet_result = self._dotnet_instance.Function
        return _wrap(dotnet_result)

    @function.setter
    def function(self, value: AlarmingStepFunction):
        """Gets or sets the function that the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming" crefType="Unqualified" /> step performs on the alarm."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Function = next(unwrapped)

    @property
    def priority_number(self) -> int:
        """Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31."""
        dotnet_result = self._dotnet_instance.PriorityNumber
        return _wrap(dotnet_result)

    @priority_number.setter
    def priority_number(self, value: int):
        """Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PriorityNumber = next(unwrapped)

    @property
    def priority(self) -> AlarmPriority:
        """This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>"""
        dotnet_result = self._dotnet_instance.Priority
        return _wrap(dotnet_result)

    @priority.setter
    def priority(self, value: AlarmPriority):
        """This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Priority = next(unwrapped)

    @property
    def default_state(self) -> AlarmState:
        """Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm."""
        dotnet_result = self._dotnet_instance.DefaultState
        return _wrap(dotnet_result)

    @default_state.setter
    def default_state(self, value: AlarmState):
        """Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DefaultState = next(unwrapped)

    @property
    def delay(self) -> float:
        """Gets or sets the amount of time to wait before triggering the alarm."""
        dotnet_result = self._dotnet_instance.Delay
        return _wrap(dotnet_result)

    @delay.setter
    def delay(self, value: float):
        """Gets or sets the amount of time to wait before triggering the alarm."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Delay = next(unwrapped)

    @property
    def upper_limit_constant(self) -> float:
        """Gets the constant that determines the high limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered."""
        dotnet_result = self._dotnet_instance.UpperLimitConstant
        return _wrap(dotnet_result)

    @property
    def lower_limit_constant(self) -> float:
        """Gets the constant that determines the low limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered."""
        dotnet_result = self._dotnet_instance.LowerLimitConstant
        return _wrap(dotnet_result)

    @property
    def upper_limit_is_constant(self) -> bool:
        """Gets information about whether the high limit value of the alarm is determined by a channel or by a constant."""
        dotnet_result = self._dotnet_instance.UpperLimitIsConstant
        return _wrap(dotnet_result)

    @property
    def lower_limit_is_constant(self) -> bool:
        """Gets information about whether the low limit value of the alarm is determined by a channel or by a constant."""
        dotnet_result = self._dotnet_instance.LowerLimitIsConstant
        return _wrap(dotnet_result)

    @property
    def using_tripped_alarm(self) -> bool:
        """Gets information about whether the step is using the tripped alarm."""
        dotnet_result = self._dotnet_instance.UsingTrippedAlarm
        return _wrap(dotnet_result)

    @property
    def alarm(self) -> BaseNode:
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm" crefType="Unqualified" /> on which to perform the step <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming.Function" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.Alarm
        return _wrap(dotnet_result)

    @alarm.setter
    def alarm(self, value: BaseNode):
        """Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm" crefType="Unqualified" /> on which to perform the step <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming.Function" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Alarm = next(unwrapped)

    @property
    def alarm_channel(self) -> BaseNode:
        """Gets or sets the channel to monitor for alarm conditions."""
        dotnet_result = self._dotnet_instance.AlarmChannel
        return _wrap(dotnet_result)

    @alarm_channel.setter
    def alarm_channel(self, value: BaseNode):
        """Gets or sets the channel to monitor for alarm conditions."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.AlarmChannel = next(unwrapped)

    @property
    def procedure(self) -> BaseNode:
        """Gets or sets the procedure to initiate when the alarm conditions are met."""
        dotnet_result = self._dotnet_instance.Procedure
        return _wrap(dotnet_result)

    @procedure.setter
    def procedure(self, value: BaseNode):
        """Gets or sets the procedure to initiate when the alarm conditions are met."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Procedure = next(unwrapped)

    @property
    def upper_limit_channel(self) -> BaseNode:
        """Gets the channel that determines the upper limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered."""
        dotnet_result = self._dotnet_instance.UpperLimitChannel
        return _wrap(dotnet_result)

    @property
    def lower_limit_channel(self) -> BaseNode:
        """Gets the channel that determines the lower limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered."""
        dotnet_result = self._dotnet_instance.LowerLimitChannel
        return _wrap(dotnet_result)

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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetUpperLimit(*unwrapped)
        return _wrap(dotnet_result)

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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetLowerLimit(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def use_tripped_alarm(self):
        ...

    def use_tripped_alarm(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.UseTrippedAlarm(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Formula
        return _wrap(dotnet_result)

    @_staticproperty
    def maximum() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Maximum
        return _wrap(dotnet_result)

    @_staticproperty
    def minimum() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Minimum
        return _wrap(dotnet_result)

    @_staticproperty
    def lowpass_filter() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.LowpassFilter
        return _wrap(dotnet_result)

    @_staticproperty
    def peak_and_valley() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.PeakAndValley
        return _wrap(dotnet_result)

    @_staticproperty
    def acceleration() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Acceleration
        return _wrap(dotnet_result)

    @_staticproperty
    def average() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Average
        return _wrap(dotnet_result)

    @_staticproperty
    def conditional() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel.Conditional
        return _wrap(dotnet_result)

    @property
    def calculated_channel_type(self) -> int:
        """Gets the type of the calculated channel."""
        dotnet_result = self._dotnet_instance.CalculatedChannelType
        return _wrap(dotnet_result)

    @overload
    def downcast(self) -> CalculatedChannel:
        ...

    def downcast(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Downcast(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.CallProcedure(*unwrapped)

    @property
    def procedure(self) -> BaseNode:
        """Gets or sets the procedure to call when this step executes."""
        dotnet_result = self._dotnet_instance.Procedure
        return _wrap(dotnet_result)

    @procedure.setter
    def procedure(self, value: BaseNode):
        """Gets or sets the procedure to call when this step executes."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Procedure = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional(*unwrapped)

    @_staticproperty
    def greater() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.Greater
        return _wrap(dotnet_result)

    @_staticproperty
    def less() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.Less
        return _wrap(dotnet_result)

    @_staticproperty
    def equal() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.Equal
        return _wrap(dotnet_result)

    @_staticproperty
    def not_equal() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.NotEqual
        return _wrap(dotnet_result)

    @_staticproperty
    def greater_or_equal() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.GreaterOrEqual
        return _wrap(dotnet_result)

    @_staticproperty
    def less_or_equal() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.LessOrEqual
        return _wrap(dotnet_result)

    @_staticproperty
    def and_() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.AND
        return _wrap(dotnet_result)

    @_staticproperty
    def or_() -> int:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.Conditional.OR
        return _wrap(dotnet_result)

    @property
    def y_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">Y</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        dotnet_result = self._dotnet_instance.YConstantValue
        return _wrap(dotnet_result)

    @property
    def w_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">W</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        dotnet_result = self._dotnet_instance.WConstantValue
        return _wrap(dotnet_result)

    @property
    def z_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">Z</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        dotnet_result = self._dotnet_instance.ZConstantValue
        return _wrap(dotnet_result)

    @property
    def y_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">Y</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        dotnet_result = self._dotnet_instance.YChannelValue
        return _wrap(dotnet_result)

    @property
    def w_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">W</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        dotnet_result = self._dotnet_instance.WChannelValue
        return _wrap(dotnet_result)

    @property
    def z_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">Z</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        dotnet_result = self._dotnet_instance.ZChannelValue
        return _wrap(dotnet_result)

    @property
    def comparison_mode(self) -> int:
        """Gets or sets the type of comparison to use for the condition."""
        dotnet_result = self._dotnet_instance.ComparisonMode
        return _wrap(dotnet_result)

    @comparison_mode.setter
    def comparison_mode(self, value: int):
        """Gets or sets the type of comparison to use for the condition."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ComparisonMode = next(unwrapped)

    @property
    def x_channel(self) -> BaseNode:
        """Gets or sets the channel to check for the comparison condition. This channel is the value of <format type="italics">X</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        dotnet_result = self._dotnet_instance.XChannel
        return _wrap(dotnet_result)

    @x_channel.setter
    def x_channel(self, value: BaseNode):
        """Gets or sets the channel to check for the comparison condition. This channel is the value of <format type="italics">X</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.XChannel = next(unwrapped)

    @overload
    def set_y_value(self, y_value: float):
        ...

    @overload
    def set_y_value(self, y_value: BaseNode):
        ...

    def set_y_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetYValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_w_value(self, w_value: float):
        ...

    @overload
    def set_w_value(self, w_value: BaseNode):
        ...

    def set_w_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetWValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_z_value(self, z_value: float):
        ...

    @overload
    def set_z_value(self, z_value: BaseNode):
        ...

    def set_z_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetZValue(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogInput(*unwrapped)

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of the analog input channel."""
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the analog input channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialValue = next(unwrapped)

    @property
    def channel_type(self) -> DAQAnalogChannelType:
        """Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>)."""
        dotnet_result = self._dotnet_instance.ChannelType
        return _wrap(dotnet_result)

    @channel_type.setter
    def channel_type(self, value: DAQAnalogChannelType):
        """Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ChannelType = next(unwrapped)

    @property
    def channel(self) -> int:
        """Gets or sets the channel number."""
        dotnet_result = self._dotnet_instance.Channel
        return _wrap(dotnet_result)

    @channel.setter
    def channel(self, value: int):
        """Gets or sets the channel number."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Channel = next(unwrapped)

    @property
    def low_level(self) -> float:
        """Gets or sets the minimum value of the channel."""
        dotnet_result = self._dotnet_instance.LowLevel
        return _wrap(dotnet_result)

    @low_level.setter
    def low_level(self, value: float):
        """Gets or sets the minimum value of the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LowLevel = next(unwrapped)

    @property
    def high_level(self) -> float:
        """Gets or sets the maximum value of the channel."""
        dotnet_result = self._dotnet_instance.HighLevel
        return _wrap(dotnet_result)

    @high_level.setter
    def high_level(self, value: float):
        """Gets or sets the maximum value of the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.HighLevel = next(unwrapped)

    @property
    def is_scxi(self) -> bool:
        """Gets whether the channel belongs to an SCXI module."""
        dotnet_result = self._dotnet_instance.IsSCXI
        return _wrap(dotnet_result)

    @property
    def scxi_module_type(self) -> str:
        """Gets the specific type of SCXI module to which the channel belongs."""
        dotnet_result = self._dotnet_instance.SCXIModuleType
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogOutput(*unwrapped)

    @property
    def initial_value(self) -> float:
        """Gets or sets the initial value of the analog output channel."""
        dotnet_result = self._dotnet_instance.InitialValue
        return _wrap(dotnet_result)

    @initial_value.setter
    def initial_value(self, value: float):
        """Gets or sets the initial value of the analog output channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InitialValue = next(unwrapped)

    @property
    def channel_type(self) -> DAQAnalogChannelType:
        """Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>)."""
        dotnet_result = self._dotnet_instance.ChannelType
        return _wrap(dotnet_result)

    @channel_type.setter
    def channel_type(self, value: DAQAnalogChannelType):
        """Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ChannelType = next(unwrapped)

    @property
    def channel(self) -> int:
        """Gets or sets the channel number."""
        dotnet_result = self._dotnet_instance.Channel
        return _wrap(dotnet_result)

    @channel.setter
    def channel(self, value: int):
        """Gets or sets the channel number."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Channel = next(unwrapped)

    @property
    def low_level(self) -> float:
        """Gets or sets the minimum value of the channel."""
        dotnet_result = self._dotnet_instance.LowLevel
        return _wrap(dotnet_result)

    @low_level.setter
    def low_level(self, value: float):
        """Gets or sets the minimum value of the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LowLevel = next(unwrapped)

    @property
    def high_level(self) -> float:
        """Gets or sets the maximum value of the channel."""
        dotnet_result = self._dotnet_instance.HighLevel
        return _wrap(dotnet_result)

    @high_level.setter
    def high_level(self, value: float):
        """Gets or sets the maximum value of the channel."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.HighLevel = next(unwrapped)

    @property
    def is_scxi(self) -> bool:
        """Gets whether the channel belongs to an SCXI module."""
        dotnet_result = self._dotnet_instance.IsSCXI
        return _wrap(dotnet_result)

    @property
    def scxi_module_type(self) -> str:
        """Gets the specific type of SCXI module to which the channel belongs."""
        dotnet_result = self._dotnet_instance.SCXIModuleType
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCountUpDown(*unwrapped)

    @property
    def count_direction(self) -> DAQCounterCountMode:
        """Gets or sets the direction of the count (up, down, or externally controlled)."""
        dotnet_result = self._dotnet_instance.CountDirection
        return _wrap(dotnet_result)

    @count_direction.setter
    def count_direction(self, value: DAQCounterCountMode):
        """Gets or sets the direction of the count (up, down, or externally controlled)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.CountDirection = next(unwrapped)

    @property
    def edge(self) -> DAQCounterEdge:
        """Gets or sets the edge on which to count (rising or falling)."""
        dotnet_result = self._dotnet_instance.Edge
        return _wrap(dotnet_result)

    @edge.setter
    def edge(self, value: DAQCounterEdge):
        """Gets or sets the edge on which to count (rising or falling)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Edge = next(unwrapped)

    @property
    def input_terminal(self) -> str:
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        dotnet_result = self._dotnet_instance.InputTerminal
        return _wrap(dotnet_result)

    @input_terminal.setter
    def input_terminal(self, value: str):
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InputTerminal = next(unwrapped)

    @property
    def reset_variable(self) -> BaseNode:
        """Gets or sets the channel whose value the counter must reach before it resets."""
        dotnet_result = self._dotnet_instance.ResetVariable
        return _wrap(dotnet_result)

    @reset_variable.setter
    def reset_variable(self, value: BaseNode):
        """Gets or sets the channel whose value the counter must reach before it resets."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ResetVariable = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPulseGeneration(*unwrapped)

    @property
    def counter(self) -> str:
        """Gets the counter channel number."""
        dotnet_result = self._dotnet_instance.Counter
        return _wrap(dotnet_result)

    @property
    def output_terminal(self) -> str:
        """Gets or sets the output terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        dotnet_result = self._dotnet_instance.OutputTerminal
        return _wrap(dotnet_result)

    @output_terminal.setter
    def output_terminal(self, value: str):
        """Gets or sets the output terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.OutputTerminal = next(unwrapped)

    @overload
    def set_counter_index(self, index: int):
        ...

    def set_counter_index(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetCounterIndex(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_data_channel(self, type: DAQDataChannelType) -> Channel:
        ...

    def get_data_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataChannel(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.DAQPulseMeasurement(*unwrapped)

    @property
    def counter(self) -> str:
        """Gets the counter channel number."""
        dotnet_result = self._dotnet_instance.Counter
        return _wrap(dotnet_result)

    @property
    def input_terminal(self) -> str:
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        dotnet_result = self._dotnet_instance.InputTerminal
        return _wrap(dotnet_result)

    @input_terminal.setter
    def input_terminal(self, value: str):
        """Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.InputTerminal = next(unwrapped)

    @overload
    def set_counter_index(self, index: int):
        ...

    def set_counter_index(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetCounterIndex(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_data_channel(self, type: DAQDataChannelType) -> Channel:
        ...

    def get_data_channel(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDataChannel(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Formula(*unwrapped)

    @property
    def formula_string(self) -> str:
        """Gets the formula for which the channel calculates the result."""
        dotnet_result = self._dotnet_instance.FormulaString
        return _wrap(dotnet_result)

    @overload
    def set_formula(self, formula: str, variable_names: Sequence[str], variables: Sequence[BaseNode]):
        ...

    def set_formula(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetFormula(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reset_formula(self):
        ...

    def reset_formula(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ResetFormula(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetInportGroups(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_inports(self) -> Sequence[Inport]:
        ...

    @overload
    def get_inports(self, deep: bool) -> Sequence[Inport]:
        ...

    def get_inports(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetInports(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.LookupTable(*unwrapped)

    @property
    def lookup_table_values(self) -> Sequence[LUTValue]:
        """Gets or sets the values of the LookupTable scale."""
        dotnet_result = self._dotnet_instance.LookupTableValues
        return _wrap(dotnet_result)

    @lookup_table_values.setter
    def lookup_table_values(self, value: Sequence[LUTValue]):
        """Gets or sets the values of the LookupTable scale."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LookupTableValues = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.LowpassFilter(*unwrapped)

    @property
    def channel_to_filter(self) -> BaseNode:
        """Gets or sets the channel to which to apply the filter."""
        dotnet_result = self._dotnet_instance.ChannelToFilter
        return _wrap(dotnet_result)

    @channel_to_filter.setter
    def channel_to_filter(self, value: BaseNode):
        """Gets or sets the channel to which to apply the filter."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ChannelToFilter = next(unwrapped)

    @property
    def filter_order(self) -> int:
        """Gets or sets the order of the filter. Increasing the value of this property causes the transition between the passband and the stopband to become steeper. However, as the filter order increases, the filter becomes more unstable."""
        dotnet_result = self._dotnet_instance.FilterOrder
        return _wrap(dotnet_result)

    @filter_order.setter
    def filter_order(self, value: int):
        """Gets or sets the order of the filter. Increasing the value of this property causes the transition between the passband and the stopband to become steeper. However, as the filter order increases, the filter becomes more unstable."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FilterOrder = next(unwrapped)

    @property
    def low_cutoff_frequency(self) -> float:
        """Gets or sets the low cutoff frequency, in hertz."""
        dotnet_result = self._dotnet_instance.LowCutoffFrequency
        return _wrap(dotnet_result)

    @low_cutoff_frequency.setter
    def low_cutoff_frequency(self, value: float):
        """Gets or sets the low cutoff frequency, in hertz."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LowCutoffFrequency = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Maximum(*unwrapped)

    @property
    def x_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel."""
        dotnet_result = self._dotnet_instance.XIsConstant
        return _wrap(dotnet_result)

    @property
    def y_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel."""
        dotnet_result = self._dotnet_instance.YIsConstant
        return _wrap(dotnet_result)

    @property
    def y_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>. regardless of whether <format type="italics">x</format> is a constant or a channel."""
        dotnet_result = self._dotnet_instance.YConstantValue
        return _wrap(dotnet_result)

    @property
    def x_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>, regardless of whether <format type="italics">x</format> is a constant or a channel."""
        dotnet_result = self._dotnet_instance.XConstantValue
        return _wrap(dotnet_result)

    @property
    def x_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>."""
        dotnet_result = self._dotnet_instance.XChannelValue
        return _wrap(dotnet_result)

    @property
    def y_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>."""
        dotnet_result = self._dotnet_instance.YChannelValue
        return _wrap(dotnet_result)

    @overload
    def set_x_value(self, x_value: float):
        ...

    @overload
    def set_x_value(self, x_value: BaseNode):
        ...

    def set_x_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetXValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_y_value(self, y_value: float):
        ...

    @overload
    def set_y_value(self, y_value: BaseNode):
        ...

    def set_y_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetYValue(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Minimum(*unwrapped)

    @property
    def x_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel."""
        dotnet_result = self._dotnet_instance.XIsConstant
        return _wrap(dotnet_result)

    @property
    def y_is_constant(self) -> bool:
        """Gets whether the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel."""
        dotnet_result = self._dotnet_instance.YIsConstant
        return _wrap(dotnet_result)

    @property
    def y_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>. regardless of whether <format type="italics">x</format> is a constant or a channel."""
        dotnet_result = self._dotnet_instance.YConstantValue
        return _wrap(dotnet_result)

    @property
    def x_constant_value(self) -> float:
        """Gets the constant value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>, regardless of whether <format type="italics">x</format> is a constant or a channel."""
        dotnet_result = self._dotnet_instance.XConstantValue
        return _wrap(dotnet_result)

    @property
    def x_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>."""
        dotnet_result = self._dotnet_instance.XChannelValue
        return _wrap(dotnet_result)

    @property
    def y_channel_value(self) -> BaseNode:
        """Gets the channel that specifies the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>."""
        dotnet_result = self._dotnet_instance.YChannelValue
        return _wrap(dotnet_result)

    @overload
    def set_x_value(self, x_value: float):
        ...

    @overload
    def set_x_value(self, x_value: BaseNode):
        ...

    def set_x_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetXValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_y_value(self, y_value: float):
        ...

    @overload
    def set_y_value(self, y_value: BaseNode):
        ...

    def set_y_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetYValue(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley(*unwrapped)

    @property
    def channel_to_analyze(self) -> BaseNode:
        """Gets or sets the channel for which to calculate the peak, valley, and offset."""
        dotnet_result = self._dotnet_instance.ChannelToAnalyze
        return _wrap(dotnet_result)

    @channel_to_analyze.setter
    def channel_to_analyze(self, value: BaseNode):
        """Gets or sets the channel for which to calculate the peak, valley, and offset."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ChannelToAnalyze = next(unwrapped)

    @property
    def channel_for_valley(self) -> BaseNode:
        """Gets or sets the channel on which to store the valley value."""
        dotnet_result = self._dotnet_instance.ChannelForValley
        return _wrap(dotnet_result)

    @channel_for_valley.setter
    def channel_for_valley(self, value: BaseNode):
        """Gets or sets the channel on which to store the valley value."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ChannelForValley = next(unwrapped)

    @property
    def channel_for_offset(self) -> BaseNode:
        """Gets or sets the channel on which to store the offset value."""
        dotnet_result = self._dotnet_instance.ChannelForOffset
        return _wrap(dotnet_result)

    @channel_for_offset.setter
    def channel_for_offset(self, value: BaseNode):
        """Gets or sets the channel on which to store the offset value."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ChannelForOffset = next(unwrapped)

    @property
    def hysteresis(self) -> float:
        """Gets or sets the amount by which the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> must exceed the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Reset" crefType="Unqualified" /> value for the calculation to reset."""
        dotnet_result = self._dotnet_instance.Hysteresis
        return _wrap(dotnet_result)

    @hysteresis.setter
    def hysteresis(self, value: float):
        """Gets or sets the amount by which the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> must exceed the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Reset" crefType="Unqualified" /> value for the calculation to reset."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Hysteresis = next(unwrapped)

    @property
    def reset(self) -> int:
        """Gets or sets the value at which to reset the calculation. If the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> surpasses this value by more than the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Hysteresis" crefType="Unqualified" />, the calculation resets."""
        dotnet_result = self._dotnet_instance.Reset
        return _wrap(dotnet_result)

    @reset.setter
    def reset(self, value: int):
        """Gets or sets the value at which to reset the calculation. If the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> surpasses this value by more than the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Hysteresis" crefType="Unqualified" />, the calculation resets."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Reset = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale(*unwrapped)

    @property
    def polynomial_coeff(self) -> Sequence[float]:
        """Gets or sets the forward coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />."""
        dotnet_result = self._dotnet_instance.PolynomialCoeff
        return _wrap(dotnet_result)

    @polynomial_coeff.setter
    def polynomial_coeff(self, value: Sequence[float]):
        """Gets or sets the forward coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PolynomialCoeff = next(unwrapped)

    @property
    def reverse_polynomial_coeff(self) -> Sequence[float]:
        """Gets or sets the reverse coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />."""
        dotnet_result = self._dotnet_instance.ReversePolynomialCoeff
        return _wrap(dotnet_result)

    @reverse_polynomial_coeff.setter
    def reverse_polynomial_coeff(self, value: Sequence[float]):
        """Gets or sets the reverse coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ReversePolynomialCoeff = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1100(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1102(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1102B(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1102C(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1104(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1104C(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1112(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1120(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1120D(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1121(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1122(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1124(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1125(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1126(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1127(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1128(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1140(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1141(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1142(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1143(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1160(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1161(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1162(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1162HV(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1163(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1163R(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1190(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1191(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1192(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1520(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1530(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1531(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1540(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.SCXI1581(*unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Acceleration(*unwrapped)

    @property
    def velocity_channel(self) -> BaseNode:
        """Gets or sets the channel on which to store the velocity of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Acceleration.XChannel" crefType="Unqualified" />."""
        dotnet_result = self._dotnet_instance.VelocityChannel
        return _wrap(dotnet_result)

    @velocity_channel.setter
    def velocity_channel(self, value: BaseNode):
        """Gets or sets the channel on which to store the velocity of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Acceleration.XChannel" crefType="Unqualified" />."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.VelocityChannel = next(unwrapped)

    @property
    def x_channel(self) -> BaseNode:
        """Gets or sets the channel for which to calculate the acceleration."""
        dotnet_result = self._dotnet_instance.XChannel
        return _wrap(dotnet_result)

    @x_channel.setter
    def x_channel(self, value: BaseNode):
        """Gets or sets the channel for which to calculate the acceleration."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.XChannel = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.Average(*unwrapped)

    @property
    def channel_to_average(self) -> BaseNode:
        """Gets or sets the channel for which to calculate the average value."""
        dotnet_result = self._dotnet_instance.ChannelToAverage
        return _wrap(dotnet_result)

    @channel_to_average.setter
    def channel_to_average(self, value: BaseNode):
        """Gets or sets the channel for which to calculate the average value."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ChannelToAverage = next(unwrapped)

    @property
    def number_of_points(self) -> int:
        """Gets or sets the number of points of data to include in the average."""
        dotnet_result = self._dotnet_instance.NumberOfPoints
        return _wrap(dotnet_result)

    @number_of_points.setter
    def number_of_points(self, value: int):
        """Gets or sets the number of points of data to include in the average."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.NumberOfPoints = next(unwrapped)
