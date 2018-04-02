import time
import os
import pytest

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException
from testutilities import configutilities


def sleep():
    time.sleep(1)


def test_worspace_api():
    TEST_ID = 124123

    wks = NIVeriStand.Workspace()
    print("")
    SYSDEFINITION = os.path.join(configutilities.get_autotest_projects_path(),
                                 "TestWorkspaceAPI",
                                 "TestWorkspaceAPI.nivssdf")
    print("Deploying %s" % SYSDEFINITION)
    wks.RunWorkspaceFile(SYSDEFINITION, 0, 1, 80000, "", "")

    try:
        # Verify the TEST_ID var on test file.
        test_ID = wks.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        result = wks.GetEngineState()
        assert result['systemdefinition_file'] == SYSDEFINITION, "Workspace file is not the same as deployed"

        wks.LockWorkspaceFile("", 'LOCK_PASSWORD')
        with pytest.raises(NIVeriStandException):
            wks.StopWorkspaceFile("")

        with pytest.raises(NIVeriStandException):
            wks.UnlockWorkspaceFile("")

        wks.UnlockWorkspaceFile('LOCK_PASSWORD')

        print("Get System Node Childern")
        result = wks.GetSystemNodeChildren(r"Controller/Simulation Models/Models/sinewave/Execution")
        assert len(result) == 4, "Model Exceution should return 4 nodes"

        print("Get System Node Channel List")
        result = wks.GetSystemNodeChannelList('')
        assert len(result) >= 100, "At the very least we always have 100 channel"
        print(result[2])

        print("Get Alias List")
        result = wks.GetAliasList()
        assert len(result) == 3, "Expected 3 alias but get something different %d" % len(result)
        assert result['TEST_ID'] == r"Targets Section/Controller/User Channel/TEST_ID", "Expected an alias for TEST_ID incorrect"

        nodes = ('Controller/User Channel', 'Controller/User Channel/TEST_ID')
        result = wks.GetMultipleSystemNodesData(nodes)
        assert len(result) == 2, "Ask for 2 node info get no info"

        print("Validating channels")
        section = result[0]
        print(section)
        assert section['isChannel'] is False, "Expecting a section to returned"

        testNode = result[1]
        print(testNode)
        assert testNode['isChannel'] is True, "Expecteing a node to returned"

        print("Test PASSED")
        print("")

        # Report your result here
        assert True
    finally:
        wks.StopWorkspaceFile("")
