from niveristand import nivs_rt_sequence, NivsParam, realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue
from niveristand.library import wait

""" This module contains a basic example of how to create an RT sequence in python.

This example mirrors 'Engine Demo Basic' in the examples that get installed with VeriStand.
Please refer to that Stimulus Profile for details on what this example tries to achieve.
"""


# RT Sequences need to be marked as such with this decorator.
@nivs_rt_sequence
# We also need to know the data type and default value of parameters,
# as well as whether they should be passed by value or by reference.
@NivsParam('engine_power', BooleanValue(0), NivsParam.BY_REF)
@NivsParam('desired_rpm', DoubleValue(0), NivsParam.BY_REF)
def engine_demo_basic(engine_power, desired_rpm):
    """Turn on the engine, set the desired_rpm to the passed value for 20 seconds, then shut down.

    Parameters passed in need to be accessed through their ".value" property.
    """
    # Channel references can also be specified.
    engine_power_chan = ChannelReference('Aliases/EnginePower')
    desired_rpm_chan = ChannelReference('Aliases/DesiredRPM')
    engine_power_chan.value = engine_power.value
    desired_rpm_chan.value = desired_rpm.value
    wait(DoubleValue(20))
    engine_power_chan.value = False
    desired_rpm_chan.value = 0


@nivs_rt_sequence
def run_engine_demo():
    """Set up channel references and call the actual test."""
    # Calling into another RT Sequence is just as calling a normal python function.
    # However, when passing by reference, strongly-typed objects need to be created.
    engine_demo_basic(BooleanValue(True), DoubleValue(2500))


def run_non_deterministic():
    """Run the sequence in a non-deterministic way.

    This function will execute the RT Sequence on the host using the public ClientAPI
    that is already available to VeriStand users. It will communicate to the gateway to
    set and get channel values.

    If using a python IDE, it's possible to debug this function as any other python function,
    so setting breakpoints, stepping into and over statements, etc., will work as expected.
    """
    run_engine_demo()


def run_deterministic():
    """Compile the sequence and run it deterministically inside the VeriStand engine.

    As the actual sequence won't be executed by python, debugging won't be available. Also, only
    functions marked as @nivs_rt_sequence will be accepted.
    """
    # The run_py_as_rtseq function takes as a parameter the function that should be called.
    realtimesequencetools.run_py_as_rtseq(run_engine_demo)


if __name__ == '__main__':
    run_non_deterministic()
    print('Finished non-deterministic')
    run_deterministic()
    print('Finished deterministic')
