from niveristand import _errormessages, errors
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from NationalInstruments.VeriStand.Data import SystemDefinitionChannelResource as SystemDefinitionChannelResourceDotNet  # noqa: E501, I100


class _SystemDefinitionChannelResourceFactory(object):
    """
    Factory class.

    Creates niveristand.clientapi._systemdefinitionchannelresource._SystemDefinitionChannelResource instances.

    """

    def __init__(self):
        pass

    @staticmethod
    def create(channel):
        """
        Creates an instance.

        The instance is of type niveristand.clientapi._systemdefinitionchannelresource._SystemDefinitionChannelResource.

        Args:
            channel (str): The channel to map the data resource to in the system definition file.

        Returns:
            niveristand.clientapi._systemdefinitionchannelresource._SystemDefinitionChannelResource: The newly created
             instance.

        """
        return _SystemDefinitionChannelResource(SystemDefinitionChannelResourceDotNet(channel))


class _SystemDefinitionChannelResource(_DotNetClassWrapperBase):
    """
    Represents a data resource mapped to a system definition channel.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SystemDefinitionChannelResource): the C# instance to
         wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, SystemDefinitionChannelResourceDotNet):
            super(_SystemDefinitionChannelResource, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type % "NationalInstruments.VeriStand.Data."
                                                              "SystemDefinitionChannelResource")
