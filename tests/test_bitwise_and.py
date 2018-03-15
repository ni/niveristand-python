import sys

from niveristand import _decorators, RealTimeSequence, TranslateError, VeristandError
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value, I64Value
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@_decorators.nivs_rt_sequence
def return_constant():
    a = I32Value(5)
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 & 3
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 1 & DoubleValue(3)
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1) & DoubleValue(3)
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) & I32Value(3)
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = BooleanValue(1) & BooleanValue(3)
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(1) & I32Value(3)
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_multiple_types():
    a = I32Value(0)
    a.value = 1 & I32Value(3) & 5
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_multiple_types1():
    a = I64Value(1)
    a.value = 1 & I64Value(5) & 3 & I32Value(7)
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_use_rtseq():
    a = DoubleValue(0)
    a.value = 1 & return_constant()
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_use_rtseq1():
    a = DoubleValue(0)
    a.value = return_constant() & 1
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_use_rtseq2():
    a = DoubleValue(0)
    a.value = I32Value(1) & return_constant()
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_use_rtseq3():
    a = DoubleValue(0)
    a.value = return_constant() & I32Value(1)
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_with_parantheses():
    a = I32Value(0)
    a.value = 1 & (5 & 3)
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_with_parantheses1():
    a = DoubleValue(0)
    a.value = 1 & (DoubleValue(3) & I32Value(5))
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_with_parantheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) & (I32Value(2) & 3.0) & DoubleValue(4)
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_variables():
    a = I32Value(5)
    b = I32Value(0)
    b.value = 1 & a
    return b.value


@_decorators.nivs_rt_sequence
def bitwise_and_variables1():
    a = I64Value(5)
    b = I64Value(0)
    b.value = 1 & a.value
    return b.value


@_decorators.nivs_rt_sequence
def bitwise_and_variable_variable():
    a = I32Value(1)
    b = I64Value(3)
    c = I32Value(0)
    c.value = a.value & b.value
    return c.value


@_decorators.nivs_rt_sequence
def bitwise_and_variable_variable1():
    a = I32Value(1)
    b = I64Value(3)
    c = DoubleValue(0)
    c.value = a.value & b.value
    return c.value


@_decorators.nivs_rt_sequence
def bitwise_and_variable_rtseq():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = a.value & return_constant()
    return b.value


@_decorators.nivs_rt_sequence
def bitwise_and_variable_rtseq1():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = return_constant() & a.value
    return b.value


@_decorators.nivs_rt_sequence
def bitwise_and_to_channelref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 & b.value
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_binary_unary():
    a = I32Value(0)
    a.value = 3 & - 1
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_complex_expr():
    a = DoubleValue(0)
    a.value = 1 & (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>

@_decorators.nivs_rt_sequence
def aug_bitwise_and_simple_numbers():
    a = I32Value(7)
    a.value &= 3
    return a.value


@_decorators.nivs_rt_sequence
def aug_bitwise_and_num_nivsdatatype():
    a = I32Value(1)
    a.value &= I32Value(3)
    return a.value


@_decorators.nivs_rt_sequence
def aug_bitwise_and_use_rtseq():
    a = I32Value(1)
    a.value &= return_constant()
    return a.value


@_decorators.nivs_rt_sequence
def aug_bitwise_and_with_parantheses():
    a = I32Value(7)
    a.value &= 1 & (5 & 3)
    return a.value


@_decorators.nivs_rt_sequence
def aug_bitwise_and_variables():
    a = I32Value(7)
    b = I32Value(3)
    b.value &= a.value
    return b.value


@_decorators.nivs_rt_sequence
def aug_bitwise_and_to_channelref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value &= b.value
    return a.value


@_decorators.nivs_rt_sequence
def aug_bitwise_and_unary():
    a = I32Value(3)
    a.value &= -1
    return a.value


# </editor-fold>

# <editor-fold desc=Invalid tests>

@_decorators.nivs_rt_sequence
def bitwise_and_invalid_variables():
    return a.value & b


@_decorators.nivs_rt_sequence
def bitwise_and_invalid_variables1():
    return a.value & b.value


@_decorators.nivs_rt_sequence
def bitwise_and_to_None():
    a = DoubleValue(0)
    a.value = None & 1
    return a.value


@_decorators.nivs_rt_sequence
def bitwise_and_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = return_constant & 1
    return a.value

# </editor-fold>


run_tests = [
    (return_constant, (), 5.0),
    (bitwise_and_simple_numbers, (), 1),
    (bitwise_and_nivsdatatype_nivsdatatype3, (), 1),
    (bitwise_and_variables, (), 1),
    (bitwise_and_variables1, (), 1),
    (bitwise_and_multiple_types, (), 1),
    (bitwise_and_multiple_types1, (), 1),
    (bitwise_and_with_parantheses, (), 1),
    (bitwise_and_variable_variable, (), 1),
    (bitwise_and_variable_variable1, (), 1),
    (bitwise_and_binary_unary, (), 3),
    (aug_bitwise_and_simple_numbers, (), 3),
    (aug_bitwise_and_variables, (), 3),
    (aug_bitwise_and_num_nivsdatatype, (), 1),
    (aug_bitwise_and_with_parantheses, (), 1),
    (aug_bitwise_and_unary, (), 3),
    (bitwise_and_complex_expr, (), 0),
    (bitwise_and_use_rtseq, (), 1),
    (bitwise_and_use_rtseq1, (), 1),
    (bitwise_and_use_rtseq2, (), 1),
    (bitwise_and_use_rtseq3, (), 1),
    (bitwise_and_variable_rtseq, (), 1),
    (bitwise_and_variable_rtseq1, (), 1),
    (aug_bitwise_and_use_rtseq, (), 1),
    (bitwise_and_num_nivsdatatype, (), 1.0),
    (bitwise_and_nivsdatatype_nivsdatatype, (), 1.0),
    (bitwise_and_nivsdatatype_nivsdatatype1, (), 1.0),
    (bitwise_and_nivsdatatype_nivsdatatype2, (), True),
    (bitwise_and_with_parantheses1, (), 1.0),
    (bitwise_and_with_parantheses2, (), 0.0),
    (bitwise_and_to_channelref, (), 1.0),
    (aug_bitwise_and_to_channelref, (), 1.0),
]

skip_tests = [
]

fail_transform_tests = [
    (bitwise_and_invalid_variables, (), TranslateError),
    (bitwise_and_invalid_variables1, (), TranslateError),
    (bitwise_and_to_None, (), TranslateError),
    (bitwise_and_invalid_rtseq_call, (), VeristandError),
]

py_only_errs = [
    (bitwise_and_num_nivsdatatype, (), 1.0),  # cannot do bitwise and on float
    (bitwise_and_nivsdatatype_nivsdatatype, (), 1.0),  # cannot do bitwise and on float
    (bitwise_and_nivsdatatype_nivsdatatype1, (), 1.0),  # cannot do bitwise and on float
    (bitwise_and_nivsdatatype_nivsdatatype2, (), True),  # cannot do bitwise and on Boolean
    (bitwise_and_with_parantheses1, (), 1.0),  # cannot do bitwise and on float
    (bitwise_and_with_parantheses2, (), 0.0),  # cannot do bitwise and on float
    (bitwise_and_to_channelref, (), 1.0),  # cannot do bitwise and on float
    (aug_bitwise_and_to_channelref, (), 1.0),  # cannot do bitwise and on float
]


def idfunc(val):
    return val.__name__


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


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
