from math import sqrt
import sys
from niveristand import nivs_rt_sequence, NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, DoubleValueArray, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def finite_recursion(x):
    res = BooleanValue(False)
    if x < 0:
        res.value = True
    else:
        finite_recursion(x - 1)
    return res.value


@nivs_rt_sequence
def circular_call_a():
    circular_call_b()


@nivs_rt_sequence
def circular_call_b():
    circular_call_a()


@NivsParam('param', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def _return_parameter(param):
    return param.value


class FunkyDecorator:
    def __init__(self, a, b):
        pass

    def __call__(self, f):
        return f


@nivs_rt_sequence
@FunkyDecorator(1, 2)
def return_parameter_invalid_decorator(param):
    return param


@NivsParam('no_param', DoubleValue(0), NivsParam.BY_VALUE)
def _return_param_wrong_param_name_pure_python(param):
    return param


@NivsParam("wrong", I32Value(5), NivsParam.BY_VALUE)
@nivs_rt_sequence
def return_parameter_with_decorator_wrong_name(param):
    return param.value


@NivsParam("param", I32Value(5), NivsParam.BY_VALUE)
@nivs_rt_sequence
def _return_parameter_with_decorator(param):
    return param.value


@NivsParam("param", I32Value(5), NivsParam.BY_REF)
@nivs_rt_sequence
def _return_parameter_with_decorator_by_ref(param):
    return param.value


@nivs_rt_sequence
@NivsParam("param", I32Value(5), NivsParam.BY_VALUE)
def _return_parameter_with_decorator_inverted(param):
    return param.value


@NivsParam("x", I32Value(5), NivsParam.BY_VALUE)
@NivsParam("y", I32Value(5), NivsParam.BY_VALUE)
@NivsParam("z", I32Value(5), NivsParam.BY_REF)
@nivs_rt_sequence
def _return_by_ref_in_z_sqrt_of_square_x_plus_square_y(x, y, z):
    z.value = sqrt(x.value ** 2 + y.value ** 2)


@NivsParam('param', DoubleValueArray([0]), NivsParam.BY_REF)
@nivs_rt_sequence
def _return_arr_element(param):
    return param[0].value


@nivs_rt_sequence
def _return_arr_element_plus1_by_ref(param):
    param[0].value += 1


@nivs_rt_sequence
def _return_parameter_plus1_by_ref(param):
    param.value += 1
    return param.value


@NivsParam('param', DoubleValue(0), NivsParam.BY_VALUE)
@nivs_rt_sequence
def _return_parameter_plus1_by_value(param):
    param.value += 1
    return param.value


@NivsParam('param', DoubleValue(0), False)
@nivs_rt_sequence
def _return_parameter_plus1_by_ref_bool(param):
    param.value += 1
    return param.value


@NivsParam('param', DoubleValue(0), True)
@nivs_rt_sequence
def _return_parameter_plus1_by_value_bool(param):
    param.value += 1
    return param.value


@NivsParam('param', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def _increment_constant_passed_by_ref(param):
    param.value += 1
    return param.value


@NivsParam('mod', DoubleValue(0), NivsParam.BY_VALUE)
@nivs_rt_sequence
def _return_parameter_with_built_in_function_name(mod):
    return mod.value


@nivs_rt_sequence
def call_increment_constant_passed_by_ref():
    a = DoubleValue(0)
    a.value = _increment_constant_passed_by_ref(5)
    return a.value


@nivs_rt_sequence
def call_return_constant_as_assignment():
    a = DoubleValue(0)
    a.value = _return_constant()
    return a.value


@nivs_rt_sequence
def call_return_constant_as_expr():
    a = BooleanValue(0)
    _return_constant()
    a.value = True
    return a.value


@nivs_rt_sequence
def call_return_parameter():
    a = DoubleValue(0)
    a.value = _return_parameter(DoubleValue(5))
    return a.value


@nivs_rt_sequence
def call_parameter_nivsdatatype():
    a = DoubleValue(5)
    _return_parameter_plus1_by_ref(a)
    return a.value


@nivs_rt_sequence
def call_parameter_nivsdatatype_by_value():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = _return_parameter_plus1_by_value(a)
    return b.value


@nivs_rt_sequence
def call_parameter_nivsdatatype_by_value_untouched_orig():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = _return_parameter_plus1_by_value(a) + a.value
    return b.value


@nivs_rt_sequence
def call_parameter_nivsdatatype_by_ref_bool_ref():
    a = DoubleValue(5)
    _return_parameter_plus1_by_ref_bool(a)
    return a.value


@nivs_rt_sequence
def call_parameter_nivsdatatype_by_value_bool_ref():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = _return_parameter_plus1_by_value_bool(a) + a.value
    return b.value


@nivs_rt_sequence
def call_parameter_builtin_math():
    a = DoubleValue(-5)
    a.value = _return_parameter(abs(a.value))
    return a.value


@nivs_rt_sequence
def call_parameter_array_elem():
    a = DoubleValueArray([1, 2, 3])
    b = DoubleValue(0)
    b.value = _return_arr_element(a)
    return b.value


@nivs_rt_sequence
def call_parameter_array_elem_by_ref():
    a = DoubleValueArray([1, 2, 3])
    return a[1].value


@nivs_rt_sequence
def call_parameter_with_decorator_diff_param_type_by_value():
    a = DoubleValue(1.2)
    b = DoubleValue(0)
    b.value = _return_parameter_with_decorator(a.value)
    return b.value


@nivs_rt_sequence
def call_parameter_with_decorator_diff_param_type_by_ref():
    a = DoubleValue(1.2)
    b = DoubleValue(0)
    b.value = _return_parameter_with_decorator_by_ref(a.value)
    return b.value


@nivs_rt_sequence
def call_parameter_with_decorator():
    a = I32Value(1)
    b = I32Value(0)
    b.value = _return_parameter_with_decorator(a.value)
    return b.value


@nivs_rt_sequence
def call_parameter_with_decorator_inverted():
    a = DoubleValue(1.2)
    b = DoubleValue(0)
    b.value = _return_parameter_with_decorator_inverted(a.value)
    return b.value


@nivs_rt_sequence
def call_parameter_with_many_decorators():
    a = DoubleValue(3.1)
    b = DoubleValue(4.999)
    c = I32Value(0)
    _return_by_ref_in_z_sqrt_of_square_x_plus_square_y(a, b, c)
    return c.value


@nivs_rt_sequence
def call_parameter_send_channel_ref_by_value():
    a = ChannelReference('Aliases/DesiredRPM')
    ret = DoubleValue(0)
    a.value = 67
    localhost_wait(0.5)
    _return_parameter_plus1_by_value(a)
    ret.value = a.value
    return ret.value


@nivs_rt_sequence
def call_parameter_send_channel_ref_by_ref():
    a = ChannelReference('Aliases/DesiredRPM')
    ret = DoubleValue(0)
    a.value = 101.2
    localhost_wait(0.5)
    _return_parameter_plus1_by_ref(a)
    localhost_wait(0.5)
    ret.value = a.value
    return ret.value


@nivs_rt_sequence
def recursive_call():
    recursive_call()


@nivs_rt_sequence
def invalid_call():
    fake_call()  # noqa: F821 this is supposed to be an undefined call.


@nivs_rt_sequence
def call_return_parameter_with_built_in_function_name():
    a = DoubleValue(1)
    a.value = _return_parameter_with_built_in_function_name(a.value)
    return a.value


def test_param_wrong_name_python():
    from niveristand import _errormessages
    with pytest.raises(VeristandError) as e:
        _return_param_wrong_param_name_pure_python(True)
    assert str(e.value) is _errormessages.param_description_no_param


@nivs_rt_sequence
def constant_passed_by_ref_is_not_actually_by_ref():
    a = DoubleValue(5)
    _increment_constant_passed_by_ref(a.value)
    return a.value


@NivsParam('param', DoubleValue(0), NivsParam.BY_REF)
def _increment_constant_passed_by_ref_without_rt_decorator(param):
    param.value += 1
    return param.value


def test_constant_passed_by_ref_without_rt_decorator():
    a = DoubleValue(5)
    _increment_constant_passed_by_ref_without_rt_decorator(a.value)
    assert a.value == 5


def test_object_passed_by_ref_without_rt_decorator():
    a = DoubleValue(5)
    _increment_constant_passed_by_ref_without_rt_decorator(a)
    assert a.value == 6


run_tests = [
    (call_return_constant_as_assignment, (), _return_constant()),
    (call_return_constant_as_expr, (), True),
    (call_return_parameter, (), 5),
    (call_parameter_nivsdatatype, (), 6),
    (call_parameter_nivsdatatype_by_value, (), 6),
    (call_parameter_nivsdatatype_by_value_untouched_orig, (), 11),
    (call_parameter_nivsdatatype_by_ref_bool_ref, (), 6),
    (call_parameter_nivsdatatype_by_value_bool_ref, (), 11),
    (call_parameter_builtin_math, (), 5),
    (call_parameter_with_decorator, (), 1),
    (call_parameter_with_decorator_diff_param_type_by_value, (), 1),
    (call_parameter_with_many_decorators, (), 5),
    (call_parameter_with_decorator_inverted, (), 1),
    (call_parameter_array_elem, (), 1),
    (call_parameter_array_elem_by_ref, (), 2),
    (call_parameter_send_channel_ref_by_ref, (), 102.2),
    (call_parameter_send_channel_ref_by_value, (), 67),
    (call_increment_constant_passed_by_ref, (), 6),
    (call_return_parameter_with_built_in_function_name, (), 1)
]

python_tests = run_tests + [
    (constant_passed_by_ref_is_not_actually_by_ref, (), 5)
]

fail_transform_tests = [
    (recursive_call, (), RuntimeError),
    (circular_call_a, (), RuntimeError),
    (circular_call_b, (), RuntimeError),
    (finite_recursion, (), RuntimeError),
    (invalid_call, (), TranslateError),
    (return_parameter_with_decorator_wrong_name, [5], VeristandError),
    (return_parameter_invalid_decorator, [1], TranslateError),
    (call_parameter_with_decorator_diff_param_type_by_ref, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", python_tests, ids=idfunc)
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
