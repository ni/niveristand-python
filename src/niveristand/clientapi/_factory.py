from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from niveristand.clientapi._stimulusprofilesession import _StimulusProfileSession
from niveristand.clientapi._workspace2 import _Workspace2
from NationalInstruments.VeriStand.ClientAPI import Factory as FactoryDotNet  # noqa: I100


class _Factory(_DotNetClassWrapperBase):
    """
    Provides access to the NI VeriStand system and the various interfaces available in the Execution API.

    Any code you write using this API must include a Factory constructor to access NI VeriStand.

    """

    def __init__(self):
        super(_Factory, self).__init__(FactoryDotNet())

    def get_existing_stimulus_profile_session(self, gateway_ip_address, session_id):
        """
        Gets an instance that implements StimulusProfileSession interface.

        The instance can be used to automate the execution of an already deployed Stimulus Profile Session.

        Args:
            gateway_ip_address(str): Specifies the IP address of the VeriStand Gateway.
            session_id(str): Specifies the Session ID of the deployed Stimulus Profile Session.

        Returns:
            niveristand.clientapi._stimulusprofilesession._StimulusProfileSession : A StimulusProfileSession instance

        """
        pass

    def get_new_stimulus_profile_session(self, gateway_ip_address, name, sequences, description):
        """
        Gets an instance that implements StimulusProfileSession interface.

        The instance can be used to automate the execution of an already deployed Stimulus Profile Session.

        Args:
            gateway_ip_address(str): Specifies the IP address of the VeriStand Gateway.
            name(str): Specifies the name of the Stimulus Profile Session.
            sequences([niveristand.clientapi._sequencecallinfo._SequenceCallInfo]): Specifies the sequences to execute
             in the Stimulus Profile Session.
            description(str): Specifies a description for the Stimulus Profile Session.

        Returns:
            niveristand.clientapi._stimulusprofilesession._StimulusProfileSession : A StimulusProfileSession instance.

        """
        return _StimulusProfileSession(
            self._dot_net_instance.GetIStimulusProfileSession(
                gateway_ip_address,
                name,
                [seq_call_info.dot_net_instance for seq_call_info in sequences],
                description))

    def get_workspace2(self, gateway_ip_address):
        """
        Gets an instance that implements the Workspace2 interface.

        The instance can be used use to manage connections between the VeriStand Gateway and one or more targets,
         to start and stop data logging operations, and to configure events for error and status notifications.
          This method allows you to specify the IP address of the VeriStand Gateway.

        Args:
            gateway_ip_address (str): Specifies the IP address of the VeriStand Gateway.

        Returns:
            niveristand.clientapi._workspace2._Workspace2: A Workspace2 instance.

        """
        workspace2 = self._dot_net_instance.GetIWorkspace2(gateway_ip_address)
        return _Workspace2(workspace2)

    def get_localhost_workspace2(self):
        """
        Gets an instance that implements the Workspace2 interface.

        The instance can be used to manage connections between the VeriStand Gateway and one or more targets, to start
         and stop data logging operations, and to configure events for error and status notifications. This method
         assumes that the VeriStand Gateway is running on the localhost.

        Returns:
            niveristand.clientapi._workspace2._Workspace2: A Workspace2 instance.

        """
        workspace2 = self._dot_net_instance.GetIWorkspace2()
        return _Workspace2(workspace2)


class _DefaultGatewayFactory(object):
    """
    Provides access to the NI VeriStand system and the various interfaces available in the Execution API.

    All the instances that are created by this class are using the gateway at a default ip address. Any code you write
     using this API must include a Factory constructor to access NI VeriStand.

    """

    _default_gateway_ip_address = ""
    _default_workspace = None

    @classmethod
    def set_default_gateway_ip_address(cls, gateway_ip_address):
        """
        Sets the default ip address of the gateway.

        This ip address is to be used by work sessions that do not explicitly specify it for every operation.

        Args:
            gateway_ip_address (str): The default ip address of the VeriStand gateway.

        """
        cls._default_gateway_ip_address = gateway_ip_address
        cls._default_gateway = _Factory().get_workspace2(gateway_ip_address)

    @classmethod
    def get_default_gateway_ip_address(cls):
        """
        Gets the default ip address of the gateway.

        This ip address is to be used by default by work sessions that do not explicitly specify it for every operation.

        Returns:
            str: The default ip adderess of the VeriStand gateway.

        """
        return cls._default_gateway_ip_address

    @classmethod
    def get_new_stimulus_profile_session(cls, name, sequences, description):
        """
        Gets an instance that implements StimulusProfileSession interface.

        The instance can be used to automate the execution of an already deployed Stimulus Profile Session.

        Args:
            name(str): Specifies the name of the Stimulus Profile Session.
            sequences([niveristand.clientapi._sequencecallinfo._SequenceCallInfo]): Specifies the sequences to execute
             in the Stimulus Profile Session.
            description(str): Specifies a description for the Stimulus Profile Session.

        Returns:
            niveristand.clientapi._stimulusprofilesession._StimulusProfileSession : A StimulusProfileSession instance.

        """
        return _Factory().\
            get_new_stimulus_profile_session(cls._default_gateway_ip_address, name, sequences, description)

    @classmethod
    def get_workspace2(cls):
        """
        Gets an instance that implements the Workspace2 interface.

        The instance can be used use to manage connections between the VeriStand Gateway and one or more targets,
         to start and stop data logging operations, and to configure events for error and status notifications.
          This method allows you to specify the IP address of the VeriStand Gateway.

        Returns:
            niveristand.clientapi._workspace2._Workspace2: A Workspace2 instance.

        """
        if cls._default_workspace is None:
            cls._default_workspace = _Factory().get_workspace2("")
        return cls._default_workspace
