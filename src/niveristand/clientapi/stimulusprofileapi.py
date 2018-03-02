from enum import Enum
import time
from niveristand import errormessages
from niveristand import internal
from niveristand.clientapi.realtimesequencedefinitionapi.erroraction import ErrorAction
from niveristand.exceptions import SequenceError, VeristandError
from NationalInstruments.VeriStand.Data import DataType  # noqa: E501, I100 We need these C# imports to be out of order.

internal.dummy()


class StimulusProfileState(object):
    class CompletionState(Enum):
        """Enum used for possible completion states."""

        Success = 0
        Aborted = 1
        Failed = 2

    def __init__(self, session):
        self.ret_val = None
        self.rt_sequence_completed = False
        self.completion_state = None
        self.session = session
        self.last_error = None

    def sequence_complete_event_handler(self, source, args):
        data_value = args.ReturnValue
        if data_value.Type == DataType.Void:
            self.ret_val = None
        elif data_value.Type in [DataType.Boolean, DataType.Double, DataType.Int32, DataType.Int64, DataType.UInt32,
                                 DataType.UInt64]:
            self.ret_val = data_value.Value
        else:
            raise VeristandError(errormessages.invalid_return_type)
        aborted = args.Aborted
        error = args.Error
        if aborted:
            self.completion_state = StimulusProfileState.CompletionState.Aborted
            self.last_error = SequenceError(error.Code, error.Message, ErrorAction.AbortSequence)
        else:
            if error.Code != 0:
                self.completion_state = StimulusProfileState.CompletionState.Failed
                self.last_error = SequenceError(error.Code, error.Message, ErrorAction.ContinueSequenceExecution)
            else:
                self.completion_state = StimulusProfileState.CompletionState.Success
        self.rt_sequence_completed = True

    def wait_for_result(self):
        while not self.rt_sequence_completed:
            time.sleep(0.01)
