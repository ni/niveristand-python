from niveristand import _errormessages, errors
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from NationalInstruments.VeriStand.ClientAPI import NodeInfo as NodeInfoDotNet  # noqa: I100


class _NodeInfo(_DotNetClassWrapperBase):
    """
    Provides information about and configures a node in the system definition file.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.NodeInfo): the C# instance to wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, NodeInfoDotNet):
            super(_NodeInfo, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type % "NationalInstruments.VeriStand.ClientAPI.NodeInfo")

    @property
    def channel_row_dimension(self):
        """
        Gets the number of rows in a channel node value.

        Returns:
            int: The number of rows in a channel node value.

        """
        return self._dot_net_instance.ChannelRowDimension

    @property
    def channel_column_dimension(self):
        """
        Gets the number of columns in a channel node value.

        Returns:
            int: The number of columns in a channel node value.

        """
        return self._dot_net_instance.ChannelColumnDimension
