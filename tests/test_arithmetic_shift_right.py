import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value, I64Value, RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = I32Value(5)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_simple_numbers():
    a = DoubleValue(0)
    a.value = 3 >> 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 3 >> DoubleValue(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(3) >> DoubleValue(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(3) >> I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = BooleanValue(3) >> BooleanValue(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(3) >> I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_multiple_types():
    a = I32Value(0)
    a.value = 15 >> I32Value(3) >> 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_multiple_types1():
    a = I64Value(0)
    a.value = 127 >> I64Value(2) >> 3 >> I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq():
    a = DoubleValue(1)
    a.value = 64 >> _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() >> 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq2():
    a = DoubleValue(0)
    a.value = I32Value(64) >> _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() >> I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(64) >> _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq5():
    a = DoubleValue(0)
    a.value = _return_constant() >> I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_with_parentheses():
    a = I32Value(0)
    a.value = 1 >> (2 >> 1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_with_parentheses1():
    a = DoubleValue(0)
    a.value = 1 >> (DoubleValue(2) >> I32Value(1))
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) >> (I32Value(2) >> 1.0) >> DoubleValue(4)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_variables():
    a = I32Value(5)
    b = I32Value(0)
    b.value = 128 >> a
    return b.value


@nivs_rt_sequence
def arithmetic_shift_right_variables1():
    a = I64Value(5)
    b = I64Value(0)
    b.value = 128 >> a.value
    return b.value


@nivs_rt_sequence
def arithmetic_shift_right_variable_variable():
    a = I32Value(3)
    b = I64Value(1)
    c = I32Value(0)
    c.value = a.value >> b.value
    return c.value


@nivs_rt_sequence
def arithmetic_shift_right_variable_variable1():
    a = I32Value(3)
    b = I64Value(1)
    c = DoubleValue(0)
    c.value = a.value >> b.value
    return c.value


@nivs_rt_sequence
def arithmetic_shift_right_variable_rtseq():
    a = I32Value(64)
    b = DoubleValue(0)
    b.value = a.value >> _return_constant()
    return b.value


@nivs_rt_sequence
def arithmetic_shift_right_variable_rtseq1():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = _return_constant() >> a.value
    return b.value


@nivs_rt_sequence
def arithmetic_shift_right_to_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 >> b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_binary_unary():
    a = I32Value(0)
    a.value = 3 >> -1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_number():
    a = I32Value(2)
    a.value >>= 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype():
    a = I32Value(2)
    a.value >>= I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype1():
    a = I64Value(2)
    a.value >>= I64Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype2():
    a = I64Value(2)
    a.value >>= I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype3():
    a = I32Value(2)
    a.value >>= I64Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype4():
    a = I32Value(2)
    a.value >>= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_variable():
    a = I32Value(2)
    b = I32Value(1)
    a.value >>= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_variable1():
    a = I64Value(2)
    b = I64Value(1)
    a.value >>= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_variable2():
    a = I32Value(2)
    b = I64Value(1)
    a.value >>= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_variable3():
    a = I64Value(2)
    b = I32Value(1)
    a.value >>= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_variable4():
    a = I32Value(2)
    b = DoubleValue(1)
    a.value >>= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_rtseq():
    a = I32Value(32987)
    a.value >>= _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_parentheses():
    a = I32Value(1024)
    a.value >>= (2 + I32Value(1)) + I64Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_channel_ref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value >>= b.value
    return a.value


# <editor-fold desc=Invalid tests>
@nivs_rt_sequence
def arithmetic_shift_right_invalid_variables():
    return a.value >> b


@nivs_rt_sequence
def arithmetic_shift_right_invalid_variables1():
    return a.value >> b.value


@nivs_rt_sequence
def arithmetic_shift_right_to_None():
    a = DoubleValue(0)
    a.value = None >> 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant >> 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_complex_expr():
    a = DoubleValue(0)
    a.value = 15 >> (2 if 2 < 3 else 4)
    return a.value

# </editor-fold>


run_tests = [
    (arithmetic_shift_right_simple_numbers, (), 1),
    (arithmetic_shift_right_nivsdatatype_nivsdatatype1, (), 1),
    (arithmetic_shift_right_nivsdatatype_nivsdatatype3, (), 1),
    (arithmetic_shift_right_variables, (), 4),
    (arithmetic_shift_right_variables1, (), 4),
    (arithmetic_shift_right_multiple_types, (), 0),
    (arithmetic_shift_right_multiple_types1, (), 1),
    (arithmetic_shift_right_with_parentheses, (), 0),
    (arithmetic_shift_right_variable_variable, (), 1),
    (arithmetic_shift_right_variable_variable1, (), 1),
    (arithmetic_shift_right_augassign_number, (), 1),
    (arithmetic_shift_right_augassign_nivsdatatype, (), 1),
    (arithmetic_shift_right_augassign_nivsdatatype1, (), 1),
    (arithmetic_shift_right_augassign_nivsdatatype2, (), 1),
    (arithmetic_shift_right_augassign_nivsdatatype3, (), 1),
    (arithmetic_shift_right_augassign_variable, (), 1),
    (arithmetic_shift_right_augassign_variable1, (), 1),
    (arithmetic_shift_right_augassign_variable2, (), 1),
    (arithmetic_shift_right_augassign_variable3, (), 1),
    (arithmetic_shift_left_augassign_parentheses, (), 64),
    (arithmetic_shift_right_use_rtseq, (), 2),
    (arithmetic_shift_right_use_rtseq1, (), 2),
    (arithmetic_shift_right_use_rtseq2, (), 2),
    (arithmetic_shift_right_use_rtseq3, (), 2),
    (arithmetic_shift_right_use_rtseq4, (), 2),
    (arithmetic_shift_right_use_rtseq5, (), 2),
    (arithmetic_shift_right_variable_rtseq, (), 2),
    (arithmetic_shift_right_variable_rtseq1, (), 2),
    (arithmetic_shift_right_complex_expr, (), 3),
    (arithmetic_shift_right_augassign_rtseq, (), 1030),
]

fail_transform_tests = [
    (arithmetic_shift_right_invalid_variables, (), TranslateError),
    (arithmetic_shift_right_invalid_variables1, (), TranslateError),
    (arithmetic_shift_right_num_nivsdatatype, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_nivsdatatype_nivsdatatype, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_nivsdatatype_nivsdatatype2, (), VeristandError),  # cannot do shift right on Boolean
    (arithmetic_shift_right_with_parentheses1, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_with_parentheses2, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_augassign_nivsdatatype4, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_augassign_variable4, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_to_channel_ref, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_augassign_channel_ref, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_to_None, (), TranslateError),
    (arithmetic_shift_right_invalid_rtseq_call, (), VeristandError),
    (arithmetic_shift_right_binary_unary, (), TranslateError),
]

py_only_errs = [
    (arithmetic_shift_right_nivsdatatype_nivsdatatype1, (), 1),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", list(set(run_tests) - set(py_only_errs)), ids=idfunc)
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
