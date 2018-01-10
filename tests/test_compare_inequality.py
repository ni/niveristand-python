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
def notequal_bool_builtins():
    a = Boolean(True)
    a.value = True != True  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def notequal_bool_builtins1():
    a = Boolean(True)
    a.value = False != False  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def notequal_bool_builtins2():
    a = Boolean(False)
    a.value = False != a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def notequal_bool_builtins3():
    a = Boolean(False)
    a.value = True != a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def notequal_simple_numbers():
    a = Boolean(True)
    a.value = 1 != 1
    return a.value


@decorators.nivs_rt_sequence
def notequal_num_nivsdatatype():
    a = Boolean(False)
    a.value = 1 != Double(2)
    return a.value


@decorators.nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype():
    a = Boolean(True)
    a.value = Double(1) != Double(1)
    return a.value


@decorators.nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype1():
    a = Boolean(True)
    a.value = Double(1) != Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype2():
    a = Boolean(True)
    a.value = Int32(1) != Double(1)
    return a.value


@decorators.nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype3():
    a = Boolean(False)
    a.value = Int32(1) != Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def notequal_multiple_types():
    a = Boolean(True)
    a.value = 1 != Double(1) != 1.0
    return a.value


@decorators.nivs_rt_sequence
def notequal_multiple_types1():
    a = Boolean(False)
    a.value = 1 != Int32(2) != 3.0 != Double(4)
    return a.value


@decorators.nivs_rt_sequence
def notequal_use_rtseq():
    a = Boolean(True)
    a.value = 5 != return_constant()
    return a.value


@decorators.nivs_rt_sequence
def notequal_use_rtseq1():
    a = Boolean(True)
    a.value = return_constant() != 5
    return a.value


@decorators.nivs_rt_sequence
def notequal_use_rtseq2():
    a = Boolean(True)
    a.value = Double(5) != return_constant()
    return a.value


@decorators.nivs_rt_sequence
def notequal_use_rtseq3():
    a = Boolean(True)
    a.value = return_constant() != Double(5)
    return a.value


@decorators.nivs_rt_sequence
def notequal_use_rtseq4():
    a = Boolean(False)
    a.value = Int32(1) != return_constant()
    return a.value


@decorators.nivs_rt_sequence
def notequal_use_rtseq5():
    a = Boolean(False)
    a.value = return_constant() != Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def notequal_with_parantheses():
    a = Boolean(False)
    a.value = 0 != (2 != 3)
    return a.value


@decorators.nivs_rt_sequence
def notequal_with_parantheses1():
    a = Boolean(False)
    a.value = 0 != (Double(2) != Int32(5))
    return a.value


@decorators.nivs_rt_sequence
def notequal_with_parantheses2():
    a = Boolean(False)
    a.value = Double(0) != (Int32(2) != 3.0) != Double(4)
    return a.value


@decorators.nivs_rt_sequence
def notequal_variables():
    a = Double(1)
    b = Boolean(True)
    b.value = 1 != a
    return b.value


@decorators.nivs_rt_sequence
def notequal_variables1():
    a = Double(1)
    b = Boolean(True)
    b.value = 1 != a.value
    return b.value


@decorators.nivs_rt_sequence
def notequal_variable_variable():
    a = Double(1)
    b = Double(2)
    c = Boolean(False)
    c.value = a.value != b.value
    return c.value


@decorators.nivs_rt_sequence
def notequal_variable_variable1():
    a = Double(2)
    b = Double(2)
    c = Boolean(True)
    c.value = a.value != b.value
    return c.value


@decorators.nivs_rt_sequence
def notequal_variable_variable2():
    a = Double(2)
    b = Double(2)
    c = Boolean(True)
    c = a != b
    return c


@decorators.nivs_rt_sequence
def notequal_variable_rtseq():
    a = Boolean(False)
    b = Double(0)
    a.value = b.value != return_constant()
    return a.value


@decorators.nivs_rt_sequence
def notequal_variable_rtseq1():
    a = Boolean(False)
    b = Double(0)
    a.value = return_constant() != b.value
    return a.value


@decorators.nivs_rt_sequence
def notequal_to_channelref():
    a = Boolean(False)
    a.value = 1 != Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def notequal_binary_unary():
    a = Boolean(True)
    a.value = -1 != - 1
    return a.value


@decorators.nivs_rt_sequence
def notequal_with_multiple_comparators():
    a = Boolean(False)
    a.value = 1 != 2 != 3 != 4
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def notequal_invalid_variables():
    return a.value != b


@decorators.nivs_rt_sequence
def notequal_invalid_variables1():
    return a.value != b.value


@decorators.nivs_rt_sequence
def notequal_invalid_variables2():
    a = Boolean(0)
    b = Double(0)
    b.value = a.value != 2
    return b


@decorators.nivs_rt_sequence
def notequal_to_None():
    a = Boolean(0)
    a.value = None != 1  # noqa: E711 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def notequal_invalid_rtseq_call():
    a = Boolean(0)
    a.value = return_constant != 1
    return a.value


@decorators.nivs_rt_sequence
def notequal_complex_expr():
    a = Boolean(False)
    a.value = 1 != (2 if 2 < 3 else 4)
    return a.value

# end region


run_tests = [
    (return_constant, (), 5),
    (notequal_bool_builtins, (), False),
    (notequal_bool_builtins1, (), False),
    (notequal_bool_builtins2, (), False),
    (notequal_bool_builtins3, (), True),
    (notequal_simple_numbers, (), False),
    (notequal_num_nivsdatatype, (), True),
    (notequal_nivsdatatype_nivsdatatype, (), False),
    (notequal_nivsdatatype_nivsdatatype1, (), False),
    (notequal_nivsdatatype_nivsdatatype2, (), False),
    (notequal_nivsdatatype_nivsdatatype3, (), True),
    (notequal_with_parantheses, (), True),
    (notequal_with_parantheses1, (), True),
    (notequal_with_parantheses2, (), True),
    (notequal_variables, (), False),
    (notequal_variables1, (), False),
    (notequal_variable_variable, (), True),
    (notequal_variable_variable1, (), False),
    (notequal_variable_variable2, (), False),
    (notequal_with_multiple_comparators, (), True),
    (notequal_binary_unary, (), False),
]

skip_tests = [
    (notequal_use_rtseq, (), "RTSeq call not implemented yet."),
    (notequal_use_rtseq1, (), "RTSeq call not implemented yet."),
    (notequal_use_rtseq2, (), "RTSeq call not implemented yet."),
    (notequal_use_rtseq3, (), "RTSeq call not implemented yet."),
    (notequal_use_rtseq4, (), "RTSeq call not implemented yet."),
    (notequal_use_rtseq5, (), "RTSeq call not implemented yet."),
    (notequal_variable_rtseq, (), "RTSeq call not implemented yet."),
    (notequal_variable_rtseq1, (), "RTSeq call not implemented yet."),
    (notequal_to_channelref, (), "Channel ref transform not yet implemented."),
    (notequal_to_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (notequal_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
    (notequal_multiple_types, (), "SPE and Python treat 1 != 1.0 differently."),
    (notequal_multiple_types1, (), "SPE and Python treat 1 != 1.0 differently."),
    (notequal_complex_expr, (), "IfExp not implemented yet."),
]

fail_transform_tests = [
    (notequal_invalid_variables, (), TranslateError),
    (notequal_invalid_variables1, (), TranslateError),
    (notequal_invalid_variables2, (), TranslateError),
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
