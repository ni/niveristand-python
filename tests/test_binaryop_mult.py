import sys

from niveristand import decorators, RealTimeSequence
from niveristand.clientapi.datatypes import DoubleValue, I32Value
from niveristand.exceptions import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation
from testutilities.test_channels import TestChannels

a = 0
b = 1


@decorators.nivs_rt_sequence
def return_constant():
    a = DoubleValue(5)
    return a.value


@decorators.nivs_rt_sequence
def mult_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 * 2
    return a.value


@decorators.nivs_rt_sequence
def mult_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 1 * DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1) * DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) * I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype2():
    a = DoubleValue(0)
    a.value = I32Value(1) * DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(1) * I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_multiple_types():
    a = DoubleValue(0)
    a.value = 1 * DoubleValue(2) * 3.0
    return a.value


@decorators.nivs_rt_sequence
def mult_multiple_types1():
    a = I32Value(0)
    a.value = 1 * I32Value(2) * 3.0 * DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq():
    a = DoubleValue(0)
    a.value = 2 * return_constant()
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq1():
    a = DoubleValue(0)
    a.value = return_constant() * 2
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq2():
    a = DoubleValue(0)
    a.value = DoubleValue(2) * return_constant()
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq3():
    a = DoubleValue(0)
    a.value = return_constant() * DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(2) * return_constant()
    return a.value


@decorators.nivs_rt_sequence
def mult_use_rtseq5():
    a = DoubleValue(0)
    a.value = return_constant() * I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def mult_with_parantheses():
    a = DoubleValue(0)
    a.value = 1 * (2 * 3)
    return a.value


@decorators.nivs_rt_sequence
def mult_with_parantheses1():
    a = DoubleValue(1)
    a.value = 1 * (DoubleValue(2) * I32Value(5))
    return a.value


@decorators.nivs_rt_sequence
def mult_with_parantheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) * (I32Value(2) * 3.0) * DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def mult_variables():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 * a
    return b.value


@decorators.nivs_rt_sequence
def mult_variables1():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 * a.value
    return b.value


@decorators.nivs_rt_sequence
def mult_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value * b.value
    return c.value


@decorators.nivs_rt_sequence
def mult_variable_variable1():
    a = DoubleValue(1)
    b = I32Value(2)
    c = DoubleValue(0)
    c.value = a.value * b.value
    return c.value


@decorators.nivs_rt_sequence
def mult_variable_rtseq():
    a = DoubleValue(2)
    b = DoubleValue(0)
    b.value = a.value * return_constant()
    return b.value


@decorators.nivs_rt_sequence
def mult_variable_rtseq1():
    a = DoubleValue(2)
    b = DoubleValue(0)
    b.value = return_constant() * a.value
    return b.value


@decorators.nivs_rt_sequence
def mult_with_channelref():
    a = DoubleValue(0)
    a.value = 1 * DoubleValue(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def mult_binary_unary():
    a = DoubleValue(0)
    a.value = 2 * - 1
    return a.value


@decorators.nivs_rt_sequence
def mult_complex_expr():
    a = DoubleValue(0)
    a.value = 1 * (2 if 2 < 3 else 4)
    return a


# region augassign tests

@decorators.nivs_rt_sequence
def aug_mult_simple_numbers():
    a = DoubleValue(1)
    a.value *= 2
    return a.value


@decorators.nivs_rt_sequence
def aug_mult_num_nivsdatatype():
    a = DoubleValue(1)
    a.value *= DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def aug_mult_use_rtseq():
    a = DoubleValue(2)
    a.value *= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def aug_mult_with_parantheses():
    a = DoubleValue(2)
    a.value *= (I32Value(1) * 3.0) * DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def aug_mult_variables():
    a = DoubleValue(5)
    b = DoubleValue(1)
    b.value *= a.value
    return b.value


@decorators.nivs_rt_sequence
def aug_mult_to_channelref():
    a = DoubleValue(1)
    a.value *= DoubleValue(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def aug_mult_unary():
    a = DoubleValue(1)
    a.value *= -1
    return a.value


# end region augassign tests
# region invalid tests
@decorators.nivs_rt_sequence
def mult_invalid_variables():
    return a * b


@decorators.nivs_rt_sequence
def mult_invalid_variables1():
    return a.value * b.value


@decorators.nivs_rt_sequence
def mult_invalid_variables2():
    a = DoubleValue(0)
    b = DoubleValue(0)
    b.value = a.value.value * 2
    return b


@decorators.nivs_rt_sequence
def mult_with_None():
    a = DoubleValue(0)
    a.value = None * 1
    return a


@decorators.nivs_rt_sequence
def mult_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = return_constant * 1
    return a

# end region invalid tests


run_tests = [
    (return_constant, (), 5),
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
    (mult_binary_unary, (), -2),
    (aug_mult_simple_numbers, (), 2),
    (aug_mult_variables, (), 5),
    (aug_mult_num_nivsdatatype, (), 2),
    (aug_mult_with_parantheses, (), 24),
    (aug_mult_unary, (), -1),
    (mult_complex_expr, (), 2),
    (mult_variable_rtseq, (), 10),
    (mult_variable_rtseq1, (), 10),
    (mult_use_rtseq, (), 10),
    (mult_use_rtseq1, (), 10),
    (mult_use_rtseq2, (), 10),
    (mult_use_rtseq3, (), 10),
    (mult_use_rtseq4, (), 10),
    (mult_use_rtseq5, (), 10),
    (aug_mult_use_rtseq, (), 10),
]

skip_tests = [
    (mult_with_channelref, (), "Not implemented yet."),
    (mult_invalid_rtseq_call, (), "Not implemented yet."),
    (mult_invalid_variables2, (), "Attribute transformer doesn't catch the a.value.value problem."),
    (mult_with_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (aug_mult_to_channelref, (), "Channel ref transform not yet implemented."),
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


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
