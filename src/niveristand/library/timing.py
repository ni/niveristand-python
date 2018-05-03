from niveristand import nivs_rt_sequence, NivsParam
from niveristand.clientapi import BooleanValue, DoubleValue, I64Value
from niveristand.library import nivs_yield
from niveristand.library.primitives import quotient, seqtime, tickcountms, tickcountus


@NivsParam('duration', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def wait(duration):
    """
    Waits the duration, in seconds, you specify.

    Args:
        duration (:any:`DoubleValue`): time, in seconds, this function waits. You may specify fractions of seconds.

    Returns:
        float: actual seconds waited.

    This wait is non-blocking, so other tasks will run while this wait executes.

    """
    init_time = DoubleValue(0)
    init_time.value = seqtime()
    while seqtime() - init_time.value < duration.value:
        nivs_yield()

    init_time.value = seqtime()
    return init_time.value


@NivsParam('ms_multiple', I64Value(0), NivsParam.BY_REF)
@nivs_rt_sequence
def wait_until_next_ms_multiple(ms_multiple):
    """
    Waits until the next millisecond multiple of the number you specify in `ms_multiple`.

    Args:
        ms_multiple(:any:`I64Value`): the millisecond multiple to wait until.

    Returns:
        int: actual milliseconds waited.

    This wait is non-blocking, so other tasks will run while this wait executes.

    """
    ticks = I64Value(0)
    if ms_multiple.value > 0:
        last_q = I64Value(0)
        q = I64Value(0)
        ticks.value = tickcountms()
        q.value = quotient(ticks.value, ms_multiple.value)
        last_q.value = q.value
        while q.value == last_q.value:
            last_q.value = q.value
            ticks.value = tickcountms()
            q.value = quotient(ticks.value, ms_multiple.value)
            nivs_yield()
    else:
        nivs_yield()
        ticks.value = tickcountms()
    return ticks.value


@NivsParam('us_multiple', I64Value(0), NivsParam.BY_REF)
@nivs_rt_sequence
def wait_until_next_us_multiple(us_multiple):
    """
    Waits until the next microsecond multiple of the number you specify in `us_multiple`.

    Args:
        us_multiple(:any:`I64Value`): the microsecond multiple to wait until.

    Returns:
        int: actual microseconds waited.

    This wait is non-blocking, so other tasks will run while this wait executes.

    """
    ticks = I64Value(0)
    if us_multiple.value > 0:
        last_q = I64Value(0)
        q = I64Value(0)
        ticks.value = tickcountus()
        q.value = quotient(ticks.value, us_multiple.value)
        last_q.value = q.value
        while q.value == last_q.value:
            last_q.value = q.value
            ticks.value = tickcountus()
            q.value = quotient(ticks.value, us_multiple.value)
            nivs_yield()
    else:
        nivs_yield()
        ticks.value = tickcountus()
    return ticks.value


@NivsParam('signal', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('upper_limit', DoubleValue(150), NivsParam.BY_VALUE)
@NivsParam('lower_limit', DoubleValue(50), NivsParam.BY_VALUE)
@NivsParam('settle_time', DoubleValue(10), NivsParam.BY_VALUE)
@NivsParam('timeout', DoubleValue(60), NivsParam.BY_VALUE)
@nivs_rt_sequence
def wait_until_settled(signal, upper_limit, lower_limit, settle_time, timeout):
    """
    Waits until `signal` settles for the amount of time you specify in `settle_time`.

    Args:
        signal(:any:`DoubleValue`): value to monitor.
        upper_limit(:any:`DoubleValue`): maximum value of the settle range.
        lower_limit(:any:`DoubleValue`): minimum value of the settle range.
        settle_time(:any:`DoubleValue`): time, in seconds, `signal` must stay inside the settle range.
        timeout(:any:`DoubleValue`): seconds to wait before the function times out.

    Returns:
        bool:

        True: The signal failed to settle before the operation timed out.
        False: The signal settled before the operation timed out.


    This wait is non-blocking, so other tasks will run while this wait executes.

    """
    init_time = DoubleValue(0)
    curr_time = DoubleValue(0)
    in_limits_duration = DoubleValue(0)
    in_limits_start = DoubleValue(0)
    timed_out = BooleanValue(False)
    in_limits = BooleanValue(False)
    first = BooleanValue(True)

    init_time.value = seqtime()
    # first is just used to emulate a do-while loop
    while first.value \
            or ((not in_limits.value or (in_limits_duration.value < settle_time.value)) and not timed_out.value):
        first.value = False
        curr_time.value = seqtime()
        if signal.value <= upper_limit.value and signal.value >= lower_limit.value:
            if not in_limits.value:
                in_limits.value = True
                in_limits_start.value = curr_time.value
                in_limits_duration.value = 0
            else:
                in_limits_duration.value = curr_time.value - in_limits_start.value
        else:
            in_limits.value = False

        if timeout.value >= 0:
            timed_out.value = (curr_time.value - init_time.value) > timeout.value
        nivs_yield()

    return timed_out.value
