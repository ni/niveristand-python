import time
import os
import math

from niveristand.legacy import NIVeriStand
from tests.testutilities import configutilities

def sleep():
    time.sleep(1)


def test_calculated_channel_latch_legacy():
    wks = NIVeriStand.Workspace()
    print("")
    SYSDEFFILE = os.path.join(configutilities.get_autotest_projects_path(),
                              "CalcChanLatchTest", "CalcChanLatchTest.nivssdf")
    print("Deploying %s" % SYSDEFFILE)
    wks.RunWorkspaceFile(SYSDEFFILE,0,1,60000,"","")

    try:
        # Compute Machine Epsilon: The smallest floating point number when
        # added to one is greater than one.

        eps = 1.0
        while ((1.0 + eps) > 1.0):
            epsLast = eps
            eps = eps / 2.0
        eps = epsLast
        print("Machine Epsilon = %g" % (eps))

        # This test suite latches the first eleven data points into conditional
        # calculated channels. We must wait for the counter to become 10. The
        # steps are enumerated 0..10 (eleven points).

        result=0
        while (result < 10):
            sleep()
            result = wks.GetSingleChannelValue("Counter")

        # This test is sensitive to the system Delta T. Ensure that it is 0.1.

        print("Checking (Delta T)=0.1")
        expectedResult = 0.1
        result = wks.GetSingleChannelValue("Delta T")
        assert(result == expectedResult), "Delta T (%g) does not match expected (%g)"  % (result, expectedResult)
        print("...Pass")


        print("Checking first 11 latched time points")
        channels = ("Latch_T_0", "Latch_T_1", "Latch_T_2", "Latch_T_3", "Latch_T_4",
                       "Latch_T_5", "Latch_T_6", "Latch_T_7", "Latch_T_8", "Latch_T_9",
                      "Latch_T_10")

        results = wks.GetMultipleChannelValues(channels)

        expectedResults = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        abstol = eps
        reltol = math.sqrt(eps)
        for i in range(0,len(expectedResults)):
            tol = abstol + reltol*abs(expectedResult)
            assert(expectedResults[i] - tol <= results[i] <= expectedResults[i] + tol), "%s => Expected %g. Return Value %g not expected." % (channels[i], expectedResults[i], results[i])
        print("...Pass")

        channels = ("P", "Q", "R", "S")
        results = wks.GetMultipleChannelValues(channels)

        print("Input waveform: X = P*sin(Q*(Time+DeltaT) + R) + S")
        print("with P=%g, Q=%g, R=%g, S=%g" % (results[0], results[1], results[2], results[3]))

        print("Testing 11 stage latch of the first 11 points")

        channels = ("Latch_fT_0", "Latch_fT_1", "Latch_fT_2", "Latch_fT_3", "Latch_fT_4",
                       "Latch_fT_5", "Latch_fT_6", "Latch_fT_7", "Latch_fT_8", "Latch_fT_9",
                      "Latch_fT_10")
        results = wks.GetMultipleChannelValues(channels)

        channels = ("Exact_fT_0", "Exact_fT_1", "Exact_fT_2", "Exact_fT_3", "Exact_fT_4",
                       "Exact_fT_5", "Exact_fT_6", "Exact_fT_7", "Exact_fT_8", "Exact_fT_9",
                      "Exact_fT_10")
        expectedResults = wks.GetMultipleChannelValues(channels)

        for i in range(0,len(expectedResults)):
            assert(results[i] == expectedResults[i]), "%s => Expected %g. Return Value %g not expected." % (channels[i], expectedResults[i], results[i])
        print("...Pass")

        print("Test PASSED")
        print("")
    finally:
        wks.StopWorkspaceFile("")
