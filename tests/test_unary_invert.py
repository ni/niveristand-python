import sys

from niveristand import decorators, RealTimeSequence
from niveristand.clientapi.datatypes import BooleanValue, DoubleValue, I32Value, I64Value
from niveristand.exceptions import TranslateError, VeristandError
import numpy
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@decorators.nivs_rt_sequence
def returns_zero():
    a = I32Value(0)
    return a.value


@decorators.nivs_rt_sequence
def invert_bool():
    a = I32Value(0)
    a.value = ~False
    return a.value


@decorators.nivs_rt_sequence
def invert_bool_var():
    a = BooleanValue(False)
    a.value = ~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int32():
    a = I32Value(0)
    a.value = ~0
    return a.value


@decorators.nivs_rt_sequence
def invert_int32_1():
    a = I32Value(-1)
    a.value = ~-1
    return a.value


@decorators.nivs_rt_sequence
def invert_int32_2():
    a = I32Value(0x7FFFFFFF)
    a.value = ~0x7FFFFFFF
    return a.value


@decorators.nivs_rt_sequence
def invert_int32_3():
    a = I32Value(-0x80000000)
    a.value = ~-0x80000000
    return a.value


@decorators.nivs_rt_sequence
def invert_int32_4():
    a = I32Value(-0x7FFFFFFF)
    a.value = ~-0x7FFFFFFF
    return a.value


@decorators.nivs_rt_sequence
def invert_int32_var():
    a = I32Value(0)
    a.value = ~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int32_var_1():
    a = I32Value(-1)
    a.value = ~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int32_var_2():
    a = I32Value(0x7FFFFFFF)
    a.value = ~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int32_var_3():
    a = I32Value(-0x80000000)
    a.value = ~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int32_var_4():
    a = I32Value(-0x7FFFFFFF)
    a.value = ~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int64():
    a = I64Value(0)
    a.value = ~0
    return a.value


@decorators.nivs_rt_sequence
def invert_int64_1():
    a = I64Value(-1)
    a.value = ~-1
    return a.value


@decorators.nivs_rt_sequence
def invert_int64_2():
    a = I64Value(0x7FFFFFFFFFFFFFFF)
    a.value = ~0x7FFFFFFFFFFFFFFF
    return a.value


@decorators.nivs_rt_sequence
def invert_int64_3():
    a = I64Value(-0x8000000000000000)
    a.value = ~-0x8000000000000000
    return a.value


@decorators.nivs_rt_sequence
def invert_int64_4():
    a = I64Value(-0x7FFFFFFFFFFFFFFF)
    a.value = ~-0x7FFFFFFFFFFFFFFF
    return a.value


@decorators.nivs_rt_sequence
def invert_int64_var():
    a = I64Value(0)
    a.value = ~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int64_var_1():
    a = I64Value(-1)
    a.value = ~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int64_var_2():
    a = I64Value(0x7FFFFFFFFFFFFFFF)
    a.value = ~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int64_var_3():
    a = I64Value(-0x8000000000000000)
    a.value = ~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int64_var_4():
    a = I64Value(-0x7FFFFFFFFFFFFFFF)
    a.value = ~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int64_multiple():
    a = I64Value(-1)
    a.value = ~~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int64_multiple1():
    a = I64Value(-1)
    a.value = ~~~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int32_multiple():
    a = I32Value(-1)
    a.value = ~~a
    return a.value


@decorators.nivs_rt_sequence
def invert_int32_multiple1():
    a = I32Value(-1)
    a.value = ~~~a
    return a.value


@decorators.nivs_rt_sequence
def invert_parentheses():
    a = I32Value(0)
    a.value = ~(a)
    return a.value


@decorators.nivs_rt_sequence
def invert_rtseq():
    a = I32Value(0)
    a.value = ~returns_zero()
    return a.value


@decorators.nivs_rt_sequence
def invert_double():
    a = DoubleValue(0)
    a.value = ~1.2
    return a.value


@decorators.nivs_rt_sequence
def invert_double_var():
    a = DoubleValue(0)
    a.value = ~a
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def invert_invalid_variables():
    return ~a


@decorators.nivs_rt_sequence
def invert_invalid_variables1():
    return ~a.value


@decorators.nivs_rt_sequence
def invert_invalid_variables2():
    a = I32Value(0)
    b = I32Value(0)
    b.value = ~a.value.value
    return b.value


@decorators.nivs_rt_sequence
def invert_with_None():
    a = I32Value(0)
    a.value = ~None
    return a


@decorators.nivs_rt_sequence
def invert_invalid_rtseq_call():
    a = I32Value(0)
    a.value = ~returns_zero
    return a
# end region


run_tests = [
    (returns_zero, (), 0),
    (invert_int32, (), -1),
    (invert_int32_1, (), 0),
    (invert_int32_2, (), numpy.int32(-0x80000000)),
    (invert_int32_4, (), numpy.int32(0x7FFFFFFE)),
    (invert_int32_var, (), -1),
    (invert_int32_var_1, (), 0),
    (invert_int32_var_2, (), numpy.int32(-0x80000000)),
    (invert_int32_var_4, (), numpy.int32(0x7FFFFFFE)),
    (invert_int64, (), -1),
    (invert_int64_1, (), 0),
    (invert_int64_2, (), numpy.int64(-0x8000000000000000)),
    (invert_int64_4, (), numpy.int64(0x7FFFFFFFFFFFFFFE)),
    (invert_int64_var, (), -1),
    (invert_int64_var_1, (), 0),
    (invert_int64_var_2, (), numpy.int64(-0x8000000000000000)),
    (invert_int64_var_4, (), numpy.int64(0x7FFFFFFFFFFFFFFE)),
    (invert_int32_multiple, (), -1),
    (invert_int32_multiple1, (), 0),
    (invert_int64_multiple, (), -1),
    (invert_int64_multiple1, (), 0),
    (invert_parentheses, (), -1),
    (invert_rtseq, (), numpy.int32(-1)),
]

skip_tests = [
    (invert_bool, (), "SPE returns 0 for any bitwise negate of a boolean."),
    (invert_int32_3, (), "SPE doesn't support initializing with the full int32 range."),
    (invert_int64_3, (), "SPE doesn't support initializing with the full int64 range."),
    (invert_int32_var_3, (), "SPE doesn't support initializing with the full int64 range."),
    (invert_int64_var_3, (), "SPE doesn't support initializing with the full int64 range."),
    (invert_double, (), "Bitwise operations not supported for floating point types."),
    (invert_invalid_rtseq_call, (), "Not implemented yet."),
    (invert_invalid_variables2, (), "Attribute transformer doesn't catch the a.value.value problem."),
    (invert_with_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
]

fail_transform_tests = [
    (invert_bool_var, (), VeristandError),
    (invert_double_var, (), VeristandError),
    (invert_invalid_variables, (), TranslateError),
    (invert_invalid_variables1, (), TranslateError),
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
