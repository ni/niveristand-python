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
def equal_bool_builtins():
    a = BooleanValue(False)
    a.value = True == True  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def equal_bool_builtins1():
    a = BooleanValue(False)
    a.value = False == False  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def equal_bool_builtins2():
    a = BooleanValue(False)
    a.value = False == a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def equal_bool_builtins3():
    a = BooleanValue(False)
    a.value = True == a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def equal_simple_numbers():
    a = BooleanValue(False)
    a.value = 1 == 1
    return a.value


@nivs_rt_sequence
def equal_num_nivsdatatype():
    a = BooleanValue(True)
    a.value = 1 == DoubleValue(2)
    return a.value


@nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype():
    a = BooleanValue(False)
    a.value = DoubleValue(1) == DoubleValue(1)
    return a.value


@nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype1():
    a = BooleanValue(0)
    a.value = DoubleValue(1) == I32Value(1)
    return a.value


@nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = I32Value(1) == DoubleValue(1)
    return a.value


@nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype3():
    a = BooleanValue(0)
    a.value = I32Value(1) == I32Value(2)
    return a.value


@nivs_rt_sequence
def equal_multiple_types():
    a = BooleanValue(0)
    a.value = 1 == DoubleValue(1) == 1.0
    return a.value


@nivs_rt_sequence
def equal_multiple_types1():
    a = BooleanValue(0)
    a.value = 1 == I32Value(2) == 3.0 == DoubleValue(4)
    return a.value


@nivs_rt_sequence
def equal_use_rtseq():
    a = BooleanValue(0)
    a.value = 5 == _return_constant()
    return a.value


@nivs_rt_sequence
def equal_use_rtseq1():
    a = BooleanValue(0)
    a.value = _return_constant() == 5
    return a.value


@nivs_rt_sequence
def equal_use_rtseq2():
    a = BooleanValue(0)
    a.value = DoubleValue(5) == _return_constant()
    return a.value


@nivs_rt_sequence
def equal_use_rtseq3():
    a = BooleanValue(0)
    a.value = _return_constant() == DoubleValue(5)
    return a.value


@nivs_rt_sequence
def equal_use_rtseq4():
    a = BooleanValue(0)
    a.value = I32Value(5) == _return_constant()
    return a.value


@nivs_rt_sequence
def equal_use_rtseq5():
    a = BooleanValue(0)
    a.value = _return_constant() == I32Value(5)
    return a.value


@nivs_rt_sequence
def equal_with_parentheses():
    a = BooleanValue(True)
    a.value = 1 == (2 == 3)
    return a.value


@nivs_rt_sequence
def equal_with_parentheses1():
    a = BooleanValue(True)
    a.value = 1 == (DoubleValue(2) == I32Value(5))
    return a.value


@nivs_rt_sequence
def equal_with_parentheses2():
    a = BooleanValue(True)
    a.value = DoubleValue(1) == (I32Value(2) == 3.0) == DoubleValue(4)
    return a.value


@nivs_rt_sequence
def equal_variables():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = 1 == a
    return b.value


@nivs_rt_sequence
def equal_variables1():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = 1 == a.value
    return b.value


@nivs_rt_sequence
def equal_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = BooleanValue(True)
    c.value = a.value == b.value
    return c.value


@nivs_rt_sequence
def equal_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a.value == b.value
    return c.value


@nivs_rt_sequence
def equal_variable_variable2():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a == b
    return c.value


@nivs_rt_sequence
def equal_variable_rtseq():
    a = DoubleValue(5)
    b = BooleanValue(0)
    b.value = a.value == _return_constant()
    return b.value


@nivs_rt_sequence
def equal_variable_rtseq1():
    a = DoubleValue(5)
    b = BooleanValue(0)
    b.value = _return_constant() == a.value
    return b.value


@nivs_rt_sequence
def equal_to_channel_ref():
    a = BooleanValue(True)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 == b.value
    return a.value


@nivs_rt_sequence
def equal_binary_unary():
    a = BooleanValue(0)
    a.value = -1 == - 1
    return a.value


@nivs_rt_sequence
def equal_with_multiple_comparators():
    a = BooleanValue(True)
    a.value = 1 == 2 == 3 == 4
    return a.value


@nivs_rt_sequence
def equal_complex_expr():
    a = BooleanValue(0)
    a.value = 1 == (1 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Invalid tests>

@nivs_rt_sequence
def equal_invalid_variables():
    return a.value == b


@nivs_rt_sequence
def equal_invalid_variables1():
    return a.value == b.value


@nivs_rt_sequence
def equal_to_None():
    a = BooleanValue(0)
    a.value = None == 1  # noqa: E711 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def equal_invalid_rtseq_call():
    a = BooleanValue(0)
    a.value = _return_constant == 1
    return a.value

# </editor-fold>


run_tests = [
    (equal_bool_builtins, (), True),
    (equal_bool_builtins1, (), True),
    (equal_bool_builtins2, (), True),
    (equal_bool_builtins3, (), False),
    (equal_simple_numbers, (), True),
    (equal_num_nivsdatatype, (), False),
    (equal_nivsdatatype_nivsdatatype, (), True),
    (equal_nivsdatatype_nivsdatatype1, (), True),
    (equal_nivsdatatype_nivsdatatype2, (), True),
    (equal_nivsdatatype_nivsdatatype3, (), False),
    (equal_with_parentheses, (), False),
    (equal_with_parentheses1, (), False),
    (equal_variables, (), True),
    (equal_variables1, (), True),
    (equal_variable_variable, (), False),
    (equal_variable_variable1, (), True),
    (equal_variable_variable2, (), True),
    (equal_binary_unary, (), True),
    (equal_complex_expr, (), True),
    (equal_use_rtseq, (), True),
    (equal_use_rtseq1, (), True),
    (equal_use_rtseq2, (), True),
    (equal_use_rtseq3, (), True),
    (equal_use_rtseq4, (), True),
    (equal_use_rtseq5, (), True),
    (equal_variable_rtseq, (), True),
    (equal_variable_rtseq1, (), True),
    (equal_to_channel_ref, (), False),
]

fail_transform_tests = [
    (equal_invalid_variables, (), TranslateError),
    (equal_invalid_variables1, (), TranslateError),
    (equal_to_None, (), TranslateError),
    (equal_invalid_rtseq_call, (), VeristandError),
    (equal_multiple_types, (), TranslateError),
    (equal_multiple_types1, (), TranslateError),
    (equal_with_parentheses2, (), TranslateError),
    (equal_with_multiple_comparators, (), TranslateError),
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
