import os
import pytest

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException


# This test requires Veristand 2020 or older due to the models
def test_workspace_api():
    TEST_ID = 124123

    workspace = NIVeriStand.Workspace()
    print("")
    system_definition = os.path.join(os.getcwd(), r"tests\testutilities\legacy_files\TestWorkspaceAPI\TestWorkspaceAPI.nivssdf")
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, False, True, 20000, "", "")

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        result = workspace.GetEngineState()
        assert result['systemdefinition_file'] == system_definition, "Workspace file is not the same as deployed"

        workspace.LockWorkspaceFile("", 'LOCK_PASSWORD')
        with pytest.raises(NIVeriStandException):
            workspace.StopWorkspaceFile("")

        with pytest.raises(NIVeriStandException):
            workspace.UnlockWorkspaceFile("")

        workspace.UnlockWorkspaceFile('LOCK_PASSWORD')

        print("Get System Node Childern")
        result = workspace.GetSystemNodeChildren(r"Controller/Simulation Models/Models/sinewave/Execution")
        assert len(result) == 4, "Model Exceution should return 4 nodes"

        print("Get System Node Channel List")
        result = workspace.GetSystemNodeChannelList('')
        assert len(result) >= 100, "At the very least we always have 100 channel"
        print(result[2])

        print("Get Alias List")
        result = workspace.GetAliasList()
        assert len(result) == 3, "Expected 3 alias but get something different %d" % len(result)
        assert result['TEST_ID'] == r"Targets Section/Controller/User Channel/TEST_ID", "Expected an alias for TEST_ID incorrect"

        nodes = ('Controller/User Channel', 'Controller/User Channel/TEST_ID')
        result = workspace.GetMultipleSystemNodesData(nodes)
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
        workspace.StopWorkspaceFile("")
