import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import DoubleValue, DoubleValueArray, I32Value, I32ValueArray
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def _return_constant():
    return 2


@nivs_rt_sequence
def _return_param_plus_one(param):
    param.value = param.value + 1
    return param.value


@nivs_rt_sequence
def _modify_param(param):
    param.value = param.value + 1


@nivs_rt_sequence
def number_subscript():
    a = DoubleValueArray([0, 1, 2])
    return a[1].value


@nivs_rt_sequence
def rtseq_call_subscript():
    a = DoubleValueArray([0, 1, 2])
    return a[_return_constant()].value


@nivs_rt_sequence
def subscript_in_subscript():
    a = I32ValueArray([1, 2, 3])
    return a[a[1].value].value


@nivs_rt_sequence
def operator_in_subscript():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    return a[1 + 2].value


@nivs_rt_sequence
def operator_in_subscript1():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    b = I32Value(1)
    c = I32Value(2)
    return a[b.value + c.value].value


@nivs_rt_sequence
def assign_subscript():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    b = DoubleValue(0)
    b.value = a[1].value
    return b.value


@nivs_rt_sequence
def assign_subscript1():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0] = DoubleValue(3)
    return a[0].value


@nivs_rt_sequence
def assign_subscript2():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0] = a[4]
    return a[0].value


@nivs_rt_sequence
def assign_subscript3():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0].value = 5
    return a[0].value


@nivs_rt_sequence
def assign_subroutine_return():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0].value = _return_param_plus_one(a[0])
    return a[0].value


@nivs_rt_sequence
def modify_array():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    _modify_param(a[0])
    return a[0].value


run_tests = [
    (number_subscript, (), 1),
    (rtseq_call_subscript, (), 2),
    (subscript_in_subscript, (), 3),
    (operator_in_subscript, (), 3),
    (operator_in_subscript1, (), 3),
    (assign_subscript, (), 1),
    (assign_subscript3, (), 5),
    (assign_subroutine_return, (), 1),
    (modify_array, (), 1),
]

fail_transform_tests = [
    (assign_subscript1, TranslateError),
    (assign_subscript2, TranslateError),
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
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name()


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
