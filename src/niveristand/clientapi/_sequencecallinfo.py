from niveristand import _errormessages, errors
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from NationalInstruments.VeriStand.ClientAPI import SequenceCallInfo as SequenceCallInfoDotNet  # noqa: I100


class _SequenceCallInfoFactory(object):
    """Factory class to create niveristand.clientapi._sequencecallinfo._SequenceCallInfo instances."""

    def __init__(self):
        pass

    @staticmethod
    def create(sequence_path, target, parameters, debug, timeout):
        """
        Creates an instance of niveristand.clientapi._sequencecallinfo._SequenceCallInfo class.

        Args:
            sequence_path (str): The file path of the sequence file to execute.
            target (str): The name of the target on which to execute the sequence.
            parameters (list[niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo]):
             The parameter assignments for the sequence.
            debug (bool): Whether the sequence executes in debug mode.
            timeout (float): The timeout in milliseconds within which the sequence must complete each time step.

        Returns:
            niveristand.clientapi._sequencecallinfo._SequenceCallInfo: Newly created instance.

        """
        parameters_dot_net = [parameter.dot_net_instance for parameter in parameters]
        sequence_call_info_dot_net = SequenceCallInfoDotNet(sequence_path, target, parameters_dot_net, debug, timeout)
        sequence_call_info = _SequenceCallInfo(sequence_call_info_dot_net)
        return sequence_call_info


class _SequenceCallInfo(_DotNetClassWrapperBase):
    """
    Provides information about a stimulus profile sequence.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SequenceCallInfo): the C# instance to wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, SequenceCallInfoDotNet):
            super(_SequenceCallInfo, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type % "NationalInstruments.VeriStand.ClientAPI."
                                                              "SequenceCallInfo")
