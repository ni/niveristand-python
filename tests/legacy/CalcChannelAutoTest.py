import time
import os

from niveristand.legacy import NIVeriStand
from tests.testutilities import configutilities

def sleep():
    time.sleep(1)

def test_calculated_channel_legacy():
    TEST_ID = 1112
    wks = NIVeriStand.Workspace()
    print("")
    SYSDEFINITION = os.path.join(configutilities.get_autotest_projects_path(),
                                 "CalculatedChannelTest", "CalculatedChannelTest.nivssdf")
    print("Deploying %s" % SYSDEFINITION)
    wks.RunWorkspaceFile(SYSDEFINITION,0,1,60000,"","")

    try:
        #Verify the TEST_ID var on test file.
        test_ID = wks.GetSingleChannelValue("TEST_ID")
        assert(test_ID == TEST_ID), "Deployed wrong test file"

        print("Checking Get Constant")
        channels = ("MaxConstant","MinConstant")
        expectedResults = [5,-5]
        results = wks.GetMultipleChannelValues(channels)
        for i in range(0,len(expectedResults)):
            assert(results[i] == expectedResults[i]), "%s Expected %f Return Value %f not expected"  % (channels[i],expectedResults[i],results[i])

        print("Checking Max Min Mode")
        channels = ("MaxUV1","MaxUV2","MinUV1","MinUV2")
        channelsValues = (-1000,-1000.1,1000,1000.1)
        wks.SetMultipleChannelValues(channels,channelsValues)
        sleep()
        #verifying the value get set on these channels
        results = wks.GetMultipleChannelValues(channels)
        for i in range(0,len(results)):
            assert(results[i] == channelsValues[i]), "%s Expected %f Return Value %f not expected"  % (channels[i],channelsValues[i],results[i])
        #verifying the new max min value is correct
        outchannels = ("MaxUV1ToConstVal5","MaxUV2ToConstVal10","MinUV1ToConstVal2","MinUV2ToConstVal3","Max2Var","Min2Var")
        expectedResults = [5,10,2,3,-1000,1000]
        results = wks.GetMultipleChannelValues(outchannels)
        for i in range(0,len(expectedResults)):
            assert(results[i] == expectedResults[i]), "%s Expected %f Return Value %f not expected"  % (outchannels[i],expectedResults[i],results[i])
        #verifying that the new max min value take the value of the variable.
        channelsValues = (10,15,1,-1)
        wks.SetMultipleChannelValues(channels,channelsValues)
        sleep()
        results = wks.GetMultipleChannelValues(outchannels)
        expectedResults = [10,15,1,-1,15,-1]
        for i in range(0,len(expectedResults)):
            assert(results[i] == expectedResults[i]), "%s Expected %f Return Value %f values not expected"  % (outchannels[i],expectedResults[i],results[i])

        print("Checking Acceleration Mode - assuming delta T for low priority loop is .2")
        channels = ("AccelerationOnDistanceChannel","VelocityChan","DistanceChannel","VelocityChanPrevIteration","DistanceChannelPrevIteration")
        results = wks.GetMultipleChannelValues(channels)
        accelerationCalculated = round((results[1] - results[3]) / .2)
        assert(accelerationCalculated == round(results[0])), "%s Expected %f Return Value %f value not expected" % (channels[0],accelerationCalculated,results[0])

        print("Computing velocity")
        velocityCalculated = round((results[2]-results[4])/ 0.2)
        assert(velocityCalculated == round(results[1])), "%s Expected %f Return Value %f value not expected" % (channels[1],velocityCalculated,results[1])


        print("Checking Averaging Mode")
        #Get a list of the last 6 points.  if we take a sum of the complete 3 elements we are bound to find the correct average.
        channels = ("3PointAverager","ChanToAverage","ChanToAverageMin1Step","ChanToAverageMin2Step","ChanToAverageMin3Step","ChanToAverageMin4Step","ChanToAverageMin5Step","ChanToAverageMin6Step")
        results = wks.GetMultipleChannelValues(channels)

        i = 0
        for channel in channels:
            print(("%s value is %f" % (channel,round(results[i],3))))
            i = i + 1

        possibleAverages = []
        for i in range(0,4):
            temp = 0
            for y in range(0,3):
                temp = temp + results[1 + i + y]
            possibleAverages.append(temp / 3)

        found = 0
        for potentialAverage in possibleAverages:
            print(("Potential Averages %f" % round(potentialAverage,3)))
            if(round(potentialAverage,3) == round(results[0],3)):
                found = 1

        assert(found == 1), "Fail to auto check averaging module"

        print("Test PASSED")

    finally:
        wks.StopWorkspaceFile("")
