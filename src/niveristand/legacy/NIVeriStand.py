"""
NI VeriStand Python API.

@ Copyright 2009-2018 by National Instruments Corp.
All righs reserved.

C-Python code wrapper of NI Veristand client API.
"""

import os
import warnings
import clr
from niveristand import _internal
clr.AddReference("NationalInstruments.VeriStand, Version=2018.0.0.0, Culture=neutral, PublicKeyToken=a6d690c380daa308")
clr.AddReference(
    "NationalInstruments.VeriStand.ClientAPI, Version=2018.0.0.0, Culture=neutral, PublicKeyToken=a6d690c380daa308")
import System  # noqa
from NationalInstruments.VeriStand import DataArray  # noqa
from NationalInstruments.VeriStand.ClientAPI import Factory  # noqa
from NationalInstruments.VeriStand.ClientAPI import SystemState  # noqa
from NationalInstruments.VeriStand.ClientAPI import AlarmInfo  # noqa
from NationalInstruments.VeriStand.ClientAPI import AlarmPriority  # noqa
from NationalInstruments.VeriStand.ClientAPI import AlarmState  # noqa
from NationalInstruments.VeriStand.ClientAPI import AlarmMode  # noqa
from NationalInstruments.VeriStand.ClientAPI import ModelState  # noqa
from NationalInstruments.VeriStand.ClientAPI import ModelCommand  # noqa
from NationalInstruments.VeriStand.ClientAPI import StimulusState  # noqa
from NationalInstruments.VeriStand.ClientAPI import StimulusResult  # noqa
from NationalInstruments.VeriStand.ClientAPI import LogChannel  # noqa
from NationalInstruments.VeriStand.ClientAPI import LogInfo  # noqa
from NationalInstruments.VeriStand.ClientAPI import PlayModeEnum  # noqa
from NationalInstruments.VeriStand.ClientAPI import PlayStateEnum  # noqa

_internal.dummy()
warnings.warn("NIVeriStand.py module is deprecated. "
              "Use only if required functionality is not yet present in niverstinad.clientapi",
              DeprecationWarning, stacklevel=2)


def LaunchNIVeriStand():
    """Launch NI VeriStand.exe from the installed location."""
    import subprocess
    path = _internal._get_install_path()
    veristand = os.path.join(path, "NI VeriStand.exe")
    print(veristand)
    try:
        subprocess.Popen([veristand, ""]).pid
    except OSError:
        raise NIVeriStandException(-307652, "Could not launch NI VeriStand.")


def _ConvertMATRIXTO1DARRVAL_(values):
    dataArray = []
    rowDim = len(values)
    colDim = len(values[0])
    for col in range(0, colDim):
        for row in range(0, rowDim):
            dataArray.append(values[row][col])
    return tuple(dataArray)


# Exception
class NIVeriStandException(Exception):
    """NI VeriStand exception."""

    def __init__(self, errcode, errstring):
        self.errcode = errcode
        self.errstring = errstring

    def errorcode(self):
        """Return the error code."""
        return self.errcode

    def message(self):
        """Return a formatted message of the error."""
        return 'Consult NI VeriStand help for error code 0x%x error message %s' % (self.errcode, self.errstring)

    def __str__(self):
        return self.message()

    def __repr__(self):
        return self.message()


def _RaiseException_(errorObject):
    if (errorObject.IsError):
        raise NIVeriStandException(errorObject.Code, errorObject.Message)


# Helper function to convert 1D flat array of values into a 2 dimensional data. Data is packed by its column first.
def _Convert1DARRVALTOMATRIX_(rowDim, colDim, data):
    values = []
    for row in range(0, rowDim):
        values.append([])
    for row in range(0, rowDim):
        dataIdx = row
        for col in range(0, colDim):
            values[row].append(data[dataIdx])
            dataIdx = dataIdx + rowDim
    return values


def _ConvertMATRIXARRToDataArray_(matArr):
    dataArrayArray = []
    numElements = len(matArr)
    for elIdx in range(0, numElements):
        rowDim = len(matArr[elIdx])
        colDim = len(matArr[elIdx][0])
        dimValue = []
        dimValue.append(rowDim)
        dimValue.append(colDim)
        doubleVectorValue = []
        for col in range(0, colDim):
            for row in range(0, rowDim):
                doubleVectorValue.append(matArr[elIdx][row][col])
        dataArrayElem = DataArray()
        dataArrayElem.Value = tuple(doubleVectorValue)
        dataArrayElem.Dim = tuple(dimValue)
        dataArrayArray.append(dataArrayElem)
    return tuple(dataArrayArray)


def _ConvertListParamToTuple_(param):
    if isinstance(param, list):
        return tuple(param)
    else:
        return param


# Workspace enum:
class PySystemState:
    """
    The State of the NI VeriStand.exe.

    Idle indicate there is no workspace configuration file deployed
    Active indicate there is a workspace configuration file deployed
    """

    Idle = 0
    Active = 1


# Helper function to create Log Info and Log Channel classes.
def CreateLogChannel(channel_path):
    return LogChannel(channel_path)


def CreateLogInfo():
    return LogInfo()


# define Log Info Trigger Type
class PyLogInfoTriggerType:
    """Priority of an alarm."""

    none = 0
    in_limits = 1
    out_of_limits = 2


def SetLogInfoTrigger(logInfo, triggerType):
    if (triggerType == 0):
        logInfo.trigger_type = LogInfo.trigger.none
    elif (triggerType == 1):
        logInfo.trigger_type = LogInfo.trigger.in_limits
    elif (triggerType == 2):
        logInfo.trigger_type = LogInfo.trigger.out_of_limits


def SetLogInfoChannels(logInfo, logChannelList):
    tupleChannels = _ConvertListParamToTuple_(logChannelList)
    logInfo.channels = tupleChannels


# Workspace definition
class Workspace:
    """Interface to control the running state of the system and access the channels in the system."""

    def __init__(self):
        self.iwks = Factory().GetIWorkspace()

    def GetEngineState(self):
        """Return the current state of the system."""
        data = self.iwks.GetEngineState(0, "", "", "")
        _RaiseException_(data[0])
        return {'state': self._NetSystemStateToPy_(data[1]), 'workspace_file': data[2],
                'systemdefinition_file': data[3], 'ip_address': data[4]}

    def RunWorkspaceFile(self, file, launchworkspacewindow, deploysystemdefinition, timeout, username, password):
        """Start running on the specified workspace configuration file.

        Function error out when there is already a configuration running.
        Caller need to explicitly stop the running configuration.
        Function will wait for the specified timeout.
        If the process timeout, the deployment process might have taken longer than expected,
        check the status of the system with GetEngineState function.
        """
        _RaiseException_(
            self.iwks.RunWorkspaceFile(file, launchworkspacewindow, deploysystemdefinition, timeout, username,
                                       password))

    def StopWorkspaceFile(self, password):
        """Stop the current configuration."""
        _RaiseException_(self.iwks.StopWorkspaceFile(password))

    def LockWorkspaceFile(self, old_password, new_password):
        """
        Lock the currently running configuration.

        Function succeed if there is a running configuration.
        If the currently running configuration has an existing password
        the user need to provide the current password in old_password.
        """
        _RaiseException_(self.iwks.LockWorkspaceFile(old_password, new_password))

    def UnlockWorkspaceFile(self, password):
        """Unlock the currently running configuration."""
        _RaiseException_(self.iwks.UnlockWorkspaceFile(password))

    def GetSingleChannelValue(self, name):
        """Get the channel value."""
        data = 0.0
        data = self.iwks.GetSingleChannelValue(name, data)
        _RaiseException_(data[0])
        return data[1]

    def GetMultipleChannelValues(self, names):
        """Get multiple channel values."""
        tuppleNames = _ConvertListParamToTuple_(names)
        data = self.iwks.GetMultipleChannelValues(tuppleNames)
        _RaiseException_(data[0])
        values = []
        for i in data[1]:
            values.append(i)
        return values

    def GetChannelVectorValues(self, name):
        """Get a channel vector values."""
        data = self.iwks.GetChannelVectorValues(name)
        _RaiseException_(data[0])
        return _Convert1DARRVALTOMATRIX_(data[1], data[2], data[3])

    def SetSingleChannelValue(self, name, value):
        """Set the channel value."""
        _RaiseException_(self.iwks.SetSingleChannelValue(name, value))

    def SetMultipleChannelValues(self, names, values):
        """Set the multiple channels."""
        tuppleNames = _ConvertListParamToTuple_(names)
        tuppleValues = _ConvertListParamToTuple_(values)
        _RaiseException_(self.iwks.SetMultipleChannelValues(tuppleNames, tuppleValues))

    def SetChannelVectorValues(self, name, values):
        """
        Set a parameter vector values.

        Values are expected to be a matrix type.
        """
        ws2 = Workspace2("")
        ws2.SetChannelValues([name], [values])

    def GetMultipleSystemNodesData(self, names):
        """Get multiple nodes info."""
        tuppleNames = _ConvertListParamToTuple_(names)
        data = self.iwks.GetMultipleSystemNodesData(tuppleNames, None)
        _RaiseException_(data[0])
        nodes = []
        for i in data[1]:
            nodes.append(self._ConvertNodeInfoToDictionary_(i))
        return nodes

    def GetSystemNodeChildren(self, name):
        """Get the node list under a specific node."""
        data = self.iwks.GetSystemNodeChildren(name, None)
        _RaiseException_(data[0])
        nodes = []
        for i in data[1]:
            nodes.append(self._ConvertNodeInfoToDictionary_(i))
        return nodes

    def GetSystemNodeChannelList(self, name):
        """
        Get all channels under a specified node.

        If node name is "" then it will get all channels in the system
        """
        data = self.iwks.GetSystemNodeChannelList(name, None)
        _RaiseException_(data[0])
        nodes = []
        for i in data[1]:
            nodes.append(self._ConvertNodeInfoToDictionary_(i))
        return nodes

    def GetAliasList(self):
        """Get all aliases under a system."""
        data = self.iwks.GetAliasList(None, None)
        _RaiseException_(data[0])
        dict = {}
        for i in range(0, len(data[1])):
            dict[data[1][i]] = data[2][i]
        return dict

    def _NetSystemStateToPy_(self, net):
        if (net == SystemState.Idle):
            return PySystemState.Idle
        elif (net == SystemState.Active):
            return PySystemState.Active
        else:
            raise ValueError

    def _ConvertNodeInfoToDictionary_(self, nodeInfo):
        return {'name': nodeInfo.Name, 'path': nodeInfo.FullPath,
                'isChannel': nodeInfo.IsChannel, 'isReadable': nodeInfo.IsReadable,
                'isWritable': nodeInfo.IsWritable, 'isScalable': nodeInfo.IsScalable,
                'unit': nodeInfo.ChannelUnit}


class Workspace2(Workspace):
    """Interface to control the running state of the system and access the channels in the system."""

    def __init__(self, gatewayIPAddress=None):
        if (gatewayIPAddress is None):
            self.iwks = Factory().GetIWorkspace2("")
        else:
            self.iwks = Factory().GetIWorkspace2(gatewayIPAddress)

    def GetSystemState(self):
        """Return the current state of the system."""
        data = self.iwks.GetSystemState(0, "", None)
        _RaiseException_(data[0])
        targets = []
        for target in data[3]:
            targets.append(target)
        return {'state': self._NetSystemStateToPy_(data[1]), 'systemdefinition_file': data[2],
                'targets': tuple(targets)}

    def ConnectToSystem(self, systemdefinition_file, deploy, timeout):
        """Connect the VeriStand Gateway to one or more targets running the specified System Definition file."""
        _RaiseException_(
            self.iwks.ConnectToSystem(systemdefinition_file, System.Boolean(deploy), System.UInt32(timeout)))

    def DisconnectFromSystem(self, password, undeploy_system_definition):
        """Disconnect the VeriStand Gateway from the targets."""
        _RaiseException_(self.iwks.DisconnectFromSystem(password, undeploy_system_definition))

    def LockConnection(self, old_password, new_password):
        """
        Lock the current VeriStand Gateway connection.

        If the connection has already been locked, the previous password must be supplied.
        """
        _RaiseException_(self.iwks.LockConnection(old_password, new_password))

    def UnlockConnection(self, password):
        """Unlock the current VeriStand Gateway connection."""
        _RaiseException_(self.iwks.UnlockConnection(password))

    def StartDataLogging(self, configuration_name, logInfo):
        """Start logging data according to the specified configuration."""
        _RaiseException_(self.iwks.StartDataLogging(configuration_name, logInfo))

    def StopDataLogging(self, configuration_name):
        """Terminates data logging for the specified configuration."""
        _RaiseException_(self.iwks.StopDataLogging(configuration_name))

    def SetChannelValues(self, channels, newValues):
        """Set multiple channel values can be a mix of scalar or vector or matrix."""
        tupleChannelNames = _ConvertListParamToTuple_(channels)
        tupleArray = _ConvertMATRIXARRToDataArray_(newValues)
        _RaiseException_(self.iwks.SetChannelValues(tupleChannelNames, tupleArray))


# define Alarm enums
class PyAlarmPriority:
    """Priority of an alarm."""

    Low = 0
    Medium = 1
    High = 2


class PyAlarmState:
    """State of a an alarm in the engine."""

    Disabled = 0
    Enabled = 1
    Tripped = 2
    DelayedTripped = 3
    Indicate = 4


class PyAlarmMode:
    """
    Mode of an alarm when it get triggered.

    Normal will run the associated script, Indicate will only trigger the alarm.
    """

    Normal = 0
    IndicateOnly = 1


# define alarm class
class Alarm:
    """Interface to query information on a configured alarm."""

    def __init__(self, name, target=None, gatewayIPAddress=None):
        if ((target is None) and (gatewayIPAddress is None)):
            self.ialarm = Factory().GetIAlarm(name)
        elif (target is None):
            self.ialarm = Factory().GetIAlarm("", name, gatewayIPAddress)
        elif (gatewayIPAddress is None):
            self.ialarm = Factory().GetIAlarm(target, name, "")
        else:
            self.ialarm = Factory().GetIAlarm(target, name, gatewayIPAddress)

    def GetAlarmData(self, timeout):
        """Get alarm info for this alarm."""
        data = self.ialarm.GetAlarmData(None, System.UInt32(timeout))
        _RaiseException_(data[0])
        return self._ConvertAlarmToDictionary_(data[1])

    def SetAlarmData(self, alarmDict):
        """
        Set alarm data.

        DEPRECATED function. This function does not support the Priority Number field.
        Use SetAlarmData2() instead.
        """
        netAlarmInfo = self._ConvertDictionaryToAlarm_(alarmDict)
        _RaiseException_(self.ialarm.SetAlarmData(netAlarmInfo))

    def SetAlarmData2(self, alarmDict):
        """Modify an alarm in the system."""
        netAlarmInfo = self._ConvertDictionaryToAlarm2_(alarmDict)
        _RaiseException_(self.ialarm.SetAlarmData(netAlarmInfo))

    def SetEnabledState(self, enabled):
        """Enable or Disable the current alarm."""
        _RaiseException_(self.ialarm.SetEnabledState(enabled))

    def SetAlarmMode(self, mode):
        """Change the mode of this alarm. See PyAlarmMode for possible value."""
        _RaiseException_(self.ialarm.SetAlarmMode(self._PyAlarmModeToNet_(mode)))

    def _NetAlarmPriorityToPy_(self, net):
        if (net == AlarmPriority.Low):
            return PyAlarmPriority.Low
        elif (net == AlarmPriority.Medium):
            return PyAlarmPriority.Medium
        elif (net == AlarmPriority.High):
            return PyAlarmPriority.High
        else:
            raise ValueError

    def _PyAlarmPriorityToNet_(self, py):
        if (py == PyAlarmPriority.Low):
            return AlarmPriority.Low
        elif (py == PyAlarmPriority.Medium):
            return AlarmPriority.Medium
        elif (py == PyAlarmPriority.High):
            return AlarmPriority.High
        else:
            raise ValueError

    def _NetAlarmStateToPy_(self, net):
        if (net == AlarmState.Disabled):
            return PyAlarmState.Disabled
        elif (net == AlarmState.Enabled):
            return PyAlarmState.Enabled
        elif (net == AlarmState.Tripped):
            return PyAlarmState.Tripped
        elif (net == AlarmState.DelayedTripped):
            return PyAlarmState.DelayedTripped
        elif (net == AlarmState.Indicate):
            return PyAlarmState.Indicate
        else:
            raise ValueError

    def _PyAlarmStateToNet_(self, py):
        if (py == PyAlarmState.Disabled):
            return AlarmState.Disabled
        elif (py == PyAlarmState.Enabled):
            return AlarmState.Enabled
        elif (py == PyAlarmState.Tripped):
            return AlarmState.Tripped
        elif (py == PyAlarmState.DelayedTripped):
            return AlarmState.DelayedTripped
        elif (py == PyAlarmState.Indicaet):
            return AlarmState.Indicate
        else:
            raise ValueError

    def _NetAlarmModeToPy_(self, net):
        if (net == AlarmMode.Normal):
            return PyAlarmMode.Normal
        elif (net == AlarmMode.IndicateOnly):
            return PyAlarmMode.IndicateOnly
        else:
            raise ValueError

    def _PyAlarmModeToNet_(self, py):
        if (py == PyAlarmMode.Normal):
            return AlarmMode.Normal
        elif (py == PyAlarmMode.IndicateOnly):
            return AlarmMode.IndicateOnly
        else:
            raise ValueError

    def _ConvertAlarmToDictionary_(self, alarm):
        return {'WatchChannel': alarm.WatchChannel,
                'HighLimitIsConstant': alarm.HighLimitIsConstant, 'HighLimit': alarm.HighLimit,
                'HighLimitChannel': alarm.HighLimitChannelName,
                'LowLimitIsConstant': alarm.LowLimitIsConstant, 'LowLimit': alarm.LowLimit,
                'LowLimitChannel': alarm.LowLimitChannelName,
                'DelayDuration': alarm.DelayDuration, 'TripValue': alarm.TripValue,
                'ProcedureName': alarm.ProcedureName,
                'Priority': self._NetAlarmPriorityToPy_(alarm.Priority),
                'PriorityNumber': alarm.PriorityNumber,
                'State': self._NetAlarmStateToPy_(alarm.State),
                'Mode': self._NetAlarmModeToPy_(alarm.Mode),
                'GroupNumber': alarm.GroupNumber,
                'Name': alarm.Name,
                'FullName': alarm.FullName}

    def _ConvertDictionaryToAlarm_(self, alarm):
        net = AlarmInfo()
        net.WatchChannel = alarm['WatchChannel']
        net.HighLimitIsConstant = alarm['HighLimitIsConstant']
        net.HighLimit = alarm['HighLimit']
        net.HighLimitChannelName = alarm['HighLimitChannel']
        net.LowLimitIsConstant = alarm['LowLimitIsConstant']
        net.LowLimit = alarm['LowLimit']
        net.LowLimitChannelName = alarm['LowLimitChannel']
        net.DelayDuration = alarm['DelayDuration']
        net.TripValue = alarm['TripValue']
        net.ProcedureName = alarm['ProcedureName']
        net.Priority = self._PyAlarmPriorityToNet_(alarm['Priority'])
        net.State = self._PyAlarmStateToNet_(alarm['State'])
        net.Mode = self._PyAlarmModeToNet_(alarm['Mode'])
        return net

    def _ConvertDictionaryToAlarm2_(self, alarm):
        net = AlarmInfo()
        net.WatchChannel = alarm['WatchChannel']
        net.HighLimitIsConstant = alarm['HighLimitIsConstant']
        net.HighLimit = alarm['HighLimit']
        net.HighLimitChannelName = alarm['HighLimitChannel']
        net.LowLimitIsConstant = alarm['LowLimitIsConstant']
        net.LowLimit = alarm['LowLimit']
        net.LowLimitChannelName = alarm['LowLimitChannel']
        net.DelayDuration = alarm['DelayDuration']
        net.TripValue = alarm['TripValue']
        net.ProcedureName = alarm['ProcedureName']
        net.PriorityNumber = alarm['PriorityNumber']
        net.State = self._PyAlarmStateToNet_(alarm['State'])
        net.Mode = self._PyAlarmModeToNet_(alarm['Mode'])
        return net


# define AlarmManager class
class AlarmManager:
    """Interface to get information on the server alarms state."""

    def __init__(self):
        self.iamgr = Factory().GetIAlarmManager()

    def GetAlarmList(self):
        """Get the configured alarms' name in the system."""
        data = []
        data = self.iamgr.GetAlarmList(data)
        _RaiseException_(data[0])
        values = []
        for i in data[1]:
            values.append(i)
        return values

    def GetAlarmsStatus(self):
        """Get status on high,med,low alarm in the system."""
        a0 = a1 = a2 = System.Boolean(False)
        aname0 = aname1 = aname2 = System.String('')
        data = self.iamgr.GetAlarmsStatus(a0, a1, a2, aname0, aname1, aname2)
        _RaiseException_(data[0])
        return {'HighAlarm': data[1], 'MediumAlarm': data[2], 'LowAlarm': data[3], 'HighAlarmName': data[4],
                'MedAlarmName': data[5], 'LowAlarmName': data[6]}

    def GetMultipleAlarmsData(self, alarms, timeout):
        """Get alarm info for a list of alarms."""
        data = self.iamgr.GetMultipleAlarmsData(list(alarms), System.UInt32(timeout), [])
        _RaiseException_(data[0])
        temp = Alarm('')
        values = []
        for netAlarmInfo in data[1]:
            values.append(temp._ConvertAlarmToDictionary_(netAlarmInfo))
        return values


class AlarmManager2:
    """Interface to get information on the server alarms state."""

    def __init__(self, gateway_ip_address=None):
        if (gateway_ip_address is None):
            self.iamgr = Factory().GetIAlarmManager2("")
        else:
            self.iamgr = Factory().GetIAlarmManager2(gateway_ip_address)

    def GetAlarmList(self, target):
        """Get the configured alarms' name in the system."""
        data = self.iamgr.GetAlarmList(target, None)
        _RaiseException_(data[0])
        values = []
        for i in data[1]:
            values.append(i)
        return values

    def GetAlarmsStatus(self, target):
        """Get status on high,med,low alarm in the system."""
        data = self.iamgr.GetAlarmsStatus(target)
        _RaiseException_(data[0])
        return {'HighAlarm': data[1], 'MediumAlarm': data[2], 'LowAlarm': data[3], 'HighAlarmName': data[4],
                'MedAlarmName': data[5], 'LowAlarmName': data[6]}

    def GetMultipleAlarmsData(self, target, alarms, timeout):
        """Get alarm info for a list of alarms."""
        tupleAlarmNames = _ConvertListParamToTuple_(alarms)
        data = self.iamgr.GetMultipleAlarmsData(target, tupleAlarmNames, System.UInt32(timeout), None)
        _RaiseException_(data[0])
        temp = Alarm('')
        values = []
        for netAlarmInfo in data[1]:
            values.append(temp._ConvertAlarmToDictionary_(netAlarmInfo))
        return values


# define Model enum
class PyModelState:
    """State of a model."""

    Running = 0
    Paused = 1
    Resetting = 2
    Idle = 3
    Stopped = 4
    Restoring = 5
    Stopping = 6


class PyModelCommand:
    """Command to change model state."""

    Start = 0
    Pause = 1
    Reset = 2


# define Model class
class Model:
    """Interface to get information on a specific model running on the system."""

    def __init__(self, name, target=None, gatewayIPAddress=None):
        if ((target is None) and (gatewayIPAddress is None)):
            self.imodel = Factory().GetIModel(name)
        elif (target is None):
            self.imodel = Factory().GetIModel(gatewayIPAddress, "", name)
        elif (gatewayIPAddress is None):
            self.imodel = Factory().GetIModel("", target, name)
        else:
            self.imodel = Factory().GetIModel(gatewayIPAddress, target, name)

    def GetModelExecutionState(self):
        """Get the model time and status."""
        data = self.imodel.GetModelExecutionState()
        _RaiseException_(data[0])
        values = {'time': data[1], 'state': self._NetModelStateToPy_(data[2])}
        return values

    def SetModelExecutionState(self, command):
        """
        Change the current state of the model.

        This is a request operation on the server.
        Successful invocation of the function does not imply the model state has change.
        See PyModelState for command values
        """
        _RaiseException_(self.imodel.SetModelExecutionState(self._PyModelStateToNet_(command)))

    def SaveModelState(self, filepath):
        """Save the current model state to the specified file path on the target."""
        _RaiseException_(self.imodel.SaveModelState(filepath))

    def RestoreModelState(self, filepath):
        """Restore the model state from a specified file path on the target."""
        _RaiseException_(self.imodel.RestoreModelState(filepath))

    def _NetModelStateToPy_(self, net):
        if (net == ModelState.Running):
            return PyModelState.Running
        elif (net == ModelState.Paused):
            return PyModelState.Paused
        elif (net == ModelState.Resetting):
            return PyModelState.Resetting
        elif (net == ModelState.Idle):
            return PyModelState.Idle
        elif (net == ModelState.Stopped):
            return PyModelState.Stopped
        elif (net == ModelState.Restoring):
            return PyModelState.Restoring
        elif (net == ModelState.Saving):
            return PyModelState.Saving
        else:
            raise ValueError

    def _PyModelStateToNet_(self, py):
        if (py == PyModelCommand.Start):
            return ModelCommand.Start
        elif (py == PyModelCommand.Pause):
            return ModelCommand.Pause
        elif (py == PyModelCommand.Reset):
            return ModelCommand.Reset
        else:
            raise ValueError


# define ModelManager
class ModelManager:
    """Interface to query information on the configured models in the system."""

    def __init__(self):
        self.modmgr = Factory().GetIModelManager()

    def GetModelList(self):
        """Return the list of models."""
        data = self.modmgr.GetModelList()
        _RaiseException_(data[0])
        models = []
        for i in data[1]:
            models.append(i)
        return models

    def GetParametersList(self):
        """Return the list of parameters in the system."""
        data = self.modmgr.GetParametersList()
        _RaiseException_(data[0])
        params = []
        for i in data[1]:
            params.append(i)
        return params

    def GetSingleParameterValue(self, name):
        """Get the parameters value."""
        data = self.modmgr.GetSingleParameterValue(name)
        _RaiseException_(data[0])
        return data[1]

    def GetMultipleParameterValues(self, names):
        """Get multiple parameters values."""
        tupleParamNames = _ConvertListParamToTuple_(names)
        data = self.modmgr.GetMultipleParameterValues(tupleParamNames)
        _RaiseException_(data[0])
        values = []
        for i in data[1]:
            values.append(i)
        return values

    def GetParameterVectorValues(self, name):
        """Get a parameter vector values."""
        data = self.modmgr.GetParameterVectorValues(name)
        _RaiseException_(data[0])
        return _Convert1DARRVALTOMATRIX_(data[1], data[2], data[3])

    def SetSingleParameterValue(self, name, value):
        """Set parameter value."""
        _RaiseException_(self.modmgr.SetSingleParameterValue(name, value))

    def SetMultipleParameterValues(self, names, values):
        """Set multiple parameters values."""
        tupleParamNames = _ConvertListParamToTuple_(names)
        tupleParamValues = _ConvertListParamToTuple_(values)
        _RaiseException_(self.modmgr.SetMultipleParameterValues(tupleParamNames, tupleParamValues))

    def SetParameterVectorValues(self, name, values):
        """
        Set a parameter vector values.

        Values are expected to be a matrix type.
        """
        tupleArray = _ConvertMATRIXTO1DARRVAL_(values)
        _RaiseException_(self.modmgr.SetParameterVectorValues(name, tupleArray))


class ModelManager2(ModelManager):
    """Interface to query information on the configured models in the system."""

    def __init__(self, gateway_ip_address=None):
        if (gateway_ip_address is None):
            self.modmgr = Factory().GetIModelManager2("")
        else:
            self.modmgr = Factory().GetIModelManager2(gateway_ip_address)

    def GetModelList(self, target):
        """Return the list of models on the specified target."""
        data = self.modmgr.GetModelList(target)
        _RaiseException_(data[0])
        models = []
        for i in data[1]:
            models.append(i)
        return models

    def GetParametersList(self, target):
        """Return the list of parameters in the specified target."""
        data = self.modmgr.GetParametersList(target)
        _RaiseException_(data[0])
        params = []
        for i in data[1]:
            params.append(i)
        return params

    def GetSingleParameterValue(self, target, name):
        """Get the parameters value."""
        data = self.modmgr.GetSingleParameterValue(target, name)
        _RaiseException_(data[0])
        return data[1]

    def GetMultipleParameterValues(self, target, names):
        """Get multiple parameters values."""
        tupleNames = _ConvertListParamToTuple_(names)
        data = self.modmgr.GetMultipleParameterValues(target, tupleNames)
        _RaiseException_(data[0])
        values = []
        for i in data[1]:
            values.append(i)
        return values

    def GetParameterVectorValues(self, target, name):
        """Get a parameter vector values."""
        data = self.modmgr.GetParameterVectorValues(target, name)
        _RaiseException_(data[0])
        return _Convert1DARRVALTOMATRIX_(data[1], data[2], data[3])

    def SetSingleParameterValue(self, target, name, value):
        """Set parameter value."""
        _RaiseException_(self.modmgr.SetSingleParameterValue(target, name, value))

    def SetMultipleParameterValues(self, target, names, values):
        """Set multiple parameters values."""
        tupleNames = _ConvertListParamToTuple_(names)
        tupleValues = _ConvertListParamToTuple_(values)
        _RaiseException_(self.modmgr.SetMultipleParameterValues(target, tupleNames, tupleValues))

    def SetParameterVectorValues(self, target, name, values):
        """Set a parameter vector values.

        Values are expected to be a matrix type.
        """
        self.SetParameterValues(target, [name], [values])

    def SetParameterValues(self, target, names, matrixArr):
        """
        Set multiple parameter vector values.

        Values are expceted to be a array of matrix type.
        Sample usage ModelManager2.SetParameterValues("target1",["1By3Param","2By3Param"],[[[1,2,3]],[[1,2,3],[4,5,6]]])
        """
        tupleNames = _ConvertListParamToTuple_(names)
        dataArrayArrays = _ConvertMATRIXARRToDataArray_(matrixArr)
        _RaiseException_(self.modmgr.SetParameterValues(target, tupleNames, dataArrayArrays))

    def UpdateParametersFromFile(self, parameterfiles):
        """Update a set of parameters specified in the parameter files."""
        tupleFiles = _ConvertListParamToTuple_(parameterfiles)
        _RaiseException_(self.modmgr.UpdateParametersFromFile(tupleFiles))


# define class ChannelFaultManager
class ChannelFaultManager:
    """Interface to do software value forcing on the system."""

    def __init__(self, gatewayIPAddress=None):
        if (gatewayIPAddress is None):
            self.isfiu = Factory().GetIChannelFault("")
        else:
            self.isfiu = Factory().GetIChannelFault(gatewayIPAddress)

    def GetFaultList(self):
        """Get the current list of all faulted channels."""
        data = self.isfiu.GetFaultList()
        _RaiseException_(data[0])
        return zip(data[1], data[2])

    def GetFaultValue(self, name):
        """Get the fault value of a faulted channel."""
        data = self.isfiu.GetFaultValue(name)
        _RaiseException_(data[0])
        return {'faulted': data[1], 'fault value': data[2]}

    def SetFaultValue(self, name, value):
        """Set the fault value of a faulted channel."""
        _RaiseException_(self.isfiu.SetFaultValue(name, value))

    def ClearFault(self, name):
        """Remove the channel from faulted list."""
        _RaiseException_(self.isfiu.ClearFault(name))

    def ClearAllFaults(self):
        """Clear all faults."""
        _RaiseException_(self.isfiu.ClearAllFaults())


# define stimulus enum
class PyStimulusState:
    """State of the Stimulus Generation Server."""

    Stopped = 0
    Starting = 1
    Running = 2
    Stopping = 3


class PyStimulusResult:
    """Stimulus Generation Result."""

    NoResult = 0
    Passed = 1
    Failed = 2
    Error = 3


# define stimulus
class Stimulus:
    def __init__(self):
        self.istim = Factory().GetIStimulus()

    def __del__(self):
        self.UnreserveStimulusProfileManager()

    def ReserveStimulusProfileManager(self):
        """
        Create a task will reserve the stimulus generation server for use.

        Creation of a task will prevent other client to interrupt the stimulus generation process.
        """
        _RaiseException_(self.istim.ReserveStimulusProfileManager())

    def UnreserveStimulusProfileManager(self):
        """Destroy a task will unreserve the stimulus genertion server for other client to use."""
        _RaiseException_(self.istim.UnreserveStimulusProfileManager())

    def GetStimulusProfileManagerState(self):
        """Return the state of the stimulus generation component."""
        data = self.istim.GetStimulusProfileManagerState()
        _RaiseException_(data[0])
        return self._NetStimulusStateToPy_(data[1])

    def RunStimulusProfile(self, testfile, baselogpath, timeout, autostart, stopondisconnect):
        """Start the stimulus generation defined by the file."""
        _RaiseException_(self.istim.RunStimulusProfile(testfile, baselogpath, timeout, autostart, stopondisconnect))

    def StopStimulusProfile(self):
        """Stop the stimulus generation."""
        _RaiseException_(self.istim.StopStimulusProfile())

    def GetStimulusProfileFile(self):
        """Get the current stimulus definion file."""
        data = self.istim.GetStimulusProfileFile()
        _RaiseException_(data[0])
        return data[1]

    def GetStimulusProfileResult(self):
        """
        Get the result of stimulus generation test.

        Only table test will produce a test file result.
        """
        data = self.istim.GetStimulusProfileResult()
        _RaiseException_(data[0])
        values = {'Result': self._NetStimulusResultToPy_(data[1]), 'File': data[2]}
        return values

    def _NetStimulusStateToPy_(self, net):
        if (net == StimulusState.Stopped):
            return PyStimulusState.Stopped
        elif (net == StimulusState.Starting):
            return PyStimulusState.Starting
        elif (net == StimulusState.Running):
            return PyStimulusState.Running
        elif (net == StimulusState.Stopping):
            return PyStimulusState.Stopping
        else:
            raise ValueError

    def _NetStimulusResultToPy_(self, net):
        # TODO: This is supposed to be StimulusResult.None !
        if (net == StimulusResult.Passed):
            return PyStimulusResult.NoResult
        elif (net == StimulusResult.Passed):
            return PyStimulusResult.Passed
        elif (net == StimulusResult.Failed):
            return PyStimulusResult.Failed
        elif (net == PyStimulusResult.Error):
            return PyStimulusResult.Error
        else:
            raise ValueError


class Stimulus2(Stimulus):
    """Class to automate the execution of stimulus profiles."""

    def __init__(self, gatewayIPAddress=None):
        if (gatewayIPAddress is None):
            self.istim = Factory().GetIStimulus2("")
        else:
            self.istim = Factory().GetIStimulus2(gatewayIPAddress)

    def __del__(self):
        self.UnreserveStimulusProfileManager()

    def RunStimulusProfile(self, testfile, baselogpath, timeout, autostart, stopondisconnect, parameterfiles=()):
        """Start the stimulus generation defined by the file."""
        tupleFiles = _ConvertListParamToTuple_(parameterfiles)
        _RaiseException_(
            self.istim.RunStimulusProfile(testfile, baselogpath, timeout, autostart, stopondisconnect, tupleFiles))


# define MacroRecorder
class MacroRecorder:
    def __init__(self):
        self.record = Factory().GetIMacroRecorder()

    def StartRecording(self):
        _RaiseException_(self.record.StartRecording())

    def StopRecording(self):
        _RaiseException_(self.record.StopRecording())

    def ResumeRecording(self):
        _RaiseException_(self.record.ResumeRecording())

    def SaveMacro(self, file):
        _RaiseException_(self.record.SaveMacro(file))

    def GetCommandLines(self):
        data = self.record.GetCommandLines()
        _RaiseException_(data[0])
        commandLines = []
        for i in data[1]:
            data = {'seconds': i.seconds, 'cmdLine': i.cmdLine}
            commandLines.append(data)
        return commandLines


# define MacroPlayer
class PyMacroPlayerState:
    """The Macro player state."""

    NotPlaying = 0
    Playing = 1
    Paused = 2


class PyMacroPlayerMode:
    """The Macro player replay mode."""

    IgnoreTiming = 0
    UseTiming = 1


class MacroPlayer:
    def __init__(self, gatewayIPAddress=None):
        if (gatewayIPAddress is None):
            self.player = Factory().GetIMacroPlayer("")
        else:
            self.player = Factory().GetIMacroPlayer(gatewayIPAddress)

    def LoadMacro(self, file):
        """Load a workspace macro."""
        _RaiseException_(self.player.LoadMacro(file))

    def PlayState(self):
        """Get the current play state."""
        data = self.player.PlayState()
        if (data == PlayStateEnum.NotPlaying):
            return PyMacroPlayerState.NotPlaying
        elif (data == PlayStateEnum.Playing):
            return PyMacroPlayerState.Playing
        elif (data == PlayStateEnum.Paused):
            return PyMacroPlayerState.Paused

    def PlayMacro(self, mode):
        """Replay the loaded macro."""
        if (mode == 0):
            _RaiseException_(self.player.PlayMacro(PlayModeEnum.IgnoreTiming))
        else:
            _RaiseException_(self.player.PlayMacro(PlayModeEnum.UseTiming))

    def Wait(self):
        _RaiseException_(self.player.Wait())

    def PausePlaying(self):
        _RaiseException_(self.player.PausePlaying())

    def ResumePlaying(self):
        _RaiseException_(self.player.ResumePlaying())

    def StopPlaying(self):
        _RaiseException_(self.player.StopPlaying())

    def GetCommandLines(self):
        data = self.player.GetCommandLines()
        _RaiseException_(data[0])
        commandLines = []
        for i in data[1]:
            data = {'seconds': i.seconds, 'cmdLine': i.cmdLine}
            commandLines.append(data)
        return commandLines
