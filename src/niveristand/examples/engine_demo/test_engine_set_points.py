from niveristand import decorators, realtimesequencetools
from niveristand.clientapi.datatypes import BooleanValue, ChannelReference, DoubleValue, DoubleValueArray
from niveristand.library.primitives import localhost_wait, seqtime
from niveristand.library.timing import wait_until_settled


""" This module contains a complex example for running multiple tests in sequence.

This example is based on the 'Test Engine Setpoints' stimulus profile found in the examples installed with VeriStand.

Instead of using a Stimulus Profile to report results, it uses the py.test unit-testing framework that is commonly used
for running python tests.
"""


@decorators.nivs_rt_sequence
@decorators.NivsParam('on_off', BooleanValue(False), decorators.NivsParam.BY_VALUE)
def set_engine_power(on_off):
    """Turn the engine on or off."""
    engine_power = ChannelReference('Aliases/EnginePower')
    engine_power.value = on_off.value


# Where are the parameter decorator markers?
# If no parameter decorator is found for a particular parameter, it will default to the following
# Type=DoubleValue
# Default Value = 0
# Passed by reference.
# In this case, that default is adequate so there's no need to specify it.
@decorators.nivs_rt_sequence
def measure_set_point_response(setpoint, timeout, tolerance):
    """Set the desired rpm to the specified setpoint and wait until the signal settles.

    The tolerance is used to create upper and lower boundaries for the signal.
    Returns the amount of time it took to settle, or timeout if it didn't.
    """
    actual_rpm = ChannelReference('Aliases/ActualRPM')
    desired_rpm = ChannelReference('Aliases/DesiredRPM')
    start_time = DoubleValue(0)
    settle_time = DoubleValue(0)

    desired_rpm.value = setpoint.value
    # wait a little bit so the gateway has a chance to update if we're running from the host.
    localhost_wait(0.5)

    start_time.value = seqtime()
    wait_until_settled(actual_rpm,
                       desired_rpm.value + tolerance.value,
                       desired_rpm.value - tolerance.value,
                       DoubleValue(2.0),
                       timeout.value)
    settle_time.value = seqtime() - start_time.value
    return settle_time.value


@decorators.nivs_rt_sequence
def inbounds_check(test_value, upper, lower):
    """Return True if lower <= value <= upper.

    A simple helper to do an inbounds check.
    """
    result = BooleanValue(False)
    # Even though python supports cascading operators and this instruction could be written as
    # lower.value <= test_value.value <= upper.value
    # for Real-Time sequences all comparisons must be done on only two operators.
    result.value = test_value.value >= lower.value and test_value.value <= upper.value
    return result.value


@decorators.nivs_rt_sequence
def engine_set_points_profile():
    """Run three tests in one profile."""
    try:
        all_passed = BooleanValue(True)
        test1_passed = BooleanValue(False)
        test2_passed = BooleanValue(False)
        test3_passed = BooleanValue(False)
        seq_res = DoubleValue(0)

        # turn on the engine
        set_engine_power(True)

        # Each test case changes the desired rpm and then we check if we settled within 60 seconds
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


# This function will run the profile above deterministically. It will be found by unit test frameworks like py.test.
def test_run_engine_set_points_profile_deterministic():
    result = realtimesequencetools.run_py_as_rtseq(engine_set_points_profile)
    assert result is True


# This function can be run as part of a py.test run if determinism is not a concern.
def test_run_engine_set_points_python():
    set_engine_power(True)
    setpoints = DoubleValueArray([2500, 6000, 3000])
    try:
        for setpoint in setpoints:
            assert 0 < measure_set_point_response(setpoint, DoubleValue(60), DoubleValue(100)) <= 60, "Setpoint %d failed" % setpoint
    finally:
        set_engine_power(False)
