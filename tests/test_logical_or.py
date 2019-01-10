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
def logical_or_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 or 2
    return a.value


@nivs_rt_sequence
def logical_or_nivsdatatype_double():
    a = BooleanValue(0)
    a = DoubleValue(3) or DoubleValue(0)
    return a.value


@nivs_rt_sequence
def logical_or_nivsdatatype_int32():
    a = BooleanValue(0)
    a = I32Value(2) or I32Value(0)
    return a.value


@nivs_rt_sequence
def logical_or_nivsdatatype_int64():
    a = BooleanValue(0)
    a = I64Value(2) or I64Value(0)
    return a.value


@nivs_rt_sequence
def logical_or_nivsdatatype_bool():
    a = BooleanValue(True)
    a.value = True or False
    return a.value


@nivs_rt_sequence
def logical_or_multiple_types():
    a = BooleanValue(False)
    a.value = True or I32Value(2) or DoubleValue(3) or True
    return a.value


@nivs_rt_sequence
def logical_or_multiple_types1():
    a = BooleanValue(False)
    a.value = True or BooleanValue(False) or False
    return a.value


@nivs_rt_sequence
def logical_or_variables_redefined():
    a = BooleanValue(False)
    b = BooleanValue(True)
    c = BooleanValue(False)
    a = b or c
    return a.value


@nivs_rt_sequence
def logical_or_variables1():
    a = BooleanValue(True)
    b = BooleanValue(True)
    c = BooleanValue(False)
    a.value = b.value or c.value
    return a.value


@nivs_rt_sequence
def logical_or_rtseq():
    a = BooleanValue(False)
    a.value = _return_true() or True
    return a.value


@nivs_rt_sequence
def logical_or_rtseq1():
    a = BooleanValue(False)
    a.value = True or _return_true()
    return a.value


@nivs_rt_sequence
def logical_or_parentheses():
    a = BooleanValue(True)
    a.value = True or (BooleanValue(False) or BooleanValue(True)) or False
    return a.value


@nivs_rt_sequence
def logical_or_unary():
    a = BooleanValue(True)
    a.value = 1 or -2
    return a.value


# <editor-fold desc=Invalid tests>

@nivs_rt_sequence
def logical_or_invalid_variables():
    return a.value or b


@nivs_rt_sequence
def logical_or_invalid_variables1():
    return a.value or b.value


@nivs_rt_sequence
def logical_or_None():
    a = BooleanValue(True)
    a.value = True or None
    return a.value


@nivs_rt_sequence
def logical_or_invalid_rtseq_call():
    a = BooleanValue(False)
    a.value = True or _return_true
    return a.value

# </editor-fold>


run_tests = [
    (logical_or_nivsdatatype_bool, (), True),
    (logical_or_multiple_types1, (), True),
    (logical_or_variables1, (), True),
    (logical_or_parentheses, (), True),
    (logical_or_rtseq, (), True),
    (logical_or_rtseq1, (), True),
]

fail_transform_tests = [
    (logical_or_simple_numbers, (), TranslateError),
    (logical_or_multiple_types, (), TranslateError),
    (logical_or_invalid_variables, (), TranslateError),
    (logical_or_invalid_variables1, (), TranslateError),
    (logical_or_None, (), TranslateError),
    (logical_or_invalid_rtseq_call, (), VeristandError),
    (logical_or_unary, (), TranslateError),
    (logical_or_nivsdatatype_double, (), TranslateError),
    (logical_or_nivsdatatype_int32, (), TranslateError),
    (logical_or_nivsdatatype_int64, (), TranslateError),
    (logical_or_variables_redefined, (), TranslateError),
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
