import os
import pytest
import time

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException

TEST_ID = 12234


def test_alarm_api():
    workspace = NIVeriStand.Workspace()
    system_definition = os.path.join(os.getcwd(), r"tests\testutilities\legacy_files\TestAlarmAPI\TestAlarmAPI.nivssdf")
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, False, True, 20000, "", "")

    try:
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert (test_ID == TEST_ID), "Deployed wrong test file"

        print("Testing Alarm manager functionality")
        alarmMgr = NIVeriStand.AlarmManager()
        result = alarmMgr.GetAlarmList()
        assert (len(result) == 3), "Expected 3 alarms returned from the system"

        print("Testing support for deprecated GetAlarmStatus() function")
        result = alarmMgr.GetAlarmsStatus()
        print(result)
        assert (result['HighAlarm'] == 0), "Not expecting any alarm to be trigger"
        assert (result['MediumAlarm'] == 0), "Not expecting any alarm to be trigger"
        assert (result['LowAlarm'] == 0), "Not expecting any alarm to be trigger"


        print("Testing Read Alarm Data")
        alarms = ('Alarm Group/AlarmTest1','Alarm Group/AlarmTest2','ConstantBoundAlarm')
        result = alarmMgr.GetMultipleAlarmsData(alarms, 60000)
        print("Verifying alarm data returned")
        assert (len(result) == 3), "Expected to get 3 alarms data back"

        print("Verifying Alarm Data")
        alarmTest1 = result[0]
        constantBoundAlarm = result[2]
        print(alarmTest1)
        # assert (alarmTest1['WatchChannel'] == r"AlarmChannel1"), "Fail to confirm alarm channel"
        assert ((alarmTest1['HighLimitIsConstant'] == 0) | (alarmTest1['HighLimitChannel'] == r"AlarmChannel1High")), "Fail to confirm high limit"
        assert ((alarmTest1['LowLimitIsConstant'] == 0) | (alarmTest1['LowLimitChannel'] == r"AlarmChannel1Low")), "Fail to confirm low limit"
        assert (alarmTest1['DelayDuration'] == 0.5), "Fail to confirm delay duration"
        assert (alarmTest1['ProcedureName'] == r"ResetAlarmTest1"), "Fail to confirm procedure"
        assert (alarmTest1['Priority'] == 2), "Fail to confirm priority enum (deprecated)"
        # TODO: PriorityNumber not found key
        assert (alarmTest1['PriorityNumber'] == 5), "Fail to confirm priority number"
        assert (alarmTest1['State'] == 1), "Fail to confirm state"
        assert (alarmTest1['Mode'] == 0), "Fail to confirm mode"
        # TODO: GroupNumber not found key
        assert (alarmTest1['GroupNumber'] == 1), "Fail to confirm group number"

        print("Test alarm interface")
        BoundAlarmRef = NIVeriStand.Alarm('ConstantBoundAlarm')
        result = BoundAlarmRef.GetAlarmData(30000)
        assert (result == constantBoundAlarm), "Alarm data from alarm interface differ from alarm manager"

        print("Test modifying alarm data")
        modAlarmData = result
        modAlarmData['HighLimit'] = 3
        modAlarmData['LowLimit'] = -3


        print("Testing support for deprecated SetAlarmData() function")
        BoundAlarmRef.SetAlarmData(modAlarmData)
        time.sleep(1)
        result = BoundAlarmRef.GetAlarmData(30000)
        assert (result == modAlarmData), "Alarm data set cannot be confirmed on deprecated function"

        # TODO: SetAlarmData2 not implemented.
        print("Testing support using SetAlarmData2() function")
        BoundAlarmRef.SetAlarmData2(modAlarmData)
        time.sleep(1)
        result = BoundAlarmRef.GetAlarmData(30000)
        assert (result == modAlarmData), "Alarm data set cannot be confirmed on function"

        print("Test modifying alarm state and mode")
        BoundAlarmRef.SetEnabledState(0)
        #indicate only
        BoundAlarmRef.SetAlarmMode(1)
        time.sleep(1)

        result = BoundAlarmRef.GetAlarmData(30000)
        assert (result['State'] == 0), "Alarm Mode is wrong"

        assert (result['Mode'] == 1), "Alarm Mode is wrong"

        BoundAlarmRef.SetEnabledState(1)
        BoundAlarmRef.SetAlarmMode(0)
        time.sleep(2)
        workspace.SetSingleChannelValue(r"Controller/User Channel/AlarmChannel1",20)
        workspace.SetSingleChannelValue(r"Controller/User Channel/AlarmChannel2",10)
        time.sleep(2)

        print("Testing alarm mutual exclusion within a group")
        AlarmTest2Ref = NIVeriStand.Alarm('Alarm Group/AlarmTest2')
        AlarmTest1Ref = NIVeriStand.Alarm('Alarm Group/AlarmTest1')
        result = AlarmTest1Ref .GetAlarmData(30000)
        result2 = AlarmTest2Ref .GetAlarmData(30000)
        assert ( result['State'] == 2), "Alarm should be tripped"
        assert ( result2['State'] != 2), "Alarm should not be running due to an execution of a higher priority."

        # print("Testing Alarm Execution Across Groups")
        # result = BoundAlarmRef.GetAlarmData(30000)
        # result2 = AlarmTest2Ref.GetAlarmData(30000)
        # assert ((result['State'] == 2) and (result2['State'] == 2)), " Two alarms should be tripped simulteneously."

        print("Test PASSED")

    finally:
        workspace.StopWorkspaceFile("")
