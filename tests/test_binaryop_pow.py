import sys

from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Double, Int32
from niveristand.exceptions import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner
from testutilities.test_channels import TestChannels

a = 0
b = 1


@decorators.nivs_rt_sequence
def return_constant():
    a = Double(5)
    return a.value


@decorators.nivs_rt_sequence
def exp_simple_numbers():
    a = Double(0)
    a.value = 2 ** 2
    return a.value


@decorators.nivs_rt_sequence
def exp_num_nivsdatatype():
    a = Double(0)
    a.value = 2 ** Double(2)
    return a.value


@decorators.nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype():
    a = Double(0)
    a.value = Double(2) ** Double(3)
    return a.value


@decorators.nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype1():
    a = Double(0)
    a.value = Double(2) ** Int32(3)
    return a.value


@decorators.nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype2():
    a = Double(0)
    a.value = Int32(2) ** Double(3)
    return a.value


@decorators.nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype3():
    a = Int32(0)
    a.value = Int32(2) ** Int32(3)
    return a.value


@decorators.nivs_rt_sequence
def exp_use_rtseq():
    a = Double(0)
    a.value = 2 ** return_constant()
    return a.value


@decorators.nivs_rt_sequence
def exp_use_rtseq1():
    a = Double(0)
    a.value = return_constant() ** 2
    return a.value


@decorators.nivs_rt_sequence
def exp_use_rtseq2():
    a = Double(0)
    a.value = Double(2) ** return_constant()
    return a.value


@decorators.nivs_rt_sequence
def exp_use_rtseq3():
    a = Double(0)
    a.value = return_constant() ** Double(2)
    return a.value


@decorators.nivs_rt_sequence
def exp_use_rtseq4():
    a = Double(0)
    a.value = Int32(2) ** return_constant()
    return a.value


@decorators.nivs_rt_sequence
def exp_use_rtseq5():
    a = Double(0)
    a.value = return_constant() ** Int32(3)
    return a.value


@decorators.nivs_rt_sequence
def exp_with_parantheses():
    a = Double(0)
    a.value = 2 ** (2 + 3)
    return a.value


@decorators.nivs_rt_sequence
def exp_with_parantheses1():
    a = Double(1)
    a.value = 2 ** (Double(2) ** Int32(2))
    return a.value


@decorators.nivs_rt_sequence
def exp_with_parantheses2():
    a = Double(0)
    a.value = Double(1) * (Int32(2) ** 3.0) ** Double(2)
    return a.value


@decorators.nivs_rt_sequence
def exp_variables():
    a = Double(5)
    b = Double(0)
    b.value = 2 ** a
    return b.value


@decorators.nivs_rt_sequence
def exp_variables1():
    a = Double(5)
    b = Double(0)
    b.value = 2 ** a.value
    return b.value


@decorators.nivs_rt_sequence
def exp_variable_variable():
    a = Double(2)
    b = Double(3)
    c = Double(0)
    c.value = a.value ** b.value
    return c.value


@decorators.nivs_rt_sequence
def exp_variable_variable1():
    a = Double(2)
    b = Int32(3)
    c = Double(0)
    c.value = a.value ** b.value
    return c.value


@decorators.nivs_rt_sequence
def exp_variable_rtseq():
    a = Double(2)
    b = Double(0)
    b.value = a.value ** return_constant()
    return b.value


@decorators.nivs_rt_sequence
def exp_variable_rtseq1():
    a = Double(2)
    b = Double(0)
    b.value = return_constant() ** a.value
    return b.value


@decorators.nivs_rt_sequence
def exp_with_channelref():
    a = Double(0)
    a.value = 2 ** Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def exp_binary_unary():
    a = Double(0)
    a.value = 2 ** -1
    return a.value


@decorators.nivs_rt_sequence
def exp_complex_expr():
    a = Double(0)
    a.value = 3 ** (2 if 2 < 3 else 4)
    return a


# region augassign tests

@decorators.nivs_rt_sequence
def aug_exp_simple_numbers():
    a = Double(2)
    a.value **= 2
    return a.value


@decorators.nivs_rt_sequence
def aug_exp_num_nivsdatatype():
    a = Double(3)
    a.value **= Double(2)
    return a.value


@decorators.nivs_rt_sequence
def aug_exp_use_rtseq():
    a = Double(1)
    a.value **= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def aug_exp_with_parantheses():
    a = Double(2)
    a.value **= (Int32(2) ** 3.0) ** Double(2)
    return a.value


@decorators.nivs_rt_sequence
def aug_exp_variables():
    a = Double(5)
    b = Double(2)
    b.value **= a.value
    return b.value


@decorators.nivs_rt_sequence
def aug_exp_to_channelref():
    a = Double(1)
    a.value **= Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def aug_exp_unary():
    a = Double(2)
    a.value **= -1
    return a.value


# end region augassign tests

@decorators.nivs_rt_sequence
def exp_invalid_variables():
    return a ** b


@decorators.nivs_rt_sequence
def exp_invalid_variables1():
    return a.value ** b.value


@decorators.nivs_rt_sequence
def exp_invalid_variables2():
    a = Double(0)
    b = Double(0)
    b.value = a.value.value ** 2
    return b


@decorators.nivs_rt_sequence
def exp_with_None():
    a = Double(0)
    a.value = None ** 1
    return a


@decorators.nivs_rt_sequence
def exp_invalid_rtseq_call():
    a = Double(0)
    a.value = return_constant ** 1
    return a


run_tests = [
    (exp_simple_numbers, (), 4),
    (exp_num_nivsdatatype, (), 4),
    (exp_nivsdatatype_nivsdatatype, (), 8),
    (exp_nivsdatatype_nivsdatatype1, (), 8),
    (exp_nivsdatatype_nivsdatatype2, (), 8),
    (exp_nivsdatatype_nivsdatatype3, (), 8),
    (exp_with_parantheses, (), 32),
    (exp_with_parantheses1, (), 16),
    (exp_with_parantheses2, (), 64),
    (exp_variables, (), 32),
    (exp_variables1, (), 32),
    (exp_variable_variable, (), 8),
    (exp_variable_variable1, (), 8),
    (exp_binary_unary, (), 0.5),
    (aug_exp_simple_numbers, (), 4),
    (aug_exp_variables, (), 32),
    (aug_exp_num_nivsdatatype, (), 9),
    (aug_exp_with_parantheses, (), float(2**64)),
    (aug_exp_unary, (), 0.5),
    (exp_complex_expr, (), 9),
]

skip_tests = [
    (exp_with_channelref, (), "Not implemented yet."),
    (exp_invalid_rtseq_call, (), "Not implemented yet."),
    (exp_invalid_variables2, (), "Attribute transformer doesn't catch the a.value.value problem."),
    (exp_with_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (exp_variable_rtseq, (), "RTseq call not yet implemented."),
    (exp_variable_rtseq1, (), "RTseq call not yet implemented"),
    (exp_use_rtseq, (), "RTseq call not yet implemented."),
    (exp_use_rtseq1, (), "RTseq call not yet implemented."),
    (exp_use_rtseq2, (), "RTseq call not yet implemented."),
    (exp_use_rtseq3, (), "RTseq call not yet implemented."),
    (exp_use_rtseq4, (), "RTseq call not yet implemented."),
    (exp_use_rtseq5, (), "RTseq call not yet implemented."),
    (aug_exp_use_rtseq, (), "RTSeq call not implemented yet."),
    (aug_exp_to_channelref, (), "Channel ref transform not yet implemented."),
]

fail_transform_tests = [
    (exp_invalid_variables, (), TranslateError),
    (exp_invalid_variables1, (), TranslateError),
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
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    try:
        RealTimeSequence(func_name)
    except expected_result:
        pass
    except VeristandError as e:
        pytest.fail('Unexpected exception raised:' +
                    str(e.__class__) + ' while expected was: ' + expected_result.__name__)
    else:
        pytest.fail('ExpectedException not raised: ' + sys.exc_info()[0])


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)
