import time
import os
import math

from niveristand.legacy import NIVeriStand
from testutilities import configutilities


def sleep():
    time.sleep(1)

def test_calculated_channel_formula_legacy():
    wks = NIVeriStand.Workspace()
    print("")
    SYSDEFFILE = os.path.join(configutilities.get_autotest_projects_path(),
                              "CalcChanFormulaTest", "CalcChanFormulaTest.nivssdf")
    print("Deploying %s" % SYSDEFFILE)
    wks.RunWorkspaceFile(SYSDEFFILE,0,1,5000,"","")

    try:
        # Compute Machine Epsilon: The smallest floating point number when
        # added to one is greater than one.

        eps = 1.0
        while ((1.0 + eps) > 1.0):
            epsLast = eps;
            eps = eps / 2.0;
        eps = epsLast;
        print("Machine Epsilon = %g" % (eps))

        # Sleep until the first Time (a calculated channel) is greater than
        # zero. This will be either the first or second time the calculated
        # channels are computed. In VeriStand 2010, the first time the
        # channels are calculated is at Delta T. At any rate, we do not want
        # to proceed until we have performed some calculations.

        result=0
        while (result <= 0):
            sleep()
            result = wks.GetSingleChannelValue("Time")

        # All formulas in VeriStand must have input values. Zero is computed
        # so that it can be used as an input to certain formulas. The way
        # it is computed, it should be precisely zero. No epsilon logic should
        # be used to ensure that it is in fact zero.

        print("Checking Zero=(Time - Time)")
        expectedResult = 0
        result = wks.GetSingleChannelValue("Zero")
        assert (result == expectedResult), "Time-Time (%g) does not match calculated (%g)"  % (expectedResult, result)
        print("...Pass")

        # All formulas in VeriStand must have input values. MinusOne is computed
        # so that it can be used as an input to certain formulas. The way
        # it is computed, it should be precisely -1. No epsilon logic should
        # be used to ensure that it is in fact -1.

        print("Checking MinusOne=(Zero - 1)")
        expectedResult = -1
        result = wks.GetSingleChannelValue("MinusOne")
        assert (result == expectedResult), "Zero-1 (%g) does not match calculated (%g)"  % (expectedResult, result)
        print("...Pass")

        # This computation of Pi should be accurate to all bits in the mantissa.
        # We only use epsilon logic to allow for difference between the transfer
        # between C# and Python.

        print("Checking Pi=acos(-1) Computation")
        expectedResult = math.pi
        abstol = 0
        reltol = eps
        result = wks.GetSingleChannelValue("Pi")
        tol = abstol + reltol*abs(expectedResult);
        assert ((result >= expectedResult - tol) and (result <= expectedResult + tol)), "Pi=acos(-1) (%g) does not match calculated (%g)"  % (expectedResult, result)
        print("...Pass")

        # Exponentiation is higher precedence than multiplication and
        # multiplication is higher precedence than addition. The floating
        # point values contain integers. Therefore no epsilon logic is
        # needed.

        print("Checking Operator Precedence with P+Q*R^2 == P+(Q*(R^2))")
        channels = ("P","Q","R")
        channelsValues= (12,6,3)
        wks.SetMultipleChannelValues(channels,channelsValues)

        channels = ("PplusQtimesRsq","PplusQtimesRsq_Exact")
        expectedResults = [66,66]
        results = wks.GetMultipleChannelValues(channels)
        for i in range(0,len(expectedResults)):
            assert (results[i] == expectedResults[i]), "%s Expected %g Return Value %g not expected" % (channels[i], expectedResult, result)
        print("...Pass")

        # Testing against zero; don't use reltol; only use abstol.

        print("Testing T-acos(cos(T)) where T=(Time modulo Pi)")
        expectedResult = 0
        abstol = eps
        reltol = 1
        result = wks.GetSingleChannelValue("ZeroEqualsTMinusAcosCosT")
        tol = abstol + reltol*abs(expectedResult);
        assert (expectedResult - tol <= result <= expectedResult + tol), "T-acos(cos(T)) (%g) does not match calculated (%g)"  % (expectedResult, result)
        print("...Pass")

        # Testing against zero; don't use reltol; only use abstol.

        print("Testing T-asin(sin(T)) where T=(Time modulo Pi) - (Pi/2)")
        expectedResult = 0
        abstol = eps
        reltol = 1
        result = wks.GetSingleChannelValue("ZeroEqualsTMinusAsinSinT")
        tol = abstol + reltol*abs(expectedResult);
        assert (expectedResult - tol <= result <= expectedResult + tol), "T-asin(sin(T)) (%g) does not match calculated (%g)"  % (expectedResult, result)
        print("...Pass")

        # Testing against one; don't use abstol; only use reltol.

        print("Testing Sin^2(T)+Cos^2(T) [should be one]")
        expectedResult = 1.0
        abstol = 0
        reltol = eps
        result = wks.GetSingleChannelValue("OneEqualsSinSqTPlusCosSqT")
        tol = abstol + reltol*abs(expectedResult);
        assert (expectedResult - tol <= result <= expectedResult + tol), "Sin^2(T)+Cos^2(T) (%g) does not match calculated (%g)"  % (expectedResult, result)
        print("...Pass")

        # This computation of Pi should be accurate to all bits in the mantissa.
        # We only use epsilon logic to allow for difference between the transfer
        # between C# and Python.

        print("Checking Pi=4*atan(1) Computation")
        expectedResult = math.pi
        abstol = 0
        reltol = eps
        result = wks.GetSingleChannelValue("PiEquals4TimesAtan1")
        tol = abstol + reltol*abs(expectedResult);
        assert (expectedResult - tol <= result <= expectedResult + tol), "Pi=4*atan(1) (%g) does not match calculated (%g)"  % (expectedResult, result)
        print("...Pass")

        # Each value in the subtraction should be plus or minus one.
        # The result should be precisely zero. The only value for this
        # equation that is not zero happens when Time=0.

        print("Checking (-1)^int(Time/Pi) - sign(sin(Time)); Should be zero")
        expectedResult = 0
        result = wks.GetSingleChannelValue("AnotherFormulaForZero")
        assert (result == expectedResult), "Test value (%g) does not match calculated (%g)"  % (expectedResult, result)
        print("...Pass")

        # To check the properties of random numbers, we must wait
        # until we have at least 100 data points.

        print("Checking mean and variance of a uniform random number between 0 and 1.")
        print("Mean should be 1/2 and the variance should be 1/12.")

        result=0
        while (result < 100):
            sleep()
            result = wks.GetSingleChannelValue("RandCount")

        # We must be sloppy in our checks here. We cannot expect the
        # underlying pseudo random number generator to be precisely white.

        channels = ("RandRunningMean","RandRunningVariance","RandErrorInVariance")
        expectedResults = [0.5, 1./12., 0.0]
        abstol = 0.03
        reltol = 0.2
        results = wks.GetMultipleChannelValues(channels)
        print("...Got mean=%g, variance=%g, errorInVariance=%g" % (results[0], results[1], results[2]))

        for i in range(0,len(expectedResults)):
            tol = abstol + reltol*abs(expectedResults[i]);
            assert (expectedResults[i] - tol <= results[i] <= expectedResults[i] + tol), "%s Expected %g Return Value %g not expected" % (channels[i], expectedResults[i], results[i])
        print("...Pass")

        # In order to test Peak & Valley, we must wait for at least
        # one cycle time of our input waveform. The time period for
        # the cosine is 2*Pi. We will wait for 10 seconds to allow
        # the waveform to be filtered and the peak detection's offset
       # algorithm to complete.

        print("Input waveform: X = 2*sin(30*Time) + 0.5*cos(Time) + 4")
        print("Applied lowpass Butterworth filter at 3Hz")
        print("Expected output waveform: 0.5*cos(Time) + 4")

        result=0
        while (result < 10):
            sleep()
            result = wks.GetSingleChannelValue("Time")

       # Be a bit sloppy on these checks.

        print("Checking error (tol) and offset (4.0) of output waveform")
        channels = ("ErrorInFilterOutMinusFour", "Z")
        channelNames=("Error", "Offset")
        expectedResults = [0.0, 4.0]
        abstol = 0.05
        reltol = 0.1
        results = wks.GetMultipleChannelValues(channels)
        print("...Got offset=%g, acceptable error=%g" % (results[1], results[0]))

        for i in range(0,len(expectedResults)):
            tol = abstol + reltol*abs(expectedResults[i])
            assert (expectedResults[i] - tol <= results[i] <= expectedResults[i] + tol), "%s Expected %g Return Value %g not expected" % (channelNames[i], expectedResults[i], results[i])
        print("...Pass")

        # Wait a lot more for the peak detection algorithm to publish
        # the peak and valley of our expected sinusoidal channel.

        result=0
        while (result < 30):
            sleep()
            result = wks.GetSingleChannelValue("Time")

        print("Checking peak (4.5) and valley (3.5) of output waveform")
        channels = ("PeakAndValleyOfFilterOut","Y")
        channelNames=("Peak", "Valley")
        expectedResults = [4.5, 3.5]
        abstol = 0.0001
        reltol = 0.01
        results = wks.GetMultipleChannelValues(channels)
        print("...Got peak=%g, valley=%g" % (results[0], results[1]))

        for i in range(0,len(expectedResults)):
            tol = abstol + reltol*abs(expectedResults[i]);
            assert (expectedResults[i] - tol <= results[i] <= expectedResults[i] + tol), "%s Expected %g Return Value %g not expected" % (channelNames[i], expectedResults[i], results[i])
        print("...Pass")

       # Be a bit sloppy in the following test. We have filtered the
        # two tone input and subtracted its offset and we are now
       # integrating the waveform using Simpson's rule.

        print("Applied Simpson's rule integration formula")
        print("Expected output waveform: 0.5*sin(Time)")

        expectedResult = 0
        abstol = 0.05
        reltol = 0.5
        result = wks.GetSingleChannelValue("ErrorInIntegral")
        print("...Got acceptable error=%g" % (result))

        tol = abstol + reltol*abs(expectedResult);
        assert (expectedResult - tol <= result <= expectedResult + tol), "Integral of (FilterOut - 4) does not match expected. Error is %g "  % (result)
        print("...Pass")

        # VeriStand computes all calculated channels in one time step.
        # We check here that it did just that.

        print("Checking final calculated channels time equals initial calculated channels time")
        channels = ("Time","FinalTime")
        results = wks.GetMultipleChannelValues(channels)
        assert (results[0] == results[1]), "Final Calculated Channels Time (%g) does not equal Initial (%g)" % (results[1], results[0])
        print("...Pass")

        print("Test PASSED")
        print("")

    finally:
        wks.StopWorkspaceFile("")
