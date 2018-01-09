from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Boolean, Double, Int32
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
def greater_simple_numbers():
    a = Boolean(False)
    a.value = 5 > 1
    return a.value


@decorators.nivs_rt_sequence
def greater_nivsdatatype_num():
    a = Boolean(False)
    a.value = Double(5) > 2
    return a.value


@decorators.nivs_rt_sequence
def greater_num_nivsdatatype():
    a = Boolean(False)
    a.value = 5 > Double(2)
    return a.value


@decorators.nivs_rt_sequence
def greater_nivsdatatype_nivsdatatype():
    a = Boolean(False)
    a.value = Double(5) > Double(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_nivsdatatype_nivsdatatype1():
    a = Boolean(False)
    a.value = Double(5) > Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_nivsdatatype_nivsdatatype2():
    a = Boolean(False)
    a.value = Int32(5) > Double(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_nivsdatatype_nivsdatatype3():
    a = Boolean(False)
    a.value = Int32(5) > Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def greater_multiple_types():
    a = Boolean(False)
    a.value = Double(5) > 2 > 1.0
    return a.value


@decorators.nivs_rt_sequence
def greater_multiple_types1():
    a = Boolean(False)
    a.value = Int32(5) > Double(4) > 3 > 2.0
    return a.value


@decorators.nivs_rt_sequence
def greater_use_rtseq():
    a = Boolean(False)
    a.value = 5 > return_constant()
    return a.value


@decorators.nivs_rt_sequence
def greater_use_rtseq1():
    a = Boolean(False)
    a.value = return_constant() > 4
    return a.value


@decorators.nivs_rt_sequence
def greater_use_rtseq2():
    a = Boolean(False)
    a.value = Double(6) > return_constant()
    return a.value


@decorators.nivs_rt_sequence
def greater_use_rtseq3():
    a = Boolean(False)
    a.value = return_constant() > Double(4)
    return a.value


@decorators.nivs_rt_sequence
def greater_use_rtseq4():
    a = Boolean(False)
    a.value = Int32(6) > return_constant()
    return a.value


@decorators.nivs_rt_sequence
def greater_use_rtseq5():
    a = Boolean(False)
    a.value = return_constant() > Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_with_parantheses():
    a = Boolean(False)
    a.value = 5 > (3 > 2)
    return a.value


@decorators.nivs_rt_sequence
def greater_variables():
    a = Double(5)
    b = Boolean(False)
    b.value = a > 1
    return b.value


@decorators.nivs_rt_sequence
def greater_variables1():
    a = Double(1)
    b = Boolean(False)
    b.value = 5 > a.value
    return b.value


@decorators.nivs_rt_sequence
def greater_variable_variable():
    a = Double(2)
    b = Double(1)
    c = Boolean(False)
    c.value = a.value > b.value
    return c.value


@decorators.nivs_rt_sequence
def greater_variable_variable1():
    a = Double(2)
    b = Double(1)
    c = Boolean(False)
    c = a > b
    return c


@decorators.nivs_rt_sequence
def greater_variable_rtseq():
    a = Double(6.0)
    b = Boolean(False)
    b.value = a.value > return_constant()
    return b.value


@decorators.nivs_rt_sequence
def greater_variable_rtseq1():
    a = Double(1)
    b = Boolean(False)
    b.value = return_constant() > a.value
    return b.value


@decorators.nivs_rt_sequence
def greater_to_channelref():
    a = Boolean(False)
    a.value = 5 > Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def greater_binary_unary():
    a = Boolean(False)
    a.value = 2 > - 1
    return a.value


@decorators.nivs_rt_sequence
def greater_with_multiple_comparators():
    a = Boolean(False)
    a.value = 5 > 4 > 3 > 2
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def greater_invalid_variables():
    return a.value > b


@decorators.nivs_rt_sequence
def greater_invalid_variables1():
    return a.value > b.value


@decorators.nivs_rt_sequence
def greater_invalid_variables2():
    a = Boolean(0)
    b = Double(0)
    b.value = a.value > 2
    return b


@decorators.nivs_rt_sequence
def greater_to_None():
    a = Boolean(False)
    a.value = None > 1
    return a.value


@decorators.nivs_rt_sequence
def greater_invalid_rtseq_call():
    a = Boolean(False)
    a.value = return_constant > 1
    return a.value


@decorators.nivs_rt_sequence
def greater_complex_expr():
    a = Boolean(False)
    a.value = 1 > (2 if 2 < 3 else 4)
    return a.value

# end region


run_tests = [
    (return_constant, (), 5),
    (greater_simple_numbers, (), True),
    (greater_nivsdatatype_num, (), True),
    (greater_nivsdatatype_nivsdatatype, (), True),
    (greater_nivsdatatype_nivsdatatype1, (), True),
    (greater_nivsdatatype_nivsdatatype2, (), True),
    (greater_nivsdatatype_nivsdatatype3, (), True),
    (greater_with_parantheses, (), True),
    (greater_variables, (), True),
    (greater_variables1, (), True),
    (greater_variable_variable, (), True),
    (greater_variable_variable1, (), True),
]

skip_tests = [
    (greater_num_nivsdatatype, (), "Builtins as the left comparer can't be overriden"),
    (greater_use_rtseq, (), "RTSeq call not implemented yet."),
    (greater_use_rtseq1, (), "RTSeq call not implemented yet."),
    (greater_use_rtseq2, (), "RTSeq call not implemented yet."),
    (greater_use_rtseq3, (), "RTSeq call not implemented yet."),
    (greater_use_rtseq4, (), "RTSeq call not implemented yet."),
    (greater_use_rtseq5, (), "RTSeq call not implemented yet."),
    (greater_variable_rtseq, (), "RTSeq call not implemented yet."),
    (greater_variable_rtseq1, (), "RTSeq call not implemented yet."),
    (greater_to_channelref, (), "Channel ref transform not yet implemented."),
    (greater_binary_unary, (), "Unary operator not implemented."),
    (greater_to_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (greater_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
    (greater_complex_expr, (), "Not implemented yet."),
    (greater_multiple_types, (), "Cascading comparators untested in VM"),
    (greater_multiple_types1, (), "Cascading comparators untested in VM"),
    (greater_with_multiple_comparators, (), "Cascading comparators untested in VM"),
]

fail_transform_tests = [
    (greater_invalid_variables, (), TranslateError),
    (greater_invalid_variables1, (), TranslateError),
    (greater_invalid_variables2, (), TranslateError),
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
