import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import ChannelReference, DoubleValue, I32Value, RealTimeSequence
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
def exp_simple_numbers():
    a = DoubleValue(0)
    a.value = 2 ** 2
    return a.value


@nivs_rt_sequence
def exp_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 2 ** DoubleValue(2)
    return a.value


@nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(2) ** DoubleValue(3)
    return a.value


@nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(2) ** I32Value(3)
    return a.value


@nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype2():
    a = DoubleValue(0)
    a.value = I32Value(2) ** DoubleValue(3)
    return a.value


@nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype3():
    a = I32Value(0)
    a.value = I32Value(2) ** I32Value(3)
    return a.value


@nivs_rt_sequence
def exp_use_rtseq():
    a = DoubleValue(0)
    a.value = 2 ** _return_constant()
    return a.value


@nivs_rt_sequence
def exp_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() ** 2
    return a.value


@nivs_rt_sequence
def exp_use_rtseq2():
    a = DoubleValue(0)
    a.value = DoubleValue(2) ** _return_constant()
    return a.value


@nivs_rt_sequence
def exp_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() ** DoubleValue(2)
    return a.value


@nivs_rt_sequence
def exp_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(2) ** _return_constant()
    return a.value


@nivs_rt_sequence
def exp_use_rtseq5():
    a = DoubleValue(0)
    a.value = _return_constant() ** I32Value(3)
    return a.value


@nivs_rt_sequence
def exp_with_parentheses():
    a = DoubleValue(0)
    a.value = 2 ** (2 + 3)
    return a.value


@nivs_rt_sequence
def exp_with_parentheses1():
    a = DoubleValue(1)
    a.value = 2 ** (DoubleValue(2) ** I32Value(2))
    return a.value


@nivs_rt_sequence
def exp_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) * (I32Value(2) ** 3.0) ** DoubleValue(2)
    return a.value


@nivs_rt_sequence
def exp_variables():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 2 ** a
    return b.value


@nivs_rt_sequence
def exp_variables1():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 2 ** a.value
    return b.value


@nivs_rt_sequence
def exp_variable_variable():
    a = DoubleValue(2)
    b = DoubleValue(3)
    c = DoubleValue(0)
    c.value = a.value ** b.value
    return c.value


@nivs_rt_sequence
def exp_variable_variable1():
    a = DoubleValue(2)
    b = I32Value(3)
    c = DoubleValue(0)
    c.value = a.value ** b.value
    return c.value


@nivs_rt_sequence
def exp_variable_rtseq():
    a = DoubleValue(2)
    b = DoubleValue(0)
    b.value = a.value ** _return_constant()
    return b.value


@nivs_rt_sequence
def exp_variable_rtseq1():
    a = DoubleValue(2)
    b = DoubleValue(0)
    b.value = _return_constant() ** a.value
    return b.value


@nivs_rt_sequence
def exp_with_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 2 ** b.value
    return a.value


@nivs_rt_sequence
def exp_binary_unary():
    a = DoubleValue(0)
    a.value = 2 ** -1
    return a.value


@nivs_rt_sequence
def exp_complex_expr():
    a = DoubleValue(0)
    a.value = 3 ** (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>

@nivs_rt_sequence
def aug_exp_simple_numbers():
    a = DoubleValue(2)
    a.value **= 2
    return a.value


@nivs_rt_sequence
def aug_exp_num_nivsdatatype():
    a = DoubleValue(3)
    a.value **= DoubleValue(2)
    return a.value


@nivs_rt_sequence
def aug_exp_use_rtseq():
    a = DoubleValue(2)
    a.value **= _return_constant()
    return a.value


@nivs_rt_sequence
def aug_exp_with_parentheses():
    a = DoubleValue(2)
    a.value **= (I32Value(2) ** 3.0) ** DoubleValue(2)
    return a.value


@nivs_rt_sequence
def aug_exp_variables():
    a = DoubleValue(5)
    b = DoubleValue(2)
    b.value **= a.value
    return b.value


@nivs_rt_sequence
def aug_exp_to_channel_ref():
    a = DoubleValue(2)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value **= b.value
    return a.value


@nivs_rt_sequence
def aug_exp_unary():
    a = DoubleValue(2)
    a.value **= -1
    return a.value


# </editor-fold>

# <editor-fold desc=Invalid tests>

@nivs_rt_sequence
def exp_invalid_variables():
    return a ** b


@nivs_rt_sequence
def exp_invalid_variables1():
    return a.value ** b.value


@nivs_rt_sequence
def exp_with_None():
    a = DoubleValue(0)
    a.value = None ** 1
    return a


@nivs_rt_sequence
def exp_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant ** 1
    return a

# </editor-fold>


run_tests = [
    (exp_simple_numbers, (), 4),
    (exp_num_nivsdatatype, (), 4),
    (exp_nivsdatatype_nivsdatatype, (), 8),
    (exp_nivsdatatype_nivsdatatype1, (), 8),
    (exp_nivsdatatype_nivsdatatype2, (), 8),
    (exp_nivsdatatype_nivsdatatype3, (), 8),
    (exp_with_parentheses, (), 32),
    (exp_with_parentheses1, (), 16),
    (exp_with_parentheses2, (), 64),
    (exp_variables, (), 32),
    (exp_variables1, (), 32),
    (exp_variable_variable, (), 8),
    (exp_variable_variable1, (), 8),
    (exp_binary_unary, (), 0.5),
    (aug_exp_simple_numbers, (), 4),
    (aug_exp_variables, (), 32),
    (aug_exp_num_nivsdatatype, (), 9),
    (aug_exp_with_parentheses, (), float(2 ** 64)),
    (aug_exp_unary, (), 0.5),
    (exp_complex_expr, (), 9),
    (exp_variable_rtseq, (), 32),
    (exp_variable_rtseq1, (), 25),
    (exp_use_rtseq, (), 32),
    (exp_use_rtseq1, (), 25),
    (exp_use_rtseq2, (), 32),
    (exp_use_rtseq3, (), 25),
    (exp_use_rtseq4, (), 32),
    (exp_use_rtseq5, (), 125),
    (aug_exp_use_rtseq, (), 32),
    (exp_with_channel_ref, (), 32),
    (aug_exp_to_channel_ref, (), 32),
]

fail_transform_tests = [
    (exp_invalid_variables, (), TranslateError),
    (exp_invalid_variables1, (), TranslateError),
    (exp_with_None, (), TranslateError),
    (exp_invalid_rtseq_call, (), VeristandError),
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
