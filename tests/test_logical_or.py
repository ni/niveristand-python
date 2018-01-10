from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Boolean, Double, Int32, Int64
from niveristand.exceptions import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner

a = 1
b = 2


@decorators.nivs_rt_sequence
def return_true():
    a = Boolean(True)
    return a.value


@decorators.nivs_rt_sequence
def logical_or_simple_numbers():
    a = Double(0)
    a.value = 1 or 2
    return a.value


@decorators.nivs_rt_sequence
def logical_or_simple_numbers1():
    a = Double(0)
    a.value = 1 or 2
    return a.value


@decorators.nivs_rt_sequence
def logical_or_nivsdatatype_double():
    a = Double(0)
    a = Double(3) or Double(1)
    return a.value


@decorators.nivs_rt_sequence
def logical_or_nivsdatatype_int32():
    a = Int32(0)
    a = Int32(2) or Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def logical_or_nivsdatatype_int64():
    a = Int64(0)
    a = Int64(2) or Int64(1)
    return a.value


@decorators.nivs_rt_sequence
def logical_or_nivsdatatype_bool():
    a = Boolean(True)
    a.value = True or False
    return a.value


@decorators.nivs_rt_sequence
def logical_or_multiple_types():
    a = Boolean(False)
    a.value = True or Int32(2) or Double(3) or True
    return a.value


@decorators.nivs_rt_sequence
def logical_or_variables():
    a = Boolean(True)
    b = Boolean(True)
    c = Boolean(False)
    a = b or c
    return a.value


@decorators.nivs_rt_sequence
def logical_or_variables1():
    a = Boolean(True)
    b = Boolean(True)
    c = Boolean(False)
    a.value = b.value or c.value
    return a.value


@decorators.nivs_rt_sequence
def logical_or_rtseq():
    a = Boolean(False)
    a.value = return_true() or True
    return a.value


@decorators.nivs_rt_sequence
def logical_or_rtseq1():
    a = Boolean(False)
    a.value = True or return_true()


@decorators.nivs_rt_sequence
def logical_or_parantheses():
    a = Boolean(True)
    a.value = True or (Double(2) or Int32(3)) or False
    return a.value


@decorators.nivs_rt_sequence
def logical_or_unary():
    a = Boolean(True)
    a.value = 1 or -2
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def logical_or_invalid_variables():
    return a.value or b


@decorators.nivs_rt_sequence
def logical_or_invalid_variables1():
    return a.value or b.value


@decorators.nivs_rt_sequence
def logical_or_None():
    a = Boolean(True)
    a.value = True or None
    return a.value


@decorators.nivs_rt_sequence
def logical_or_invalid_rtseq_call():
    a = Boolean(False)
    a.value = True or return_true
    return a.value


# endregion


run_tests = [
    (logical_or_simple_numbers, (), 1),
    (logical_or_nivsdatatype_bool, (), True),
    (logical_or_multiple_types, (), True),
    (logical_or_variables1, (), True),
    (logical_or_unary, (), True),
    (logical_or_parantheses, (), True),
]

skip_tests = [
    (logical_or_nivsdatatype_double, (), "Or between two constant DataTypes returns a DataType object, we have to"
                                         "research this how to solve it. A solution is to always use variables in"
                                         "logical operators, and use var.value."),
    (logical_or_nivsdatatype_int32, (), "Or between two constant DataTypes returns a DataType object, we have to"
                                        "research this how to solve it. A solution is to always use variables in"
                                        "logical operators, and use var.value."),
    (logical_or_nivsdatatype_int64, (), "Or between two constant DataTypes returns a DataType object, we have to"
                                        "research this how to solve it. A solution is to always use variables in"
                                        "logical operators, and use var.value."),
    (logical_or_simple_numbers1, (), "For 1 && 2 SPE return 1 and Python returns 2. From logical perspective they are"
                                     "equal, but we can't test it only by casting to Boolean. Users should be aware of"
                                     "thi difference when &&-ing numeric types."),
    (logical_or_variables, (), "Or between two constant DataTypes returns a DataType object, we have to"
                               "research this how to solve it. A solution is to always use variables in"
                               "logical operators, and use var.value."),
    (logical_or_rtseq, (), "RTSeq call not implemented yet."),
    (logical_or_rtseq1, (), "RTSeq call not implemented yet."),
    (logical_or_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (logical_or_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
]

fail_transform_tests = [
    (logical_or_invalid_variables, (), TranslateError),
    (logical_or_invalid_variables1, (), TranslateError),
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
