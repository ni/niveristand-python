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
def mult_simple_numbers():
    a = Double(0)
    a.value = 1 * 2
    return a.value


@decorators.nivs_rt_sequence
def mult_num_nivsdatatype():
    a = Double(0)
    a.value = 1 * Double(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype():
    a = Double(0)
    a.value = Double(1) * Double(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype1():
    a = Double(0)
    a.value = Double(1) * Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype2():
    a = Double(0)
    a.value = Int32(1) * Double(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype3():
    a = Double(0)
    a.value = Int32(1) * Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_multiple_types():
    a = Double(0)
    a.value = 1 * Double(2) * 3.0
    return a.value


@decorators.nivs_rt_sequence
def mult_multiple_types1():
    a = Int32(0)
    a.value = 1 * Int32(2) * 3.0 * Double(4)
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq():
    a = Double(0)
    a.value = 1 * return_constant()
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq1():
    a = Double(0)
    a.value = return_constant() * 1
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq2():
    a = Double(0)
    a.value = Double(1) * return_constant()
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq3():
    a = Double(0)
    a.value = return_constant() * Double(1)
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq4():
    a = Double(0)
    a.value = Int32(1) * return_constant()
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq5():
    a = Double(0)
    a.value = return_constant() * Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def mult_with_parantheses():
    a = Double(0)
    a.value = 1 * (2 * 3)
    return a.value


@decorators.nivs_rt_sequence
def mult_with_parantheses1():
    a = Double(1)
    a.value = 1 * (Double(2) * Int32(5))
    return a.value


@decorators.nivs_rt_sequence
def mult_with_parantheses2():
    a = Double(0)
    a.value = Double(1) * (Int32(2) * 3.0) * Double(4)
    return a.value


@decorators.nivs_rt_sequence
def mult_variables():
    a = Double(5)
    b = Double(0)
    b.value = 1 * a
    return b.value


@decorators.nivs_rt_sequence
def mult_variables1():
    a = Double(5)
    b = Double(0)
    b.value = 1 * a.value
    return b.value


@decorators.nivs_rt_sequence
def mult_variable_variable():
    a = Double(1)
    b = Double(2)
    c = Double(0)
    c.value = a.value * b.value
    return c.value


@decorators.nivs_rt_sequence
def mult_variable_variable1():
    a = Double(1)
    b = Int32(2)
    c = Double(0)
    c.value = a.value * b.value
    return c.value


@decorators.nivs_rt_sequence
def mult_variable_rtseq():
    a = Double(1)
    b = Double(0)
    b.value = a.value * return_constant()
    return b.value


@decorators.nivs_rt_sequence
def mult_variable_rtseq1():
    a = Double(1)
    b = Double(0)
    b.value = return_constant() * a.value
    return b.value


@decorators.nivs_rt_sequence
def mult_with_channelref():
    a = Double(0)
    a.value = 1 * Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def mult_binary_unary():
    a = Double(0)
    a.value = 2 * - 1
    return a.value


##################################################################
#                       INVALID TESTS                            #
##################################################################
@decorators.nivs_rt_sequence
def mult_invalid_variables():
    return a * b


@decorators.nivs_rt_sequence
def mult_invalid_variables1():
    return a.value * b.value


@decorators.nivs_rt_sequence
def mult_invalid_variables2():
    a = Double(0)
    b = Double(0)
    b.value = a.value.value * 2
    return b


@decorators.nivs_rt_sequence
def mult_with_None():
    a = Double(0)
    a.value = None * 1
    return a


@decorators.nivs_rt_sequence
def mult_invalid_rtseq_call():
    a = Double(0)
    a.value = return_constant * 1
    return a


@decorators.nivs_rt_sequence
def mult_complex_expr():
    a = Double(0)
    a.value = 1 * (2 if 2 < 3 else 4)
    return a


run_tests = [
    (mult_simple_numbers, (), 2),
    (mult_num_nivsdatatype, (), 2),
    (mult_nivsdatatype_nivsdatatype, (), 2),
    (mult_nivsdatatype_nivsdatatype1, (), 2),
    (mult_nivsdatatype_nivsdatatype2, (), 2),
    (mult_nivsdatatype_nivsdatatype3, (), 2),
    (mult_multiple_types, (), 6),
    (mult_multiple_types1, (), 24),
    (mult_with_parantheses, (), 6),
    (mult_with_parantheses1, (), 10),
    (mult_with_parantheses2, (), 24),
    (mult_variables, (), 5),
    (mult_variables1, (), 5),
    (mult_variable_variable, (), 2),
    (mult_variable_variable1, (), 2),
]

skip_tests = [
    (mult_with_channelref, (), "Not implemented yet."),
    (mult_binary_unary, (), "Not implemented yet."),
    (mult_invalid_rtseq_call, (), "Not implemented yet."),
    (mult_complex_expr, (), "Not implemented yet."),
    (mult_invalid_variables2, (), "Attribute transformer doesn't catch the a.value.value problem."),
    (mult_with_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (mult_variable_rtseq, (), "RTseq call not yet implemented."),
    (mult_variable_rtseq1, (), "RTseq call not yet implemented"),
    (mult_use_rtseq, (), "RTseq call not yet implemented."),
    (mult_use_rtseq1, (), "RTseq call not yet implemented."),
    (mult_use_rtseq2, (), "RTseq call not yet implemented."),
    (mult_use_rtseq3, (), "RTseq call not yet implemented."),
    (mult_use_rtseq4, (), "RTseq call not yet implemented."),
    (mult_use_rtseq5, (), "RTseq call not yet implemented."),
]

fail_transform_tests = [
    (mult_invalid_variables, (), TranslateError),
    (mult_invalid_variables1, (), TranslateError),
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
