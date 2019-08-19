from niveristand import _errormessages, errors
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from niveristand.clientapi._error import _Error
from niveristand import _internal
from NationalInstruments.VeriStand.ClientAPI import ISequenceControl as ISequenceControlDotNet  # noqa: I100
from NationalInstruments.VeriStand.ClientAPI import IStimulusProfileSession as IStimulusProfileSessionDotNet

_internal.dummy()

class _StimulusProfileSession(_DotNetClassWrapperBase):
    """
    Interface to control and monitor Stimulus Profile Session execution.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.StimulusProfileSessionImpl): the C# instance to wrap.
         around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, IStimulusProfileSessionDotNet):
            super(_StimulusProfileSession, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type % "NationalInstruments.VeriStand.ClientAPI."
                                                              "IStimulusProfileSession")

    def __getitem__(self, item):
        """
        Gets a reference to the sequence specified by the qualified sequence name in the Stimulus Profile Session.

        Args:
            item (str): The sequence for which to get the reference.

        Returns:
            niveristand.clientapi._stimulusprofilesession._SequenceControl: Sequence control reference.

        """
        sequence_control = self._dot_net_instance[item]
        return _SequenceControl(sequence_control)

    def deploy(self, auto_start):
        """
        Deploys the Stimulus Profile Session.

        Args:
            auto_start (bool): If True, starts sequences immediately upon deploy. If False, waits for an external Run
             command.

        Returns:
            str: The ID of the Stimulus profile session.

        """
        ret_val, session_id, err = self._dot_net_instance.Deploy(auto_start, None, None)
        err = _Error(err)
        if err.is_error:
            raise \
                errors.VeristandError(_errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message))
        return session_id

    def undeploy(self):
        """
        Undeploys the Stimulus Profile Session.

        Returns:
            None:

        """
        err = self._dot_net_instance.Undeploy(None)
        err = _Error(err)
        if err.is_error:
            raise \
                errors.VeristandError(_errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message))


class _SequenceControl(_DotNetClassWrapperBase):
    """
    Automates and monitors the execution of a sequence in a stimulus profile session.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SequenceControl): the C# instance to wrap.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, ISequenceControlDotNet):
            super(_SequenceControl, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type % "NationalInstruments.VeriStand.ClientAPI."
                                                              "ISequenceControl")

    def register_sequence_complete_event_handler(self, handler):
        """
        Register callback for when a sequence completes execution.

        Args:
            handler (method): The callback function.

        Returns:
            None:

        """
        self._dot_net_instance.SequenceComplete += handler
