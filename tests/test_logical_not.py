import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, DoubleValue, I32Value, I64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_true():
    a = BooleanValue(True)
    return a.value


@nivs_rt_sequence
def logical_not_simple_numbers():
    a = BooleanValue(0)
    a.value = not 2
    return a.value


@nivs_rt_sequence
def logical_not_simple_numbers1():
    a = BooleanValue(0)
    a.value = not 0
    return a.value


@nivs_rt_sequence
def logical_not_nivsdatatype_double():
    a = BooleanValue(0)
    a.value = not DoubleValue(3)
    return a.value


@nivs_rt_sequence
def logical_not_nivsdatatype_double1():
    a = BooleanValue(0)
    a.value = not DoubleValue(0)
    return a.value


@nivs_rt_sequence
def logical_not_nivsdatatype_int32():
    a = BooleanValue(0)
    a.value = not I32Value(0)
    return a.value


@nivs_rt_sequence
def logical_not_nivsdatatype_int64():
    a = BooleanValue(0)
    a.value = not I64Value(0)
    return a.value


@nivs_rt_sequence
def logical_not_bool():
    a = BooleanValue(True)
    a.value = not True
    return a.value


@nivs_rt_sequence
def logical_not_bool1():
    a = BooleanValue(False)
    a.value = not False
    return a.value


@nivs_rt_sequence
def logical_not_variables():
    a = BooleanValue(False)
    b = BooleanValue(False)
    a.value = not b.value
    return a.value


@nivs_rt_sequence
def logical_not_rtseq():
    a = BooleanValue(True)
    a.value = not _return_true()
    return a.value


@nivs_rt_sequence
def logical_not_parentheses():
    a = BooleanValue(True)
    a.value = not (True and (BooleanValue(True) and BooleanValue(True)) and False)
    return a.value


@nivs_rt_sequence
def logical_not_unary():
    a = BooleanValue(True)
    a.value = not -1
    return a.value


@nivs_rt_sequence
def logical_not_sequence():
    a = BooleanValue(False)
    a.value = not not not False
    return a.value


# <editor-fold desc=Invalid tests>

@nivs_rt_sequence
def logical_not_invalid_variables():
    return not a.value


@nivs_rt_sequence
def logical_not_None():
    a = BooleanValue(False)
    a.value = not None
    return a.value


@nivs_rt_sequence
def logical_not_invalid_rtseq_call():
    a = BooleanValue(False)
    a.value = not _return_true
    return a.value

# </editor-fold>


run_tests = [
    (logical_not_bool, (), False),
    (logical_not_bool1, (), True),
    (logical_not_variables, (), True),
    (logical_not_parentheses, (), True),
    (logical_not_sequence, (), True),
    (logical_not_sequence, (), True),
    (logical_not_rtseq, (), False),
]

fail_transform_tests = [
    (logical_not_invalid_variables, (), TranslateError),
    (logical_not_None, (), TranslateError),
    (logical_not_invalid_rtseq_call, (), VeristandError),
    (logical_not_simple_numbers, (), TranslateError),
    (logical_not_simple_numbers1, (), TranslateError),
    (logical_not_nivsdatatype_double, (), TranslateError),
    (logical_not_nivsdatatype_double1, (), TranslateError),
    (logical_not_nivsdatatype_int32, (), TranslateError),
    (logical_not_nivsdatatype_int64, (), TranslateError),
    (logical_not_unary, (), TranslateError),
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


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
