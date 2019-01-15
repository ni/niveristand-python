class _DotNetClassWrapperBase(object):
    """

    The base class for all the classes that wrap around a VeriStand public api C# class.

    Args:
        dot_net_instance (): a C# instance of the wrapped C# class.

    """

    def __init__(self, dot_net_instance):
        self._dot_net_instance = dot_net_instance

    @property
    def dot_net_instance(self):
        """
        Gets the C# instance of the wrapped C# class.

        Returns:
            (): The C# instance of the wrapped C# class

        """
        return self._dot_net_instance
