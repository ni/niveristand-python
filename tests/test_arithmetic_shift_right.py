from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Boolean, Double, Int32, Int64
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
def arithmetic_shift_right_simple_numbers():
    a = Double(0)
    a.value = 3 >> 1
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_num_nivsdatatype():
    a = Double(0)
    a.value = 3 >> Double(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype():
    a = Double(0)
    a.value = Double(3) >> Double(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype1():
    a = Double(0)
    a.value = Double(3) >> Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype2():
    a = Boolean(0)
    a.value = Boolean(3) >> Boolean(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype3():
    a = Double(0)
    a.value = Int32(3) >> Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_multiple_types():
    a = Int32(0)
    a.value = 15 >> Int32(3) >> 1
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_multiple_types1():
    a = Int64(0)
    a.value = 127 >> Int64(2) >> 3 >> Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_use_rtseq():
    a = Double(1)
    a.value = 1 >> return_constant()
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_use_rtseq1():
    a = Double(0)
    a.value = return_constant() >> 1
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_use_rtseq2():
    a = Double(0)
    a.value = Double(1) >> return_constant()
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_use_rtseq3():
    a = Double(0)
    a.value = return_constant() >> Double(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_use_rtseq4():
    a = Double(0)
    a.value = Int32(1) >> return_constant()
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_use_rtseq5():
    a = Double(0)
    a.value = return_constant() >> Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_with_parantheses():
    a = Int32(0)
    a.value = 1 >> (2 >> 1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_with_parantheses1():
    a = Double(0)
    a.value = 1 >> (Double(2) >> Int32(1))
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_with_parantheses2():
    a = Double(0)
    a.value = Double(1) >> (Int32(2) >> 1.0) >> Double(4)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_variables():
    a = Int32(5)
    b = Int32(0)
    b.value = 128 >> a
    return b.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_variables1():
    a = Int64(5)
    b = Int64(0)
    b.value = 128 >> a.value
    return b.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_variable_variable():
    a = Int32(3)
    b = Int64(1)
    c = Int32(0)
    c.value = a.value >> b.value
    return c.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_variable_variable1():
    a = Int32(3)
    b = Int64(1)
    c = Double(0)
    c.value = a.value >> b.value
    return c.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_variable_rtseq():
    a = Double(1)
    b = Double(0)
    b.value = a.value >> return_constant()
    return b.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_variable_rtseq1():
    a = Double(1)
    b = Double(0)
    b.value = return_constant() >> a.value
    return b.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_to_channelref():
    a = Double(0)
    a.value = 1 >> Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_binary_unary():
    a = Int32(0)
    a.value = 3 >> - 1
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_number():
    a = Int32(2)
    a.value >>= 1
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype():
    a = Int32(2)
    a.value >>= Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype1():
    a = Int64(2)
    a.value >>= Int64(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype2():
    a = Int64(2)
    a.value >>= Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype3():
    a = Int32(2)
    a.value >>= Int64(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype4():
    a = Int32(2)
    a.value >>= Double(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_variable():
    a = Int32(2)
    b = Int32(1)
    a.value >>= b.value
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_variable1():
    a = Int64(2)
    b = Int64(1)
    a.value >>= b.value
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_variable2():
    a = Int32(2)
    b = Int64(1)
    a.value >>= b.value
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_variable3():
    a = Int64(2)
    b = Int32(1)
    a.value >>= b.value
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_variable4():
    a = Int32(2)
    b = Double(1)
    a.value >>= b.value
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_rtseq():
    a = Int32(32987)
    a.value >>= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def arithemtic_shift_left_augassign_paranthesis():
    a = Int32(1024)
    a.value >>= (2 + Int32(1)) + Int64(1)
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_augassign_channelref():
    a = Int32(1024)
    a.value >>= Int32(Double(TestChannels.HP_COUNT))
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def arithmetic_shift_right_invalid_variables():
    return a.value >> b


@decorators.nivs_rt_sequence
def arithmetic_shift_right_invalid_variables1():
    return a.value >> b.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_invalid_variables2():
    a = Double(0)
    b = Double(0)
    b.value = a.value >> 2
    return b


@decorators.nivs_rt_sequence
def arithmetic_shift_right_to_None():
    a = Double(0)
    a.value = None >> 1
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_invalid_rtseq_call():
    a = Double(0)
    a.value = return_constant >> 1
    return a.value


@decorators.nivs_rt_sequence
def arithmetic_shift_right_complex_expr():
    a = Double(0)
    a.value = 1 >> (2 if 2 < 3 else 4)
    return a.value

# end region


run_tests = [
    (return_constant, (), 5.0),
    (arithmetic_shift_right_simple_numbers, (), 1),
    (arithmetic_shift_right_nivsdatatype_nivsdatatype3, (), 1),
    (arithmetic_shift_right_variables, (), 4),
    (arithmetic_shift_right_variables1, (), 4),
    (arithmetic_shift_right_multiple_types, (), 0),
    (arithmetic_shift_right_multiple_types1, (), 1),
    (arithmetic_shift_right_with_parantheses, (), 0),
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
    (arithemtic_shift_left_augassign_paranthesis, (), 64),
]

skip_tests = [
    (arithmetic_shift_right_use_rtseq, (), "RTSeq call not implemented yet."),
    (arithmetic_shift_right_use_rtseq1, (), "RTSeq call not implemented yet."),
    (arithmetic_shift_right_use_rtseq2, (), "RTSeq call not implemented yet."),
    (arithmetic_shift_right_use_rtseq3, (), "RTSeq call not implemented yet."),
    (arithmetic_shift_right_use_rtseq4, (), "RTSeq call not implemented yet."),
    (arithmetic_shift_right_use_rtseq5, (), "RTSeq call not implemented yet."),
    (arithmetic_shift_right_variable_rtseq, (), "RTSeq call not implemented yet."),
    (arithmetic_shift_right_variable_rtseq1, (), "RTSeq call not implemented yet."),
    (arithmetic_shift_right_to_channelref, (), "Channel ref transform not yet implemented."),
    (arithmetic_shift_right_invalid_variables2, (), "Attribute transformer doesn't catch the a.value.value problem."),
    (arithmetic_shift_right_to_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (arithmetic_shift_right_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
    (arithmetic_shift_right_complex_expr, (), "Not implemented yet."),
    (arithmetic_shift_right_binary_unary, (), "Different behaviour between python and SPE."),
    (arithmetic_shift_right_augassign_rtseq, (), "RTSeq call not implemented yet."),
    (arithmetic_shift_right_augassign_channelref, (), "Channel ref transform not yet implemented."),
]

fail_transform_tests = [
    (arithmetic_shift_right_invalid_variables, (), TranslateError),
    (arithmetic_shift_right_invalid_variables1, (), TranslateError),
    (arithmetic_shift_right_num_nivsdatatype, (), VeristandError),
    (arithmetic_shift_right_nivsdatatype_nivsdatatype, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_nivsdatatype_nivsdatatype1, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_nivsdatatype_nivsdatatype2, (), VeristandError),  # cannot do shift right on Boolean
    (arithmetic_shift_right_with_parantheses1, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_with_parantheses2, (), VeristandError),  # cannot do shift right on Double
    (arithmetic_shift_right_augassign_nivsdatatype4, (), VeristandError),  # cannot do shift right on double
    (arithmetic_shift_right_augassign_variable4, (), VeristandError),  # cannot do shift right on double
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
