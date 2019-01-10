import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def less_eq_simple_numbers():
    a = BooleanValue(True)
    a.value = 5 <= 1
    return a.value


@nivs_rt_sequence
def less_eq_nivsdatatype_num():
    a = BooleanValue(True)
    a.value = DoubleValue(5) <= 2
    return a.value


@nivs_rt_sequence
def less_eq_num_nivsdatatype():
    a = BooleanValue(True)
    a.value = 5 <= DoubleValue(2)
    return a.value


@nivs_rt_sequence
def less_eq_nivsdatatype_nivsdatatype():
    a = BooleanValue(True)
    a.value = DoubleValue(5) <= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def less_eq_nivsdatatype_nivsdatatype1():
    a = BooleanValue(True)
    a.value = DoubleValue(5) <= I32Value(1)
    return a.value


@nivs_rt_sequence
def less_eq_nivsdatatype_nivsdatatype2():
    a = BooleanValue(True)
    a.value = I32Value(5) <= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def less_eq_nivsdatatype_nivsdatatype3():
    a = BooleanValue(True)
    a.value = I32Value(5) <= I32Value(2)
    return a.value


@nivs_rt_sequence
def less_eq_multiple_types():
    a = BooleanValue(True)
    a.value = DoubleValue(5) <= 2 <= 1.0
    return a.value


@nivs_rt_sequence
def less_eq_multiple_types1():
    a = BooleanValue(True)
    a.value = I32Value(2.0) <= DoubleValue(3) <= 4 <= 5.0
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq():
    a = BooleanValue(True)
    a.value = 6 <= _return_constant()
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq1():
    a = BooleanValue(True)
    a.value = _return_constant() <= 4
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq2():
    a = BooleanValue(True)
    a.value = DoubleValue(6) <= _return_constant()
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq3():
    a = BooleanValue(True)
    a.value = _return_constant() <= DoubleValue(4)
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq4():
    a = BooleanValue(True)
    a.value = I32Value(6) <= _return_constant()
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq5():
    a = BooleanValue(True)
    a.value = _return_constant() <= I32Value(1)
    return a.value


@nivs_rt_sequence
def less_eq_with_parentheses():
    a = BooleanValue(True)
    a.value = 5 <= (3 <= 2)
    return a.value


@nivs_rt_sequence
def less_eq_variables():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = a <= 1
    return b.value


@nivs_rt_sequence
def less_eq_variables1():
    a = DoubleValue(1)
    b = BooleanValue(False)
    b.value = 5 <= a.value
    return b.value


@nivs_rt_sequence
def less_eq_variable_variable():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(False)
    c.value = a.value <= b.value
    return c.value


@nivs_rt_sequence
def less_eq_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(False)
    c.value = a <= b
    return c.value


@nivs_rt_sequence
def less_eq_variable_rtseq():
    a = DoubleValue(6.0)
    b = BooleanValue(False)
    b.value = a.value <= _return_constant()
    return b.value


@nivs_rt_sequence
def less_eq_variable_rtseq1():
    a = DoubleValue(1)
    b = BooleanValue(False)
    b.value = _return_constant() <= a.value
    return b.value


@nivs_rt_sequence
def less_eq_to_channel_ref():
    a = BooleanValue(False)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 <= b.value
    return a.value


@nivs_rt_sequence
def less_eq_binary_unary():
    a = BooleanValue(True)
    a.value = 2 <= - 1
    return a.value


@nivs_rt_sequence
def less_eq_with_multiple_comparators():
    a = BooleanValue(True)
    a.value = 5 <= 4 <= 3 <= 2
    return a.value


@nivs_rt_sequence
def less_eq_complex_expr():
    a = BooleanValue(False)
    a.value = 1 <= (2 if 2 < 3 else 1)
    return a.value


# <editor-fold desc=Invalid tests>

@nivs_rt_sequence
def less_eq_invalid_variables():
    return a.value <= b


@nivs_rt_sequence
def less_eq_invalid_variables1():
    return a.value <= b.value


@nivs_rt_sequence
def less_eq_to_None():
    a = BooleanValue(True)
    a.value = None <= 1
    return a.value


@nivs_rt_sequence
def less_eq_invalid_rtseq_call():
    a = BooleanValue(True)
    a.value = _return_constant <= 1
    return a.value

# </editor-fold>


@nivs_rt_sequence
def lt_equal_simple_numbers():
    a = BooleanValue(True)
    a.value = 1 <= 1
    return a.value


@nivs_rt_sequence
def lt_equal_num_nivsdatatype():
    a = BooleanValue(False)
    a.value = DoubleValue(1) <= 2
    return a.value


@nivs_rt_sequence
def lt_equal_nivsdatatype_nivsdatatype():
    a = BooleanValue(True)
    a.value = DoubleValue(1) <= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def lt_equal_nivsdatatype_nivsdatatype1():
    a = BooleanValue(True)
    a.value = DoubleValue(1) <= I32Value(1)
    return a.value


@nivs_rt_sequence
def lt_equal_nivsdatatype_nivsdatatype2():
    a = BooleanValue(True)
    a.value = I32Value(1) <= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def lt_equal_nivsdatatype_nivsdatatype3():
    a = BooleanValue(True)
    a.value = I32Value(2) <= I32Value(1)
    return a.value


@nivs_rt_sequence
def lt_equal_multiple_types():
    a = BooleanValue(True)
    a.value = DoubleValue(1) <= 1 <= 1.0
    return a.value


@nivs_rt_sequence
def lt_equal_multiple_types1():
    a = BooleanValue(True)
    a.value = I32Value(4) <= DoubleValue(3) <= 2.0 <= 1
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq():
    a = BooleanValue(False)
    a.value = 5 <= _return_constant()
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq1():
    a = BooleanValue(False)
    a.value = _return_constant() <= 5
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq2():
    a = BooleanValue(False)
    a.value = DoubleValue(5) <= _return_constant()
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq3():
    a = BooleanValue(False)
    a.value = _return_constant() <= DoubleValue(5)
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq4():
    a = BooleanValue(False)
    a.value = I32Value(5) <= _return_constant()
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq5():
    a = BooleanValue(True)
    a.value = _return_constant() <= I32Value(1)
    return a.value


@nivs_rt_sequence
def lt_equal_with_parentheses():
    a = BooleanValue(False)
    a.value = 1 <= (2 <= 3)
    return a.value


@nivs_rt_sequence
def lt_equal_with_parentheses1():
    a = BooleanValue(False)
    a.value = 3 <= (DoubleValue(2) <= I32Value(2))
    return a.value


@nivs_rt_sequence
def lt_equal_variables():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = a <= 1
    return b.value


@nivs_rt_sequence
def lt_equal_variables1():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = a.value <= 1
    return b.value


@nivs_rt_sequence
def lt_equal_variable_variable():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(True)
    c.value = a.value <= b.value
    return c.value


@nivs_rt_sequence
def lt_equal_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a.value <= b.value
    return c.value


@nivs_rt_sequence
def lt_equal_variable_variable2():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a <= b
    return c.value


@nivs_rt_sequence
def lt_equal_variable_rtseq():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = a.value <= _return_constant()
    return b.value


@nivs_rt_sequence
def lt_equal_variable_rtseq1():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = _return_constant() <= a.value
    return b.value


@nivs_rt_sequence
def lt_equal_to_channel_ref():
    a = BooleanValue(False)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 1.0
    localhost_wait()
    a.value = 1 <= b.value
    return a.value


@nivs_rt_sequence
def lt_equal_binary_unary():
    a = BooleanValue(True)
    a.value = -1 <= - 1
    return a.value


@nivs_rt_sequence
def lt_equal_with_multiple_comparators():
    a = BooleanValue(False)
    a.value = 4 <= 3 <= 2 <= 1
    return a.value


@nivs_rt_sequence
def lt_equal_complex_expr():
    a = BooleanValue(False)
    a.value = 1 <= (1 if 2 < 3 else 0)
    return a.value


# <editor-fold desc=Invalid tests>

@nivs_rt_sequence
def lt_equal_invalid_variables():
    return a.value <= b


@nivs_rt_sequence
def lt_equal_invalid_variables1():
    return a.value <= b.value


@nivs_rt_sequence
def lt_equal_to_None():
    a = BooleanValue(True)
    a.value = None <= 1  # noqa: E711 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def lt_equal_invalid_rtseq_call():
    a = BooleanValue(True)
    a.value = _return_constant <= 1
    return a.value

# </editor-fold>


run_tests = [
    (less_eq_simple_numbers, (), False),
    (less_eq_nivsdatatype_num, (), False),
    (less_eq_nivsdatatype_nivsdatatype, (), False),
    (less_eq_nivsdatatype_nivsdatatype1, (), False),
    (less_eq_nivsdatatype_nivsdatatype2, (), False),
    (less_eq_nivsdatatype_nivsdatatype3, (), False),
    (less_eq_with_parentheses, (), False),
    (less_eq_variables, (), False),
    (less_eq_variables1, (), False),
    (less_eq_variable_variable, (), False),
    (less_eq_variable_variable1, (), False),
    (less_eq_binary_unary, (), False),
    (less_eq_complex_expr, (), True),
    (lt_equal_simple_numbers, (), True),
    (lt_equal_num_nivsdatatype, (), True),
    (lt_equal_nivsdatatype_nivsdatatype, (), True),
    (lt_equal_nivsdatatype_nivsdatatype1, (), True),
    (lt_equal_nivsdatatype_nivsdatatype2, (), True),
    (lt_equal_nivsdatatype_nivsdatatype3, (), False),
    (lt_equal_with_parentheses, (), True),
    (lt_equal_with_parentheses1, (), False),
    (lt_equal_variables, (), True),
    (lt_equal_variables1, (), True),
    (lt_equal_variable_variable, (), False),
    (lt_equal_variable_variable1, (), True),
    (lt_equal_variable_variable2, (), True),
    (lt_equal_binary_unary, (), True),
    (lt_equal_complex_expr, (), True),
    (less_eq_use_rtseq, (), False),
    (less_eq_use_rtseq1, (), False),
    (less_eq_use_rtseq2, (), False),
    (less_eq_use_rtseq3, (), False),
    (less_eq_use_rtseq4, (), False),
    (less_eq_use_rtseq5, (), False),
    (less_eq_variable_rtseq, (), False),
    (less_eq_variable_rtseq1, (), False),
    (lt_equal_use_rtseq, (), True),
    (lt_equal_use_rtseq1, (), True),
    (lt_equal_use_rtseq2, (), True),
    (lt_equal_use_rtseq3, (), True),
    (lt_equal_use_rtseq4, (), True),
    (lt_equal_use_rtseq5, (), False),
    (lt_equal_variable_rtseq, (), True),
    (lt_equal_variable_rtseq1, (), True),
    (less_eq_to_channel_ref, (), True),
    (lt_equal_to_channel_ref, (), True),
    (less_eq_num_nivsdatatype, (), False),
]

fail_transform_tests = [
    (less_eq_invalid_variables, (), TranslateError),
    (less_eq_invalid_variables1, (), TranslateError),
    (lt_equal_invalid_variables, (), TranslateError),
    (lt_equal_invalid_variables1, (), TranslateError),
    (less_eq_to_None, (), TranslateError),
    (lt_equal_to_None, (), TranslateError),
    (less_eq_invalid_rtseq_call, (), VeristandError),
    (lt_equal_invalid_rtseq_call, (), VeristandError),
    (less_eq_multiple_types, (), TranslateError),
    (less_eq_multiple_types1, (), TranslateError),
    (less_eq_with_multiple_comparators, (), TranslateError),
    (lt_equal_multiple_types, (), TranslateError),
    (lt_equal_multiple_types1, (), TranslateError),
    (lt_equal_with_multiple_comparators, (), TranslateError),
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
