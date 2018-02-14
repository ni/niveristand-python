import sys
from niveristand import decorators, RealTimeSequence
from niveristand.clientapi.datatypes import ChannelReference, DoubleValue, I32Value
from niveristand.exceptions import TranslateError, VeristandError
from niveristand.library.builtins import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@decorators.nivs_rt_sequence
def return_constant():
    a = DoubleValue(5)
    return a.value


@decorators.nivs_rt_sequence
def add_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 + 2
    return a.value


@decorators.nivs_rt_sequence
def add_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 1 + DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1) + DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) + I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype2():
    a = DoubleValue(0)
    a.value = I32Value(1) + DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def add_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(1) + I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def add_multiple_types():
    a = DoubleValue(0)
    a.value = 1 + DoubleValue(2) + 3.0
    return a.value


@decorators.nivs_rt_sequence
def add_multiple_types1():
    a = I32Value(0)
    a.value = 1 + I32Value(2) + 3.0 + DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def add_use_rtseq():
    a = DoubleValue(0)
    a.value = 1 + return_constant()
    return a.value


@decorators.nivs_rt_sequence
def add_use_rtseq1():
    a = DoubleValue(0)
    a.value = return_constant() + 1
    return a.value


@decorators.nivs_rt_sequence
def add_use_rtseq2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) + return_constant()
    return a.value


@decorators.nivs_rt_sequence
def add_use_rtseq3():
    a = DoubleValue(0)
    a.value = return_constant() + DoubleValue(1)
    return a.value


@decorators.nivs_rt_sequence
def add_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(1) + return_constant()
    return a.value


@decorators.nivs_rt_sequence
def add_use_rtseq5():
    a = DoubleValue(0)
    a.value = return_constant() + I32Value(1)
    return a.value


@decorators.nivs_rt_sequence
def add_with_parantheses():
    a = DoubleValue(0)
    a.value = 1 + (2 + 3)
    return a.value


@decorators.nivs_rt_sequence
def add_with_parantheses1():
    a = DoubleValue(0)
    a.value = 1 + (DoubleValue(2) + I32Value(5))
    return a.value


@decorators.nivs_rt_sequence
def add_with_parantheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) + (I32Value(2) + 3.0) + DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def add_variables():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 + a
    return b.value


@decorators.nivs_rt_sequence
def add_variables1():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 + a.value
    return b.value


@decorators.nivs_rt_sequence
def add_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value + b.value
    return c.value


@decorators.nivs_rt_sequence
def add_variable_variable1():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value + b.value
    return c.value


@decorators.nivs_rt_sequence
def add_variable_rtseq():
    a = DoubleValue(1)
    b = DoubleValue(0)
    b.value = a.value + return_constant()
    return b.value


@decorators.nivs_rt_sequence
def add_variable_rtseq1():
    a = DoubleValue(1)
    b = DoubleValue(0)
    b.value = return_constant() + a.value
    return b.value


@decorators.nivs_rt_sequence
def add_to_channelref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 + b.value
    return a.value


@decorators.nivs_rt_sequence
def add_binary_unary():
    a = DoubleValue(0)
    a.value = 2 + - 1
    return a.value


@decorators.nivs_rt_sequence
def add_with_multiple_plus():
    a = DoubleValue(0)
    a.value = 1 ++ 2   # noqa: E225 it's ok to test this
    return a.value


@decorators.nivs_rt_sequence
def add_with_multiple_plus1():
    a = DoubleValue(0)
    a.value = 1 +++ 2   # noqa: E225 it's ok to test this
    return a.value


@decorators.nivs_rt_sequence
def add_binary_unary_sequence():
    a = DoubleValue(0)
    a.value = 1+ - - - - - - - - -2  # noqa: E225 it's ok to test this
    return a.value


@decorators.nivs_rt_sequence
def add_complex_expr():
    a = DoubleValue(0)
    a.value = 1 + (2 if 2 < 3 else 4)
    return a.value


# region augassign tests

@decorators.nivs_rt_sequence
def aug_add_simple_numbers():
    a = DoubleValue(1)
    a.value += 2
    return a.value


@decorators.nivs_rt_sequence
def aug_add_num_nivsdatatype():
    a = DoubleValue(1)
    a.value += DoubleValue(2)
    return a.value


@decorators.nivs_rt_sequence
def aug_add_use_rtseq():
    a = DoubleValue(1)
    a.value += return_constant()
    return a.value


@decorators.nivs_rt_sequence
def aug_add_with_parantheses():
    a = DoubleValue(1)
    a.value += (I32Value(2) + 3.0) + DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def aug_add_variables():
    a = DoubleValue(5)
    b = DoubleValue(1)
    b.value += a.value
    return b.value


@decorators.nivs_rt_sequence
def aug_add_to_channelref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value += b.value
    return a.value


@decorators.nivs_rt_sequence
def aug_add_unary():
    a = DoubleValue(1)
    a.value += -1
    return a.value


# end region augassign tests

# region invalid tests
@decorators.nivs_rt_sequence
def add_invalid_variables():
    return a.value + b


@decorators.nivs_rt_sequence
def add_invalid_variables1():
    return a.value + b.value


@decorators.nivs_rt_sequence
def add_invalid_variables2():
    a = DoubleValue(0)
    b = DoubleValue(0)
    b.value = a.value + 2
    return b


@decorators.nivs_rt_sequence
def add_to_None():
    a = DoubleValue(0)
    a.value = None + 1
    return a.value


@decorators.nivs_rt_sequence
def add_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = return_constant + 1
    return a.value

# end region


run_tests = [
    (return_constant, (), 5),
    (add_simple_numbers, (), 3),
    (add_num_nivsdatatype, (), 3),
    (add_nivsdatatype_nivsdatatype, (), 3),
    (add_nivsdatatype_nivsdatatype1, (), 3),
    (add_nivsdatatype_nivsdatatype2, (), 3),
    (add_nivsdatatype_nivsdatatype3, (), 3),
    (add_multiple_types, (), 6),
    (add_multiple_types1, (), 10),
    (add_with_parantheses, (), 6),
    (add_with_parantheses1, (), 8),
    (add_with_parantheses2, (), 10),
    (add_variables, (), 6),
    (add_variables1, (), 6),
    (add_variable_variable, (), 3),
    (add_variable_variable1, (), 3),
    (add_binary_unary, (), 1),
    (aug_add_simple_numbers, (), 3),
    (aug_add_variables, (), 6),
    (aug_add_num_nivsdatatype, (), 3),
    (aug_add_with_parantheses, (), 10),
    (aug_add_unary, (), 0),
    (add_complex_expr, (), 3),
    (add_use_rtseq, (), 6),
    (add_use_rtseq1, (), 6),
    (add_use_rtseq2, (), 6),
    (add_use_rtseq3, (), 6),
    (add_use_rtseq4, (), 6),
    (add_use_rtseq5, (), 6),
    (add_variable_rtseq, (), 6),
    (add_variable_rtseq1, (), 6),
    (aug_add_use_rtseq, (), 6),
    (add_to_channelref, (), 6),
    (aug_add_to_channelref, (), 6),
]

skip_tests = [
    (add_invalid_variables2, (), "Attribute transformer doesn't catch the a.value.value problem."),
    (add_to_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (add_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
    (add_binary_unary_sequence, (), "This test takes 1000x more than the rest. Ignoring for now."),
]

fail_transform_tests = [
    (add_invalid_variables, (), TranslateError),
    (add_invalid_variables1, (), TranslateError),
    (add_with_multiple_plus, (), VeristandError),  # "UnaryAdd not supported by SPE"
    (add_with_multiple_plus1, (), VeristandError),  # "UnaryAdd not supported by SPE"
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
