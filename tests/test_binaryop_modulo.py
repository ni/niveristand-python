import sys

from niveristand import decorators, RealTimeSequence
from niveristand.clientapi.datatypes import DoubleValue, I32Value, I64Value
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
def modulo_simple_numbers():
    a = DoubleValue(0)
    a.value = 3 % 2
    return a.value


@decorators.nivs_rt_sequence
def modulo_num_nivsdatatype():
    a = DoubleValue(0)
    b = DoubleValue(2)
    a.value = 3 % b.value
    return a.value


@decorators.nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(5) % DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(5) % I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype2():
    a = DoubleValue(0)
    a.value = I32Value(7) % DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype3():
    a = I32Value(0)
    a.value = I32Value(7) % I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_multiple_types():
    a = DoubleValue(0)
    a.value = 7 % DoubleValue(4) % 2
    return a.value


@decorators.nivs_rt_sequence
def modulo_multiple_types1():
    a = I32Value(0)
    a.value = 12 % I32Value(7) % 3
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq():
    a = DoubleValue(0)
    a.value = 6 % return_constant()
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq1():
    a = DoubleValue(0)
    a.value = return_constant() % 2
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq2():
    a = DoubleValue(0)
    a.value = DoubleValue(7) % return_constant()
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq3():
    a = DoubleValue(0)
    a.value = return_constant() % DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(7) % return_constant()
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq5():
    a = DoubleValue(0)
    a.value = return_constant() % I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses():
    a = DoubleValue(0)
    a.value = 5 % (5 % 3)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses1():
    a = DoubleValue(1)
    a.value = 5 % (DoubleValue(5) % I32Value(3))
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses2():
    a = DoubleValue(0)
    a.value = I32Value(11) % (I64Value(11) % I64Value(7)) % DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses3():
    a = DoubleValue(0)
    a.value = I64Value(11) % (I32Value(11) % I32Value(7)) % DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses4():
    a = DoubleValue(0)
    a.value = I32Value(11) % (I64Value(11) % I32Value(7)) % DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses5():
    a = DoubleValue(0)
    a.value = I64Value(11) % (I32Value(11) % I64Value(7)) % DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses6():
    a = DoubleValue(0)
    a.value = I64Value(11) % (I32Value(11) % DoubleValue(7)) % DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses7():
    a = DoubleValue(0)
    a.value = I32Value(11) % (I64Value(11) % DoubleValue(7)) % DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_variables():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 7 % a
    return b.value


@decorators.nivs_rt_sequence
def modulo_variables1():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 7 % a.value
    return b.value


@decorators.nivs_rt_sequence
def modulo_variable_variable():
    a = DoubleValue(5)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value % b.value
    return c.value


@decorators.nivs_rt_sequence
def modulo_variable_variable1():
    a = DoubleValue(5)
    b = I32Value(2)
    c = DoubleValue(0)
    c.value = a.value % b.value
    return c.value


@decorators.nivs_rt_sequence
def modulo_variable_rtseq():
    a = DoubleValue(6)
    b = DoubleValue(0)
    b.value = a.value % return_constant()
    return b.value


@decorators.nivs_rt_sequence
def modulo_variable_rtseq1():
    a = DoubleValue(2)
    b = DoubleValue(0)
    b.value = return_constant() % a.value
    return b.value


@decorators.nivs_rt_sequence
def modulo_with_channelref():
    a = DoubleValue(0)
    a.value = 1 % DoubleValue(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def modulo_binary_unary():
    a = DoubleValue(0)
    a.value = -5 % 2
    return a.value


@decorators.nivs_rt_sequence
def modulo_complex_expr():
    a = DoubleValue(0)
    a.value = 1 % (2 if 2 < 3 else 4)
    return a


# region augassign tests

@decorators.nivs_rt_sequence
def aug_modulo_simple_numbers():
    a = DoubleValue(1)
    a.value %= 2
    return a.value


@decorators.nivs_rt_sequence
def aug_modulo_num_nivsdatatype():
    a = DoubleValue(1)
    a.value %= DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def aug_modulo_use_rtseq():
    a = DoubleValue(6)
    a.value %= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def aug_modulo_with_parantheses():
    a = DoubleValue(5)
    a.value %= (I32Value(2) % 3.0) % DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def aug_modulo_variables():
    a = DoubleValue(5)
    b = DoubleValue(1)
    b.value %= a.value
    return b.value


@decorators.nivs_rt_sequence
def aug_modulo_to_channelref():
    a = DoubleValue(1)
    a.value %= DoubleValue(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def aug_modulo_unary():
    a = DoubleValue(1)
    a.value %= -1
    return a.value


# end region augassign tests

# region invalid tests
@decorators.nivs_rt_sequence
def modulo_invalid_variables():
    return a % b


@decorators.nivs_rt_sequence
def modulo_invalid_variables1():
    return a.value % b.value


@decorators.nivs_rt_sequence
def modulo_invalid_variables2():
    a = DoubleValue(0)
    b = DoubleValue(0)
    b.value = a.value.value % 2
    return b


@decorators.nivs_rt_sequence
def modulo_with_None():
    a = DoubleValue(0)
    a.value = None % 1
    return a


@decorators.nivs_rt_sequence
def modulo_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = return_constant % 1
    return a

# endregion


run_tests = [
    (return_constant, (), 5),
    (modulo_simple_numbers, (), 1),
    (modulo_num_nivsdatatype, (), 1),
    (modulo_nivsdatatype_nivsdatatype, (), 1),
    (modulo_nivsdatatype_nivsdatatype1, (), 1),
    (modulo_nivsdatatype_nivsdatatype2, (), 1),
    (modulo_nivsdatatype_nivsdatatype3, (), 1),
    (modulo_multiple_types, (), 1),
    (modulo_multiple_types1, (), 2),
    (modulo_with_parantheses, (), 1),
    (modulo_with_parantheses1, (), 1),
    (modulo_with_parantheses2, (), 1),
    (modulo_with_parantheses3, (), 1),
    (modulo_with_parantheses4, (), 1),
    (modulo_with_parantheses5, (), 1),
    (modulo_with_parantheses6, (), 1),
    (modulo_with_parantheses7, (), 1),
    (modulo_variables, (), 2),
    (modulo_variables1, (), 2),
    (modulo_variable_variable, (), 1),
    (modulo_variable_variable1, (), 1),
    (aug_modulo_simple_numbers, (), 1),
    (aug_modulo_variables, (), 1),
    (aug_modulo_num_nivsdatatype, (), 1),
    (aug_modulo_with_parantheses, (), 1),
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
]

skip_tests = [
    (modulo_binary_unary, (), "SPE implements remainder. Python implements module. "
                              "The difference is subtle but the sign of the result is different."),
    (aug_modulo_unary, (), "SPE and Python treat negative module differently."),
    (modulo_with_channelref, (), "Not implemented yet."),
    (modulo_invalid_rtseq_call, (), "Not implemented yet."),
    (modulo_invalid_variables2, (), "Attribute transformer doesn't catch the a.value.value problem."),
    (modulo_with_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (aug_modulo_to_channelref, (), "Channel ref transform not yet implemented."),
]

fail_transform_tests = [
    (modulo_invalid_variables, (), TranslateError),
    (modulo_invalid_variables1, (), TranslateError),
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
