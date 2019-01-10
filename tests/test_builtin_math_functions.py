from math import acos, acosh, asin, asinh, atan, atan2, atanh, ceil, cos, cosh, exp, expm1, floor, fmod, hypot, isnan, \
    log, log10, log1p, pi, sin, sinh, sqrt, tan, tanh
import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value, I64Value, U32Value, U64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.library.primitives import localhost_wait
import numpy
import pytest
from testutilities import rtseqrunner, validation

if sys.version_info > (3, 2):
    from math import log2
else:
    def log2(x):
        return log(x, 2)


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(-5)
    return a.value


# <editor-fold desc=Abs tests>

@nivs_rt_sequence
def abs_simple_number():
    a = DoubleValue(0)
    a.value = abs(-5)
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype_value():
    a = DoubleValue(0)
    a.value = abs(DoubleValue(-5).value)
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype():
    a = DoubleValue(0)
    a.value = abs(DoubleValue(-5))
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype1():
    a = I32Value(0)
    a.value = abs(I32Value(-5))
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype2():
    a = DoubleValue(0)
    a.value = abs(I64Value(-5))
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype3():
    a = DoubleValue(0)
    a.value = abs(U32Value(5))
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype4():
    a = DoubleValue(0)
    a.value = abs(U64Value(5))
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype5():
    a = DoubleValue(0)
    a.value = abs(BooleanValue(5))
    return a.value


@nivs_rt_sequence
def abs_variable_double():
    a = DoubleValue(0)
    b = DoubleValue(-5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_variable_i32():
    a = I32Value(0)
    b = I32Value(-5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_variable_i64():
    a = I64Value(0)
    b = I64Value(-5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_variable_u32():
    a = U32Value(0)
    b = U32Value(5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_variable_u64():
    a = U64Value(0)
    b = U64Value(5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_variable_boolean():
    a = BooleanValue(0)
    b = BooleanValue(-5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = -5.0
    localhost_wait()
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_call_rtseq():
    a = DoubleValue(0)
    a.value = abs(_return_constant())
    return a.value


@nivs_rt_sequence
def abs_expr():
    a = DoubleValue(0)
    a.value = abs(1 - 2)
    return a.value


@nivs_rt_sequence
def abs_expr_parentheses():
    a = DoubleValue(0)
    a.value = abs(2 * (2 - 3))
    return a.value


@nivs_rt_sequence
def abs_ifexpr():
    a = DoubleValue(0)
    a.value = abs(1 if True else 2)
    return a.value


@nivs_rt_sequence
def abs_builtin():
    a = DoubleValue(0)
    a.value = abs(abs(-5))
    return a.value

# </editor-fold>


@nivs_rt_sequence
def acos_double():
    a = DoubleValue(0)
    b = DoubleValue(0)
    a.value = acos(b.value)
    return a.value


@nivs_rt_sequence
def acosh_double():
    a = DoubleValue(1)
    b = DoubleValue(1)
    a.value = acosh(b.value)
    return a.value


@nivs_rt_sequence
def asin_double():
    a = DoubleValue(1)
    b = DoubleValue(1)
    a.value = asin(b.value)
    return a.value


@nivs_rt_sequence
def asinh_double():
    a = DoubleValue(1)
    b = DoubleValue(0)
    a.value = asinh(b.value)
    return a.value


@nivs_rt_sequence
def atan_double():
    a = DoubleValue(1)
    b = DoubleValue(0)
    a.value = atan(b.value)
    return a.value


@nivs_rt_sequence
def atan2_double():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = DoubleValue(-2)
    a.value = atan2(c.value, b.value)
    return a.value


@nivs_rt_sequence
def atanh_double():
    a = DoubleValue(1)
    b = DoubleValue(0)
    a.value = atanh(b.value)
    return a.value


@nivs_rt_sequence
def ceil_double():
    a = DoubleValue(0)
    b = DoubleValue(1.2)
    a.value = ceil(b.value)
    return a.value


@nivs_rt_sequence
def ceil_double_negative():
    a = DoubleValue(0)
    b = DoubleValue(-1.2)
    a.value = ceil(b.value)
    return a.value


@nivs_rt_sequence
def cos_double():
    a = DoubleValue(0)
    b = DoubleValue(0)
    a.value = cos(b.value)
    return a.value


@nivs_rt_sequence
def cosh_double():
    a = DoubleValue(0)
    b = DoubleValue(0)
    a.value = cosh(b.value)
    return a.value


@nivs_rt_sequence
def exp_double():
    a = DoubleValue(0)
    b = DoubleValue(0)
    a.value = exp(b.value)
    return a.value


@nivs_rt_sequence
def expm1_double():
    a = DoubleValue(1)
    b = DoubleValue(0)
    a.value = expm1(b.value)
    return a.value


@nivs_rt_sequence
def floor_double():
    a = DoubleValue(5.7)
    a.value = floor(a.value)
    return a.value


@nivs_rt_sequence
def hypot_double():
    a = DoubleValue(4)
    b = DoubleValue(3)
    a.value = hypot(a.value, b.value)
    return a.value


@nivs_rt_sequence
def isnan_double():
    a = DoubleValue(0)
    b = BooleanValue(False)
    b.value = isnan(a.value)
    return b.value


@nivs_rt_sequence
def ln_double():
    a = DoubleValue(1)
    a.value = log(exp(a.value))
    return a.value


@nivs_rt_sequence
def lnp1_double():
    a = DoubleValue(0)
    a.value = expm1(10)
    a.value = log1p(a.value)
    return a.value


@nivs_rt_sequence
def log_double():
    a = DoubleValue(27.0)
    b = DoubleValue(3)
    a.value = log(a.value, b.value)
    return a.value


@nivs_rt_sequence
def log10_double():
    a = DoubleValue(1000)
    a.value = log10(a.value)
    return a.value


@nivs_rt_sequence
def log2_double():
    a = DoubleValue(1024)
    a.value = log2(a.value)
    return a.value


@nivs_rt_sequence
def max_double():
    a = DoubleValue(1024)
    b = DoubleValue(2048)
    a.value = max(b.value, a.value)
    return a.value


@nivs_rt_sequence
def min_double():
    a = DoubleValue(1024)
    b = DoubleValue(2048)
    a.value = min(b.value, a.value)
    return a.value


@nivs_rt_sequence
def mod_double():
    a = DoubleValue(3)
    b = DoubleValue(-2048)
    a.value = fmod(b.value, a.value)
    return a.value


@nivs_rt_sequence
def pow_double():
    a = DoubleValue(3.0)
    b = DoubleValue(3)
    a.value = pow(a.value, b.value)
    return a.value


@nivs_rt_sequence
def round_double():
    a = DoubleValue(3.7)
    a.value = round(a.value)
    return a.value


@nivs_rt_sequence
def sin_double():
    a = DoubleValue(0)
    a.value = pi / 2
    a.value = sin(a.value)
    return a.value


@nivs_rt_sequence
def sinh_double():
    a = DoubleValue(0)
    a.value = pi
    a.value = sinh(a.value)
    return a.value


@nivs_rt_sequence
def sqrt_double():
    a = DoubleValue(25)
    a.value = sqrt(a.value)
    return a.value


@nivs_rt_sequence
def tan_double():
    a = DoubleValue(0)
    a.value = pi / 2
    a.value = tan(a.value)
    return a.value


@nivs_rt_sequence
def tanh_double():
    a = DoubleValue(0)
    a.value = pi
    a.value = tanh(a.value)
    return a.value


run_tests = [
    (abs_nivsdatatype_value, (), 5),
    (abs_simple_number, (), 5),
    (abs_variable_double, (), 5.0),
    (abs_variable_i32, (), numpy.int32(5)),
    (abs_variable_i64, (), numpy.int64(5)),
    (abs_variable_u32, (), numpy.uint32(5)),
    (abs_variable_u64, (), numpy.uint64(5)),
    (abs_call_rtseq, (), 5),
    (abs_expr, (), 1.0),
    (abs_expr_parentheses, (), 2.0),
    (abs_ifexpr, (), 1.0),
    (abs_builtin, (), 5.0),
    (acos_double, (), pi / 2),
    (acosh_double, (), 0.0),
    (asin_double, (), pi / 2),
    (asinh_double, (), 0.0),
    (atan_double, (), 0.0),
    (atan2_double, (), -pi / 4),
    (atanh_double, (), 0.0),
    (ceil_double, (), 2.0),
    (ceil_double_negative, (), -1.0),
    (cos_double, (), 1.0),
    (cosh_double, (), 1),
    (exp_double, (), 1),
    (expm1_double, (), 0),
    (floor_double, (), 5.0),
    (hypot_double, (), 5.0),
    (isnan_double, (), False),
    (log10_double, (), 3),
    (ln_double, (), log(exp(1))),
    (lnp1_double, (), 10),
    (log_double, (), 3),
    (log2_double, (), 10),
    (max_double, (), 2048),
    (min_double, (), 1024),
    (mod_double, (), 1.0),
    (pow_double, (), 27),
    (round_double, (), 4),
    (sin_double, (), 1),
    (sinh_double, (), sinh(pi)),
    (sqrt_double, (), 5),
    (tan_double, (), tan(pi / 2)),
    (tanh_double, (), tanh(pi)),
    (abs_channel_ref, (), 5.0),
    (abs_variable_boolean, (), False),
]

transform_tests = run_tests + [
    (abs_nivsdatatype, (), 5),
    (abs_nivsdatatype1, (), 5),
    (abs_nivsdatatype2, (), 5),
    (abs_nivsdatatype3, (), 5),
    (abs_nivsdatatype4, (), 5),
    (abs_nivsdatatype5, (), 5),
]

py_only_different_behavior_tests = [
    (abs_variable_boolean, (), False),
    (mod_double, (), 1.0),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", transform_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", list(set(run_tests) -
                                                                    set(py_only_different_behavior_tests)), ids=idfunc)
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


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
