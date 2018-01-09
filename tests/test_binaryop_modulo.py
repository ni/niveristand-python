import sys

from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Double, Int32, Int64
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
def modulo_simple_numbers():
    a = Double(0)
    a.value = 3 % 2
    return a.value


@decorators.nivs_rt_sequence
def modulo_num_nivsdatatype():
    a = Double(0)
    b = Double(2)
    a.value = 3 % b.value
    return a.value


@decorators.nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype():
    a = Double(0)
    a.value = Double(5) % Double(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype1():
    a = Double(0)
    a.value = Double(5) % Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype2():
    a = Double(0)
    a.value = Int32(7) % Double(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype3():
    a = Int32(0)
    a.value = Int32(7) % Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_multiple_types():
    a = Double(0)
    a.value = 7 % Double(4) % 2
    return a.value


@decorators.nivs_rt_sequence
def modulo_multiple_types1():
    a = Int32(0)
    a.value = 12 % Int32(7) % 3
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq():
    a = Double(0)
    a.value = 6 % return_constant()
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq1():
    a = Double(0)
    a.value = return_constant() % 2
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq2():
    a = Double(0)
    a.value = Double(7) % return_constant()
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq3():
    a = Double(0)
    a.value = return_constant() % Double(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq4():
    a = Double(0)
    a.value = Int32(7) % return_constant()
    return a.value


@decorators.nivs_rt_sequence
def modulo_use_rtseq5():
    a = Double(0)
    a.value = return_constant() % Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses():
    a = Double(0)
    a.value = 5 % (5 % 3)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses1():
    a = Double(1)
    a.value = 5 % (Double(5) % Int32(3))
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses2():
    a = Double(0)
    a.value = Int32(11) % (Int64(11) % Int64(7)) % Double(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses3():
    a = Double(0)
    a.value = Int64(11) % (Int32(11) % Int32(7)) % Double(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses4():
    a = Double(0)
    a.value = Int32(11) % (Int64(11) % Int32(7)) % Double(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses5():
    a = Double(0)
    a.value = Int64(11) % (Int32(11) % Int64(7)) % Double(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses6():
    a = Double(0)
    a.value = Int64(11) % (Int32(11) % Double(7)) % Double(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_with_parantheses7():
    a = Double(0)
    a.value = Int32(11) % (Int64(11) % Double(7)) % Double(2)
    return a.value


@decorators.nivs_rt_sequence
def modulo_variables():
    a = Double(5)
    b = Double(0)
    b.value = 7 % a
    return b.value


@decorators.nivs_rt_sequence
def modulo_variables1():
    a = Double(5)
    b = Double(0)
    b.value = 7 % a.value
    return b.value


@decorators.nivs_rt_sequence
def modulo_variable_variable():
    a = Double(5)
    b = Double(2)
    c = Double(0)
    c.value = a.value % b.value
    return c.value


@decorators.nivs_rt_sequence
def modulo_variable_variable1():
    a = Double(5)
    b = Int32(2)
    c = Double(0)
    c.value = a.value % b.value
    return c.value


@decorators.nivs_rt_sequence
def modulo_variable_rtseq():
    a = Double(6)
    b = Double(0)
    b.value = a.value % return_constant()
    return b.value


@decorators.nivs_rt_sequence
def modulo_variable_rtseq1():
    a = Double(1)
    b = Double(0)
    b.value = return_constant() % a.value
    return b.value


@decorators.nivs_rt_sequence
def modulo_with_channelref():
    a = Double(0)
    a.value = 1 % Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def modulo_binary_unary():
    a = Double(0)
    a.value = -5 % 2
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def modulo_invalid_variables():
    return a % b


@decorators.nivs_rt_sequence
def modulo_invalid_variables1():
    return a.value % b.value


@decorators.nivs_rt_sequence
def modulo_invalid_variables2():
    a = Double(0)
    b = Double(0)
    b.value = a.value.value % 2
    return b


@decorators.nivs_rt_sequence
def modulo_with_None():
    a = Double(0)
    a.value = None % 1
    return a


@decorators.nivs_rt_sequence
def modulo_invalid_rtseq_call():
    a = Double(0)
    a.value = return_constant % 1
    return a


@decorators.nivs_rt_sequence
def modulo_complex_expr():
    a = Double(0)
    a.value = 1 % (2 if 2 < 3 else 4)
    return a

# endregion


run_tests = [
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
]

skip_tests = [
    (modulo_with_channelref, (), "Not implemented yet."),
    (modulo_binary_unary, (), "SPE implements remainder. Python implements module. "
                              "The difference is subtle but the sign of the result is different."),
    (modulo_invalid_rtseq_call, (), "Not implemented yet."),
    (modulo_complex_expr, (), "Not implemented yet."),
    (modulo_invalid_variables2, (), "Attribute transformer doesn't catch the a.value.value problem."),
    (modulo_with_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (modulo_variable_rtseq, (), "RTseq call not yet implemented."),
    (modulo_variable_rtseq1, (), "RTseq call not yet implemented"),
    (modulo_use_rtseq, (), "RTseq call not yet implemented."),
    (modulo_use_rtseq1, (), "RTseq call not yet implemented."),
    (modulo_use_rtseq2, (), "RTseq call not yet implemented."),
    (modulo_use_rtseq3, (), "RTseq call not yet implemented."),
    (modulo_use_rtseq4, (), "RTseq call not yet implemented."),
    (modulo_use_rtseq5, (), "RTseq call not yet implemented."),
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
