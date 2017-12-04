from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Double, Int32
import pytest
from testutilities import rtseqrunner
from testutilities.test_channels import TestChannels


a = 1
b = 2


@decorators.nivs_rt_sequence
def return_constant():
    a = Double(5)
    return a


@decorators.nivs_rt_sequence
def add_simple_numbers():
    a = Double(0)
    a.value = 1 + 2
    return a


def test_add_simple_numbers():
    RealTimeSequence(add_simple_numbers)


def test_run_add_simple_numbers():
    rtseqrunner.assert_run_python_equals_rtseq(add_simple_numbers, 3)


@decorators.nivs_rt_sequence
def add_num_nivsdatatype():
    a = Double(0)
    a.value = 1 + Double(2)
    return a


def test_add_num_nivsdatatype():
    RealTimeSequence(add_num_nivsdatatype)


def test_run_add_num_nivsdatatype():
    rtseqrunner.assert_run_python_equals_rtseq(add_num_nivsdatatype, 3)


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype():
    a = Double(0)
    a.value = Double(1) + Double(2)
    return a


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype1():
    a = Double(0)
    a.value = Double(1) + Int32(2)
    return a


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype2():
    a = Double(0)
    a.value = Int32(1) + Double(2)
    return a


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype3():
    a = Double(0)
    a.value = Int32(1) + Int32(2)
    return a


def test_add_nivsdatatype_nivsdatatype():
    RealTimeSequence(add_nivsdatatype_nivsdatatype)
    RealTimeSequence(add_nivsdatatype_nivsdatatype1)
    RealTimeSequence(add_nivsdatatype_nivsdatatype2)
    RealTimeSequence(add_nivsdatatype_nivsdatatype3)


def test_run_add_nivsdatatype_nivsdatatype():
    rtseqrunner.assert_run_python_equals_rtseq(add_nivsdatatype_nivsdatatype, 3)
    rtseqrunner.assert_run_python_equals_rtseq(add_nivsdatatype_nivsdatatype2, 3)
    rtseqrunner.assert_run_python_equals_rtseq(add_nivsdatatype_nivsdatatype1, 3)
    rtseqrunner.assert_run_python_equals_rtseq(add_nivsdatatype_nivsdatatype3, 3)


@decorators.nivs_rt_sequence
def add_multiple_types():
    a = Double(0)
    a.value = 1 + Double(2) + 3.0
    return a


@decorators.nivs_rt_sequence
def add_multiple_types1():
    a = Int32(0)
    a.value = 1 + Int32(2) + 3.0 + Double(4)
    return a


def test_add_multiple_types():
    RealTimeSequence(add_multiple_types)
    RealTimeSequence(add_multiple_types1)


def test_run_add_multiple_types():
    rtseqrunner.assert_run_python_equals_rtseq(add_multiple_types, 6)
    rtseqrunner.assert_run_python_equals_rtseq(add_multiple_types1, 10)


@decorators.nivs_rt_sequence
def add_use_rtseq():
    a = Double(0)
    a.value = 1 + return_constant()
    return a


@decorators.nivs_rt_sequence
def add_use_rtseq1():
    a = Double(0)
    a.value = return_constant() + 1
    return a


@decorators.nivs_rt_sequence
def add_use_rtseq2():
    a = Double(0)
    a.value = Double(1) + return_constant()
    return a


@decorators.nivs_rt_sequence
def add_use_rtseq3():
    a = Double(0)
    a.value = return_constant() + Double(1)
    return a


@decorators.nivs_rt_sequence
def add_use_rtseq4():
    a = Double(0)
    a.value = Int32(1) + return_constant()
    return a


@decorators.nivs_rt_sequence
def add_use_rtseq5():
    a = Double(0)
    a.value = return_constant() + Int32(1)
    return a


def test_add_use_rtseq():
    RealTimeSequence(add_use_rtseq)
    RealTimeSequence(add_use_rtseq1)
    RealTimeSequence(add_use_rtseq2)
    RealTimeSequence(add_use_rtseq3)
    RealTimeSequence(add_use_rtseq4)
    RealTimeSequence(add_use_rtseq5)


@pytest.mark.skip("Call transformer not working in local runner yet")
def test_run_add_use_rtseq():
    rtseqrunner.assert_run_python_equals_rtseq(add_use_rtseq, 6.0)
    rtseqrunner.assert_run_python_equals_rtseq(add_use_rtseq1, 6.0)
    rtseqrunner.assert_run_python_equals_rtseq(add_use_rtseq2, 6.0)
    rtseqrunner.assert_run_python_equals_rtseq(add_use_rtseq3, 6.0)
    rtseqrunner.assert_run_python_equals_rtseq(add_use_rtseq4, 6.0)
    rtseqrunner.assert_run_python_equals_rtseq(add_use_rtseq5, 6.0)


@decorators.nivs_rt_sequence
def add_with_parantheses():
    a = Double(0)
    a.value = 1 + (2 + 3)
    return a


@decorators.nivs_rt_sequence
def add_with_parantheses1():
    a = Double(0)
    a.value = 1 + (Double(2) + Int32(5))
    return a


@decorators.nivs_rt_sequence
def add_with_parantheses2():
    a = Double(0)
    a.value = Double(1) + (Int32(2) + 3.0) + Double(4)
    return a


def test_add_with_parantheses():
    RealTimeSequence(add_with_parantheses)
    RealTimeSequence(add_with_parantheses1)
    RealTimeSequence(add_with_parantheses2)


def test_run_add_with_parantheses():
    rtseqrunner.assert_run_python_equals_rtseq(add_with_parantheses, 6.0)
    rtseqrunner.assert_run_python_equals_rtseq(add_with_parantheses1, 8.0)
    rtseqrunner.assert_run_python_equals_rtseq(add_with_parantheses2, 10.0)


@decorators.nivs_rt_sequence
def add_variables():
    a = Double(5)
    b = Double(0)
    b.value = 1 + a
    return b


@decorators.nivs_rt_sequence
def add_variables1():
    a = Double(5)
    b = Double(0)
    b.value = 1 + a.value
    return b


def test_add_variables():
    RealTimeSequence(add_variables)
    RealTimeSequence(add_variables1)


@decorators.nivs_rt_sequence
def add_variable_variable():
    a = Double(1)
    b = Double(2)
    c = Double(0)
    c.value = a.value + b.value
    return c


@decorators.nivs_rt_sequence
def add_variable_variable1():
    a = Double(1)
    b = Double(2)
    c = Double(0)
    c.value = a.value + b.value
    return c


def test_add_variable_variable():
    RealTimeSequence(add_variable_variable)
    RealTimeSequence(add_variable_variable1)


@pytest.mark.skip("RTseqrunner is returning the wrong value here for some reason.")
def test_run_add_variable_variable():
    rtseqrunner.assert_run_python_equals_rtseq(add_variable_variable, 3.0)
    rtseqrunner.assert_run_python_equals_rtseq(add_variable_variable1, 3.0)


@decorators.nivs_rt_sequence
def add_variable_rtseq():
    a = Double(1)
    b = Double(0)
    b.value = a.value + return_constant()
    return b


@decorators.nivs_rt_sequence
def add_variable_rtseq1():
    a = Double(1)
    b = Double(0)
    b.value = return_constant() + a.value
    return b


def test_add_variable_rtseq():
    RealTimeSequence(add_variable_rtseq)
    RealTimeSequence(add_variable_rtseq1)


@pytest.mark.skip("Call transformer not working in local runner yet")
def test_run_add_variable_rtseq():
    rtseqrunner.assert_run_python_equals_rtseq(add_variable_rtseq, 6.0)
    rtseqrunner.assert_run_python_equals_rtseq(add_variable_rtseq1, 6.0)


@decorators.nivs_rt_sequence
def add_to_channelref():
    a = Double(0)
    a.value = 1 + Double(TestChannels.HP_COUNT)
    return a


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_to_channelref():
    RealTimeSequence(add_to_channelref)


@decorators.nivs_rt_sequence
def add_binary_unary():
    a = Double(0)
    a.value = 2 + - 1
    return a


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_binary_unary():
    RealTimeSequence(add_binary_unary)


@decorators.nivs_rt_sequence
def add_with_multiple_plus():
    a = Double(0)
    a.value = 1 ++ 2   # noqa: E225 it's ok to test this
    return a


@decorators.nivs_rt_sequence
def add_with_multiple_plus1():
    a = Double(0)
    a.value = 1 +++ 2   # noqa: E225 it's ok to test this
    return a


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_with_multiple_plus():
    RealTimeSequence(add_with_multiple_plus)
    RealTimeSequence(add_with_multiple_plus1)


@pytest.mark.skip(reason="no way of currently testing this")
def test_run_add_with_multiple_plus():
    rtseqrunner.assert_run_python_equals_rtseq(add_with_multiple_plus, 3.0)
    rtseqrunner.assert_run_python_equals_rtseq(add_with_multiple_plus1, 3.0)


@decorators.nivs_rt_sequence
def add_binary_unary_sequence():
    a = Double(0)
    a.value = 1+ - + - + - + - + -2  # noqa: E225 it's ok to test this
    return a


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_binary_unary_sequence():
    RealTimeSequence(add_binary_unary_sequence)


@pytest.mark.skip(reason="no way of currently testing this")
def test_run_add_binary_unary_sequence():
    rtseqrunner.assert_run_python_equals_rtseq(add_binary_unary_sequence, -1.0)


##################################################################
#                       INVALID TESTS                            #
##################################################################
@decorators.nivs_rt_sequence
def add_invalid_variables():
    return a + b


@decorators.nivs_rt_sequence
def add_invalid_variables1():
    return a.value + b.value


@decorators.nivs_rt_sequence
def add_invalid_variables2():
    a = Double(0)
    b = Double(0)
    b.value = a.value.value + 2
    return b


@pytest.mark.skip(reason="no way of currently testing this")
def test_invalid_variables():
    # TODO create exceptions
    RealTimeSequence(add_invalid_variables)
    RealTimeSequence(add_invalid_variables1)
    RealTimeSequence(add_invalid_variables2)


@decorators.nivs_rt_sequence
def add_to_None():
    a = Double(0)
    a.value = None + 1
    return a


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_to_None():
    # TODO create exception
    RealTimeSequence(add_to_None)


@decorators.nivs_rt_sequence
def add_invalid_rtseq_call():
    a = Double(0)
    a.value = return_constant + 1
    return a


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_invalid_rtseq_call():
    # TODO create exception
    RealTimeSequence(add_invalid_rtseq_call)


@decorators.nivs_rt_sequence
def add_complex_expr():
    a = Double(0)
    a.value = 1 + (2 if 2 < 3 else 4)
    return a


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_complex_expr():
    # TODO create exception
    RealTimeSequence(add_complex_expr)
