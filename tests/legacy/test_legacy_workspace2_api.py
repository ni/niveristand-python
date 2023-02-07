import os
import pytest

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException
from testutilities import configutilities

def sleep():
    import time
    time.sleep(1)

TEST_RESULT = 0 #Testresult set to false in beginning
TEST_COMMENT = "" #Test  comment to append to result
TEST_ID = 124123

def test_worksspace2_api():
    wks = NIVeriStand.Workspace2("localhost")
    print("")
    system_definition = os.path.join(configutilities.get_autotest_projects_path(),
                                 "TestWorkspaceAPI","TestWorkspaceAPI.nivssdf")
    print("Deploying %s" % system_definition)
    wks.ConnectToSystem(system_definition,True,5000)

    try:
        #Verify the TEST_ID var on test file.
        test_ID = wks.GetSingleChannelValue("TEST_ID")
        assert (test_ID == TEST_ID), "Deployed wrong test file"

        result = wks.GetSystemState()
        assert (result['systemdefinition_file'] == system_definition), "System definition file is not the same as deployed"

        wks.LockConnection("",'LOCK_PASSWORD')
        with pytest.raises(NIVeriStandException):
            wks.DisconnectFromSystem("",0)

        with pytest.raises(NIVeriStandException):
            wks.UnlockConnection("")

        wks.UnlockConnection('LOCK_PASSWORD')

        print("Get System Node Children")
        result = wks.GetSystemNodeChildren(r"Controller/Simulation Models/Models/sinewave/Execution")
        assert (len(result) == 4), "Model Exceution should return 4 node"

        #test we can still get system node children with full path.
        result = wks.GetSystemNodeChildren(r"Targets Section/Controller/Simulation Models/Models/sinewave/Execution")
        assert (len(result) == 4), "Model Exceution should return 4 node"

        print("Get System Node Channel List")
        result = wks.GetSystemNodeChannelList('')
        assert (len(result) >= 100), "At the very list we always have 100 channel"
        print(result[2])

        print("Get Alias List")
        result = wks.GetAliasList()
        assert (len(result) == 3), "Expected 3 alias but get something different %d" % len(result)
        assert (result['TEST_ID'] == r"Targets Section/Controller/User Channel/TEST_ID"), "Expected an alias for TEST_ID incorrect"

        #Mix up different mode of how we look up system nodes data: full path and also relative to Targets Section.
        nodes = ('Targets Section/Controller/User Channel', 'Controller/User Channel/TEST_ID')
        result = wks.GetMultipleSystemNodesData(nodes)
        assert (len(result) == 2), "Ask for 2 node info get no info"

        print("Validating channels")
        section = result[0]
        print(section)
        assert (section['isChannel'] == 0), "Expecting a section to returned"

        testNode = result[1]
        print(testNode)
        assert (testNode['isChannel'] == 1), "Expecteing a node to returned"

        print("Test PASSED")
        print("")

    finally:
        wks.DisconnectFromSystem("",1)
