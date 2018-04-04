import time
import os

from niveristand.legacy import NIVeriStand
from testutilities import configutilities

def sleep():
    time.sleep(1)


def test_fault_api_legacy():
    TEST_ID = 1879

    wks = NIVeriStand.Workspace()
    print("")
    SYSDEFFILE = os.path.join(configutilities.get_autotest_projects_path(),
                              "FaultChannelTest", "FaultChannelTest.nivssdf")
    print("Deploying %s" % SYSDEFFILE)
    wks.RunWorkspaceFile(SYSDEFFILE,0,1,60000,"","")

    try:
        #Verify the TEST_ID var on test file.
        test_ID = wks.GetSingleChannelValue("TEST_ID")
        assert(test_ID == TEST_ID), "Deployed wrong test file"

        faultChannel0 = 'FaultChannel0'

        chanfault = NIVeriStand.ChannelFaultManager()
        result = chanfault.GetFaultList()
        assert(len(result) == 0), "No channel should be faulted on startup"

        result = chanfault.GetFaultValue(faultChannel0)
        assert(result['faulted'] == 0), "Channel should not be faulted"

        nonFaultValue = wks.GetSingleChannelValue(faultChannel0)
        channel = chanfault.SetFaultValue(faultChannel0,512)
        sleep()
        faultedValue = wks.GetSingleChannelValue(faultChannel0)
        assert(faultedValue == 512), "Channel is faulted and not returning expected value"

        result = chanfault.GetFaultValue(faultChannel0)
        assert(result['faulted'] == 1), "Channel should have been faulted"

        chanfault.ClearFault(faultChannel0)
        sleep()
        newValue = wks.GetSingleChannelValue(faultChannel0)
        assert(newValue == nonFaultValue), "Channel should have return to original value"

        result = chanfault.GetFaultList()
        assert(len(result) == 0), "All channel should have been cleared"

        print("Test multiple channel faults")
        FaultValues= [('FaultChannel2',12231),('FaultChannel4',123235),('FaultChannel5',1238945)]
        checkChannel = []
        checkValues = []
        for toFault in FaultValues:
            print("Set Fault %s"  % (toFault[0]))
            chanfault.SetFaultValue(toFault[0],toFault[1])
            checkChannel.append(toFault[0])
            checkValues.append(toFault[1])
            wks.SetSingleChannelValue(toFault[0],11)
        sleep()
        result = chanfault.GetFaultList()
        assert(result == FaultValues), "Channel faulted does not match"
        chanValues = wks.GetMultipleChannelValues(tuple(checkChannel))
        assert(checkValues == chanValues), "Get Channel Value differ from Get Fault List result"
        print("Done test multiple channel faults")

        chanfault.ClearAllFaults()
        result = chanfault.GetFaultList()
        assert(len(result) == 0), "Fault channels should have been cleard"

        chanfault.ClearAllFaults()

        print("Test PASSED")
    finally:
        wks.StopWorkspaceFile("")
