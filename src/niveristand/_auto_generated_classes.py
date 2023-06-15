"""Module for NationalInstruments.VeriStand."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand")
import NationalInstruments.VeriStand  # type: ignore
import System  # type: ignore


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

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


class VeriStandSdfError(Exception):
    """Represents NI VeriStand error information, including an integer error code and a string error message. Error objects are immutable once created."""

    def __str__(self) -> str:
        # Only use resolved_error_message if necessary; it often returns
        # "Additional error information is not available" before the error
        message = self.message if self.message else self.resolved_error_message
        return f"{int(self.error_code)} ({str(self._dotnet_instance)}): {message}"

    @overload
    def __init__(self, code: int, message: str):
        ...

    @overload
    def __init__(self, code: ErrorCode, message: str):
        ...

    @overload
    def __init__(self, code: int, message: str, resolved_error: str):
        ...

    @overload
    def __init__(self, code: ErrorCode, message: str, resolved_error: str):
        ...

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, code: int):
        ...

    @overload
    def __init__(self, code: ErrorCode):
        ...

    @overload
    def __init__(self, e: System.Exception):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.Error:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.Error(*unwrapped)

    @property
    def code(self) -> int:
        """Gets the error code for the current instance of <see cref="T:NationalInstruments.VeriStand.Error" /> and returns it as an integer."""
        dotnet_result = self._dotnet_instance.Code
        return _wrap(dotnet_result)

    @property
    def message(self) -> str:
        """Gets the error message and returns it as a string."""
        dotnet_result = self._dotnet_instance.Message
        return _wrap(dotnet_result)

    @property
    def is_error(self) -> bool:
        """Gets a Boolean value indicating whether the <see cref="T:NationalInstruments.VeriStand.Error" /> object contains an error state."""
        dotnet_result = self._dotnet_instance.IsError
        return _wrap(dotnet_result)

    @property
    def resolved_error_message(self) -> str:
        """Gets the resolved error message. The resolved error message provides error information for non-LabVIEW applications."""
        dotnet_result = self._dotnet_instance.ResolvedErrorMessage
        return _wrap(dotnet_result)

    @property
    def is_defined_error_code(self) -> bool:
        """Gets a Boolean value indicating whether or not the integer error code is defined in the <see cref="T:NationalInstruments.VeriStand.ErrorCode" /> enumeration."""
        dotnet_result = self._dotnet_instance.IsDefinedErrorCode
        return _wrap(dotnet_result)

    @property
    def error_code(self) -> ErrorCode:
        """Gets the <see cref="T:NationalInstruments.VeriStand.ErrorCode" /> enumeration for the current <see cref="T:NationalInstruments.VeriStand.Error" />. If the integer error code is not defined in <see cref="T:NationalInstruments.VeriStand.ErrorCode" />, returns the UnexpectedError enumeration."""
        dotnet_result = self._dotnet_instance.ErrorCode
        return _wrap(dotnet_result)

    @overload
    def to_string(self) -> str:
        ...

    def to_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ToString(*unwrapped)
        return _wrap(dotnet_result)


class ErrorCode(_DotNetEnum):
    """Defines the types of error codes that NI VeriStand can return."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.ErrorCode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ErrorCode")

    @_staticproperty
    def SUCCESS() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "Success")
        return ErrorCode(dotnet_result, "SUCCESS")

    @_staticproperty
    def LAB_VIEW_MATHEMATICS_VI_BRACKET_PROBLEM() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "LabVIEWMathematicsVIBracketProblem")
        return ErrorCode(dotnet_result, "LAB_VIEW_MATHEMATICS_VI_BRACKET_PROBLEM")

    @_staticproperty
    def LAB_VIEW_MATHEMATICS_VI_BEGINNING_BRACKET_PROBLEM() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "LabVIEWMathematicsVIBeginningBracketProblem")
        return ErrorCode(dotnet_result, "LAB_VIEW_MATHEMATICS_VI_BEGINNING_BRACKET_PROBLEM")

    @_staticproperty
    def LAB_VIEW_MATHEMATICS_VI_END_BRACKET_PROBLEM() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "LabVIEWMathematicsVIEndBracketProblem")
        return ErrorCode(dotnet_result, "LAB_VIEW_MATHEMATICS_VI_END_BRACKET_PROBLEM")

    @_staticproperty
    def FILE_VERSION_UNSUPPORTED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "FileVersionUnsupported")
        return ErrorCode(dotnet_result, "FILE_VERSION_UNSUPPORTED")

    @_staticproperty
    def SERVICE_CONFIGURATION_FILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ServiceConfigurationFile")
        return ErrorCode(dotnet_result, "SERVICE_CONFIGURATION_FILE")

    @_staticproperty
    def UNEXPECTED_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "UnexpectedError")
        return ErrorCode(dotnet_result, "UNEXPECTED_ERROR")

    @_staticproperty
    def FUNCTION_NOT_SUPPORTED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "FunctionNotSupported")
        return ErrorCode(dotnet_result, "FUNCTION_NOT_SUPPORTED")

    @_staticproperty
    def FAILED_SERVER_CONNECTION() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "FailedServerConnection")
        return ErrorCode(dotnet_result, "FAILED_SERVER_CONNECTION")

    @_staticproperty
    def INVALID_FILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InvalidFile")
        return ErrorCode(dotnet_result, "INVALID_FILE")

    @_staticproperty
    def NOT_DEPLOYED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotDeployed")
        return ErrorCode(dotnet_result, "NOT_DEPLOYED")

    @_staticproperty
    def COMPONENT_NOT_AVAILABLE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ComponentNotAvailable")
        return ErrorCode(dotnet_result, "COMPONENT_NOT_AVAILABLE")

    @_staticproperty
    def NO_SYSTEM_DEFINITION_LOADED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NoSystemDefinitionLoaded")
        return ErrorCode(dotnet_result, "NO_SYSTEM_DEFINITION_LOADED")

    @_staticproperty
    def INVALID_CONFIGURATION_PASSWORD() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InvalidConfigurationPassword")
        return ErrorCode(dotnet_result, "INVALID_CONFIGURATION_PASSWORD")

    @_staticproperty
    def HOST_RUNNING_DIFFERENT_SYSTEM_DEFINITION() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "HostRunningDifferentSystemDefinition")
        return ErrorCode(dotnet_result, "HOST_RUNNING_DIFFERENT_SYSTEM_DEFINITION")

    @_staticproperty
    def SYSTEM_DEFINITION_ALREADY_ACTIVE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SystemDefinitionAlreadyActive")
        return ErrorCode(dotnet_result, "SYSTEM_DEFINITION_ALREADY_ACTIVE")

    @_staticproperty
    def EMPTY_PASSWORD() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "EmptyPassword")
        return ErrorCode(dotnet_result, "EMPTY_PASSWORD")

    @_staticproperty
    def SYSTEM_DEFINITION_DEPLOYMENT_TIMEOUT() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SystemDefinitionDeploymentTimeout")
        return ErrorCode(dotnet_result, "SYSTEM_DEFINITION_DEPLOYMENT_TIMEOUT")

    @_staticproperty
    def SYSTEM_DEFINITION_DEPLOYMENT_FAILURE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SystemDefinitionDeploymentFailure")
        return ErrorCode(dotnet_result, "SYSTEM_DEFINITION_DEPLOYMENT_FAILURE")

    @_staticproperty
    def NODE_NOT_FOUND() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NodeNotFound")
        return ErrorCode(dotnet_result, "NODE_NOT_FOUND")

    @_staticproperty
    def TIMEOUT() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "Timeout")
        return ErrorCode(dotnet_result, "TIMEOUT")

    @_staticproperty
    def CHANNEL_NOT_READABLE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelNotReadable")
        return ErrorCode(dotnet_result, "CHANNEL_NOT_READABLE")

    @_staticproperty
    def CHANNEL_NOT_WRITABLE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelNotWritable")
        return ErrorCode(dotnet_result, "CHANNEL_NOT_WRITABLE")

    @_staticproperty
    def CHANNEL_CANNOT_BE_FAULTED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelCannotBeFaulted")
        return ErrorCode(dotnet_result, "CHANNEL_CANNOT_BE_FAULTED")

    @_staticproperty
    def TARGET_INVALID() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "TargetInvalid")
        return ErrorCode(dotnet_result, "TARGET_INVALID")

    @_staticproperty
    def TARGET_DISABLED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "TargetDisabled")
        return ErrorCode(dotnet_result, "TARGET_DISABLED")

    @_staticproperty
    def MODEL_DIMENSION_MISMATCH() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ModelDimensionMismatch")
        return ErrorCode(dotnet_result, "MODEL_DIMENSION_MISMATCH")

    @_staticproperty
    def CHANNEL_MAPPINGS_SIZE_MISMATCH() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelMappingsSizeMismatch")
        return ErrorCode(dotnet_result, "CHANNEL_MAPPINGS_SIZE_MISMATCH")

    @_staticproperty
    def NOT_A_CHANNEL() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotAChannel")
        return ErrorCode(dotnet_result, "NOT_A_CHANNEL")

    @_staticproperty
    def NOT_A_WAVEFORM() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotAWaveform")
        return ErrorCode(dotnet_result, "NOT_A_WAVEFORM")

    @_staticproperty
    def WAVEFORM_DATA_TYPE_MISMATCH() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "WaveformDataTypeMismatch")
        return ErrorCode(dotnet_result, "WAVEFORM_DATA_TYPE_MISMATCH")

    @_staticproperty
    def INVALID_STREAM_CONDITION_FOR_DATA_TYPE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InvalidStreamConditionForDataType")
        return ErrorCode(dotnet_result, "INVALID_STREAM_CONDITION_FOR_DATA_TYPE")

    @_staticproperty
    def CHANNEL_NODE_REMOVED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelNodeRemoved")
        return ErrorCode(dotnet_result, "CHANNEL_NODE_REMOVED")

    @_staticproperty
    def NODE_NOT_FOUND_DURING_COMPILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NodeNotFoundDuringCompile")
        return ErrorCode(dotnet_result, "NODE_NOT_FOUND_DURING_COMPILE")

    @_staticproperty
    def CHANNEL_LENGTH_MISMATCH() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelLengthMismatch")
        return ErrorCode(dotnet_result, "CHANNEL_LENGTH_MISMATCH")

    @_staticproperty
    def CHANNEL_NOT_SCALABLE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelNotScalable")
        return ErrorCode(dotnet_result, "CHANNEL_NOT_SCALABLE")

    @_staticproperty
    def NO_PROJECT_OPEN() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NoProjectOpen")
        return ErrorCode(dotnet_result, "NO_PROJECT_OPEN")

    @_staticproperty
    def STIMULUS_PROFILE_SESSION_LOCKED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "StimulusProfileSessionLocked")
        return ErrorCode(dotnet_result, "STIMULUS_PROFILE_SESSION_LOCKED")

    @_staticproperty
    def SEQUENCE_NOT_FOUND_IN_SESSION() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SequenceNotFoundInSession")
        return ErrorCode(dotnet_result, "SEQUENCE_NOT_FOUND_IN_SESSION")

    @_staticproperty
    def SESSION_NOT_DEPLOYED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SessionNotDeployed")
        return ErrorCode(dotnet_result, "SESSION_NOT_DEPLOYED")

    @_staticproperty
    def SESSION_ALREADY_DEPLOYED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SessionAlreadyDeployed")
        return ErrorCode(dotnet_result, "SESSION_ALREADY_DEPLOYED")

    @_staticproperty
    def RTSEQ_PARAMETER_ASSIGNMENT_PARAMETER_DOES_NOT_EXIST() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "RtseqParameterAssignmentParameterDoesNotExist")
        return ErrorCode(dotnet_result, "RTSEQ_PARAMETER_ASSIGNMENT_PARAMETER_DOES_NOT_EXIST")

    @_staticproperty
    def BY_REFERENCE_PARAMETER_VALUE_NOT_ASSIGNED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ByReferenceParameterValueNotAssigned")
        return ErrorCode(dotnet_result, "BY_REFERENCE_PARAMETER_VALUE_NOT_ASSIGNED")

    @_staticproperty
    def SEQUENCE_COMPILE_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SequenceCompileError")
        return ErrorCode(dotnet_result, "SEQUENCE_COMPILE_ERROR")

    @_staticproperty
    def RTSEQ_PARAMETER_ASSIGNMENT_INVALID_DATA_TYPE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "RtseqParameterAssignmentInvalidDataType")
        return ErrorCode(dotnet_result, "RTSEQ_PARAMETER_ASSIGNMENT_INVALID_DATA_TYPE")

    @_staticproperty
    def MODEL_PARAMETER_FILE_PARSE_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ModelParameterFileParseError")
        return ErrorCode(dotnet_result, "MODEL_PARAMETER_FILE_PARSE_ERROR")

    @_staticproperty
    def NUMBER_OF_COEFFICIENTS_OUT_OF_RANGE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NumberOfCoefficientsOutOfRange")
        return ErrorCode(dotnet_result, "NUMBER_OF_COEFFICIENTS_OUT_OF_RANGE")

    @_staticproperty
    def DUPLICATE_LOG_SESSION_NAME() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "DuplicateLogSessionName")
        return ErrorCode(dotnet_result, "DUPLICATE_LOG_SESSION_NAME")

    @_staticproperty
    def LOG_SESSION_NOT_FOUND() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "LogSessionNotFound")
        return ErrorCode(dotnet_result, "LOG_SESSION_NOT_FOUND")

    @_staticproperty
    def NOT_ENOUGH_DYNAMIC_DATA_SHARING_SPACE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotEnoughDynamicDataSharingSpace")
        return ErrorCode(dotnet_result, "NOT_ENOUGH_DYNAMIC_DATA_SHARING_SPACE")

    @_staticproperty
    def TARGET_MISSING_DATA_SHARING_DEVICE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "TargetMissingDataSharingDevice")
        return ErrorCode(dotnet_result, "TARGET_MISSING_DATA_SHARING_DEVICE")

    @_staticproperty
    def LOG_TRIGGER_CONDITION_SYNTAX_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "LogTriggerConditionSyntaxError")
        return ErrorCode(dotnet_result, "LOG_TRIGGER_CONDITION_SYNTAX_ERROR")

    @_staticproperty
    def SERVER_PORT_ALREADY_IN_USE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ServerPortAlreadyInUse")
        return ErrorCode(dotnet_result, "SERVER_PORT_ALREADY_IN_USE")

    @_staticproperty
    def NOT_AN_INLINE_CUSTOM_DEVICE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotAnInlineCustomDevice")
        return ErrorCode(dotnet_result, "NOT_AN_INLINE_CUSTOM_DEVICE")

    @_staticproperty
    def PARAMETER_NOT_FOUND() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ParameterNotFound")
        return ErrorCode(dotnet_result, "PARAMETER_NOT_FOUND")

    @_staticproperty
    def INVALID_DAQ_PLUGIN_FILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InvalidDaqPluginFile")
        return ErrorCode(dotnet_result, "INVALID_DAQ_PLUGIN_FILE")

    @_staticproperty
    def DUPLICATE_CHANNEL_ALIAS_MAPPINGS() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "DuplicateChannelAliasMappings")
        return ErrorCode(dotnet_result, "DUPLICATE_CHANNEL_ALIAS_MAPPINGS")

    @_staticproperty
    def MISMATCHED_LENGTHS() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "MismatchedLengths")
        return ErrorCode(dotnet_result, "MISMATCHED_LENGTHS")

    @_staticproperty
    def INCOMPATIBLE_MODEL() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "IncompatibleModel")
        return ErrorCode(dotnet_result, "INCOMPATIBLE_MODEL")

    @_staticproperty
    def UNSUPPORTED_MODEL_ARCHITECTURE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "UnsupportedModelArchitecture")
        return ErrorCode(dotnet_result, "UNSUPPORTED_MODEL_ARCHITECTURE")

    @_staticproperty
    def UNSUPPORTED_FMU_KIND() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "UnsupportedFMUKind")
        return ErrorCode(dotnet_result, "UNSUPPORTED_FMU_KIND")

    @_staticproperty
    def NON_POSITIVE_STEP_SIZE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NonPositiveStepSize")
        return ErrorCode(dotnet_result, "NON_POSITIVE_STEP_SIZE")

    @_staticproperty
    def UNSUPPORTED_FMI_VERSION() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "UnsupportedFMIVersion")
        return ErrorCode(dotnet_result, "UNSUPPORTED_FMI_VERSION")

    @_staticproperty
    def UNMAPPED_ALIAS() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "UnmappedAlias")
        return ErrorCode(dotnet_result, "UNMAPPED_ALIAS")

    @_staticproperty
    def EMPTY_NODE_NAME() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "EmptyNodeName")
        return ErrorCode(dotnet_result, "EMPTY_NODE_NAME")

    @_staticproperty
    def NODE_ALREADY_EXISTS_BY_NAME() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NodeAlreadyExistsByName")
        return ErrorCode(dotnet_result, "NODE_ALREADY_EXISTS_BY_NAME")

    @_staticproperty
    def INPUT_PARAMETER_INVALID() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InputParameterInvalid")
        return ErrorCode(dotnet_result, "INPUT_PARAMETER_INVALID")

    @_staticproperty
    def NO_ACTION_REQUIRED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NoActionRequired")
        return ErrorCode(dotnet_result, "NO_ACTION_REQUIRED")

    @_staticproperty
    def INCORRECT_LOG_FILE_NAME() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "IncorrectLogFileName")
        return ErrorCode(dotnet_result, "INCORRECT_LOG_FILE_NAME")

    @_staticproperty
    def DOWNLOAD_FILE_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "DownloadFileError")
        return ErrorCode(dotnet_result, "DOWNLOAD_FILE_ERROR")

    @_staticproperty
    def TARGET_DISCONNECTED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "TargetDisconnected")
        return ErrorCode(dotnet_result, "TARGET_DISCONNECTED")

    @_staticproperty
    def GATEWAY_NOT_ON_LOCALHOST() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "GatewayNotOnLocalhost")
        return ErrorCode(dotnet_result, "GATEWAY_NOT_ON_LOCALHOST")

    @_staticproperty
    def CHANNEL_GROUP_NOT_FOUND_IN_LOG_FILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelGroupNotFoundInLogFile")
        return ErrorCode(dotnet_result, "CHANNEL_GROUP_NOT_FOUND_IN_LOG_FILE")

    @_staticproperty
    def CHANNEL_NOT_FOUND_IN_LOG_FILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelNotFoundInLogFile")
        return ErrorCode(dotnet_result, "CHANNEL_NOT_FOUND_IN_LOG_FILE")

    @_staticproperty
    def DEPENDENCIES_CYCLE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "DependenciesCycle")
        return ErrorCode(dotnet_result, "DEPENDENCIES_CYCLE")

    @_staticproperty
    def STI_FILE_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "STIFileError")
        return ErrorCode(dotnet_result, "STI_FILE_ERROR")

    @_staticproperty
    def SLSC_CHASSIS_LOAD_FAILED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SLSCChassisLoadFailed")
        return ErrorCode(dotnet_result, "SLSC_CHASSIS_LOAD_FAILED")

    @_staticproperty
    def ELECTRICAL_ERROR_NOT_HANDLED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ElectricalErrorNotHandled")
        return ErrorCode(dotnet_result, "ELECTRICAL_ERROR_NOT_HANDLED")

    @_staticproperty
    def MODEL_NOT_FOUND() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ModelNotFound")
        return ErrorCode(dotnet_result, "MODEL_NOT_FOUND")

    @_staticproperty
    def INVALID_SIGNAL_INDEX() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InvalidSignalIndex")
        return ErrorCode(dotnet_result, "INVALID_SIGNAL_INDEX")

    @_staticproperty
    def NOT_SCALAR_SIGNAL() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotScalarSignal")
        return ErrorCode(dotnet_result, "NOT_SCALAR_SIGNAL")

    @_staticproperty
    def TARGET_RUNNING_CONNECTED_TO_A_DIFFERENT_GATEWAY() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "TargetRunningConnectedToADifferentGateway")
        return ErrorCode(dotnet_result, "TARGET_RUNNING_CONNECTED_TO_A_DIFFERENT_GATEWAY")

    @_staticproperty
    def NO_SPACE_TO_DEPLOY_SEQUENCE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NoSpaceToDeploySequence")
        return ErrorCode(dotnet_result, "NO_SPACE_TO_DEPLOY_SEQUENCE")


class XMLVersionInfo(_DotNetBase):
    """Provides and configures version data for an XML file, including the major, minor, fix, and build version of the XML file."""

    @overload
    def __init__(self, major: int, minor: int, fix: int, build: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.XMLVersionInfo:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.XMLVersionInfo(*unwrapped)

    @property
    def major(self) -> int:
        """Gets or sets the major version number for the current XML file."""
        dotnet_result = self._dotnet_instance.Major
        return _wrap(dotnet_result)

    @major.setter
    def major(self, value: int):
        """Gets or sets the major version number for the current XML file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Major = next(unwrapped)

    @property
    def minor(self) -> int:
        """Gets or sets the minor version number for the current XML file."""
        dotnet_result = self._dotnet_instance.Minor
        return _wrap(dotnet_result)

    @minor.setter
    def minor(self, value: int):
        """Gets or sets the minor version number for the current XML file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Minor = next(unwrapped)

    @property
    def fix(self) -> int:
        """Gets or sets the fix number for the current XML file."""
        dotnet_result = self._dotnet_instance.Fix
        return _wrap(dotnet_result)

    @fix.setter
    def fix(self, value: int):
        """Gets or sets the fix number for the current XML file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Fix = next(unwrapped)

    @property
    def build(self) -> int:
        """Gets or sets the build number for the current XML file."""
        dotnet_result = self._dotnet_instance.Build
        return _wrap(dotnet_result)

    @build.setter
    def build(self, value: int):
        """Gets or sets the build number for the current XML file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Build = next(unwrapped)

    @overload
    def to_string(self) -> str:
        ...

    def to_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ToString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def equals(self, obj: Any) -> bool:
        ...

    @overload
    def equals(self, other: XMLVersionInfo) -> bool:
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

    @overload
    def clone(self) -> Any:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def compare_to(self, other: Any) -> int:
        ...

    @overload
    def compare_to(self, other: XMLVersionInfo) -> int:
        ...

    def compare_to(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CompareTo(*unwrapped)
        return _wrap(dotnet_result)
