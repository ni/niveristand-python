import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, DoubleValue, I64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import VeristandError
from niveristand.library import multitask, nivs_yield, seqtime, task, tickcountms, tickcountus
from niveristand.library.timing import wait, wait_until_next_ms_multiple, wait_until_next_us_multiple, \
    wait_until_settled
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def wait_nivstype():
    init = DoubleValue(0)
    duration = DoubleValue(1)
    end = DoubleValue(0)
    ret = BooleanValue(False)

    init.value = seqtime()
    end.value = wait(duration) - init.value
    if end.value >= duration.value and end.value <= duration.value + 0.1:
        ret.value = True
    return ret.value


@nivs_rt_sequence
def wait_const():
    init = DoubleValue(0)
    end = DoubleValue(0)
    ret = BooleanValue(False)

    init.value = seqtime()
    end.value = wait(DoubleValue(1)) - init.value
    if end.value >= 1 and end.value <= 1.1:
        ret.value = True
    return ret.value


@nivs_rt_sequence
def wait_multitask():
    ret = BooleanValue(False)
    init1 = DoubleValue(0)
    end1 = DoubleValue(0)
    init2 = DoubleValue(0)
    end2 = DoubleValue(0)
    tot_init = DoubleValue(0)
    tot_end = DoubleValue(0)

    tot_init.value = seqtime()
    with multitask() as mt:
        @task(mt)
        def f1():
            init1.value = seqtime()
            nivs_yield()
            end1.value = wait(DoubleValue(1)) - init1.value

        @task(mt)
        def f2():
            init2.value = seqtime()
            end2.value = wait(DoubleValue(3)) - init2.value

    tot_end.value = seqtime() - tot_init.value
    ret.value = tot_end.value >= 3 and tot_end.value <= 4 and \
        end1.value >= 1 and end1.value <= 2 and \
        end2.value >= 3 and end2.value <= 4
    return ret.value


@nivs_rt_sequence
def wait_const_negative():
    init = DoubleValue(0)
    end = DoubleValue(0)
    ret = BooleanValue(True)

    init.value = seqtime()
    end.value = wait(DoubleValue(-1)) - init.value
    if end.value >= 0.1 or end.value < 0:
        ret.value = False
    return ret.value


@nivs_rt_sequence
def _return_one():
    a = DoubleValue(1)
    return a.value


@nivs_rt_sequence
def wait_subseq_call():
    init = DoubleValue(0)
    end = DoubleValue(0)
    ret = BooleanValue(False)

    init.value = seqtime()
    end.value = wait(_return_one()) - init.value
    if end.value >= 1 and end.value <= 1.1:
        ret.value = True
    return ret.value


@nivs_rt_sequence
def wait_until_next_ms():
    init = I64Value(0)
    end = I64Value(0)
    ret = BooleanValue(False)

    init.value = tickcountms()
    end.value = wait_until_next_ms_multiple(DoubleValue(231)) - init.value
    if end.value <= 231 and end.value >= 0:
        ret.value = True
    return ret.value


@nivs_rt_sequence
def wait_until_next_us():
    init = I64Value(0)
    end = I64Value(0)
    ret = BooleanValue(False)

    init.value = tickcountus()
    end.value = wait_until_next_us_multiple(DoubleValue(17000)) - init.value
    # give this one a few us buffer because come on, no way python can do it all that fast
    if end.value <= 22000 and end.value >= 0:
        ret.value = True
    return ret.value


@nivs_rt_sequence
def wait_until_settled_multitask():
    a = DoubleValue(15000)
    timer = DoubleValue(0)
    ret = BooleanValue(False)
    timer.value = seqtime()
    with multitask() as mt:
        @task(mt)
        def monitor():
            ret.value = wait_until_settled(a, DoubleValue(1000), DoubleValue(500), DoubleValue(2), DoubleValue(-1))

        @task(mt)
        def signal():
            a.value = 600
            wait(DoubleValue(1))
            a.value = 12000
            wait(DoubleValue(1))
            a.value = 300
            wait(DoubleValue(1))
            a.value = 750

    timer.value = seqtime() - timer.value
    ret.value = a.value == 750 and timer.value >= 4 and timer.value <= 6 and not ret.value
    return ret.value


@nivs_rt_sequence
def wait_until_settled_timeout():
    pass_test = BooleanValue(False)
    time = DoubleValue(0)
    time.value = seqtime()
    pass_test.value = wait_until_settled(DoubleValue(100),
                                         DoubleValue(90),
                                         DoubleValue(0),
                                         DoubleValue(2),
                                         DoubleValue(1))
    time.value = seqtime() - time.value
    pass_test.value &= time.value > 1 and time.value < 1.1
    return pass_test.value


@nivs_rt_sequence
def wait_wrong_param_type():
    duration = I64Value(1)
    wait(duration)
    return duration.value


run_tests = [
    (wait_nivstype, (), True),
    (wait_const, (), True),
    (wait_const_negative, (), True),
    (wait_subseq_call, (), True),
    (wait_multitask, (), True),
    (wait_until_next_us, (), True),
    (wait_until_next_ms, (), True),
    (wait_until_settled_multitask, (), True),
    (wait_until_settled_timeout, (), True),
]

skip_tests = [
    (wait, (), "Imported RT sequence that we're trying to test."),
    (wait_until_next_ms_multiple, (), "Imported RT sequence that we're trying to test."),
    (wait_until_next_us_multiple, (), "Imported RT sequence that we're trying to test."),
    (wait_until_settled, (), "Imported RT sequence that we're trying to test."),
]

fail_transform_tests = [
    (wait_wrong_param_type, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name, deltat=0.01)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
