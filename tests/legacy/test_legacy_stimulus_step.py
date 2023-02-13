import os
import pytest
import time

from niveristand.legacy import NIVeriStand


def wait_for_test(stimulus, wait_time):
    test_state = stimulus.GetStimulusProfileManagerState()
    start_time = time.perf_counter()
    elapsed_time = 0
    while ((test_state == 1) or (test_state == 2)) and (elapsed_time < wait_time):
        time.sleep(1)
        test_state = stimulus.GetStimulusProfileManagerState()
        elapsed_time = time.perf_counter() - start_time
    return elapsed_time > wait_time


def run_test(workspace, stimulus, test_name, wait_time):
    base_directory = os.path.join(os.getcwd(), r"tests\testutilities\legacy_files")
    TESTFILE = os.path.join(base_directory, "ProfileTest", test_name)
    print("")
    print("Running stimulus profile %s" % test_name)
    print("File Path: %s" % TESTFILE)
    print("...")
    import tempfile

    stimulus.RunStimulusProfile(TESTFILE, "", 5000, 1, 1)
    timeout = wait_for_test(stimulus, wait_time)

    assert not timeout, "Test %s timed out." % test_name

    print("Stimulus Profile completed.")
    result = workspace.GetSingleChannelValue("Gen 1 Pass Fail")
    print("Result = %d" % result)
    print("")
    return result


def test_stimulus_steps_legacy():
    # Every test should have a user variable that have a test ID number to ensure that you are running the correct test configuration.
    TEST_ID = 12000
    workspace = NIVeriStand.Workspace2()

    # print(statement take a string and it is piped out to a single trace file in the background, for your tracing needs.)
    print("")

    system_definition = os.path.join(
        os.getcwd(),
        r"tests\testutilities\legacy_files\ProfileTest\Profile Test.nivssdf",
    )
    print("Deploying %s" % system_definition)
    workspace.ConnectToSystem(system_definition, 1, 5000)
    print("System Definition deployed")

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        stm = NIVeriStand.Stimulus()

        assert run_test(workspace, stm, "Ramp Test.nivstest", 120)
        time.sleep(1)
        assert run_test(workspace, stm, "Conditional Test.nivstest", 120)
        time.sleep(1)
        assert run_test(workspace, stm, "Dwell Test.nivstest", 120)

    finally:
        # Always stop the engine.
        workspace.DisconnectFromSystem("", 0)
