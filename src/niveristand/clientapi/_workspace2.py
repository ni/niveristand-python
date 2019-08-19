from niveristand import _errormessages, errors
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from niveristand.clientapi._error import _Error
from niveristand.clientapi._nodeinfo import _NodeInfo
from NationalInstruments.VeriStand.ClientAPI import IWorkspace2 as IWorkspace2DotNet  # noqa: I100


class _Workspace2(_DotNetClassWrapperBase):
    """
    Class to perform basic workspace operations, such as getting, setting, and logging channel data.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.WorkspaceImpl): the C# instance to wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, IWorkspace2DotNet):
            super(_Workspace2, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type % "NationalInstruments.VeriStand.ClientAPI.IWorkspace2")

    def get_channel_vector_values(self, channel):
        """
        Gets the vector values of a channel on the target.

        Args:
            channel (): The name of the channel. You must enter the full path to the channel as specified in the system
             definition file.

        Returns:
            int: The number of rows in the vector array.
            int: The number of columns in the vector array.
            [float]: The vector values.

        """
        err, row_dim, col_dim, value = self._dot_net_instance.GetChannelVectorValues(channel)
        err = _Error(err)
        if err.is_error:
            raise \
                errors.VeristandError(_errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message))
        return row_dim, col_dim, value

    def get_multiple_system_nodes_data(self, names):
        """
        Gets information about multiple nodes in the system definition file.

        Args:
            names ([str]): The names of the nodes. You must enter the full path to each node as specified in the system
             definition file.

        Returns:
            niveristand.clientapi._nodeinfo._NodeInfo: Information about the nodes.

        """
        err, node_infos = self._dot_net_instance.GetMultipleSystemNodesData(names, None)
        err = _Error(err)
        if err.is_error:
            raise \
                errors.VeristandError(_errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message))
        return [_NodeInfo(node_info) for node_info in node_infos]

    def get_single_channel_value(self, name):
        """
        Gets the value of a single channel on the target.

        Args:
            name (str): The name of the channel. You must enter the full path to the channel as specified in the system
             definition file.

        Returns:
            float: The value of the specified channel.

        """
        err, value = self._dot_net_instance.GetSingleChannelValue(name, 0)
        err = _Error(err)
        if err.is_error:
            raise \
                errors.VeristandError(_errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message))
        return value

    def set_channel_vector_values(self, channel, new_values):
        """
        Sets the vector values of a channel on the target.

        Args:
            channel (str): The name of the channel. You must enter the full path to the channel as specified in the
             system definition file.
            new_values (List[float]): The vector values. This parameter expects a 1D array. If the channel expects
             two-dimensional data, convert the 2D channel data into a 1D array before passing it to this method.

        """
        err = self._dot_net_instance.SetChannelVectorValues(channel, new_values)
        err = _Error(err)
        if err.is_error:
            raise \
                errors.VeristandError(_errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message))

    def set_single_channel_value(self, name, new_val):
        """
        Sets the value of a single channel on the target.

        Args:
            name (str): The name of the channel. You must enter the full path to the channel as specified in the system
             definition file.
            new_val (float): The value to set.

        Returns:
            None:

        """
        err = self._dot_net_instance.SetSingleChannelValue(name, new_val)
        err = _Error(err)
        if err.is_error:
            raise \
                errors.VeristandError(_errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message))
