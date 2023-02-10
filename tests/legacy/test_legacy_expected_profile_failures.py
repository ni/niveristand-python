import time
import os
import pytest

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException


def wait_for_test(stimulus, wait_time):
    test_state = stimulus.GetStimulusProfileManagerState()
    start_time = time.perf_counter()
    elapsed_time = 0
    while (((test_state == 1) or (test_state == 2)) and (elapsed_time < wait_time)):
        time.sleep(1)
        test_state = stimulus.GetStimulusProfileManagerState()
        elapsed_time = time.perf_counter() - start_time
    return (elapsed_time > wait_time)

def run_test(workspace, stimulus, test_name, wait_time):
    TESTFILE = os.path.join(r"C:\Users\virtual\Desktop\AutoTestProjects",
                            "ProfileTest", test_name)
    result = -1
    print("")
    print("Running stimulus profile %s" % test_name)
    print("File Path: %s" % TESTFILE)
    print("...")
    LOGDIR = os.path.join(r"C:\Users\virtual\Desktop\AutoTestProjects", "ProfileTest", "Logs")
    stimulus.RunStimulusProfile(TESTFILE,LOGDIR,60000,1,1)
    timeout = wait_for_test(stimulus, 120)

    assert not timeout, "Timed out waiting for test to complete!"

    print("Stimulus Profile completed.")
    result = workspace.GetSingleChannelValue("Gen 1 Pass Fail")
    print("Result = %d" % result)
    print("")
    return result


def test_expected_profile_failures_legacy():

    #Every test should have a user variable that have a test ID number to ensure that you are running the correct test configuration.
    TEST_ID = 12000

    #Getting a handle to the workspace API
    #Other API: Model, Alarm, AlarmManager, SoftwareForcing, ModelManager
    workspace = NIVeriStand.Workspace2()

    try:
        #print(statement take a string and it is piped out to a single trace file in the background, for your tracing needs.)
        print("")

        #standard way of running a configuration file.  VSTANDPROJECTDIR is configured to the location where test project files get sync. So just append your folder and rig file.
        system_definition = os.path.join(os.getcwd(), r"tests\testutilities\legacy_files\ProfileTest\Profile Test.nivssdf")
        print("Deploying %s" % system_definition )
        workspace.ConnectToSystem(system_definition, 1, 20000)
        print("System Definition deployed")

        #Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert (test_ID == TEST_ID), "Deployed wrong test file"


        stm = NIVeriStand.Stimulus()

        with pytest.raises(NIVeriStandException):
            gens_error = run_test(workspace, stm, "Too Many Gens.nivstest", 120)
            assert (gens_error == 4294659383)

        with pytest.raises(NIVeriStandException):
            steps_error = run_test(workspace, stm, "Too Many Steps.nivstest", 120)
            assert (steps_error == 4294659395)

        with pytest.raises(NIVeriStandException):
            aux_error = run_test(workspace, stm, "Aux Buffer Overflow.nivstest", 120)
            assert (aux_error == 4294659393)

        with pytest.raises(NIVeriStandException):
            chan_error = run_test(workspace, stm, "Invalid Channel.nivstest", 120)
            assert (chan_error == 4294659387)

    finally:
        #Always stop the engine.
        workspace.DisconnectFromSystem("", 0)
