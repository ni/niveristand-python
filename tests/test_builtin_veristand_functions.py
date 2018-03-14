import sys
from niveristand import _decorators, RealTimeSequence
from niveristand import realtimesequencetools
from niveristand.clientapi._datatypes import BooleanValue, ChannelReference, DoubleValue, DoubleValueArray, I64Value
from niveristand.library.primitives import abstime, arraysize, clearfault, clearlasterror, deltat, deltatus, fault, \
    fix, getlasterror, iteration, quotient, recip, rem, seqtime, seqtimeus, tickcountms, tickcountus
import pytest
from testutilities import rtseqrunner, validation


@_decorators.nivs_rt_sequence
def call_abstime():
    a = DoubleValue(0)
    a.value = abstime()
    return a.value


@_decorators.nivs_rt_sequence
def call_arraysize():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3])
    a.value = arraysize(b.value)
    return a.value


@_decorators.nivs_rt_sequence
def call_clearfault():
    a = ChannelReference("Aliases/ActualRPM")
    b = DoubleValue(0)
    c = BooleanValue(False)
    b.value = a.value
    fault(a, 1001)
    clearfault(a)
    c.value = b.value == a.value
    return c.value


@_decorators.nivs_rt_sequence
def call_clearlasterror():
    clearlasterror()


@_decorators.nivs_rt_sequence
def call_deltat():
    a = DoubleValue(0)
    a.value = deltat()
    return a.value


@_decorators.nivs_rt_sequence
def call_deltatus():
    a = DoubleValue(0)
    a.value = deltatus()
    return a.value


@_decorators.nivs_rt_sequence
def call_fault():
    a = ChannelReference("Aliases/DesiredRPM")
    b = DoubleValue(0)
    fault(a, 1001)
    b.value = a.value
    # cleanup the fault so that other tests are still able to use this channel
    clearfault(a)
    return b.value


@_decorators.nivs_rt_sequence
def call_fix():
    a = DoubleValue(4.9)
    a.value = fix(a.value)
    return a.value


@_decorators.nivs_rt_sequence
def call_getlasterror():
    getlasterror()
    return True


@_decorators.nivs_rt_sequence
def call_iteration():
    a = I64Value(0)
    a.value = iteration()
    return a.value


@_decorators.nivs_rt_sequence
def call_quotient():
    a = I64Value(1440)
    b = DoubleValue(12)
    b.value = quotient(a, b)
    return b.value


@_decorators.nivs_rt_sequence
def call_recip():
    a = DoubleValue(1024)
    a.value = recip(a)
    return a.value


@_decorators.nivs_rt_sequence
def call_rem():
    a = I64Value(1439)
    b = DoubleValue(12)
    b.value = rem(a, b)
    return b.value


@_decorators.nivs_rt_sequence
def call_seqtime():
    a = DoubleValue(0)
    a.value = seqtime()
    return a.value


@_decorators.nivs_rt_sequence
def call_seqtimeus():
    a = I64Value(0)
    a.value = seqtimeus()
    return a.value


@_decorators.nivs_rt_sequence
def call_tickcountms():
    a = I64Value(0)
    a.value = tickcountms()
    return a.value


@_decorators.nivs_rt_sequence
def call_tickcountus():
    a = I64Value(0)
    a.value = tickcountus()
    return a.value


run_tests = [
    (call_abstime, (), None),
    (call_arraysize, (), 3),
    (call_deltat, (), 0.01),  # it is 0.01 for engine demo
    (call_deltatus, (), 10 ** 4),  # 0.01 seconds in microseconds
    (call_fault, (), 1001),
    (call_fix, (), 4),
    (call_iteration, (), 0),
    (call_quotient, (), 120),
    (call_recip, (), 1.0 / 1024),
    (call_rem, (), 11),
    (call_seqtime, (), 0),  # time has not run long enough in the sequence
    (call_seqtimeus, (), 0),  # time has not run long enough in the sequence
    (call_tickcountms, (), None),
    (call_tickcountus, (), None),
]

skip_tests = [
    (call_clearfault, (), "Seems like rtseqrunner has a bug in handling faults. Will investigate separately."),
    (call_clearlasterror, (), "GenerateError not implemented"),
    (call_getlasterror, (), "GenerateError not implemented"),
]

fail_transform_tests = []


def idfunc(val):
    return val.__name__


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.skip("Python implementations missing")
@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    # some of these functions are time sensitive so we can't know what to expect
    # so if the expected result is None we just check that a non-zero value got returned
    if expected_result is None:
        assert actual > 0
    else:
        assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name, 0.01)
    # some of these functions are time sensitive so we can't know what to expect
    # so if the expected result is None we just check that a non-zero value got returned
    if expected_result is None:
        assert actual > 0
    else:
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
