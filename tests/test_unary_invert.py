import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, DoubleValue, I32Value, I64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
import numpy
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _returns_zero():
    a = I32Value(0)
    return a.value


@nivs_rt_sequence
def invert_bool():
    a = I32Value(0)
    a.value = ~False
    return a.value


@nivs_rt_sequence
def invert_bool_var():
    a = BooleanValue(False)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int32():
    a = I32Value(0)
    a.value = ~0
    return a.value


@nivs_rt_sequence
def invert_int32_1():
    a = I32Value(-1)
    a.value = ~-1
    return a.value


@nivs_rt_sequence
def invert_int32_2():
    a = I32Value(0x7FFFFFFF)
    a.value = ~0x7FFFFFFF
    return a.value


@nivs_rt_sequence
def invert_int32_limit():
    a = I32Value(-0x80000000)
    a.value = ~-0x80000000
    return a.value


@nivs_rt_sequence
def invert_int32_4():
    a = I32Value(-0x7FFFFFFF)
    a.value = ~-0x7FFFFFFF
    return a.value


@nivs_rt_sequence
def invert_int32_var():
    a = I32Value(0)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int32_var_1():
    a = I32Value(-1)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int32_var_2():
    a = I32Value(0x7FFFFFFF)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int32_var_limit():
    a = I32Value(-0x80000000)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int32_var_4():
    a = I32Value(-0x7FFFFFFF)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64():
    a = I64Value(0)
    a.value = ~0
    return a.value


@nivs_rt_sequence
def invert_int64_1():
    a = I64Value(-1)
    a.value = ~-1
    return a.value


@nivs_rt_sequence
def invert_int64_2():
    a = I64Value(0x7FFFFFFFFFFFFFFF)
    a.value = ~0x7FFFFFFFFFFFFFFF
    return a.value


@nivs_rt_sequence
def invert_int64_out_of_spe_range():
    a = I64Value(-0x8000000000000000)
    a.value = ~-0x8000000000000000
    return a.value


@nivs_rt_sequence
def invert_int64_4():
    a = I64Value(-0x7FFFFFFFFFFFFFFF)
    a.value = ~-0x7FFFFFFFFFFFFFFF
    return a.value


@nivs_rt_sequence
def invert_int64_var():
    a = I64Value(0)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64_var_1():
    a = I64Value(-1)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64_var_2():
    a = I64Value(0x7FFFFFFFFFFFFFFF)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64_var_out_of_spe_range():
    a = I64Value(-0x8000000000000000)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64_var_4():
    a = I64Value(-0x7FFFFFFFFFFFFFFF)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64_multiple():
    a = I64Value(-1)
    a.value = ~~a
    return a.value


@nivs_rt_sequence
def invert_int64_multiple1():
    a = I64Value(-1)
    a.value = ~~~a
    return a.value


@nivs_rt_sequence
def invert_int32_multiple():
    a = I32Value(-1)
    a.value = ~~a
    return a.value


@nivs_rt_sequence
def invert_int32_multiple1():
    a = I32Value(-1)
    a.value = ~~~a
    return a.value


@nivs_rt_sequence
def invert_parentheses():
    a = I32Value(0)
    a.value = ~(a)
    return a.value


@nivs_rt_sequence
def invert_rtseq():
    a = I32Value(0)
    a.value = ~_returns_zero()
    return a.value


@nivs_rt_sequence
def invert_double():
    a = DoubleValue(0)
    a.value = ~1.2
    return a.value


@nivs_rt_sequence
def invert_double_var():
    a = DoubleValue(0)
    a.value = ~a
    return a.value


# <editor-fold desc=Invalid tests>

@nivs_rt_sequence
def invert_invalid_variables():
    return ~a


@nivs_rt_sequence
def invert_invalid_variables1():
    return ~a.value


@nivs_rt_sequence
def invert_with_None():
    a = I32Value(0)
    a.value = ~None
    return a


@nivs_rt_sequence
def invert_invalid_rtseq_call():
    a = I32Value(0)
    a.value = ~_returns_zero
    return a

# </editor-fold>


run_tests = [
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
    (invert_bool_var, (), False),  # For RTSeqs, negating a bool or double is always 0
    (invert_double_var, (), 0),  # For RTSeqs, negating a bool or double is always 0
    (invert_int32_limit, (), ~-0x80000000),
    (invert_int32_var_limit, (), ~-0x80000000),
]

fail_transform_tests = [
    (invert_invalid_variables, (), TranslateError),
    (invert_invalid_variables1, (), TranslateError),
    (invert_with_None, (), TranslateError),
    (invert_invalid_rtseq_call, (), VeristandError),
    (invert_bool, (), TranslateError),
    (invert_double, (), TranslateError),
    # SPE doesn't support initializing with the full int32/int64 range.
    (invert_int64_out_of_spe_range, (), VeristandError),
    (invert_int64_var_out_of_spe_range, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


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
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
