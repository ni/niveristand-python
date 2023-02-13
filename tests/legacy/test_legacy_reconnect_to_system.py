import os
import pytest

from niveristand.legacy import NIVeriStand


# This test requires VeriStand 2020 or older due to the models
def test_reconnect_to_system():
    system_definition = r"C:\Users\Public\Documents\National Instruments\NI VeriStand 2020\Projects\Example\Sinewave Delay.nivssdf"
    # connect to system with a separate instance of the workspace
    prior_workspace = NIVeriStand.Workspace2("localhost")
    print("Initial deployment of system definition file")
    prior_workspace.ConnectToSystem(system_definition, True, 20000)
    print("")
    workspace = NIVeriStand.Workspace2("localhost")
    print("Connecting to the localhost, target Controller")
    workspace.ReconnectToSystem("Controller", True, None, 20000)

    try:
        # result = workspace.GetSystemState()
        # assert (result['systemdefinition_file'] == system_definition), "System definition file is not the same as deployed"

        print("Get System Node Children")
        result = workspace.GetSystemNodeChildren(
            r"Controller/Simulation Models/Models/sinewave/Execution"
        )
        assert len(result) == 4, "Model Exceution should return 4 node"

        # test we can still get system node children with full path.
        result = workspace.GetSystemNodeChildren(
            r"Targets/Controller/Simulation Models/Models/sinewave/Execution"
        )
        assert len(result) == 4, "Model Exceution should return 4 node"

        print("Get System Node Channel List")
        result = workspace.GetSystemNodeChannelList("")
        assert len(result) >= 100, "At the very least we always have 100 channel"
        print(result[2])

        print("Get Alias List")
        result = workspace.GetAliasList()
        assert (
            len(result) == 6
        ), "Expected 6 aliases but get something different %d" % len(result)
        assert (
            result["SineWave"]
            == r"Targets/Controller/Simulation Models/Models/sinewave/Signals/sine/SineWave"
        ), "Alias for SineWave incorrect"

        # Mix up different mode of how we look up system nodes data: full path and also relative to Targets Section.
        nodes = (
            "Aliases/SineWave",
            "Targets/Controller/System Channels/Actual Loop Rate",
        )
        result = workspace.GetMultipleSystemNodesData(nodes)
        assert len(result) == 2, "Ask for 2 node info get no info"

        print("Validating channels")
        section = result[0]
        print(section)
        assert section["isChannel"] == 1, "Expected channel, got something different."

        testNode = result[1]
        print(testNode)
        assert testNode["isChannel"] == 1, "Expected channel, got something different."

        print("Test PASSED")
        print("")

    finally:
        pass
        workspace.DisconnectFromSystem("", True)
