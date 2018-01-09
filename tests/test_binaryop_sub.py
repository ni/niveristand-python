from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Double, Int32
from niveristand.exceptions import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner
from testutilities.test_channels import TestChannels


a = 1
b = 2


@decorators.nivs_rt_sequence
def return_constant():
    a = Double(5)
    return a.value


@decorators.nivs_rt_sequence
def sub_simple_numbers():
    a = Double(0)
    a.value = 1 - 2
    return a.value


def test_sub_simple_numbers():
    RealTimeSequence(sub_simple_numbers)


@decorators.nivs_rt_sequence
def sub_num_nivsdatatype():
    a = Double(0)
    a.value = 1 - Double(2)
    return a.value


@decorators.nivs_rt_sequence
def sub_nivsdatatype_nivsdatatype():
    a = Double(0)
    a.value = Double(1) - Double(2)
    return a.value


@decorators.nivs_rt_sequence
def sub_nivsdatatype_nivsdatatype1():
    a = Double(0)
    a.value = Double(1) - Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def sub_nivsdatatype_nivsdatatype2():
    a = Double(0)
    a.value = Int32(1) - Double(2)
    return a.value


@decorators.nivs_rt_sequence
def sub_nivsdatatype_nivsdatatype3():
    a = Double(0)
    a.value = Int32(1) - Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def sub_multiple_types():
    a = Double(0)
    a.value = 1 - Double(2) - 3.0
    return a.value


@decorators.nivs_rt_sequence
def sub_multiple_types1():
    a = Int32(0)
    a.value = 1 - Int32(2) - 3.0 - Double(4)
    return a.value


@decorators.nivs_rt_sequence
def sub_use_rtseq():
    a = Double(0)
    a.value = 1 - return_constant()
    return a.value


@decorators.nivs_rt_sequence
def sub_use_rtseq1():
    a = Double(0)
    a.value = return_constant() - 1
    return a.value


@decorators.nivs_rt_sequence
def sub_use_rtseq2():
    a = Double(0)
    a.value = Double(1) - return_constant()
    return a.value


@decorators.nivs_rt_sequence
def sub_use_rtseq3():
    a = Double(0)
    a.value = return_constant() - Double(1)
    return a.value


@decorators.nivs_rt_sequence
def sub_use_rtseq4():
    a = Double(0)
    a.value = Int32(1) - return_constant()
    return a.value


@decorators.nivs_rt_sequence
def sub_use_rtseq5():
    a = Double(0)
    a.value = return_constant() - Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def sub_with_parantheses():
    a = Double(0)
    a.value = 1 - (2 - 3)
    return a.value


@decorators.nivs_rt_sequence
def sub_with_parantheses1():
    a = Double(0)
    a.value = 1 - (Double(2) - Int32(5))
    return a.value


@decorators.nivs_rt_sequence
def sub_with_parantheses2():
    a = Double(0)
    a.value = Double(5) - (Int32(2) - 3.0) - Double(4)
    return a.value


@decorators.nivs_rt_sequence
def sub_variables():
    a = Double(5)
    b = Double(0)
    b.value = 1 - a
    return b.value


@decorators.nivs_rt_sequence
def sub_variables1():
    a = Double(5)
    b = Double(0)
    b.value = 1 - a.value
    return b.value


@decorators.nivs_rt_sequence
def sub_variable_variable():
    a = Double(1)
    b = Double(2)
    c = Double(0)
    c.value = a.value - b.value
    return c.value


@decorators.nivs_rt_sequence
def sub_variable_variable1():
    a = Double(1)
    b = Double(2)
    c = Double(0)
    c.value = a.value - b.value
    return c.value


@decorators.nivs_rt_sequence
def sub_variable_rtseq():
    a = Double(1)
    b = Double(0)
    b.value = a.value - return_constant()
    return b.value


@decorators.nivs_rt_sequence
def sub_variable_rtseq1():
    a = Double(1)
    b = Double(0)
    b.value = return_constant() - a.value
    return b.value


@decorators.nivs_rt_sequence
def sub_to_channelref():
    a = Double(0)
    a.value = 1 - Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def sub_binary_unary():
    a = Double(0)
    a.value = 2 - -1
    return a.value


@decorators.nivs_rt_sequence
def sub_with_multiple_minus():
    a = Double(0)
    a.value = 1 - 2   # noqa: E225 it's ok to test this
    return a.value


@decorators.nivs_rt_sequence
def sub_with_multiple_minus1():
    a = Double(0)
    a.value = 1 - 2   # noqa: E225 it's ok to test this
    return a.value


@decorators.nivs_rt_sequence
def sub_binary_unary_sequence():
    a = Double(0)
    a.value = 1 - -----2  # noqa: E225 it's ok to test this
    return a.value


##################################################################
#                       INVALID TESTS                            #
##################################################################
@decorators.nivs_rt_sequence
def sub_invalid_variables():
    return a - b


@decorators.nivs_rt_sequence
def sub_invalid_variables1():
    return a.value - b.value


@decorators.nivs_rt_sequence
def sub_invalid_variables2():
    a = Double(0)
    b = Double(0)
    b.value = a.value - 2
    return b.value


@decorators.nivs_rt_sequence
def sub_from_None():
    a = Double(0)
    a.value = None - 1
    return a.value


@decorators.nivs_rt_sequence
def sub_invalid_rtseq_call():
    a = Double(0)
    a.value = return_constant - 1
    return a.value


@decorators.nivs_rt_sequence
def sub_complex_expr():
    a = Double(0)
    a.value = 1 - (2 if 2 < 3 else 4)
    return a.value


run_tests = [
    (return_constant, (), 5),
    (sub_simple_numbers, (), -1),
    (sub_num_nivsdatatype, (), -1),
    (sub_nivsdatatype_nivsdatatype, (), -1),
    (sub_nivsdatatype_nivsdatatype1, (), -1),
    (sub_nivsdatatype_nivsdatatype2, (), -1),
    (sub_nivsdatatype_nivsdatatype3, (), -1),
    (sub_multiple_types, (), -4),
    (sub_multiple_types1, (), -8),
    (sub_with_parantheses, (), 2),
    (sub_with_parantheses1, (), 4),
    (sub_with_parantheses2, (), 2),
    (sub_variables, (), -4),
    (sub_variables1, (), -4),
    (sub_variable_variable, (), -1),
    (sub_variable_variable1, (), -1),
    (sub_binary_unary, (), 3),
    (sub_binary_unary_sequence, (), 3),
]

skip_tests = [
    (sub_use_rtseq, (), "RTSeq call not implemented yet."),
    (sub_use_rtseq1, (), "RTSeq call not implemented yet."),
    (sub_use_rtseq2, (), "RTSeq call not implemented yet."),
    (sub_use_rtseq3, (), "RTSeq call not implemented yet."),
    (sub_use_rtseq4, (), "RTSeq call not implemented yet."),
    (sub_use_rtseq5, (), "RTSeq call not implemented yet."),
    (sub_variable_rtseq, (), "RTSeq call not implemented yet."),
    (sub_variable_rtseq1, (), "RTSeq call not implemented yet."),
    (sub_to_channelref, (), "Channel ref transform not yet implemented."),
    (sub_invalid_variables2, (), "Attribute transformer doesn't catch the a.value.value problem. -DE14612"),
    (sub_from_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7. - DE14611"),
    (sub_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
    (sub_complex_expr, (), "Not implemented yet."),
]

fail_transform_tests = [
    (sub_invalid_variables, (), TranslateError),
    (sub_invalid_variables1, (), TranslateError),
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
    except Exception as exception:
        pytest.fail('ExpectedException not raised: ' + exception)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)
