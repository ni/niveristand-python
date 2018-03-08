from niveristand import decorators, realtimesequencetools
from niveristand.clientapi.datatypes import BooleanValue, ChannelReference, DoubleValue
from niveristand.library.tasks import multitask, nivs_yield, stop_task
from niveristand.library.timing import wait_until_settled

""" This module contains an expansion on the basic example.

This example mirrors 'Engine Demo Advanced and Return Value' in the examples that get installed with VeriStand.
Please refer to that Stimulus Profile for details on what this example tries to achieve.
"""


@decorators.NivsParam('desired_rpm', DoubleValue(0), decorators.NivsParam.BY_REF)
@decorators.NivsParam('actual_rpm', DoubleValue(0), decorators.NivsParam.BY_REF)
@decorators.NivsParam('engine_temp', DoubleValue(0), decorators.NivsParam.BY_REF)
def engine_demo_advanced(desired_rpm, actual_rpm, engine_temp):
    """Turn on the engine and set it to the desired rpm, while also monitoring engine temperature."""
    # These are local variable declarations that will be used to keep track of the test's status
    warmup_complete = BooleanValue(False)
    warmup_succeeded = BooleanValue(False)

    # Create a multitask with two tasks, one for setting rpm values and one for monitoring.
    # In general, a multitask can contain as many tasks as desired. They will all execute asynchronously,
    # but not in parallel. For more information on Multitask behavior please refer to VeriStand documentation.
    with multitask() as mt:
        # Tasks need to be decorated as such. This notation is required.
        # A task is
        @decorators.task(mt)
        def engine_warmup():
            """Spawn task to wait for the actual rpm signal to settle."""
            desired_rpm.value = 2500
            # wait for up to 120 seconds for the actual RPM to be between 999999 and 2450 for 25 seconds
            wait_until_settled(actual_rpm, 9999999, 2450, 25, 120)
            desired_rpm.value = 8000
            wait_until_settled(actual_rpm, 9999999, 7800, 25, 120)
            warmup_complete.value = True

        @decorators.task(mt)
        def monitor_temp():
            """Spawn task to monitor engine temperature. If it goes above 110 it will stop the other task."""
            while warmup_complete.value is False:
                if engine_temp.value > 110:
                    stop_task(engine_warmup)
                    warmup_complete.value = True
                    warmup_succeeded.value = False
                nivs_yield()
    # A return value can be used, however some restrictions will be in place.
    # For example, only previously declared variables may be returned.
    return warmup_succeeded.value


@decorators.nivs_rt_sequence
def run_engine_demo_advanced():
    """Run the engine_demo_advanced example.

    Since there's a possibility that something will go wrong
    (in this case, the engine temperature rising above a safe value)
    a try/finally block is used.

    Regardless of the result of the execution, the finally block can be used to safely shut down the engine.
    """
    try:
        warmup_succeeded = BooleanValue(False)
        engine_power = ChannelReference('Aliases/EnginePower')
        desired_rpm = ChannelReference('Aliases/DesiredRPM')
        actual_rpm = ChannelReference('Aliases/ActualRPM')
        engine_temp = ChannelReference('Aliases/EngineTemp')
        engine_power.value = True
        warmup_succeeded.value = engine_demo_advanced(desired_rpm, actual_rpm, engine_temp)
    finally:
        engine_power.value = False
        desired_rpm.value = 0
    return warmup_succeeded.value


def run_deterministic():
    return realtimesequencetools.run_py_as_rtseq(run_engine_demo_advanced)


def run_non_deterministic():
    return run_engine_demo_advanced()


if __name__ == '__main__':
    # Run the tests.
    # Note: They're expected to fail because engine temperature raises above 110,
    # but the engine should be turned off at the end thanks to the cleanup code.
    print("Non-Deterministic test:")
    print("Test Passed!" if run_non_deterministic() else "Test Failed (expected)!")
    print("Deterministic test:")
    print("Test Passed!" if run_deterministic() else "Test Failed (expected)!")
