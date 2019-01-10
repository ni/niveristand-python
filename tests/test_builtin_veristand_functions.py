import inspect
import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, DoubleValueArray, I64Value
from niveristand.clientapi import ErrorAction
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import RunFailedError, VeristandError
from niveristand.library.primitives import abstime, arraysize, clearfault, clearlasterror, deltat, deltatus, fault, \
    fix, generate_error, getlasterror, iteration, quotient, recip, rem, seqtime, seqtimeus, tickcountms, tickcountus
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def call_abstime():
    a = DoubleValue(0)
    a.value = abstime()
    return a.value


@nivs_rt_sequence
def call_arraysize():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3])
    a.value = arraysize(b.value)
    return a.value


@nivs_rt_sequence
def call_clearfault():
    a = ChannelReference("Aliases/DesiredRPM")
    b = DoubleValue(0)
    c = BooleanValue(False)
    # Store initial channel value
    b.value = a.value
    fault(a, 1001)
    clearfault(a)
    # Try to assign back to the channel the initial value
    a.value = b.value
    # If everything went well the initial value and the current value should now be equal
    c.value = b.value == a.value
    return c.value


@nivs_rt_sequence
def call_clearlasterror():
    generate_error(1, "Continue1", ErrorAction.ContinueSequenceExecution)
    generate_error(2, "Continue2", ErrorAction.ContinueSequenceExecution)
    a = BooleanValue(False)
    b = I64Value(5)
    clearlasterror()
    b.value = getlasterror()
    if b.value == 0:
        a.value = True
    return a.value


@nivs_rt_sequence
def call_deltat():
    a = DoubleValue(0)
    a.value = deltat()
    return a.value


@nivs_rt_sequence
def call_deltatus():
    a = DoubleValue(0)
    a.value = deltatus()
    return a.value


@nivs_rt_sequence
def call_fault():
    a = ChannelReference("Aliases/DesiredRPM")
    b = DoubleValue(0)
    fault(a, 1001)
    b.value = a.value
    # cleanup the fault so that other tests are still able to use this channel
    clearfault(a)
    return b.value


@nivs_rt_sequence
def call_fix():
    a = DoubleValue(4.9)
    a.value = fix(a.value)
    return a.value


@nivs_rt_sequence
def call_getlasterror():
    generate_error(1, "Continue1", ErrorAction.ContinueSequenceExecution)
    generate_error(2, "Continue2", ErrorAction.ContinueSequenceExecution)
    a = BooleanValue(False)
    b = I64Value(0)
    b.value = getlasterror()
    if b.value == 2:
        a.value = True
    return a.value


@nivs_rt_sequence
def call_iteration():
    a = I64Value(0)
    a.value = iteration()
    return a.value


@nivs_rt_sequence
def call_quotient():
    a = I64Value(1440)
    b = DoubleValue(12)
    b.value = quotient(a, b)
    return b.value


@nivs_rt_sequence
def call_recip():
    a = DoubleValue(1024)
    a.value = recip(a)
    return a.value


@nivs_rt_sequence
def call_rem():
    a = I64Value(1439)
    b = DoubleValue(12)
    b.value = rem(a, b)
    return b.value


@nivs_rt_sequence
def call_seqtime():
    a = DoubleValue(0)
    a.value = seqtime()
    a.value = seqtime() - a.value
    return a.value


@nivs_rt_sequence
def call_seqtimeus():
    a = DoubleValue(0)
    a.value = seqtimeus()
    a.value = seqtimeus() - a.value
    return a.value


@nivs_rt_sequence
def call_tickcountms():
    a = I64Value(0)
    a.value = tickcountms()
    a.value = tickcountms() - a.value
    return a.value


@nivs_rt_sequence
def call_tickcountus():
    a = I64Value(0)
    a.value = tickcountus()
    a.value = tickcountus() - a.value
    return a.value


run_everywhere_tests = [
    (call_abstime, (), None),
    (call_arraysize, (), 3),
    (call_clearfault, (), True),
    (call_clearlasterror, (), True),
    (call_deltat, (), 0.01),  # it is 0.01 for engine demo
    (call_deltatus, (), 10 ** 4),  # 0.01 seconds in microseconds
    (call_fault, (), 1001),
    (call_fix, (), 4),
    (call_iteration, (), 0),
    (call_quotient, (), 120),
    (call_recip, (), 1.0 / 1024),
    (call_rem, (), 11),
    (call_seqtime, (), None),
    (call_seqtimeus, (), None),
    (call_tickcountms, (), None),
    (call_tickcountus, (), None),
]

run_tests = run_everywhere_tests + [
    (call_getlasterror, (), True),
]

py_only_errs = [
    (call_abstime, (), None),
    (call_clearfault, (), True),
    (call_clearlasterror, (), True),
    (call_deltat, (), 0.01),  # it is 0.01 for engine demo
    (call_deltatus, (), 10 ** 4),  # 0.01 seconds in microseconds
    (call_fault, (), 1001),
    (call_fix, (), 4),
    (call_getlasterror, (), True),
    (call_recip, (), 1.0 / 1024),
    (call_rem, (), 11),
]

run_as_rts_tests = run_everywhere_tests + [
    (call_getlasterror, (), RunFailedError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", list(set(run_tests) - set(py_only_errs)), ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    if expected_result is None:
        assert actual >= 0
    else:
        assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_as_rts_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    if inspect.isclass(expected_result) and issubclass(expected_result, VeristandError):
        with pytest.raises(expected_result):
            realtimesequencetools.run_py_as_rtseq(func_name)
    else:
        actual = realtimesequencetools.run_py_as_rtseq(func_name)
        # some of these functions are time sensitive so we can't know what to expect
        # so if the expected result is None we just check that a non-zero value got returned
        if expected_result is None:
            assert actual >= 0
        else:
            assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name, 0.01)
    # some of these functions are time sensitive so we can't know what to expect
    # so if the expected result is None we just check that a non-zero value got returned
    if expected_result is None:
        assert actual >= 0
    else:
        assert actual == expected_result


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
