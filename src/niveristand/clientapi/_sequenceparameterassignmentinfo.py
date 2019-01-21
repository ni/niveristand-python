from niveristand import _errormessages, errors
from niveristand.clientapi._datatypes.rtprimitives import ChannelReference, DataType
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from niveristand.clientapi._systemdefinitionchannelresource import _SystemDefinitionChannelResourceFactory
from NationalInstruments.VeriStand.ClientAPI import SequenceParameterAssignmentInfo as SequenceParameterAssignmentInfoDotNet  # noqa: E501, I100


class _SequenceParameterAssignmentInfoFactory(object):
    """
    Factory class.

    Creates niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo instances.

    """

    def __init__(self):
        pass

    @staticmethod
    def create(parameter_name, value):
        """
        Creates an instance.

        The instance is of type niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo.

        Args:
            parameter_name (): The name of the parameter.
            value (niveristand.clientapi.DataType): The value of the parameter.

        Returns:
            niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo: Newly created
             instance.

        """
        if isinstance(value, ChannelReference):
            sysdef_ch_res = _SystemDefinitionChannelResourceFactory.create(value._channel_name)
            data_resource_dot_net = sysdef_ch_res.dot_net_instance
        elif isinstance(value, DataType):
            data_resource_dot_net = value._data_value
        else:
            raise ValueError

        seq_param_assignment_info_dot_net = SequenceParameterAssignmentInfoDotNet(parameter_name, data_resource_dot_net)
        seq_param_assignment_info = _SequenceParameterAssignmentInfo(seq_param_assignment_info_dot_net)
        return seq_param_assignment_info


class _SequenceParameterAssignmentInfo(_DotNetClassWrapperBase):
    """
    Provides information about an input parameter of a real-time sequence.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SequenceParameterAssignmentInfo): the C# instance to
         wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, SequenceParameterAssignmentInfoDotNet):
            super(_SequenceParameterAssignmentInfo, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type % "NationalInstruments.VeriStand.ClientAPI."
                                                              "SequenceParameterAssignmentInfo")
