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
def logical_and_simple_numbers():
    a = DoubleValue(0)
    a.value = 2 and 1
    return a.value


@decorators.nivs_rt_sequence
def logical_and_simple_numbers1():
    a = DoubleValue(0)
    a.value = 1 and 2
    return a.value


@decorators.nivs_rt_sequence
def logical_and_nivsdatatype_double():
    a = DoubleValue(0)
    a = DoubleValue(3) and DoubleValue(1)
    return a.value


@decorators.nivs_rt_sequence
def logical_and_nivsdatatype_int32():
    a = I32Value(0)
    a = I32Value(2) and I32Value(1)
    return a.value


@decorators.nivs_rt_sequence
def logical_and_nivsdatatype_int64():
    a = I64Value(0)
    a = I64Value(2) and I64Value(1)
    return a.value


@decorators.nivs_rt_sequence
def logical_and_nivsdatatype_bool():
    a = BooleanValue(True)
    a.value = True and False
    return a.value


@decorators.nivs_rt_sequence
def logical_and_multiple_types():
    a = BooleanValue(False)
    a.value = True and I32Value(2) and DoubleValue(3) and True
    return a.value


@decorators.nivs_rt_sequence
def logical_and_variables():
    a = BooleanValue(True)
    b = BooleanValue(True)
    c = BooleanValue(False)
    a = b and c
    return a.value


@decorators.nivs_rt_sequence
def logical_and_variables1():
    a = BooleanValue(True)
    b = BooleanValue(True)
    c = BooleanValue(False)
    a.value = b.value and c.value
    return a.value


@decorators.nivs_rt_sequence
def logical_and_rtseq():
    a = BooleanValue(False)
    a.value = return_true() and True
    return a.value


@decorators.nivs_rt_sequence
def logical_and_rtseq1():
    a = BooleanValue(False)
    a.value = True and return_true()
    return a.value


@decorators.nivs_rt_sequence
def logical_and_parantheses():
    a = BooleanValue(True)
    a.value = True and (DoubleValue(2) and I32Value(3)) and False
    return a.value


@decorators.nivs_rt_sequence
def logical_and_unary():
    a = BooleanValue(True)
    a.value = -2 and 1
    return a.value


# <editor-fold desc=Invalid tests>

@decorators.nivs_rt_sequence
def logical_and_invalid_variables():
    return a.value and b


@decorators.nivs_rt_sequence
def logical_and_invalid_variables1():
    return a.value and b.value


@decorators.nivs_rt_sequence
def logical_and_None():
    a = BooleanValue(True)
    a.value = True and None
    return a.value


@decorators.nivs_rt_sequence
def logical_and_invalid_rtseq_call():
    a = BooleanValue(False)
    a.value = True and return_true
    return a.value

# </editor-fold>


run_tests = [
    (return_true, (), True),
    (logical_and_simple_numbers, (), 1),
    (logical_and_nivsdatatype_bool, (), False),
    (logical_and_multiple_types, (), True),
    (logical_and_variables1, (), False),
    (logical_and_parantheses, (), False),
    (logical_and_rtseq, (), True),
    (logical_and_rtseq1, (), True),
    (logical_and_unary, (), True),
]

skip_tests = [
    (logical_and_nivsdatatype_double, (), "And between two constant DataTypes returns a DataType object, we have to"
                                          "research this how to solve it. A solution is to always use variables in"
                                          "logical operators, and use var.value."),
    (logical_and_nivsdatatype_int32, (), "And between two constant DataTypes returns a DataType object, we have to"
                                         "research this how to solve it. A solution is to always use variables in"
                                         "logical operators, and use var.value."),
    (logical_and_nivsdatatype_int64, (), "And between two constant DataTypes returns a DataType object, we have to"
                                         "research this how to solve it. A solution is to always use variables in"
                                         "logical operators, and use var.value."),
    (logical_and_simple_numbers1, (), "For 1 && 2 SPE return 1 and Python returns 2. From logical perspective they are"
                                      "equal, but we can't test it only by casting to Boolean. Users should be aware of"
                                      "thi difference when &&-ing numeric types."),
    (logical_and_variables, (), "And between two constant DataTypes returns a DataType object, we have to"
                                "research this how to solve it. A solution is to always use variables in"
                                "logical operators, and use var.value."),
    (logical_and_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
]

fail_transform_tests = [
    (logical_and_invalid_variables, (), TranslateError),
    (logical_and_invalid_variables1, (), TranslateError),
    (logical_and_None, (), TranslateError),
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
