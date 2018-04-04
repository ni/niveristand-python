import time
import os
from niveristand.legacy import NIVeriStand
from testutilities import configutilities

def sleep():
    time.sleep(.5)

#Every test should have a user variable that have a test ID number to ensure that you are running the correct test configuration.
TEST_ID = 3000 


def test_procedures_legacy():
    wks = NIVeriStand.Workspace2("localhost")
    SYSDEFINITION = os.path.join(configutilities.get_autotest_projects_path(),
                                 "ProceduresTest", "ProceduresTest.nivssdf")
    print("Deploying %s" % SYSDEFINITION)
    wks.ConnectToSystem(SYSDEFINITION,1,60000)

    try:
        #Verify the TEST_ID var on test file.
        test_ID = wks.GetSingleChannelValue("TEST_ID")
        assert(test_ID == TEST_ID), "Deployed wrong test file"

        print("")
        print("Test ID =", TEST_ID)

        #Now do your test
        #Sample common operation

        #Give some time for the startup procedure to finish setting the initial variables
        time.sleep(2)

        print("")

        #Check that we skipped the first procedure and executed the Startup Procedure
        assert(wks.GetSingleChannelValue("Test Channel 6") >= 0), "Invalid procedure executed before Startup!"
        print("Successfully skipped initial procedure. Checking Startup Procedure was invoked...")

        channelValues = wks.GetMultipleChannelValues(("Test Channel 0","Test Channel 1","Test Channel 2","Test Channel 3","Test Channel 4","Test Channel 7","Test Channel 10", "Test Channel 11"))

        print("Startup channel values =", channelValues)
        assert(channelValues == [1000,2000,20000,30000,40000,0,10,11]), "Startup Test Data Errors!"
        print("Startup Procedure invoked successfully")

        print("Checking that Startup Procedure is waiting on Test Channel 5 before continuing")
        #Check that AfterStartupProcedure hasn't run yet. StartupProcedure should be waiting for TC5 >= 50000
        assert (wks.GetSingleChannelValue("Test Channel 5") != -50000), "After Startup Procedure premature execution!"
        print("Startup Procedure successfully waiting")


        #Set Test Channel 5 to 50000 so that the Startup Procedure ends and proceeds to After Startup Procedure
        print("Triggering After Startup Procedure")
        wks.SetSingleChannelValue("Test Channel 5", 50000)
        time.sleep(2)
        assert(wks.GetSingleChannelValue("Test Channel 5") == -50000), "Failed to move onto After Startup Procedure"
        print("After Startup Procedure Executed Successfully")

        #Check that we don't move onto Also Should Not Run Procedure, because After Startup ends with End
        time.sleep(1)
        assert(wks.GetSingleChannelValue("Test Channel 6")>=0), "Invalid procedure executed after After Startup!"
        print("Procedure execution ended successfully")

        #Test triggering alarms

        #Set number of alarm triggers. Each triggered alarm procedure should increment its trigger count variable.
        x = 5
        print("Triggering Alarm 1 and 2 and 3", x, "times")
        for i in range(x):
                wks.SetSingleChannelValue("Alarm Channel 1", 1)
                time.sleep(2)
                wks.SetSingleChannelValue("Alarm Channel 2", 1)
                time.sleep(2)
                wks.SetSingleChannelValue("Alarm Channel 3", 1)
                time.sleep(2)

        a1TrigCount = wks.GetSingleChannelValue("Alarm 1 Trigger Count")
        a2TrigCount = wks.GetSingleChannelValue("Alarm 2 Trigger Count")
        a3TrigCount = wks.GetSingleChannelValue("Alarm 3 Trigger Count")
        print("Alarm 1 Trigger Count =", a1TrigCount)
        print("Alarm 2 Trigger Count =", a2TrigCount)
        print("Alarm 3 Trigger Count =", a3TrigCount)

        assert ((a1TrigCount == x) and (a2TrigCount == x)), "Alarms failed to trigger Alarm Procedures!"
        print("Alarm procedures successfully triggered")

        assert (a3TrigCount <= 0), "Alarm 3 triggered while disabled!"
        print("Alarm 3 successfully disabled, did not trigger")

        print("Triggering Procedure 4 which should enable Alarm 3")
        wks.SetSingleChannelValue("Alarm Channel 4",1)
        time.sleep(1)

        print("Attempting to trigger Alarm 3...")
        wks.SetSingleChannelValue("Alarm Channel 3",1)
        time.sleep(1)
        a3TrigCount = wks.GetSingleChannelValue("Alarm 3 Trigger Count")
        assert (a3TrigCount == 1), "Alarm 3 not successfully enabled!"
        print("Alarm 3 Trigger Count =", a3TrigCount)
        print("Alarm 3 successfully triggered")

        print("Attempting to retrigger Alarm 3, which should now be disabled again after Alarm 3 Procedure executed")
        wks.SetSingleChannelValue("Alarm Channel 3",1)
        time.sleep(1)
        a3TrigCount = wks.GetSingleChannelValue("Alarm 3 Trigger Count")
        assert (a3TrigCount == 1), "Alarm 3 failed to be set to disabled and was triggered!"
        print("Alarm 3 Trigger Count =", a3TrigCount)
        print("Alarm 3 successfully disabled and not triggered")

        #Alarms 5 and 6 test resetting multiple alarms in same sub-procedure using "Reset This Alarm".
        #Alarms 7 and 8 test the "Triggered alarm" checkbox of an Alarm command by having one sub-procedure which can reset any calling alarm.
        #(Using a sub-procedure tests to make sure that the triggered alarm is correctly passed to sub-procedures)
        x = 3
        print("Triggering Alarm 5, 6, 7 and ", x, "times")
        for i in range(x):
                wks.SetSingleChannelValue("Alarm Channel 5", 1)
                time.sleep(2)
                wks.SetSingleChannelValue("Alarm Channel 6", 1)
                time.sleep(2)
                wks.SetSingleChannelValue("Alarm Channel 7", 1)
                time.sleep(2)
                wks.SetSingleChannelValue("Alarm Channel 8", 1)
                time.sleep(2)

        a5TrigCount = wks.GetSingleChannelValue("Alarm 5 Trigger Count")
        a6TrigCount = wks.GetSingleChannelValue("Alarm 6 Trigger Count")
        a7TrigCount = wks.GetSingleChannelValue("Alarm 7 Trigger Count")
        a8TrigCount = wks.GetSingleChannelValue("Alarm 8 Trigger Count")
        print("Alarm 5 Trigger Count =", a5TrigCount)
        print("Alarm 6 Trigger Count =", a6TrigCount)
        print("Alarm 7 Trigger Count =", a7TrigCount)
        print("Alarm 8 Trigger Count =", a8TrigCount)

        #Testing the alarm call stack with alarms 9, 10, and 11.  Each alarm waits 5 seconds, then calls "Reset Triggered Alarm Sub-Procedure".
        #During this test, procedure 9 starts and is interrupted by procedure 10, which is interrupted by procedure 11.
        #The whole thing is run twice and makes sure that preempted alarms are properly reset once they resume.
        x = 2
        print("Triggering Alarm 9, 10, 11 and ", x, "times")
        for i in range(x):
                wks.SetSingleChannelValue("Alarm Channel 9", 1)
                time.sleep(2)
                wks.SetSingleChannelValue("Alarm Channel 10", 1)
                time.sleep(2)
                wks.SetSingleChannelValue("Alarm Channel 11", 1)
                time.sleep(20)

        a9TrigCount = wks.GetSingleChannelValue("Alarm 9 Trigger Count")
        a10TrigCount = wks.GetSingleChannelValue("Alarm 10 Trigger Count")
        a11TrigCount = wks.GetSingleChannelValue("Alarm 11 Trigger Count")
        print("Alarm 9 Trigger Count =", a9TrigCount)
        print("Alarm 10 Trigger Count =", a10TrigCount)
        print("Alarm 11 Trigger Count =", a11TrigCount)

        assert ((a9TrigCount == x) and (a10TrigCount == x) and (a11TrigCount == x)), "Alarms failed to trigger Alarm Procedures!"
        print("Alarm procedures successfully triggered")


        print("Test PASSED")
    finally:
        #Always stop the engine.
        wks.StopWorkspaceFile("")
