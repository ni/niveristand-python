from niveristand import _errormessages, errors
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from NationalInstruments.VeriStand import Error as ErrorDotNet  # noqa: I100 We need these C# imports to be out of order


class _Error(_DotNetClassWrapperBase):
    """

    Represents NI VeriStand error information, including an integer error code and a string error message.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.Error):  the C# instance to wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, ErrorDotNet):
            super(_Error, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type % "NationalInstruments.VeriStand.Error")

    @property
    def error_code(self):
        """
        Gets the VeriStand specific ErrorCode.

        Returns:
            (int): the VeriStand specific error code

        """
        return self.dot_net_instance.ErrorCode

    @property
    def is_error(self):
        """
        Gets a Boolean value indicating whether the Error object contains an error state.

        Returns:
            (bool): True if the Error contains an error state.

        """
        return self.dot_net_instance.IsError

    @property
    def resolved_error_message(self):
        """
        Gets the resolved error message.

        The resolved error message provides error information for non-LabVIEW applications.

        Returns:
            (str): The resolved error message for the current Error.

        """
        return self.dot_net_instance.ResolvedErrorMessage
