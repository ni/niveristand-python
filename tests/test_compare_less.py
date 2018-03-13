import sys

from niveristand import decorators, RealTimeSequence
from niveristand import realtimesequencetools
from niveristand.clientapi.datatypes import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.exceptions import TranslateError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@decorators.nivs_rt_sequence
def return_constant():
    a = DoubleValue(5)
    return a.value


@decorators.nivs_rt_sequence
def less_simple_numbers():
    a = BooleanValue(True)
    a.value = 5 < 1
    return a.value


@decorators.nivs_rt_sequence
def less_nivsdatatype_num():
    a = BooleanValue(True)
    a.value = DoubleValue(5) < 2
    return a.value


@decorators.nivs_rt_sequence
def less_num_nivsdatatype():
    a = BooleanValue(True)
    a.value = 5 < DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def less_nivsdatatype_nivsdatatype():
    a = BooleanValue(True)
    a.value = DoubleValue(5) < DoubleValue(1)
    return a.value


@decorators.nivs_rt_sequence
def less_nivsdatatype_nivsdatatype1():
    a = BooleanValue(True)
    a.value = DoubleValue(5) < I32Value(1)
    return a.value


@decorators.nivs_rt_sequence
def less_nivsdatatype_nivsdatatype2():
    a = BooleanValue(True)
    a.value = I32Value(5) < DoubleValue(1)
    return a.value


@decorators.nivs_rt_sequence
def less_nivsdatatype_nivsdatatype3():
    a = BooleanValue(True)
    a.value = I32Value(5) < I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def less_multiple_types():
    a = BooleanValue(True)
    a.value = DoubleValue(5) < 2 < 1.0
    return a.value


@decorators.nivs_rt_sequence
def less_multiple_types1():
    a = BooleanValue(True)
    a.value = I32Value(5) < DoubleValue(4) < 3 < 2.0
    return a.value


@decorators.nivs_rt_sequence
def less_use_rtseq():
    a = BooleanValue(True)
    a.value = 5 < return_constant()
    return a.value


@decorators.nivs_rt_sequence
def less_use_rtseq1():
    a = BooleanValue(True)
    a.value = return_constant() < 4
    return a.value


@decorators.nivs_rt_sequence
def less_use_rtseq2():
    a = BooleanValue(True)
    a.value = DoubleValue(6) < return_constant()
    return a.value


@decorators.nivs_rt_sequence
def less_use_rtseq3():
    a = BooleanValue(True)
    a.value = return_constant() < DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def less_use_rtseq4():
    a = BooleanValue(True)
    a.value = I32Value(6) < return_constant()
    return a.value


@decorators.nivs_rt_sequence
def less_use_rtseq5():
    a = BooleanValue(True)
    a.value = return_constant() < I32Value(6)
    return a.value


@decorators.nivs_rt_sequence
def less_with_parantheses():
    a = BooleanValue(True)
    a.value = 5 < (3 < 2)
    return a.value


@decorators.nivs_rt_sequence
def less_variables():
    a = DoubleValue(5)
    b = BooleanValue(True)
    b.value = a < 1
    return b.value


@decorators.nivs_rt_sequence
def less_variables1():
    a = DoubleValue(1)
    b = BooleanValue(True)
    b.value = 5 < a.value
    return b.value


@decorators.nivs_rt_sequence
def less_variable_variable():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(True)
    c.value = a.value < b.value
    return c.value


@decorators.nivs_rt_sequence
def less_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(True)
    c.value = a < b
    return c.value


@decorators.nivs_rt_sequence
def less_variable_rtseq():
    a = DoubleValue(6.0)
    b = BooleanValue(True)
    b.value = a.value < return_constant()
    return b.value


@decorators.nivs_rt_sequence
def less_variable_rtseq1():
    a = DoubleValue(1)
    b = BooleanValue(True)
    b.value = return_constant() < a.value
    return b.value


@decorators.nivs_rt_sequence
def less_to_channelref():
    a = BooleanValue(False)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 < b.value
    return a.value


@decorators.nivs_rt_sequence
def less_binary_unary():
    a = BooleanValue(True)
    a.value = 2 < - 1
    return a.value


@decorators.nivs_rt_sequence
def less_with_multiple_comparators():
    a = BooleanValue(True)
    a.value = 5 < 4 < 3 < 2
    return a.value


@decorators.nivs_rt_sequence
def less_complex_expr():
    a = BooleanValue(False)
    a.value = 1 < (2 if 2 < 3 else 1)
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def less_invalid_variables():
    return a.value < b


@decorators.nivs_rt_sequence
def less_invalid_variables1():
    return a.value < b.value


@decorators.nivs_rt_sequence
def less_invalid_variables2():
    a = BooleanValue(0)
    b = DoubleValue(0)
    b.value = a.value < 2
    return b


@decorators.nivs_rt_sequence
def less_to_None():
    a = BooleanValue(True)
    a.value = None < 1
    return a.value


@decorators.nivs_rt_sequence
def less_invalid_rtseq_call():
    a = BooleanValue(True)
    a.value = return_constant < 1
    return a.value

# end region


run_tests = [
    (return_constant, (), 5),
    (less_simple_numbers, (), False),
    (less_nivsdatatype_num, (), False),
    (less_nivsdatatype_nivsdatatype, (), False),
    (less_nivsdatatype_nivsdatatype1, (), False),
    (less_nivsdatatype_nivsdatatype2, (), False),
    (less_nivsdatatype_nivsdatatype3, (), False),
    (less_with_parantheses, (), False),
    (less_variables, (), False),
    (less_variables1, (), False),
    (less_variable_variable, (), False),
    (less_variable_variable1, (), False),
    (less_complex_expr, (), True),
    (less_binary_unary, (), False),
    (less_use_rtseq, (), False),
    (less_use_rtseq1, (), False),
    (less_use_rtseq2, (), False),
    (less_use_rtseq3, (), False),
    (less_use_rtseq4, (), False),
    (less_use_rtseq5, (), True),
    (less_variable_rtseq, (), False),
    (less_variable_rtseq1, (), False),
    (less_to_channelref, (), True),
]

skip_tests = [
    (less_num_nivsdatatype, (), "Builtins as the left comparer can't be overriden"),
    (less_to_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (less_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
    (less_multiple_types, (), "Cascading comparators untested in VM"),
    (less_multiple_types1, (), "Cascading comparators untested in VM"),
    (less_with_multiple_comparators, (), "Cascading comparators untested in VM"),
]

fail_transform_tests = [
    (less_invalid_variables, (), TranslateError),
    (less_invalid_variables1, (), TranslateError),
    (less_invalid_variables2, (), TranslateError),
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
