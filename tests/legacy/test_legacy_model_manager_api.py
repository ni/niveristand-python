import os
import pytest
import time

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException


#Every test should have a user variable that have a test ID number to ensure that you are running the correct test configuration.
TEST_ID = 1122


@pytest.mark.skip('need to replace models')
def test_model_manager_legacy():
    #Getting a handle to the workspace API
    #Other API: Model, Alarm, AlarmManager, SoftwareForcing, ModelManager
    workspace = NIVeriStand.Workspace()
    mmgr = NIVeriStand.ModelManager()

    system_definition = os.path.join(os.getcwd(), r"tests\testutilities\legacy_files\ModelParameterAPI_AUTOTEST\ModelParameterAPI_AUTOTEST.nivssdf")
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, 0, 1, 20000, "", "")

    try:
        #Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert (test_ID == TEST_ID), "Deployed wrong test file"

        #declaring known and expected system values
        models = ["VectMod","VectModWorkspace","VectModWorkspace2","clocktest","sinewave"]
        sinewaveParams = ["Amplitude","Bias","Frequency","Gain","Phase"]
        workspaceList = ["CONST1by5","CONST2by3","CONST5by1"]
        paramList = ["VectMod/1by5Param/Value","VectMod/2by3Param/Value","VectMod/5by1Param/Value"]
        vectorParamList = workspaceList + paramList
        nonVectorParamList = sinewaveParams
        allParamInSystem = vectorParamList + nonVectorParamList
        CONST_1by5_initValue = [[1,2,3,4,5]]
        CONST_2by3_initValue = [[1,2,3],[10,20,30]]
        CONST_5by1_initValue = [[1],[2],[3],[4],[5]]
        CONST_VALUES = [CONST_1by5_initValue, CONST_2by3_initValue,CONST_5by1_initValue]

        #Now do your test
        print("Testing GetModelList")
        sysmodels = mmgr.GetModelList()
        for model in models:
            assert model in sysmodels, "Missing model expected to be returned by system"

        print("Testing GetParameterList")
        sysparamlist =  mmgr.GetParametersList()
        for param in allParamInSystem:
            assert param in sysparamlist, "Missing parameter expected to be returned by system %s" % param

        print("Testing Get Single Parameter Value")
        result = mmgr.GetSingleParameterValue(workspaceList[1])
        assert (result == CONST_1by5_initValue[0][0]), "Error on getting single parameter value get %f and expected %d" % (result,CONST_1by5_initValue[0][0])

        print("Testing Get Multiple Parameter Values")
        result = mmgr.GetMultipleParameterValues(vectorParamList)
        expresult = [1,1,1,1,1,1]
        for i in result:
            assert (i == 1), "Error on getting multiple parameter value get %d and expected 1" % i

        print("Testing Get Parameter Vector Values")
        for i in range(0,3):
            result = mmgr.GetParameterVectorValues(workspaceList[i])
            assert (result == CONST_VALUES[i]), "Error verifying vector values %s" % workspaceList[i]

        print("Testing Get Parameter Vector Values 2")
        for i in range(0,3):
            result = mmgr.GetParameterVectorValues(paramList[i])
            assert (result == CONST_VALUES[i]), "Error verifying vector values %s" % paramList[i]

        print("Test Set Single Parameter Value")
        for param in nonVectorParamList:
            print(("Set parameter " + param))
            mmgr.SetSingleParameterValue(param,2)
            time.sleep(1)

        for param in nonVectorParamList:
            print(("Verifying Set Paramater " + param))
            result = mmgr.GetSingleParameterValue(param)
            assert (result == 2), "Error verifying set single parameter value %s %d" % (param,result)

        print("Test Set Multiple Parameter Values")
        newValue = (3,3,3,3,3)
        mmgr.SetMultipleParameterValues(nonVectorParamList,newValue)
        time.sleep(1)
        result = mmgr.GetMultipleParameterValues(nonVectorParamList)
        for i in result:
            assert (i == 3), "Error verifying set multiple parameter value get %d and expected 3" % i

        print("Test Set Single Vector Values")
        CONST_1by5_modValue = [[6,7,8,9,10]]
        CONST_2by3_modValue = [[4,5,6],[7,8,9]]
        CONST_5by1_modValue = [[6],[7],[8],[9],[10]]
        CONST_MODVALUES = [CONST_1by5_modValue,CONST_2by3_modValue,CONST_5by1_modValue,CONST_1by5_modValue,CONST_2by3_modValue,CONST_5by1_modValue]
        for i in range(0,6):
            print("Set Parameter Vector for " + vectorParamList[i])
            mmgr.SetParameterVectorValues(vectorParamList[i],CONST_MODVALUES[i])
            time.sleep(1)

        for i in range(0,6):
            print("Verifying Set Parameter Vector for " + vectorParamList[i])
            result = mmgr.GetParameterVectorValues(vectorParamList[i])
            assert (result == CONST_MODVALUES[i]), "Error verifying set parameter vector values %s" % vectorParamList[i]

        print("Test Set and Get Vector Channel Values")
        #VectModWorksace_2by3Out value = VectModWorkspace_2by3In value + CONST2by3 param value
        #VectModWorksace2_2by3Out value = VectModWorkspace2_2by3In value + CONST2by3 param value
        CONST_2by3_VECTOR = [[1,2,3],[10,20,30]]
        CONST_2by3_VECTOR_TIMES2 = [[2,4,6],[20,40,60]]
        CONST_2by3_VECTOR_ZEROES = [[0,0,0],[0,0,0]]
        inports = ["VectModWorkspace_2by3In","VectModWorkspace2_2by3In"]
        outports = ["VectModWorkspace_2by3Out","VectModWorkspace2_2by3Out"]
        workspace.SetChannelVectorValues(inports[0],CONST_2by3_VECTOR_ZEROES)
        workspace.SetChannelVectorValues(inports[1],CONST_2by3_VECTOR)
        mmgr.SetParameterVectorValues("CONST2by3",CONST_2by3_VECTOR)
        time.sleep(1)
        result = workspace.GetChannelVectorValues(outports[0])
        assert (result == CONST_2by3_VECTOR), "Error verifying get channel vector value for %s" % outports[0]

        result = workspace.GetChannelVectorValues(outports[1])
        assert (result == CONST_2by3_VECTOR_TIMES2), "Error verifying get channel vector value for %s" % outports[1]

        print("Test Model Set State")
        model = NIVeriStand.Model("VectMod")

        #return 'time' : 'state'
        #Running = 0 Paused = 1 Resetting = 2 Idle = 3 Stopped = 4 Restoring = 5 Stopping = 6
        #Start = 0, Pause = 1, Reset = 2
        result = model.GetModelExecutionState()
        assert (result['state'] == 0), "Expected the model to be running"

        model.SetModelExecutionState(1)
        time.sleep(1)
        result = model.GetModelExecutionState()
        assert (result['state'] == 1), "Expected the model to be paused"

        model.SetModelExecutionState(2)
        time.sleep(1)
        result = model.GetModelExecutionState()
        assert (result['state'] == 3), "Expected the model to be idle"

        model.SetModelExecutionState(0)
        time.sleep(1)
        result = model.GetModelExecutionState()
        assert (result['state'] == 0), "Expected the model to be running"

        print("Test Save and Restore Model state")
        import tempfile
        SAVE_STATE_LOC  = os.path.join(tempfile.mkdtemp(), 'saveModelState.txt')
        clock = NIVeriStand.Model("clocktest")

        print("Pause and get clock time")
        clock.SetModelExecutionState(1)
        time.sleep(1)
        result = clock.GetModelExecutionState()
        timeAtSave = result['time']
        print("Time At Save %d" % timeAtSave)
        clock.SaveModelState(SAVE_STATE_LOC)
        time.sleep(1)

        print("Set model running")
        clock.SetModelExecutionState(0)
        time.sleep(5)

        print("Check if save state file exist on disk")
        assert ((os.path.isfile(SAVE_STATE_LOC)) == 1), "Error verifying that the save parameter state file is on disk %s" % SAVE_STATE_LOC

        print("Pause and restore model state")
        clock.SetModelExecutionState(1)
        time.sleep(1)
        result = clock.GetModelExecutionState()
        currentTime = result['time']
        print("Current Model Time %d" % currentTime)
        clock.RestoreModelState(SAVE_STATE_LOC)
        time.sleep(1)
        clock.SetModelExecutionState(0)
        time.sleep(1)
        result = clock.GetModelExecutionState()
        timeRestored = result['time']
        print("Time Restored %d" % timeRestored)
        assert timeAtSave <= timeRestored <= currentTime, "Error verifying restore parameter state"

        print("Test PASSED")
    finally:
        #Always stop the engine.
        workspace.StopWorkspaceFile("")
