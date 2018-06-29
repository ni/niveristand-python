from niveristand import nivs_rt_sequence, NivsParam, run_py_as_rtseq
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, DoubleValueArray
from niveristand.library import localhost_wait, seqtime, wait_until_settled


""" This module contains a complex example for running multiple tests in sequence.

This example mirrors the 'Test Engine Setpoints' stimulus profile found in the examples that install with VeriStand.

Instead of using a stimulus profile to report results, this example uses the py.test
unit-testing framework that is commonly used for running Python tests.
"""


@nivs_rt_sequence
@NivsParam('on_off', BooleanValue(False), NivsParam.BY_VALUE)
def set_engine_power(on_off):
    """Turns the engine on or off."""
    engine_power = ChannelReference('Aliases/EnginePower')
    engine_power.value = on_off.value


# If you do not specify a parameter decorator, the parameter defaults to the following:
# Type=DoubleValue
# Default Value = 0
# Passed by reference.
# In this case, the default is adequate, so you do not need to specify the decorator.
@nivs_rt_sequence
def measure_set_point_response(setpoint, timeout, tolerance):
    """Sets the desired rpm to the specified setpoint and wait until the signal settles.

    The tolerance is used to create upper and lower boundaries for the signal.
    Returns the amount of time it takes the signal to settle or timeout.
    """
    actual_rpm = ChannelReference('Aliases/ActualRPM')
    desired_rpm = ChannelReference('Aliases/DesiredRPM')
    start_time = DoubleValue(0)
    settle_time = DoubleValue(0)

    desired_rpm.value = setpoint.value
    # Waits .5 seconds, so the gateway has time to update.
    localhost_wait(0.5)

    start_time.value = seqtime()
    wait_until_settled(actual_rpm,
                       desired_rpm.value + tolerance.value,
                       desired_rpm.value - tolerance.value,
                       DoubleValue(2.0),
                       timeout.value)
    settle_time.value = seqtime() - start_time.value
    return settle_time.value


@nivs_rt_sequence
def inbounds_check(test_value, upper, lower):
    """Returns True if lower <= value <= upper.

    Performs an inbounds check.
    """
    result = BooleanValue(False)
    # Typically, you could write this instruction as lower.value <= test_value.value <= upper.value
    # because Python supports cascading operators. However, for real-time sequences,
    # you must write all comparisons using only two operands.
    result.value = test_value.value >= lower.value and test_value.value <= upper.value
    return result.value


@nivs_rt_sequence
def engine_set_points_profile():
    """Runs three tests in one profile."""
    try:
        all_passed = BooleanValue(True)
        test1_passed = BooleanValue(False)
        test2_passed = BooleanValue(False)
        test3_passed = BooleanValue(False)
        seq_res = DoubleValue(0)

        # Turns on the engine.
        set_engine_power(True)

        # Each test changes the desired rpm and checks to see if the signal settles within 60 seconds.
        seq_res.value = measure_set_point_response(DoubleValue(2500), DoubleValue(60), DoubleValue(100))
        test1_passed.value = inbounds_check(seq_res.value, DoubleValue(60), DoubleValue(0))

        seq_res.value = measure_set_point_response(DoubleValue(6000), DoubleValue(60), DoubleValue(100))
        test2_passed.value = inbounds_check(seq_res.value, DoubleValue(60), DoubleValue(0))

        seq_res.value = measure_set_point_response(DoubleValue(3000), DoubleValue(60), DoubleValue(100))
        test3_passed.value = inbounds_check(seq_res.value, DoubleValue(60), DoubleValue(0))

        all_passed.value = test1_passed.value and test2_passed.value and test3_passed.value
    finally:
        set_engine_power(False)

    return all_passed.value


# The following function runs the profile above deterministically.
# A unit test framework, such as py.test, can find the function.
def test_run_engine_set_points_profile_deterministic():
    result = run_py_as_rtseq(engine_set_points_profile)
    assert result is True


# If you do not need to run the profile deterministically, you can run this function as part of a py.test run.
def test_run_engine_set_points_python():
    set_engine_power(True)
    setpoints = DoubleValueArray([2500, 6000, 3000])
    try:
        for setpoint in setpoints:
            assert 0 < measure_set_point_response(setpoint,
                                                  DoubleValue(60),
                                                  DoubleValue(100)) <= 60, "Setpoint %d failed" % setpoint
    finally:
        set_engine_power(False)
