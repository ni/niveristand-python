import sys

from niveristand import decorators, RealTimeSequence
from niveristand import realtimesequencetools
from niveristand.clientapi.datatypes import BooleanValue, DoubleValue, I32Value, I64Value
from niveristand.exceptions import TranslateError
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@decorators.nivs_rt_sequence
def return_true():
    a = BooleanValue(True)
    return a.value


@decorators.nivs_rt_sequence
def logical_or_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 or 2
    return a.value


@decorators.nivs_rt_sequence
def logical_or_nivsdatatype_double():
    a = DoubleValue(0)
    a = DoubleValue(3) or DoubleValue(1)
    return a.value


@decorators.nivs_rt_sequence
def logical_or_nivsdatatype_int32():
    a = I32Value(0)
    a = I32Value(2) or I32Value(1)
    return a.value


@decorators.nivs_rt_sequence
def logical_or_nivsdatatype_int64():
    a = I64Value(0)
    a = I64Value(2) or I64Value(1)
    return a.value


@decorators.nivs_rt_sequence
def logical_or_nivsdatatype_bool():
    a = BooleanValue(True)
    a.value = True or False
    return a.value


@decorators.nivs_rt_sequence
def logical_or_multiple_types():
    a = BooleanValue(False)
    a.value = True or I32Value(2) or DoubleValue(3) or True
    return a.value


@decorators.nivs_rt_sequence
def logical_or_variables():
    a = BooleanValue(True)
    b = BooleanValue(True)
    c = BooleanValue(False)
    a = b or c
    return a.value


@decorators.nivs_rt_sequence
def logical_or_variables1():
    a = BooleanValue(True)
    b = BooleanValue(True)
    c = BooleanValue(False)
    a.value = b.value or c.value
    return a.value


@decorators.nivs_rt_sequence
def logical_or_rtseq():
    a = BooleanValue(False)
    a.value = return_true() or True
    return a.value


@decorators.nivs_rt_sequence
def logical_or_rtseq1():
    a = BooleanValue(False)
    a.value = True or return_true()
    return a.value


@decorators.nivs_rt_sequence
def logical_or_parantheses():
    a = BooleanValue(True)
    a.value = True or (DoubleValue(2) or I32Value(3)) or False
    return a.value


@decorators.nivs_rt_sequence
def logical_or_unary():
    a = BooleanValue(True)
    a.value = 1 or -2
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def logical_or_invalid_variables():
    return a.value or b


@decorators.nivs_rt_sequence
def logical_or_invalid_variables1():
    return a.value or b.value


@decorators.nivs_rt_sequence
def logical_or_None():
    a = BooleanValue(True)
    a.value = True or None
    return a.value


@decorators.nivs_rt_sequence
def logical_or_invalid_rtseq_call():
    a = BooleanValue(False)
    a.value = True or return_true
    return a.value


# endregion


run_tests = [
    (return_true, (), True),
    (logical_or_simple_numbers, (), 1),
    (logical_or_nivsdatatype_bool, (), True),
    (logical_or_multiple_types, (), True),
    (logical_or_variables1, (), True),
    (logical_or_unary, (), True),
    (logical_or_parantheses, (), True),
    (logical_or_rtseq, (), True),
    (logical_or_rtseq1, (), True),
]

skip_tests = [
    (logical_or_nivsdatatype_double, (), "Or between two constant DataTypes returns a DataType object, we have to"
                                         "research this how to solve it. A solution is to always use variables in"
                                         "logical operators, and use var.value."),
    (logical_or_nivsdatatype_int32, (), "Or between two constant DataTypes returns a DataType object, we have to"
                                        "research this how to solve it. A solution is to always use variables in"
                                        "logical operators, and use var.value."),
    (logical_or_nivsdatatype_int64, (), "Or between two constant DataTypes returns a DataType object, we have to"
                                        "research this how to solve it. A solution is to always use variables in"
                                        "logical operators, and use var.value."),
    (logical_or_variables, (), "Or between two constant DataTypes returns a DataType object, we have to"
                               "research this how to solve it. A solution is to always use variables in"
                               "logical operators, and use var.value."),
    (logical_or_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (logical_or_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
]

fail_transform_tests = [
    (logical_or_invalid_variables, (), TranslateError),
    (logical_or_invalid_variables1, (), TranslateError),
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


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
