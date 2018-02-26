from niveristand import decorators
from niveristand.clientapi.datatypes import BooleanValue, DoubleValue, I64Value
from niveristand.library.primitives import quotient, seqtime, tickcountms, tickcountus
from niveristand.library.tasks import nivs_yield


@decorators.NivsParam('duration', DoubleValue(0), decorators.NivsParam.BY_REF)
@decorators.nivs_rt_sequence
def wait(duration):
    init_time = DoubleValue(0)
    init_time.value = seqtime()
    while seqtime() - init_time.value < duration.value:
        nivs_yield()

    init_time.value = seqtime()
    return init_time.value


@decorators.NivsParam('ms_multiple', I64Value(0), decorators.NivsParam.BY_REF)
@decorators.nivs_rt_sequence
def wait_until_next_ms_multiple(ms_multiple):
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


@decorators.NivsParam('us_multiple', I64Value(0), decorators.NivsParam.BY_REF)
@decorators.nivs_rt_sequence
def wait_until_next_us_multiple(us_multiple):
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


@decorators.NivsParam('signal', DoubleValue(0), decorators.NivsParam.BY_REF)
@decorators.NivsParam('upper_limit', DoubleValue(150), decorators.NivsParam.BY_VALUE)
@decorators.NivsParam('lower_limit', DoubleValue(50), decorators.NivsParam.BY_VALUE)
@decorators.NivsParam('settle_time', DoubleValue(10), decorators.NivsParam.BY_VALUE)
@decorators.NivsParam('timeout', DoubleValue(60), decorators.NivsParam.BY_VALUE)
@decorators.nivs_rt_sequence
def wait_until_settled(signal, upper_limit, lower_limit, settle_time, timeout):
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
