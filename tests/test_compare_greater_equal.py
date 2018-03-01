import sys

from niveristand import decorators, RealTimeSequence
from niveristand import realtimesequencetools
from niveristand.clientapi.datatypes import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.exceptions import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@decorators.nivs_rt_sequence
def return_constant():
    a = DoubleValue(5)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_simple_numbers():
    a = BooleanValue(False)
    a.value = 5 >= 1
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_nivsdatatype_num():
    a = BooleanValue(False)
    a.value = DoubleValue(5) >= 2
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_num_nivsdatatype():
    a = BooleanValue(False)
    a.value = 5 >= DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype():
    a = BooleanValue(False)
    a.value = DoubleValue(5) >= DoubleValue(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype1():
    a = BooleanValue(False)
    a.value = DoubleValue(5) >= I32Value(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype2():
    a = BooleanValue(False)
    a.value = I32Value(5) >= DoubleValue(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype3():
    a = BooleanValue(False)
    a.value = I32Value(5) >= I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_multiple_types():
    a = BooleanValue(False)
    a.value = DoubleValue(5) >= 2 >= 1.0
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_multiple_types1():
    a = BooleanValue(False)
    a.value = I32Value(5) >= DoubleValue(4) >= 3 >= 2.0
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq():
    a = BooleanValue(False)
    a.value = 6 >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq1():
    a = BooleanValue(False)
    a.value = return_constant() >= 4
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq2():
    a = BooleanValue(False)
    a.value = DoubleValue(6) >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq3():
    a = BooleanValue(False)
    a.value = return_constant() >= DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq4():
    a = BooleanValue(False)
    a.value = I32Value(6) >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq5():
    a = BooleanValue(False)
    a.value = return_constant() >= I32Value(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_with_parantheses():
    a = BooleanValue(False)
    a.value = 5 >= (3 >= 2)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_variables():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = a >= 1
    return b.value


@decorators.nivs_rt_sequence
def greater_eq_variables1():
    a = DoubleValue(1)
    b = BooleanValue(False)
    b.value = 5 >= a.value
    return b.value


@decorators.nivs_rt_sequence
def greater_eq_variable_variable():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(False)
    c.value = a.value >= b.value
    return c.value


@decorators.nivs_rt_sequence
def greater_eq_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(False)
    c = a >= b
    return c


@decorators.nivs_rt_sequence
def greater_eq_variable_rtseq():
    a = DoubleValue(6.0)
    b = BooleanValue(False)
    b.value = a.value >= return_constant()
    return b.value


@decorators.nivs_rt_sequence
def greater_eq_variable_rtseq1():
    a = DoubleValue(1)
    b = BooleanValue(False)
    b.value = return_constant() >= a.value
    return b.value


@decorators.nivs_rt_sequence
def greater_eq_to_channelref():
    a = BooleanValue(True)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 >= b.value
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_binary_unary():
    a = BooleanValue(False)
    a.value = 2 >= - 1
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_with_multiple_comparators():
    a = BooleanValue(False)
    a.value = 5 >= 4 >= 3 >= 2
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_complex_expr():
    a = BooleanValue(False)
    a.value = 2 >= (1 if 2 < 3 else 4)
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def greater_eq_invalid_variables():
    return a.value >= b


@decorators.nivs_rt_sequence
def greater_eq_invalid_variables1():
    return a.value >= b.value


@decorators.nivs_rt_sequence
def greater_eq_invalid_variables2():
    a = BooleanValue(0)
    b = DoubleValue(0)
    b.value = a.value >= 2
    return b


@decorators.nivs_rt_sequence
def greater_eq_to_None():
    a = BooleanValue(False)
    a.value = None >= 1
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_invalid_rtseq_call():
    a = BooleanValue(False)
    a.value = return_constant >= 1
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_simple_numbers():
    a = BooleanValue(False)
    a.value = 1 >= 1
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_num_nivsdatatype():
    a = BooleanValue(True)
    a.value = DoubleValue(1) >= 2
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype():
    a = BooleanValue(False)
    a.value = DoubleValue(1) >= DoubleValue(1)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype1():
    a = BooleanValue(0)
    a.value = DoubleValue(1) >= I32Value(1)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = I32Value(1) >= DoubleValue(1)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype3():
    a = BooleanValue(0)
    a.value = I32Value(1) >= I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_multiple_types():
    a = BooleanValue(0)
    a.value = DoubleValue(1) >= 1 >= 1.0
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_multiple_types1():
    a = BooleanValue(0)
    a.value = I32Value(1) >= DoubleValue(2) >= 3.0 >= 4
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq():
    a = BooleanValue(0)
    a.value = 5 >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq1():
    a = BooleanValue(0)
    a.value = return_constant() >= 5
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq2():
    a = BooleanValue(0)
    a.value = DoubleValue(5) >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq3():
    a = BooleanValue(0)
    a.value = return_constant() >= DoubleValue(5)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq4():
    a = BooleanValue(0)
    a.value = I32Value(5) >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq5():
    a = BooleanValue(0)
    a.value = return_constant() >= I32Value(5)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_with_parantheses():
    a = BooleanValue(True)
    a.value = 1 >= (2 >= 3)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_with_parantheses1():
    a = BooleanValue(True)
    a.value = 0 >= (DoubleValue(2) >= I32Value(2))
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_variables():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = a >= 1
    return b.value


@decorators.nivs_rt_sequence
def gt_equal_variables1():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = a.value >= 1
    return b.value


@decorators.nivs_rt_sequence
def gt_equal_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = BooleanValue(True)
    c.value = a.value >= b.value
    return c.value


@decorators.nivs_rt_sequence
def gt_equal_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a.value >= b.value
    return c.value


@decorators.nivs_rt_sequence
def gt_equal_variable_variable2():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c = a >= b
    return c


@decorators.nivs_rt_sequence
def gt_equal_variable_rtseq():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = a.value >= return_constant()
    return b.value


@decorators.nivs_rt_sequence
def gt_equal_variable_rtseq1():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = return_constant() >= a.value
    return b.value


@decorators.nivs_rt_sequence
def gt_equal_to_channelref():
    a = BooleanValue(False)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 1.0
    localhost_wait()
    a.value = 1 >= b.value
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_binary_unary():
    a = BooleanValue(0)
    a.value = -1 >= - 1
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_with_multiple_comparators():
    a = BooleanValue(True)
    a.value = 1 >= 2 >= 3 >= 4
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_complex_expr():
    a = BooleanValue(0)
    a.value = 1 >= (1 if 2 < 3 else 4)
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def gt_equal_invalid_variables():
    return a.value >= b


@decorators.nivs_rt_sequence
def gt_equal_invalid_variables1():
    return a.value >= b.value


@decorators.nivs_rt_sequence
def gt_equal_invalid_variables2():
    a = BooleanValue(0)
    b = DoubleValue(0)
    b.value = a.value >= 2
    return b


@decorators.nivs_rt_sequence
def gt_equal_to_None():
    a = BooleanValue(0)
    a.value = None >= 1  # noqa: E711 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_invalid_rtseq_call():
    a = BooleanValue(0)
    a.value = return_constant >= 1
    return a.value

# end region


run_tests = [
    (return_constant, (), 5),
    (greater_eq_simple_numbers, (), True),
    (greater_eq_nivsdatatype_num, (), True),
    (greater_eq_nivsdatatype_nivsdatatype, (), True),
    (greater_eq_nivsdatatype_nivsdatatype1, (), True),
    (greater_eq_nivsdatatype_nivsdatatype2, (), True),
    (greater_eq_nivsdatatype_nivsdatatype3, (), True),
    (greater_eq_with_parantheses, (), True),
    (greater_eq_variables, (), True),
    (greater_eq_variables1, (), True),
    (greater_eq_variable_variable, (), True),
    (greater_eq_variable_variable1, (), True),
    (greater_eq_complex_expr, (), True),
    (greater_eq_binary_unary, (), True),
    (gt_equal_simple_numbers, (), True),
    (gt_equal_num_nivsdatatype, (), False),
    (gt_equal_nivsdatatype_nivsdatatype, (), True),
    (gt_equal_nivsdatatype_nivsdatatype1, (), True),
    (gt_equal_nivsdatatype_nivsdatatype2, (), True),
    (gt_equal_nivsdatatype_nivsdatatype3, (), False),
    (gt_equal_with_parantheses, (), True),
    (gt_equal_with_parantheses1, (), False),
    (gt_equal_variables, (), True),
    (gt_equal_variables1, (), True),
    (gt_equal_variable_variable, (), False),
    (gt_equal_variable_variable1, (), True),
    (gt_equal_variable_variable2, (), True),
    (gt_equal_complex_expr, (), True),
    (gt_equal_binary_unary, (), True),
    (greater_eq_use_rtseq, (), True),
    (greater_eq_use_rtseq1, (), True),
    (greater_eq_use_rtseq2, (), True),
    (greater_eq_use_rtseq3, (), True),
    (greater_eq_use_rtseq4, (), True),
    (greater_eq_use_rtseq5, (), True),
    (greater_eq_variable_rtseq, (), True),
    (greater_eq_variable_rtseq1, (), True),
    (gt_equal_use_rtseq, (), True),
    (gt_equal_use_rtseq1, (), True),
    (gt_equal_use_rtseq2, (), True),
    (gt_equal_use_rtseq3, (), True),
    (gt_equal_use_rtseq4, (), True),
    (gt_equal_use_rtseq5, (), True),
    (gt_equal_variable_rtseq, (), True),
    (gt_equal_variable_rtseq1, (), True),
    (greater_eq_to_channelref, (), False),
    (gt_equal_to_channelref, (), True),
]

skip_tests = [
    (greater_eq_num_nivsdatatype, (), "Builtins as the left comparer can't be overriden"),
    (greater_eq_to_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (greater_eq_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
    (greater_eq_multiple_types, (), "Cascading comparators untested in VM"),
    (greater_eq_multiple_types1, (), "Cascading comparators untested in VM"),
    (greater_eq_with_multiple_comparators, (), "Cascading comparators untested in VM"),
    (gt_equal_to_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (gt_equal_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
    (gt_equal_multiple_types, (), "Cascading comparators untested in VM"),
    (gt_equal_multiple_types1, (), "Cascading comparators untested in VM"),
    (gt_equal_with_multiple_comparators, (), "Cascading comparators untested in VM"),
]

fail_transform_tests = [
    (greater_eq_invalid_variables, (), TranslateError),
    (greater_eq_invalid_variables1, (), TranslateError),
    (greater_eq_invalid_variables2, (), TranslateError),
    (gt_equal_invalid_variables, (), TranslateError),
    (gt_equal_invalid_variables1, (), TranslateError),
    (gt_equal_invalid_variables2, (), TranslateError),
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
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
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
