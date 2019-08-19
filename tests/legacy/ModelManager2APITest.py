import time
import os
import pytest
from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException
from tests.testutilities import configutilities

#helper function to do a wait. This is used when you send a value to the engine, the engine will not reflect the value back untill the TCP Data loop send data back, currently at a 5Hz rate.
def sleep():
    time.sleep(1)

#Every test should have a user variable that have a test ID number to ensure that you are running the correct test configuration.
TEST_ID = 1122 

def test_model_manager2_legacy():
    #Getting a handle to the workspace API
    #Other API: Model, Alarm, AlarmManager, SoftwareForcing, ModelManager
    wks = NIVeriStand.Workspace2('localhost')
    mmgr = NIVeriStand.ModelManager2('localhost')

    SYSDEFINITION = os.path.join(configutilities.get_autotest_projects_path(),
                                 "ModelParameterAPI_AUTOTEST", "ModelParameterAPI_AUTOTEST.nivssdf")
    print("Deploying %s" % SYSDEFINITION)
    wks.ConnectToSystem(SYSDEFINITION,1,60000)

    try:
        #Verify the TEST_ID var on test file.
        test_ID = wks.GetSingleChannelValue("TEST_ID")
        assert(test_ID == TEST_ID), "Deployed wrong test file"

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
        sysmodels = mmgr.GetModelList("Controller")
        for model in models:
            assert model in sysmodels, "Missing model expected to be returned by system"

        with pytest.raises(NIVeriStandException):
            mmgr.GetModelList("NON_EXISTING_CONTROLLER")

        print("Testing GetParameterList")
        sysparamlist =  mmgr.GetParametersList("Controller")
        for param in allParamInSystem:
            assert param in sysparamlist, "Missing parameter expected to be returned by system %s" % param

        with pytest.raises(NIVeriStandException):
            mmgr.GetParametersList("NON_EXISTING_CONTROLLER")

        print("Testing Get Single Parameter Value")
        result = mmgr.GetSingleParameterValue("Controller",workspaceList[1])
        assert(result == CONST_1by5_initValue[0][0]), "Error on getting single parameter value get %f and expected %d" % (result,CONST_1by5_initValue[0][0])

        with pytest.raises(NIVeriStandException):
            mmgr.GetSingleParameterValue("NON_EXISTING_CONTROLLER",workspaceList[1])

        print("Testing Get Multiple Parameter Values")
        result = mmgr.GetMultipleParameterValues("Controller",vectorParamList)
        expresult = [1,1,1,1,1,1]
        for i in result:
            assert(i == 1), "Error on getting multiple parameter value get %d and expected 1" % i

        with pytest.raises(NIVeriStandException):
            mmgr.GetMultipleParameterValues("NON_EXISTING_CONTROLLER",vectorParamList)

        print("Testing Get Parameter Vector Values")
        for i in range(0,3):
            result = mmgr.GetParameterVectorValues("Controller",workspaceList[i])
            assert(result == CONST_VALUES[i]), "Error verifying vector values %s" % workspaceList[i]

        with pytest.raises(NIVeriStandException):
            mmgr.GetParameterVectorValues("NON_EXISTING_CONTROLLER",workspaceList[1])

        print("Testing Get Parameter Vector Values 2")
        for i in range(0,3):
            result = mmgr.GetParameterVectorValues("Controller",paramList[i])
            assert(result == CONST_VALUES[i]), "Error verifying vector values %s" % paramList[i]

        print("Test Set Single Parameter Value")
        for param in nonVectorParamList:
            print(("Set parameter " + param))
            mmgr.SetSingleParameterValue("Controller",param,2)
            sleep()

        with pytest.raises(NIVeriStandException):
            mmgr.SetSingleParameterValue("NON_EXISTING_CONTROLLER",nonVectorParamList[1],2)

        for param in nonVectorParamList:
            print(("Verifying Set Paramater " + param))
            result = mmgr.GetSingleParameterValue("Controller",param)
            assert(result == 2), "Error verifying set single parameter value %s %d" % (param,result)

        print("Test Set Multiple Parameter Values")
        newValue = (3,3,3,3,3)
        mmgr.SetMultipleParameterValues("Controller",nonVectorParamList,newValue)
        sleep()
        result = mmgr.GetMultipleParameterValues("Controller",nonVectorParamList)
        for i in result:
            assert(i == 3), "Error verifying set multiple parameter value get %d and expected 3" % i

        with pytest.raises(NIVeriStandException):
            mmgr.SetMultipleParameterValues("NON_EXISTING_CONTROLLER",nonVectorParamList,newValue)

        print("Test Set Single Vector Values")
        CONST_1by5_modValue = [[6,7,8,9,10]]
        CONST_2by3_modValue = [[4.25,5.25,6.25],[7.5,8.5,9.5]]
        CONST_5by1_modValue = [[6],[7],[8],[9],[10]]
        CONST_MODVALUES = [CONST_1by5_modValue,CONST_2by3_modValue,CONST_5by1_modValue,CONST_1by5_modValue,CONST_2by3_modValue,CONST_5by1_modValue]
        for i in range(0,6):
            print("Set Parameter Vector for " + vectorParamList[i])
            mmgr.SetParameterVectorValues("Controller",vectorParamList[i],CONST_MODVALUES[i])
            sleep()

        for i in range(0,6):
            print("Verifying Set Parameter Vector for " + vectorParamList[i])
            result = mmgr.GetParameterVectorValues("Controller",vectorParamList[i])
            assert(result == CONST_MODVALUES[i]), "Error verifying set parameter vector values %s" % vectorParamList[i]

        print("Test Set Parameters Values")
        TESTPARAMS = ["Amplitude","CONST1by5","VectMod/2by3Param/Value"]
        SINGLE_PARAM_TESTVALUE = [[10]]
        CONST_1by5_TestValue = [[100,200,300,400,500]]
        CONST_2by3_TestValue = [[1000.25,2000.25,3000.25],[4000.5,5000.5,6000.5]]
        TESTVALUES = [SINGLE_PARAM_TESTVALUE,CONST_1by5_TestValue,CONST_2by3_TestValue]
        mmgr.SetParameterValues("Controller",TESTPARAMS,TESTVALUES)
        sleep()
        sleep()
        assert(mmgr.GetSingleParameterValue("Controller","Amplitude") == 10), "Error verifying set parameter values to a single parameter"
        assert(mmgr.GetParameterVectorValues("Controller","CONST1by5") == CONST_1by5_TestValue), "Error verifying set parameter vector values to a 1 by 5 parameter"
        assert(mmgr.GetParameterVectorValues("Controller","VectMod/2by3Param/Value") == CONST_2by3_TestValue), "Error verifying set parameter vector values to a 2 by 3 parameter"

        print("Test Set and Get Vector Channel Values")
        #VectModWorksace_2by3Out value = VectModWorkspace_2by3In value + CONST2by3 param value
        #VectModWorksace2_2by3Out value = VectModWorkspace2_2by3In value + CONST2by3 param value
        CONST_2by3_VECTOR = [[1,2,3],[10,20,30]]
        CONST_2by3_VECTOR_TIMES2 = [[2,4,6],[20,40,60]]
        CONST_2by3_VECTOR_ZEROES = [[0,0,0],[0,0,0]]
        inports = ["VectModWorkspace_2by3In","VectModWorkspace2_2by3In"]
        outports = ["VectModWorkspace_2by3Out","VectModWorkspace2_2by3Out"]
        wks.SetChannelVectorValues(inports[0],CONST_2by3_VECTOR_ZEROES)
        wks.SetChannelVectorValues(inports[1],CONST_2by3_VECTOR)
        mmgr.SetParameterVectorValues("Controller","CONST2by3",CONST_2by3_VECTOR)
        sleep()
        result = wks.GetChannelVectorValues(outports[0])
        print(result)
        assert(result == CONST_2by3_VECTOR), "Error verifying get channel vector value for %s" % outports[0]

        result = wks.GetChannelVectorValues(outports[1])
        print(result)
        assert(result == CONST_2by3_VECTOR_TIMES2), "Error verifying get channel vector value for %s" % outports[1]

        print("Test Set Channel Values")
        CONST_2by3_VECTOR_Hundreds = [[100,200,300],[400,500,600]]
        CONST_2by3_VECTOR_Thousands = [[1000,2000,3000],[4000,5000,6000]]
        wks.SetChannelValues(inports,[CONST_2by3_VECTOR_Hundreds,CONST_2by3_VECTOR_Thousands])
        sleep()
        result = wks.GetChannelVectorValues(outports[0])
        print(result)
        assert(result == [[101,202,303],[410,520,630]]), "Error verifying get channel vector value for %s" % outports[0]

        result = wks.GetChannelVectorValues(outports[1])
        print(result)
        assert(result == [[1001,2002,3003],[4010,5020,6030]]), "Error verifying get channel vector value for %s" % outports[1]

        print("Test Model Set State")
        print("Test various constructor mode")
        Constructor1 = NIVeriStand.Model("VectMod")
        Constructor2 = NIVeriStand.Model("VectMod","Controller")
        Constructor3 = NIVeriStand.Model("VectMod",None,"localhost")
        model = NIVeriStand.Model("VectMod","Controller","localhost")

        #return 'time' : 'state'
        #Running = 0 Paused = 1 Resetting = 2 Idle = 3 Stopped = 4 Restoring = 5 Stopping = 6
        #Start = 0, Pause = 1, Reset = 2
        result = model.GetModelExecutionState()
        assert(result['state'] == 0), "Expected the model to be running"

        model.SetModelExecutionState(1)
        sleep()
        result = model.GetModelExecutionState()
        assert(result['state'] == 1), "Expected the model to be paused"

        model.SetModelExecutionState(2)
        sleep()
        result = model.GetModelExecutionState()
        assert(result['state'] == 3), "Expected the model to be idle"

        model.SetModelExecutionState(0)
        sleep()
        result = model.GetModelExecutionState()
        assert(result['state'] == 0), "Expected the model to be running"

        print("Test Save and Restore Model state")
        import tempfile
        SAVE_STATE_LOC  = os.path.join(tempfile.mkdtemp(), 'saveModelState.txt')
        clock = NIVeriStand.Model("clocktest")

        print("Pause and get clock time")
        clock.SetModelExecutionState(1)
        sleep()
        result = clock.GetModelExecutionState()
        timeAtSave = result['time']
        print("Time At Save %d" % timeAtSave)
        clock.SaveModelState(SAVE_STATE_LOC)
        sleep()

        print("Set model running")
        clock.SetModelExecutionState(0)
        sleep()
        sleep()
        sleep()
        sleep()
        sleep()

        print("Check if save state file exist on disk")
        assert ((os.path.isfile(SAVE_STATE_LOC)) == 1), "Error verifying that the save parameter state file is on disk %s" % SAVE_STATE_LOC

        print("Pause and restore model state")
        clock.SetModelExecutionState(1)
        sleep()
        result = clock.GetModelExecutionState()
        currentTime = result['time']
        print("Current Model Time %d" % currentTime)
        clock.RestoreModelState(SAVE_STATE_LOC)
        sleep()
        clock.SetModelExecutionState(0)
        sleep()
        result = clock.GetModelExecutionState()
        timeRestored = result['time']
        print("Time Restored %d" % timeRestored)
        assert timeAtSave <= timeRestored <= currentTime, "Error verifying restore parameter state"

        print("Test PASSED")
    finally:
        #Always stop the engine.
        wks.StopWorkspaceFile("")
