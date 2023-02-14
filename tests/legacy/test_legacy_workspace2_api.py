import os

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException
import pytest

TEST_ID = 124123


# This test requires VeriStand 2020 or older due to the models
def test_workspace2_api():
    workspace = NIVeriStand.Workspace2("localhost")
    print("")
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\TestWorkspaceAPI\TestWorkspaceAPI.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.ConnectToSystem(system_definition, True, 20000)

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        # result = workspace.GetSystemState()
        # assert (
        #   result['systemdefinition_file'] == system_definition),
        #   "System definition file is not the same as deployed"

        workspace.LockConnection("", "LOCK_PASSWORD")
        with pytest.raises(NIVeriStandException):
            workspace.DisconnectFromSystem("", 0)

        with pytest.raises(NIVeriStandException):
            workspace.UnlockConnection("")

        workspace.UnlockConnection("LOCK_PASSWORD")

        print("Get System Node Children")
        result = workspace.GetSystemNodeChildren(
            r"Controller/Simulation Models/Models/sinewave/Execution"
        )
        assert len(result) == 4, "Model Exceution should return 4 node"

        # test we can still get system node children with full path.
        result = workspace.GetSystemNodeChildren(
            r"Targets Section/Controller/Simulation Models/Models/sinewave/Execution"
        )
        assert len(result) == 4, "Model Exceution should return 4 node"

        print("Get System Node Channel List")
        result = workspace.GetSystemNodeChannelList("")
        assert len(result) >= 100, "At the very list we always have 100 channel"
        print(result[2])

        print("Get Alias List")
        result = workspace.GetAliasList()
        assert len(result) == 3, "Expected 3 alias but get something different %d" % len(result)
        assert (
            result["TEST_ID"] == r"Targets Section/Controller/User Channel/TEST_ID"
        ), "Expected an alias for TEST_ID incorrect"

        # Mix up different mode of how we look up system nodes data: full path
        # and also relative to Targets Section.
        nodes = ("Targets Section/Controller/User Channel", "Controller/User Channel/TEST_ID")
        result = workspace.GetMultipleSystemNodesData(nodes)
        assert len(result) == 2, "Ask for 2 node info get no info"

        print("Validating channels")
        section = result[0]
        print(section)
        assert section["isChannel"] == 0, "Expecting a section to returned"

        testNode = result[1]
        print(testNode)
        assert testNode["isChannel"] == 1, "Expecteing a node to returned"

        print("Test PASSED")
        print("")

    finally:
        workspace.DisconnectFromSystem("", 1)
