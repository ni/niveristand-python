from niveristand import nivs_rt_sequence, NivsParam, realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, DoubleValueArray, ErrorAction, \
    I32Value, I64Value
from niveristand.errors import RunError
from niveristand.library import arraysize, generate_error, iteration, nivs_yield, rand, seqtime, seqtimeus, \
    tickcountms, tickcountus, wait
from niveristand.library.waveforms import ramp, sawtooth_wave, sine_wave, square_wave, triangle_wave, \
    uniform_white_noise_wave


@NivsParam('x', DoubleValue(0), NivsParam.BY_VALUE)
@NivsParam('y', DoubleValue(0), NivsParam.BY_VALUE)
@nivs_rt_sequence
def add_two_numbers(x, y):
    result = DoubleValue(0)
    # There is an intentional mistake here. It multiplies when the function implies it adds.
    result.value = x.value * y.value
    return result.value


@nivs_rt_sequence
def call_add_two_numbers_test():
    result = DoubleValue(0)
    result.value = add_two_numbers(1, 2)
    if result.value != 3:
        generate_error(-100, "Unexpected result", ErrorAction.ContinueSequenceExecution)


def run_add_two_numbers_tests():
    # NON-Deterministic
    try:
        call_add_two_numbers_test()
    except RunError as run_error:
        print("Something Non-deterministic went wrong:" + str(run_error))

    # DETERMINISTIC
    try:
        realtimesequencetools.run_py_as_rtseq(call_add_two_numbers_test)
    except RunError as run_error:
        print("Something Deterministic went wrong:" + str(run_error))


@nivs_rt_sequence
def array_operations():
    """
    Show various operations you can do with array data types in a real-time sequence.

    An array can hold multiple values of the same data type. You cannot have arrays of arrays.
    Use arrays to pass around buffers of data for playback or storage.

    Returns:
        float: the sum of all values in the array.

    """
    var = DoubleValue(0)
    arr_size = I64Value(0)
    array = DoubleValueArray([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    # Index a value out of an array
    var.value = array[4].value + 100
    # Update a value in an array
    array[2].value = 6.0
    # Get the size of an array
    arr_size.value = arraysize(array)
    # Loop over each element of an array. Each iteration a value from the array is copied into x.
    var.value = 0.0
    for x in array:
        var.value += x
    return var.value


@nivs_rt_sequence
def measure_elapsed_time():
    """
    Show a number of ways to measure elapsed time in a sequence.

    You can measure time in milliseconds, microseconds, or in seconds.

    Returns:
        int: milliseconds it took to run this sequence.

    """
    seqtime_timer = DoubleValue(0)
    seqtime_us_timer = I64Value(0)
    tick_ms_timer = I64Value(0)
    tick_us_timer = I64Value(0)

    # These steps capture an initial timestamp in various ways.
    seqtime_timer.value = seqtime()
    seqtime_us_timer.value = seqtimeus()
    tick_ms_timer.value = tickcountms()
    tick_us_timer.value = tickcountus()

    # Simulated work to time.
    while iteration() < 1000:
        nivs_yield()

    # Measure the elapsed time by subtracting the initial timestamp from the current time
    seqtime_timer.value = seqtime() - seqtime_timer.value
    seqtime_us_timer.value = seqtimeus() - seqtime_us_timer.value
    tick_ms_timer.value = tickcountms() - tick_ms_timer.value
    tick_us_timer.value = tickcountus() - tick_us_timer.value

    return tick_ms_timer.value


@nivs_rt_sequence
def state_machine_example():
    state = I32Value(0)
    iters = I32Value(0)
    amplitude = DoubleValue(1000)
    stop = BooleanValue(False)
    output = ChannelReference('Aliases/DesiredRPM')

    while stop.value != True and iters.value < 10:  # noqa: E712 it's recommended to use comparison isntead of identity.
        state.value = rand(7)
        if state.value == 0:
            wait(2)
        elif state.value == 1:
            sine_wave(output, amplitude, 1, 0, 0, 2)
        elif state.value == 2:
            square_wave(output, amplitude, 5, 0, 0, 50, 2)
        elif state.value == 3:
            triangle_wave(output, amplitude, 1, 0, 0, 2)
        elif state.value == 4:
            uniform_white_noise_wave(output, amplitude, tickcountus(), 2)
        elif state.value == 5:
            ramp(output, -amplitude.value, amplitude, 2)
        elif state.value == 6:
            sawtooth_wave(output, amplitude, 1, 0, 0, 2)
        else:
            stop.value = True
        iters.value += 1
        state.value = rand(7)


def run_non_deterministic(func):
    """Run the sequence in a non-deterministic way.

    This function will execute the RT Sequence on the host using the public ClientAPI
    that is already available to VeriStand users. It will communicate to the gateway to
    set and get channel values.

    If using a python IDE, it's possible to debug this function as any other python function,
    so setting breakpoints, stepping into and over statements, etc., will work as expected.
    """
    result = func()
    print("Function " + func.__name__ + "(None-Deterministic):" + str(result))


def run_deterministic(func):
    """Compile the sequence and run it deterministically inside the VeriStand engine.

    As the actual sequence won't be executed by python, debugging won't be available. Also, only
    functions marked as @nivs_rt_sequence will be accepted.
    """
    # The run_py_as_rtseq function takes as a parameter the function that should be called.
    result = realtimesequencetools.run_py_as_rtseq(func)
    print("Function " + func.__name__ + "(Deterministic):" + str(result))


if __name__ == '__main__':
    run_non_deterministic(array_operations)
    run_deterministic(array_operations)
    run_non_deterministic(measure_elapsed_time)
    run_deterministic(measure_elapsed_time)

    run_add_two_numbers_tests()

    run_deterministic(state_machine_example)
    run_non_deterministic(state_machine_example)
