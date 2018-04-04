import time
import os
from niveristand.legacy import NIVeriStand
from testutilities import configutilities

#helper function to do a wait. This is used when you send a value to the engine, the engine will not reflect the value back untill the TCP Data loop send data back, currently at a 5Hz rate.
def sleep():
    time.sleep(.5)

def wait_for_test(stimulus, wait_time):
    test_state = stimulus.GetStimulusProfileManagerState()
    start_time = time.clock()
    elapsed_time = 0
    while (((test_state == 1) or (test_state == 2)) and (elapsed_time < wait_time)):
        sleep()
        test_state = stimulus.GetStimulusProfileManagerState()
        elapsed_time = time.clock() - start_time
    return (elapsed_time > wait_time)

def run_test(wks, stimulus, test_name, wait_time):
    TESTFILE = os.path.join(configutilities.get_autotest_projects_path(),"ProfileTest", test_name)
    print("")
    print("Running stimulus profile %s" % test_name)
    print("File Path: %s" % TESTFILE)
    print("...")
    import tempfile
    stimulus.RunStimulusProfile(TESTFILE,"",60000,1,1)
    timeout = wait_for_test(stimulus, wait_time)

    assert not timeout, "Test %s timed out." % test_name

    print("Stimulus Profile completed.")
    result = wks.GetSingleChannelValue("Gen 1 Pass Fail")
    print("Result = %d" % result)
    print("")
    return result


def test_stimulus_steps_legacy():
    #Every test should have a user variable that have a test ID number to ensure that you are running the correct test configuration.
    TEST_ID = 12000
    wks = NIVeriStand.Workspace2()

    #print(statement take a string and it is piped out to a single trace file in the background, for your tracing needs.)
    print("")

    SYSDEFFILE = os.path.join(configutilities.get_autotest_projects_path(),
                              "ProfileTest", "Profile Test.nivssdf")
    print("Deploying %s" % SYSDEFFILE )
    wks.ConnectToSystem(SYSDEFFILE,1,60000)
    print("System Definition deployed")

    try:
        #Verify the TEST_ID var on test file.
        test_ID = wks.GetSingleChannelValue("TEST_ID")
        assert(test_ID == TEST_ID), "Deployed wrong test file"


        stm = NIVeriStand.Stimulus()

        assert run_test(wks, stm, "Ramp Test.nivstest", 120)
        sleep()
        assert run_test(wks, stm, "Conditional Test.nivstest", 120)
        sleep()
        assert run_test(wks, stm, "Dwell Test.nivstest", 120)

    finally:
        #Always stop the engine.
        wks.DisconnectFromSystem("", 0)

