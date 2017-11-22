from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Double, Int32
import pytest
from testutilities.test_channels import TestChannels


a = 1
b = 2


@decorators.nivs_rt_sequence
def return_constant():
    return 5


@decorators.nivs_rt_sequence
def add_simple_numbers():
    return 1 + 2


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_simple_numbers():
    RealTimeSequence(add_simple_numbers)


@decorators.nivs_rt_sequence
def add_num_nivsdatatype():
    return 1 + Double(2)


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_num_nivsdatatype():
    RealTimeSequence(add_num_nivsdatatype)


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype():
    return Double(1) + Double(2)


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype1():
    return Double(1) + Int32(2)


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype2():
    return Int32(1) + Double(2)


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype3():
    return Int32(1) + Int32(2)


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_nivsdatatype_nivsdatatype():
    RealTimeSequence(add_nivsdatatype_nivsdatatype)
    RealTimeSequence(add_nivsdatatype_nivsdatatype1)
    RealTimeSequence(add_nivsdatatype_nivsdatatype2)
    RealTimeSequence(add_nivsdatatype_nivsdatatype3)


@decorators.nivs_rt_sequence
def add_multiple_types():
    return 1 + Double(2) + 3.0


@decorators.nivs_rt_sequence
def add_multiple_types1():
    return 1 + Int32(2) + 3.0


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_multiple_types():
    RealTimeSequence(add_multiple_types)
    RealTimeSequence(add_multiple_types1)


@decorators.nivs_rt_sequence
def add_use_rtseq():
    return 1 + return_constant()


@decorators.nivs_rt_sequence
def add_use_rtseq1():
    return return_constant() + 1


@decorators.nivs_rt_sequence
def add_use_rtseq2():
    return Double(1) + return_constant()


@decorators.nivs_rt_sequence
def add_use_rtseq3():
    return return_constant() + Double(1)


@decorators.nivs_rt_sequence
def add_use_rtseq4():
    return Int32(1) + return_constant()


@decorators.nivs_rt_sequence
def add_use_rtseq5():
    return return_constant() + Int32(1)


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_use_rtseq():
    RealTimeSequence(add_use_rtseq)
    RealTimeSequence(add_use_rtseq1)
    RealTimeSequence(add_use_rtseq2)
    RealTimeSequence(add_use_rtseq3)
    RealTimeSequence(add_use_rtseq4)
    RealTimeSequence(add_use_rtseq5)


@decorators.nivs_rt_sequence
def add_with_parantheses():
    return 1 + (2 + 3)


@decorators.nivs_rt_sequence
def add_with_parantheses1():
    return 1 + (Double(2) + return_constant())


@decorators.nivs_rt_sequence
def add_with_parantheses2():
    return return_constant() + (Int32(2) + 3.0) + Double(4)


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_with_parantheses():
    RealTimeSequence(add_with_parantheses)
    RealTimeSequence(add_with_parantheses1)
    RealTimeSequence(add_with_parantheses2)


@decorators.nivs_rt_sequence
def add_variables():
    a = Double(5)
    return 1 + a


@decorators.nivs_rt_sequence
def add_variables1():
    a = Double(5)
    return 1 + a.value


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_variables():
    RealTimeSequence(add_variables)
    RealTimeSequence(add_variables1)


@decorators.nivs_rt_sequence
def add_variable_variable():
    a = Double(1)
    b = Double(2)
    return a + b


@decorators.nivs_rt_sequence
def add_variable_variable1():
    a = Double(1)
    b = Double(2)
    return a.value + b.value


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_varaiable_variable():
    RealTimeSequence(add_variable_variable)
    RealTimeSequence(add_variable_variable1)


@decorators.nivs_rt_sequence
def add_variable_rtseq():
    a = Double(1)
    return a + return_constant()


@decorators.nivs_rt_sequence
def add_variable_rtseq1():
    a = Double(1)
    return return_constant() + a.value


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_variable_rtseq():
    RealTimeSequence(add_variable_rtseq)
    RealTimeSequence(add_variable_rtseq1)


@decorators.nivs_rt_sequence
def add_to_channelref():
    return 1 + Double(TestChannels.HP_COUNT)


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_to_channelref():
    RealTimeSequence(add_to_channelref)


@decorators.nivs_rt_sequence
def add_binary_unary():
    return 2 + - 1


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_binary_unary():
    RealTimeSequence(add_binary_unary)


@decorators.nivs_rt_sequence
def add_with_multiple_plus():
    return 1 ++ 2   # noqa: E225 it's ok to test this


@decorators.nivs_rt_sequence
def add_with_multiple_plus1():
    return 1 +++ 2   # noqa: E225 it's ok to test this


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_with_multiple_plus():
    RealTimeSequence(add_with_multiple_plus)
    RealTimeSequence(add_with_multiple_plus1)


@decorators.nivs_rt_sequence
def add_binary_unary_sequence():
    return 1+ - + - + - + - + -2    # noqa: E225 it's ok to test this


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_binary_unary_sequence():
    RealTimeSequence(add_binary_unary_sequence)


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
    return a.value.value + 2


@pytest.mark.skip(reason="no way of currently testing this")
def test_invalid_variables():
    # TODO create exceptions
    RealTimeSequence(add_invalid_variables)
    RealTimeSequence(add_invalid_variables1)
    RealTimeSequence(add_invalid_variables2)


@decorators.nivs_rt_sequence
def add_to_None():
    return None + 1


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_to_None():
    # TODO create exception
    RealTimeSequence(add_to_None)


@decorators.nivs_rt_sequence
def add_invalid_rtseq_call():
    return return_constant + 1


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_invalid_rtseq_call():
    # TODO create exception
    RealTimeSequence(add_invalid_rtseq_call)


@decorators.nivs_rt_sequence
def add_complex_expr():
    return 1 + (2 if 2 < 3 else 4)


@pytest.mark.skip(reason="no way of currently testing this")
def test_add_complex_expr():
    # TODO create exception
    RealTimeSequence(add_complex_expr)
