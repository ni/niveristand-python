import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import ChannelReference, DoubleValue, I32Value, I64Value, RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 0
b = 1


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def modulo_simple_numbers():
    a = DoubleValue(0)
    a.value = 3 % 2
    return a.value


@nivs_rt_sequence
def modulo_num_nivsdatatype():
    a = DoubleValue(0)
    b = DoubleValue(2)
    a.value = 3 % b.value
    return a.value


@nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(5) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(5) % I32Value(2)
    return a.value


@nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype2():
    a = DoubleValue(0)
    a.value = I32Value(7) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype3():
    a = I32Value(0)
    a.value = I32Value(7) % I32Value(2)
    return a.value


@nivs_rt_sequence
def modulo_multiple_types():
    a = DoubleValue(0)
    a.value = 7 % DoubleValue(4) % 2
    return a.value


@nivs_rt_sequence
def modulo_multiple_types1():
    a = I32Value(0)
    a.value = 12 % I32Value(7) % 3
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq():
    a = DoubleValue(0)
    a.value = 6 % _return_constant()
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() % 2
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq2():
    a = DoubleValue(0)
    a.value = DoubleValue(7) % _return_constant()
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(7) % _return_constant()
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq5():
    a = DoubleValue(0)
    a.value = _return_constant() % I32Value(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses():
    a = DoubleValue(0)
    a.value = 5 % (5 % 3)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses1():
    a = DoubleValue(1)
    a.value = 5 % (DoubleValue(5) % I32Value(3))
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses2():
    a = DoubleValue(0)
    a.value = I32Value(11) % (I64Value(11) % I64Value(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses3():
    a = DoubleValue(0)
    a.value = I64Value(11) % (I32Value(11) % I32Value(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses4():
    a = DoubleValue(0)
    a.value = I32Value(11) % (I64Value(11) % I32Value(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses5():
    a = DoubleValue(0)
    a.value = I64Value(11) % (I32Value(11) % I64Value(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses6():
    a = DoubleValue(0)
    a.value = I64Value(11) % (I32Value(11) % DoubleValue(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses7():
    a = DoubleValue(0)
    a.value = I32Value(11) % (I64Value(11) % DoubleValue(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_variables():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 7 % a
    return b.value


@nivs_rt_sequence
def modulo_variables1():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 7 % a.value
    return b.value


@nivs_rt_sequence
def modulo_variable_variable():
    a = DoubleValue(5)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value % b.value
    return c.value


@nivs_rt_sequence
def modulo_variable_variable1():
    a = DoubleValue(5)
    b = I32Value(2)
    c = DoubleValue(0)
    c.value = a.value % b.value
    return c.value


@nivs_rt_sequence
def modulo_variable_rtseq():
    a = DoubleValue(6)
    b = DoubleValue(0)
    b.value = a.value % _return_constant()
    return b.value


@nivs_rt_sequence
def modulo_variable_rtseq1():
    a = DoubleValue(2)
    b = DoubleValue(0)
    b.value = _return_constant() % a.value
    return b.value


@nivs_rt_sequence
def modulo_with_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 2.0
    localhost_wait()
    a.value = 3 % b.value
    return a.value


@nivs_rt_sequence
def modulo_binary_unary():
    a = DoubleValue(0)
    a.value = 5 % -2
    return a.value


@nivs_rt_sequence
def modulo_complex_expr():
    a = DoubleValue(0)
    a.value = 1 % (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>

@nivs_rt_sequence
def aug_modulo_simple_numbers():
    a = DoubleValue(1)
    a.value %= 2
    return a.value


@nivs_rt_sequence
def aug_modulo_num_nivsdatatype():
    a = DoubleValue(1)
    a.value %= DoubleValue(2)
    return a.value


@nivs_rt_sequence
def aug_modulo_use_rtseq():
    a = DoubleValue(6)
    a.value %= _return_constant()
    return a.value


@nivs_rt_sequence
def aug_modulo_with_parentheses():
    a = DoubleValue(5)
    a.value %= (I32Value(2) % 3.0) % DoubleValue(4)
    return a.value


@nivs_rt_sequence
def aug_modulo_variables():
    a = DoubleValue(5)
    b = DoubleValue(1)
    b.value %= a.value
    return b.value


@nivs_rt_sequence
def aug_modulo_to_channel_ref():
    a = DoubleValue(3)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 2.0
    localhost_wait()
    a.value %= b.value
    return a.value


@nivs_rt_sequence
def aug_modulo_unary():
    a = DoubleValue(5)
    a.value %= -2
    return a.value


# </editor-fold>

# <editor-fold desc=Invalid tests>

@nivs_rt_sequence
def modulo_invalid_variables():
    return a % b


@nivs_rt_sequence
def modulo_invalid_variables1():
    return a.value % b.value


@nivs_rt_sequence
def modulo_with_None():
    a = DoubleValue(0)
    a.value = None % 1
    return a


@nivs_rt_sequence
def modulo_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant % 1
    return a

# </editor-fold>


run_tests = [
    (modulo_simple_numbers, (), 1),
    (modulo_num_nivsdatatype, (), 1),
    (modulo_nivsdatatype_nivsdatatype, (), 1),
    (modulo_nivsdatatype_nivsdatatype1, (), 1),
    (modulo_nivsdatatype_nivsdatatype2, (), 1),
    (modulo_nivsdatatype_nivsdatatype3, (), 1),
    (modulo_multiple_types, (), 1),
    (modulo_multiple_types1, (), 2),
    (modulo_with_parentheses, (), 1),
    (modulo_with_parentheses1, (), 1),
    (modulo_with_parentheses2, (), 1),
    (modulo_with_parentheses3, (), 1),
    (modulo_with_parentheses4, (), 1),
    (modulo_with_parentheses5, (), 1),
    (modulo_with_parentheses6, (), 1),
    (modulo_with_parentheses7, (), 1),
    (modulo_variables, (), 2),
    (modulo_variables1, (), 2),
    (modulo_variable_variable, (), 1),
    (modulo_variable_variable1, (), 1),
    (aug_modulo_simple_numbers, (), 1),
    (aug_modulo_variables, (), 1),
    (aug_modulo_num_nivsdatatype, (), 1),
    (aug_modulo_with_parentheses, (), 1),
    (modulo_complex_expr, (), 1),
    (modulo_variable_rtseq, (), 1),
    (modulo_variable_rtseq1, (), 1),
    (modulo_use_rtseq, (), 1),
    (modulo_use_rtseq1, (), 1),
    (modulo_use_rtseq2, (), 2),
    (modulo_use_rtseq3, (), 1),
    (modulo_use_rtseq4, (), 2),
    (modulo_use_rtseq5, (), 1),
    (aug_modulo_use_rtseq, (), 1),
    (modulo_with_channel_ref, (), 1),
    (aug_modulo_to_channel_ref, (), 1),
    (modulo_binary_unary, (), 1),
    (aug_modulo_unary, (), 1),
]

py_only_different_behavior_tests = [
    (modulo_binary_unary, (), 1),
    (aug_modulo_unary, (), 1),
]

fail_transform_tests = [
    (modulo_invalid_variables, (), TranslateError),
    (modulo_invalid_variables1, (), TranslateError),
    (modulo_with_None, (), TranslateError),
    (modulo_invalid_rtseq_call, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", list(set(run_tests) -
                                                                    set(py_only_different_behavior_tests)), ids=idfunc)
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
