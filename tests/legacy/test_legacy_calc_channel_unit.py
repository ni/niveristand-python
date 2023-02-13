import math
import os
import time

from niveristand.legacy import NIVeriStand

TEST_RESULT = 0  # Testresult set to false in beginning
TEST_COMMENT = ""  # Test  comment to append to result


# @pytest.mark.skip("Pythonnet seems to have troubles with Inf and -Inf")
def test_calculated_channel_ut_legacy():
    workspace = NIVeriStand.Workspace()
    print("")
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\CalcChanUnitTest\CalcChanUnitTest.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, False, True, 20000, "", "")

    try:
        # Compute Machine Epsilon: The smallest floating point number when
        # added to one is greater than one.

        eps = 1.0
        while (1.0 + eps) > 1.0:
            epsLast = eps
            eps = eps / 2.0
        eps = epsLast
        print("Machine Epsilon = %g" % (eps))

        # We will be testing NaNs and Infs as well

        NaN = float("nan")
        Inf = float("inf")

        # Sleep until the first Time (a calculated channel) is greater than
        # zero. This will be either the first or second time the calculated
        # channels are computed. In VeriStand 2010, the first time the
        # channels are calculated is at Delta T. At any rate, we do not want
        # to proceed until we have performed some calculations.

        result = 0
        while result <= 0:
            time.sleep(1)
            result = workspace.GetSingleChannelValue("Time")

        # All formulas in VeriStand must have input values. Zero is computed
        # so that it can be used as an input to certain formulas. The way
        # it is computed, it should be precisely zero. No epsilon logic should
        # be used to ensure that it is in fact zero.

        print("Checking Zero channel is 0.0")
        expectedResult = 0.0
        result = workspace.GetSingleChannelValue("Zero")
        assert result == expectedResult, "Time-Time (%g) does not match calculated (%g)" % (
            expectedResult,
            result,
        )
        print("...Pass")

        # Test functions of one variable

        TestFct = ["abs", "int", "sign", "sin", "cos", "tan", "asin", "acos", "atan", "exp", "sqrt"]

        TestChan = [
            "Abs(X)",
            "Int(X)",
            "Sign(X)",
            "Sin(X)",
            "Cos(X)",
            "Tan(X)",
            "Asin(X)",
            "Acos(X)",
            "Atan(X)",
            "Exp(X)",
            "Sqrt(X)",
        ]

        # Input and expected output values for the calculated channels

        # NOTE: abs(-Inf) == Inf in Xmath
        # NOTE: abs( Inf) == Inf in Xmath

        absIn = [-1.0, 0.0, 1.0, NaN, Inf, Inf]
        absOut = [1.0, 0.0, 1.0, NaN, NaN, NaN]

        # NOTE: (int)(-2.718) == -2   in the c language
        # NOTE: (int)(-3.142) == -3   in the c language
        # NOTE: (int)(-1.500) == -1   in the c language
        # NOTE: (int)(-1.500) == -1   in the c language
        # NOTE: (int)(-Inf)   == -Inf in Xmath
        # NOTE: (int)( Inf)   ==  Inf in Xmath

        intIn = [-math.pi, -math.e, -1.5, 1.5, math.e, math.pi, NaN, -Inf, Inf]
        intOut = [-4.0, -3.0, -2.0, 1.0, 2.0, 3.0, NaN, NaN, NaN]

        signIn = [-math.pi, 0.0, math.pi, NaN, -Inf, Inf]
        signOut = [-1.0, 0.0, 1.0, NaN, -1.0, 1.0]

        sinIn = [-math.pi / 2.0, math.pi / 6.0, math.pi / 2.0, NaN, -Inf, Inf]
        sinOut = [-1.0, 0.5, 1.0, NaN, NaN, NaN]

        cosIn = [math.pi, math.pi / 3.0, 0.0, NaN, -Inf, Inf]
        cosOut = [-1.0, 0.5, 1.0, NaN, NaN, NaN]

        tanIn = [math.pi, math.pi / 4.0, 0.0, NaN, -Inf, Inf]
        tanOut = [0.0, 1.0, 0.0, NaN, NaN, NaN]

        asinIn = [-1.0, 0.0, 1.0, NaN, -Inf, Inf]
        asinOut = [-math.pi / 2.0, 0.0, math.pi / 2.0, NaN, NaN, NaN]

        acosIn = [-1.0, 0.0, 1.0, NaN, -Inf, Inf]
        acosOut = [math.pi, math.pi / 2.0, 0.0, NaN, NaN, NaN]

        atanIn = [-1.0, 0.0, 1.0, NaN, -Inf, Inf]
        atanOut = [-math.pi / 4.0, 0.0, math.pi / 4.0, NaN, -math.pi / 2.0, math.pi / 2.0]

        # NOTE: exp(Inf) == Inf in Xmath

        expIn = [-1.0, 0.0, 1.0, NaN, -Inf, Inf]
        expOut = [1.0 / math.e, 1.0, math.e, NaN, 0.0, NaN]

        # NOTE: sqrt(Inf) == Inf in Xmath

        sqrtIn = [0.0, 1.0, 2.0, NaN, -Inf, Inf]
        sqrtOut = [0.0, 1.0, math.sqrt(2.0), NaN, NaN, NaN]

        # Loop through the various calculated channels to test

        TestIn = (absIn, intIn, signIn, sinIn, cosIn, tanIn, asinIn, acosIn, atanIn, expIn, sqrtIn)

        TestOut = (
            absOut,
            intOut,
            signOut,
            sinOut,
            cosOut,
            tanOut,
            asinOut,
            acosOut,
            atanOut,
            expOut,
            sqrtOut,
        )

        abstol = eps
        reltol = math.sqrt(eps)

        for j in range(0, len(TestOut)):
            Fct = TestFct[j]
            Chan = TestChan[j]
            In = TestIn[j]
            Out = TestOut[j]

            for i in range(0, len(Out)):
                print("Testing: %g = %s(%g) ..." % (Out[i], Fct, In[i]))
                workspace.SetSingleChannelValue("X", In[i])
                time.sleep(1)
                result = workspace.GetSingleChannelValue(Chan)

                if math.isnan(Out[i]) and not math.isnan(result):
                    assert False, "%s(%g): Expected %g Return Value %g not expected" % (
                        Chan,
                        In[i],
                        Out[i],
                        result,
                    )

                elif math.isinf(Out[i]) and not math.isinf(result):
                    assert False, "%s(%g): Expected %g Return Value %g not expected" % (
                        Chan,
                        In[i],
                        Out[i],
                        result,
                    )

                elif math.isinf(Out[i]) and math.isinf(result):
                    if math.copysign(1, Out[i]) and not math.copysign(1, result):
                        assert False, "%s(%g): Expected %g Return Value %g not expected" % (
                            Chan,
                            In[i],
                            Out[i],
                            result,
                        )
                else:
                    tol = abstol + reltol * abs(Out[i])
                    if (result < Out[i] - tol) | (result > Out[i] + tol):
                        assert False, "%s(%g): Expected %g Return Value %g not expected" % (
                            Chan,
                            In[i],
                            Out[i],
                            result,
                        )
                    else:
                        print("...Pass")

        # Test operators: functions of two variables

        # NOTE: The following formulas can be entered in the SystemExplorer
        #       and do not report parsing errors, but, they do not deploy.
        #           X * -Y
        #          -X * -Y
        #           X / -Y
        #          -X / -Y
        #           X ^ -Y
        #          -X ^ -Y
        #
        # NOTE: The SystemExplorer allows you to create aliases with '/' in
        #       them even though this interferes with the path description.
        #       Rejected by the API:
        #           X / Y
        #          -X / Y

        TestMinus1 = ["", "-", "", "-", "", "-", "", "-", "", "-", "", "-", "", "-"]

        TestMinus2 = ["", "", "-", "-", "", "", "-", "-", "", "", "", "", "", ""]

        TestOp = ["+", "+", "+", "+", "-", "-", "-", "-", "*", "*", "/", "/", "^", "^"]

        TestChan = [
            "X + Y",
            "-X + Y",
            "X + -Y",
            "-X + -Y",
            "X - Y",
            "-X - Y",
            "X - -Y",
            "-X - -Y",
            "X * Y",
            "-X * Y",
            "X div Y",
            "-X div Y",
            "X ^ Y",
            "-X ^ Y",
        ]

        # Input and expected output values for the calculated channels

        # Inf + Inf should be Inf

        XplusYIn1 = [-5.0, 0.0, 2.0, Inf, Inf]
        XplusYIn2 = [-2.0, 0.0, 5.0, Inf, -Inf]
        XplusYOut = [-7.0, 0.0, 7.0, NaN, NaN]

        minusXplusYIn1 = [-5.0, 0.0, 2.0]
        minusXplusYIn2 = [-2.0, 0.0, 5.0]
        minusXplusYOut = [3.0, 0.0, 3.0]

        XplusMinusYIn1 = [-5.0, 0.0, 2.0]
        XplusMinusYIn2 = [-2.0, 0.0, 5.0]
        XplusMinusYOut = [-3.0, 0.0, -3.0]

        minusXplusMinusYIn1 = [-5.0, 0.0, 2.0]
        minusXplusMinusYIn2 = [-2.0, 0.0, 5.0]
        minusXplusMinusYOut = [7.0, 0.0, -7.0]

        XminusYIn1 = [-5.0, 0.0, 2.0, Inf]
        XminusYIn2 = [-2.0, 0.0, 5.0, Inf]
        XminusYOut = [-3.0, 0.0, -3.0, NaN]

        minusXminusYIn1 = [-5.0, 0.0, 2.0]
        minusXminusYIn2 = [-2.0, 0.0, 5.0]
        minusXminusYOut = [7.0, 0.0, -7.0]

        XminusMinusYIn1 = [-5.0, 0.0, 2.0]
        XminusMinusYIn2 = [-2.0, 0.0, 5.0]
        XminusMinusYOut = [-7.0, 0.0, 7.0]

        minusXminusMinusYIn1 = [-5.0, 0.0, 2.0]
        minusXminusMinusYIn2 = [-2.0, 0.0, 5.0]
        minusXminusMinusYOut = [3.0, 0.0, 3.0]

        # (2 *  Inf) should be  Inf
        # (2 * -Inf) should be -Inf

        XtimesYIn1 = [-5.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0]
        XtimesYIn2 = [-2.0, 0.0, 5.0, 24.0, Inf, Inf, -Inf]
        XtimesYOut = [10.0, 0.0, 10.0, 0.0, NaN, NaN, NaN]

        minusXtimesYIn1 = [-5.0, 0.0, 2.0]
        minusXtimesYIn2 = [-2.0, 0.0, 5.0]
        minusXtimesYOut = [-10.0, 0.0, -10.0]

        XdivYIn1 = [-5.0, 0.0, 2.0, 0.0, 1.0, -1.0]
        XdivYIn2 = [-2.0, 0.0, 5.0, 24.0, 0.0, 0.0]
        XdivYOut = [2.5, NaN, 0.4, 0.0, Inf, -Inf]

        minusXdivYIn1 = [-5.0, 0.0, 2.0, 0.0, 1.0, -1.0]
        minusXdivYIn2 = [-2.0, 0.0, 5.0, 24.0, 0.0, 0.0]
        minusXdivYOut = [-2.5, NaN, -0.4, 0.0, -Inf, Inf]

        # Most languages return NaN for 0^0

        XtoTheYIn1 = [-5.0, 0.0, 2.0]
        XtoTheYIn2 = [-2.0, 0.0, 5.0]
        XtoTheYOut = [0.04, 1.0, 32.0]

        # Most languages return NaN for -(0^0)

        minusXtoTheYIn1 = [-5.0, 0.0, 2.0, 1.0]
        minusXtoTheYIn2 = [-2.0, 0.0, 5.0, 2.0]
        minusXtoTheYOut = [-0.04, -1.0, -32.0, -1.0]

        # Loop through the various calculated channels to test

        TestIn1 = [
            XplusYIn1,
            minusXplusYIn1,
            XplusMinusYIn1,
            minusXplusMinusYIn1,
            XminusYIn1,
            minusXminusYIn1,
            XminusMinusYIn1,
            minusXminusMinusYIn1,
            XtimesYIn1,
            minusXtimesYIn1,
            XdivYIn1,
            minusXdivYIn1,
            XtoTheYIn1,
            minusXtoTheYIn1,
        ]

        TestIn2 = [
            XplusYIn2,
            minusXplusYIn2,
            XplusMinusYIn2,
            minusXplusMinusYIn2,
            XminusYIn2,
            minusXminusYIn2,
            XminusMinusYIn2,
            minusXminusMinusYIn2,
            XtimesYIn2,
            minusXtimesYIn2,
            XdivYIn2,
            minusXdivYIn2,
            XtoTheYIn2,
            minusXtoTheYIn2,
        ]

        TestOut = [
            XplusYOut,
            minusXplusYOut,
            XplusMinusYOut,
            minusXplusMinusYOut,
            XminusYOut,
            minusXminusYOut,
            XminusMinusYOut,
            minusXminusMinusYOut,
            XtimesYOut,
            minusXtimesYOut,
            XdivYOut,
            minusXdivYOut,
            XtoTheYOut,
            minusXtoTheYOut,
        ]

        abstol = eps
        reltol = math.sqrt(eps)

        for j in range(0, len(TestOut)):
            Chan = TestChan[j]
            Out = TestOut[j]
            Minus1 = TestMinus1[j]
            In1 = TestIn1[j]
            Op = TestOp[j]
            Minus2 = TestMinus2[j]
            In2 = TestIn2[j]

            for i in range(0, len(Out)):
                print(
                    "Testing: %g = %s(%g) %s %s(%g) ..."
                    % (Out[i], Minus1, In1[i], Op, Minus2, In2[i])
                )
                workspace.SetSingleChannelValue("X", In1[i])
                workspace.SetSingleChannelValue("Y", In2[i])
                time.sleep(1)
                result = workspace.GetSingleChannelValue(Chan)

                if math.isnan(Out[i]) and not math.isnan(result):
                    assert False, "%s(%g) %s %s(%g): Expected %g Return Value %g not expected" % (
                        Minus1,
                        In1[i],
                        Op,
                        Minus2,
                        In2[i],
                        Out[i],
                        result,
                    )

                elif math.isinf(Out[i]) and not math.isinf(result):
                    assert False, "%s(%g) %s %s(%g): Expected %g Return Value %g not expected" % (
                        Minus1,
                        In1[i],
                        Op,
                        Minus2,
                        In2[i],
                        Out[i],
                        result,
                    )

                elif math.isinf(Out[i]) and math.isinf(result):
                    if math.copysign(1, Out[i]) and not math.copysign(1, result):
                        assert (
                            False
                        ), "%s(%g) %s %s(%g): Expected %g Return Value %g not expected" % (
                            Minus1,
                            In1[i],
                            Op,
                            Minus2,
                            In2[i],
                            Out[i],
                            result,
                        )
                else:
                    tol = abstol + reltol * abs(Out[i])
                    if (result < Out[i] - tol) | (result > Out[i] + tol):
                        assert (
                            False
                        ), "%s(%g) %s %s(%g): Expected %g Return Value %g not expected" % (
                            Minus1,
                            In1[i],
                            Op,
                            Minus2,
                            In2[i],
                            Out[i],
                            result,
                        )
                    else:
                        print("...Pass")

        # All operations at the same precedence are evaluated left to right
        # Precedence (highest is 1)
        # 1 -- Functions
        # 2 -- Power
        # 3 -- Unary minus
        # 4 -- Multiplication and division
        # 5 -- Addition and subtraction

        print(" ")
        print("Checking Operator Precedence...")
        channels = ("P", "Q", "R", "X", "Y", "Z")
        channelsValues = (16.0, 9.0, 3.0, 5.0, 0.125, 4.0)
        workspace.SetMultipleChannelValues(channels, channelsValues)
        time.sleep(1)

        print("Using:")
        for i in range(0, 6):
            print("   %s = %g" % (channels[i], channelsValues[i]))
        print(" ")

        channels = (
            "P+(Q*(R^2))",
            "(P*Q) + (X*Z)",
            # "(P ^ Z) ^ Y",
            "(Q div R) div Y",
            "(P - Q) - R",
            # "P + Z*((Q^4)^Y)*R + (P^2)^Y",
            "(P+R)*(Q^(Y*Z)+21)",
        )

        expectedResults = [
            97.0,
            164.0,
            # 4.0,
            24.0,
            4.0,
            # 54.0,
            456.0,
        ]
        abstol = eps
        reltol = math.sqrt(eps)

        results = workspace.GetMultipleChannelValues(channels)
        for i in range(0, len(expectedResults)):
            print("Testing: %g = %s ..." % (expectedResults[i], channels[i]))
            tol = abstol + reltol * abs(expectedResults[i])
            if (results[i] < expectedResults[i] - tol) | (results[i] > expectedResults[i] + tol):
                assert False, "%s: Expected %g Return Value %g not expected" % (
                    channels[i],
                    expectedResults[i],
                    results[i],
                )
            else:
                print("...Pass")

        print("Test PASSED")

    finally:
        workspace.StopWorkspaceFile("")
