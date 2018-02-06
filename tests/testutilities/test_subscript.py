import sys
from niveristand import decorators, RealTimeSequence
from niveristand.clientapi.datatypes import DoubleValue, DoubleValueArray, I32Value, I32ValueArray
from niveristand.exceptions import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation


@decorators.nivs_rt_sequence
def return_constant():
    return 2


@decorators.nivs_rt_sequence
def return_param_plusone(param):
    param = param + 1
    return param


@decorators.nivs_rt_sequence
def modify_param(param):
    param.value = param.value + 1


@decorators.nivs_rt_sequence
def number_subscript():
    a = DoubleValueArray([0, 1, 2])
    return a[1].value


@decorators.nivs_rt_sequence
def rtseq_call_subscript():
    a = DoubleValueArray([0, 1, 2])
    return a[return_constant()].value


@decorators.nivs_rt_sequence
def subscript_in_subscript():
    a = I32ValueArray([1, 2, 3])
    return a[a[1].value].value


@decorators.nivs_rt_sequence
def operator_in_subscript():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    return a[1 + 2].value


@decorators.nivs_rt_sequence
def operator_in_subscript1():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    b = I32Value(1)
    c = I32Value(2)
    return a[b.value + c.value].value


@decorators.nivs_rt_sequence
def assign_subscript():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    b = DoubleValue(0)
    b.value = a[1].value
    return b.value


@decorators.nivs_rt_sequence
def assign_subscript1():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0] = DoubleValue(3)
    return a[0].value


@decorators.nivs_rt_sequence
def assign_subscript2():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0] = a[4]
    return a[0].value


@decorators.nivs_rt_sequence
def assign_subscript3():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0].value = 5
    return a[0].value


@decorators.nivs_rt_sequence
def assign_subroutine_return():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0].value = return_param_plusone(a[0].value)
    return a[0].value


@decorators.nivs_rt_sequence
def modify_array():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    modify_param(a[0])
    return a[0].value


run_tests = [
    (return_constant, (), 2),
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


skip_tests = [
    (return_param_plusone, (), "This call receives a parameter and it can't be faked without a caller."),
    (modify_param, (), "This call receives a parameter and it can't be faked without a caller."),
]


fail_transform_tests = [
    (assign_subscript1, TranslateError),
    (assign_subscript2, TranslateError),
]


def idfunc(val):
    return val.__name__


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, expected_result):
    try:
        RealTimeSequence(func_name)
    except expected_result:
        pass
    except VeristandError as e:
        pytest.fail('Unexpected exception raised:' +
                    str(e.__class__) + ' while expected was: ' + expected_result.__name__)
    except Exception as exception:
        pytest.fail('ExpectedException not raised: ' + exception)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
