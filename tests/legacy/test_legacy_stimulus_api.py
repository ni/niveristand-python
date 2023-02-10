import os
import pytest
import time

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException

TEST_ID = 123213

def test_stimulus_api_legacy():

    workspace = NIVeriStand.Workspace()
    print("")
    system_definition = os.path.join(os.getcwd(), r"tests\testutilities\legacy_files\TestStimulusAPI\TestStimulusAPI.nivssdf")
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, 0, 1, 20000, "", "")

    try:
        #Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert (test_ID == TEST_ID), "Deployed wrong test file"

        logging_directory = os.path.join(os.getcwd(), r"tests\testutilities\legacy_files\TestStimulusAPI\TestStimulusAPI")
        AutoStepTestStimulusAPI = os.path.join(os.getcwd(), r"tests\testutilities\legacy_files\TestStimulusAPI\AutoStepTestStimulusAPI.nivstest")

        stimTest1 = NIVeriStand.Stimulus()
        stimTest2 = NIVeriStand.Stimulus()

        print("Test Reserve and Unreserve")
        stimTest1.ReserveStimulusProfileManager()
        print("Done reserving stimulus test 1")
        with pytest.raises(NIVeriStandException):
            stimTest2.ReserveStimulusProfileManager()
        print("Start unreserving")
        stimTest1.UnreserveStimulusProfileManager()
        stimTest2.ReserveStimulusProfileManager()
        stimTest2.UnreserveStimulusProfileManager()

        print("Run and get test state")
        result = stimTest1.GetStimulusProfileManagerState()
        assert (result == 0), "Test state not expected"

        print("Running Test " + AutoStepTestStimulusAPI)
        stimTest1.RunStimulusProfile(AutoStepTestStimulusAPI,logging_directory,60000,1,1)
        time.sleep(1)
        result = stimTest1.GetStimulusProfileManagerState()
        assert (result == 2), "Test expected to started already"
        print("Test Getting back the file we are running")
        file = stimTest1.GetStimulusProfileFile()
        # assert (file == AutoStepTestStimulusAPI), "Test file are not expected"

        print("Wait until stimulus is done")
        time.sleep(40)
        result = stimTest1.GetStimulusProfileResult()

        result = stimTest1.GetStimulusProfileManagerState()
        assert (result == 0), "Test should have finished by now"

        stimTest1.RunStimulusProfile(AutoStepTestStimulusAPI,logging_directory,60000,1,1)
        time.sleep(1)
        result = stimTest1.GetStimulusProfileManagerState()
        assert (result == 2), "Test expected to started already"

        stimTest1.StopStimulusProfile()
        time.sleep(1)
        result = stimTest1.GetStimulusProfileManagerState()
        assert (result == 0), "Test expected to stop"

        print("Test PASSED")
        print("")

    finally:
        workspace.StopWorkspaceFile("")
