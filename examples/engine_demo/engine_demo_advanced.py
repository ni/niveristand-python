from niveristand import nivs_rt_sequence, NivsParam, run_py_as_rtseq
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue
from niveristand.library import multitask, nivs_yield, stop_task, task, wait_until_settled

""" This module adds multitasking, return values and cleanup tasks to engine_demo_basic.

This example mirrors the 'Engine Demo Advanced and Return Value' example that installs with VeriStand.
Open the 'Engine Demo Advanced and Return Value' stimulus profile to help you understand the following example.
"""


@NivsParam('desired_rpm', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('actual_rpm', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('engine_temp', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def engine_demo_advanced(desired_rpm, actual_rpm, engine_temp):
    """Turns on the engine, sets it to the desired rpm, and monitors the engine temperature."""
    # Use the following local variable declarations to keep track of the test's status.
    warmup_complete = BooleanValue(False)
    warmup_succeeded = BooleanValue(False)

    # Create a multitask with two tasks, one for setting rpm values and one for monitoring.
    # In general, a multitask can contain as many tasks as desired. The tasks will all execute asynchronously,
    # but not in parallel. For more information on multitask behavior, refer to VeriStand help.
    with multitask() as mt:
        # You must decorate tasks using the following notation.
        # The following code shows example of a task.
        @task(mt)
        def engine_warmup():
            """Spawn a task to wait for the actual rpm signal to settle."""
            desired_rpm.value = 2500
            # wait for up to 120 seconds for the actual RPM to be between 999999 and 2450 for 25 seconds.
            wait_until_settled(actual_rpm, 9999999, 2450, 25, 120)
            desired_rpm.value = 8000
            wait_until_settled(actual_rpm, 9999999, 7800, 25, 120)
            warmup_complete.value = True

        @task(mt)
        def monitor_temp():
            """Spawn a task to monitor engine temperature.

            If the temperature rises above 110, the previous task will stop.
            """
            while warmup_complete.value is False:
                if engine_temp.value > 110:
                    stop_task(engine_warmup)
                    warmup_complete.value = True
                    warmup_succeeded.value = False
                nivs_yield()
    # You can use a return value, but some restrictions will apply.
    # For example, the function may only return previously declared variables.
    return warmup_succeeded.value


@nivs_rt_sequence
def run_engine_demo_advanced():
    """Run the engine_demo_advanced example.

    To handle a condition that stops a task (in this case, the engine temperature rising above a safe value),
    use a try/finally block.

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
    return run_py_as_rtseq(run_engine_demo_advanced)


def run_non_deterministic():
    return run_engine_demo_advanced()


if __name__ == '__main__':
    # Run the tests.
    # Note:  We expect the tests to fail because the engine temperature rises above 110,
    # but the cleanup code at the end turns the engine off.
    print("Non-Deterministic test:")
    print("Test Passed!" if run_non_deterministic() else "Test Failed (expected)!")
    print("Deterministic test:")
    print("Test Passed!" if run_deterministic() else "Test Failed (expected)!")
