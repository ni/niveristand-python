import sys

from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Double, Int32
from niveristand.exceptions import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation
from testutilities.test_channels import TestChannels

a = 0
b = 1


@decorators.nivs_rt_sequence
def return_constant():
    a = Double(5)
    return a.value


@decorators.nivs_rt_sequence
def div_simple_numbers():
    a = Double(0)
    a.value = 1.0 / 2
    return a.value


@decorators.nivs_rt_sequence
def div_num_nivsdatatype():
    a = Double(0)
    b = Double(2)
    a.value = 1.0 / b.value
    return a.value


@decorators.nivs_rt_sequence
def div_nivsdatatype_nivsdatatype():
    a = Double(0)
    a.value = Double(1.0) / Double(2)
    return a.value


@decorators.nivs_rt_sequence
def div_nivsdatatype_nivsdatatype1():
    a = Double(0)
    a.value = Double(1) / Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def div_nivsdatatype_nivsdatatype2():
    a = Double(0)
    a.value = Int32(1) / Double(2)
    return a.value


@decorators.nivs_rt_sequence
def div_nivsdatatype_nivsdatatype3():
    a = Int32(0)
    a.value = Int32(2) / Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def div_multiple_types():
    a = Double(0)
    a.value = 1 / Double(2) / 3.0
    return a.value


@decorators.nivs_rt_sequence
def div_multiple_types1():
    a = Int32(0)
    a.value = 8 / Int32(2) / 2.0 / Double(2)
    return a.value


@decorators.nivs_rt_sequence
def div_use_rtseq():
    a = Double(0)
    a.value = 1 / return_constant()
    return a.value


@decorators.nivs_rt_sequence
def div_use_rtseq1():
    a = Double(0)
    a.value = return_constant() / 1
    return a.value


@decorators.nivs_rt_sequence
def div_use_rtseq2():
    a = Double(0)
    a.value = Double(1) / return_constant()
    return a.value


@decorators.nivs_rt_sequence
def div_use_rtseq3():
    a = Double(0)
    a.value = return_constant() / Double(1)
    return a.value


@decorators.nivs_rt_sequence
def div_use_rtseq4():
    a = Double(0)
    a.value = Int32(1) / return_constant()
    return a.value


@decorators.nivs_rt_sequence
def div_use_rtseq5():
    a = Double(0)
    a.value = return_constant() / Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def div_with_parantheses():
    a = Double(0)
    a.value = 1.0 / (2.0 / 3)
    return a.value


@decorators.nivs_rt_sequence
def div_with_parantheses1():
    a = Double(1)
    a.value = 1 / (Double(2) / Int32(5))
    return a.value


@decorators.nivs_rt_sequence
def div_with_parantheses2():
    a = Double(0)
    a.value = Double(1) / (Int32(2) / 3.0) / Double(4)
    return a.value


@decorators.nivs_rt_sequence
def div_variables():
    a = Double(5)
    b = Double(0)
    b.value = 1 / a
    return b.value


@decorators.nivs_rt_sequence
def div_variables1():
    a = Double(5)
    b = Double(0)
    b.value = 1 / a.value
    return b.value


@decorators.nivs_rt_sequence
def div_variable_variable():
    a = Double(1)
    b = Double(2)
    c = Double(0)
    c.value = a.value / b.value
    return c.value


@decorators.nivs_rt_sequence
def div_variable_variable1():
    a = Double(1)
    b = Int32(2)
    c = Double(0)
    c.value = a.value / b.value
    return c.value


@decorators.nivs_rt_sequence
def div_variable_rtseq():
    a = Double(1)
    b = Double(0)
    b.value = a.value / return_constant()
    return b.value


@decorators.nivs_rt_sequence
def div_variable_rtseq1():
    a = Double(1)
    b = Double(0)
    b.value = return_constant() / a.value
    return b.value


@decorators.nivs_rt_sequence
def div_with_channelref():
    a = Double(0)
    a.value = 1 / Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def div_binary_unary():
    a = Double(0)
    a.value = 2 / - 1
    return a.value


@decorators.nivs_rt_sequence
def div_complex_expr():
    a = Double(0)
    a.value = 1.0 / (2.0 if 2 < 3 else 4.0)
    return a


# region augassign tests

@decorators.nivs_rt_sequence
def aug_div_simple_numbers():
    a = Double(1)
    a.value /= 2
    return a.value


@decorators.nivs_rt_sequence
def aug_div_num_nivsdatatype():
    a = Double(1)
    a.value /= Double(2)
    return a.value


@decorators.nivs_rt_sequence
def aug_div_use_rtseq():
    a = Double(1)
    a.value /= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def aug_div_with_parantheses():
    a = Double(1)
    a.value /= (Int32(2) / 3.0) / Double(4)
    return a.value


@decorators.nivs_rt_sequence
def aug_div_variables():
    a = Double(5)
    b = Double(1)
    b.value /= a.value
    return b.value


@decorators.nivs_rt_sequence
def aug_div_to_channelref():
    a = Double(1)
    a.value /= Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def aug_div_unary():
    a = Double(1)
    a.value /= -1
    return a.value


# end region augassign tests

# region invalid tests
@decorators.nivs_rt_sequence
def div_invalid_variables():
    return a / b


@decorators.nivs_rt_sequence
def div_invalid_variables1():
    return a.value / b.value


@decorators.nivs_rt_sequence
def div_invalid_variables2():
    a = Double(0)
    b = Double(0)
    b.value = a.value.value / 2
    return b


@decorators.nivs_rt_sequence
def div_with_None():
    a = Double(0)
    a.value = None / 1
    return a


@decorators.nivs_rt_sequence
def div_invalid_rtseq_call():
    a = Double(0)
    a.value = return_constant / 1
    return a

# endregion


run_tests = [
    (return_constant, (), 5),
    (div_simple_numbers, (), 0.5),
    (div_num_nivsdatatype, (), 0.5),
    (div_nivsdatatype_nivsdatatype, (), 0.5),
    (div_nivsdatatype_nivsdatatype1, (), 0.5),
    (div_nivsdatatype_nivsdatatype2, (), 0.5),
    (div_nivsdatatype_nivsdatatype3, (), 2),
    (div_multiple_types, (), 0.5 / 3),
    (div_multiple_types1, (), 1),
    (div_with_parantheses, (), 1.5),
    (div_with_parantheses1, (), 2.5),
    (div_with_parantheses2, (), 3.0 / 8),
    (div_variables, (), 0.2),
    (div_variables1, (), 0.2),
    (div_variable_variable, (), 0.5),
    (div_variable_variable1, (), 0.5),
    (div_binary_unary, (), -2),
    (aug_div_simple_numbers, (), 0.5),
    (aug_div_variables, (), 0.2),
    (aug_div_num_nivsdatatype, (), 0.5),
    (aug_div_with_parantheses, (), 6.0),
    (aug_div_unary, (), -1),
    (div_complex_expr, (), 0.5),
]

skip_tests = [
    (div_with_channelref, (), "Not implemented yet."),
    (div_invalid_rtseq_call, (), "Not implemented yet."),
    (div_invalid_variables2, (), "Attribute transformer doesn't catch the a.value.value problem."),
    (div_with_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (div_variable_rtseq, (), "RTseq call not yet implemented."),
    (div_variable_rtseq1, (), "RTseq call not yet implemented"),
    (div_use_rtseq, (), "RTseq call not yet implemented."),
    (div_use_rtseq1, (), "RTseq call not yet implemented."),
    (div_use_rtseq2, (), "RTseq call not yet implemented."),
    (div_use_rtseq3, (), "RTseq call not yet implemented."),
    (div_use_rtseq4, (), "RTseq call not yet implemented."),
    (div_use_rtseq5, (), "RTseq call not yet implemented."),
    (aug_div_use_rtseq, (), "RTSeq call not implemented yet."),
    (aug_div_to_channelref, (), "Channel ref transform not yet implemented."),
]

fail_transform_tests = [
    (div_invalid_variables, (), TranslateError),
    (div_invalid_variables1, (), TranslateError),
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
