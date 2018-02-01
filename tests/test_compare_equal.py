import sys

from niveristand import decorators, RealTimeSequence
from niveristand.clientapi.datatypes import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.exceptions import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation


a = 1
b = 2


@decorators.nivs_rt_sequence
def return_constant():
    a = DoubleValue(5)
    return a.value


@decorators.nivs_rt_sequence
def equal_bool_builtins():
    a = BooleanValue(False)
    a.value = True == True  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def equal_bool_builtins1():
    a = BooleanValue(False)
    a.value = False == False  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def equal_bool_builtins2():
    a = BooleanValue(False)
    a.value = False == a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def equal_bool_builtins3():
    a = BooleanValue(False)
    a.value = True == a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def equal_simple_numbers():
    a = BooleanValue(False)
    a.value = 1 == 1
    return a.value


@decorators.nivs_rt_sequence
def equal_num_nivsdatatype():
    a = BooleanValue(True)
    a.value = 1 == DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype():
    a = BooleanValue(False)
    a.value = DoubleValue(1) == DoubleValue(1)
    return a.value


@decorators.nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype1():
    a = BooleanValue(0)
    a.value = DoubleValue(1) == I32Value(1)
    return a.value


@decorators.nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = I32Value(1) == DoubleValue(1)
    return a.value


@decorators.nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype3():
    a = BooleanValue(0)
    a.value = I32Value(1) == I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def equal_multiple_types():
    a = BooleanValue(0)
    a.value = 1 == DoubleValue(1) == 1.0
    return a.value


@decorators.nivs_rt_sequence
def equal_multiple_types1():
    a = BooleanValue(0)
    a.value = 1 == I32Value(2) == 3.0 == DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def equal_use_rtseq():
    a = BooleanValue(0)
    a.value = 5 == return_constant()
    return a.value


@decorators.nivs_rt_sequence
def equal_use_rtseq1():
    a = BooleanValue(0)
    a.value = return_constant() == 5
    return a.value


@decorators.nivs_rt_sequence
def equal_use_rtseq2():
    a = BooleanValue(0)
    a.value = DoubleValue(5) == return_constant()
    return a.value


@decorators.nivs_rt_sequence
def equal_use_rtseq3():
    a = BooleanValue(0)
    a.value = return_constant() == DoubleValue(5)
    return a.value


@decorators.nivs_rt_sequence
def equal_use_rtseq4():
    a = BooleanValue(0)
    a.value = I32Value(5) == return_constant()
    return a.value


@decorators.nivs_rt_sequence
def equal_use_rtseq5():
    a = BooleanValue(0)
    a.value = return_constant() == I32Value(5)
    return a.value


@decorators.nivs_rt_sequence
def equal_with_parantheses():
    a = BooleanValue(True)
    a.value = 1 == (2 == 3)
    return a.value


@decorators.nivs_rt_sequence
def equal_with_parantheses1():
    a = BooleanValue(True)
    a.value = 1 == (DoubleValue(2) == I32Value(5))
    return a.value


@decorators.nivs_rt_sequence
def equal_with_parantheses2():
    a = BooleanValue(True)
    a.value = DoubleValue(1) == (I32Value(2) == 3.0) == DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def equal_variables():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = 1 == a
    return b.value


@decorators.nivs_rt_sequence
def equal_variables1():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = 1 == a.value
    return b.value


@decorators.nivs_rt_sequence
def equal_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = BooleanValue(True)
    c.value = a.value == b.value
    return c.value


@decorators.nivs_rt_sequence
def equal_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a.value == b.value
    return c.value


@decorators.nivs_rt_sequence
def equal_variable_variable2():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c = a == b
    return c


@decorators.nivs_rt_sequence
def equal_variable_rtseq():
    a = DoubleValue(5)
    b = BooleanValue(0)
    b.value = a.value == return_constant()
    return b.value


@decorators.nivs_rt_sequence
def equal_variable_rtseq1():
    a = DoubleValue(5)
    b = BooleanValue(0)
    b.value = return_constant() == a.value
    return b.value


@decorators.nivs_rt_sequence
def equal_to_channelref():
    a = BooleanValue(True)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    a.value = 1 == b.value
    return a.value


@decorators.nivs_rt_sequence
def equal_binary_unary():
    a = BooleanValue(0)
    a.value = -1 == - 1
    return a.value


@decorators.nivs_rt_sequence
def equal_with_multiple_comparators():
    a = BooleanValue(True)
    a.value = 1 == 2 == 3 == 4
    return a.value


@decorators.nivs_rt_sequence
def equal_complex_expr():
    a = BooleanValue(0)
    a.value = 1 == (1 if 2 < 3 else 4)
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def equal_invalid_variables():
    return a.value == b


@decorators.nivs_rt_sequence
def equal_invalid_variables1():
    return a.value == b.value


@decorators.nivs_rt_sequence
def equal_invalid_variables2():
    a = BooleanValue(0)
    b = DoubleValue(0)
    b.value = a.value == 2
    return b


@decorators.nivs_rt_sequence
def equal_to_None():
    a = BooleanValue(0)
    a.value = None == 1  # noqa: E711 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def equal_invalid_rtseq_call():
    a = BooleanValue(0)
    a.value = return_constant == 1
    return a.value

# end region


run_tests = [
    (return_constant, (), 5),
    (equal_bool_builtins, (), True),
    (equal_bool_builtins1, (), True),
    (equal_bool_builtins2, (), True),
    (equal_bool_builtins3, (), False),
    (equal_simple_numbers, (), True),
    (equal_num_nivsdatatype, (), False),
    (equal_nivsdatatype_nivsdatatype, (), True),
    (equal_nivsdatatype_nivsdatatype1, (), True),
    (equal_nivsdatatype_nivsdatatype2, (), True),
    (equal_nivsdatatype_nivsdatatype3, (), False),
    (equal_multiple_types, (), True),
    (equal_multiple_types1, (), False),
    (equal_with_parantheses, (), False),
    (equal_with_parantheses1, (), False),
    (equal_with_parantheses2, (), False),
    (equal_variables, (), True),
    (equal_variables1, (), True),
    (equal_variable_variable, (), False),
    (equal_variable_variable1, (), True),
    (equal_variable_variable2, (), True),
    (equal_with_multiple_comparators, (), False),
    (equal_binary_unary, (), True),
    (equal_complex_expr, (), True),
    (equal_use_rtseq, (), True),
    (equal_use_rtseq1, (), True),
    (equal_use_rtseq2, (), True),
    (equal_use_rtseq3, (), True),
    (equal_use_rtseq4, (), True),
    (equal_use_rtseq5, (), True),
    (equal_variable_rtseq, (), True),
    (equal_variable_rtseq1, (), True),
    (equal_to_channelref, (), False),
]

skip_tests = [
    (equal_to_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (equal_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
]

fail_transform_tests = [
    (equal_invalid_variables, (), TranslateError),
    (equal_invalid_variables1, (), TranslateError),
    (equal_invalid_variables2, (), TranslateError),
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


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
