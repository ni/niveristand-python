from math import sqrt
import sys
from niveristand import decorators, RealTimeSequence
from niveristand import realtimesequencetools
from niveristand.clientapi.datatypes import BooleanValue, DoubleValue, DoubleValueArray, I32Value
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
def finite_recursion(x):
    res = BooleanValue(False)
    if x < 0:
        res.value = True
        return res.value
    else:
        finite_recursion(x - 1)


@decorators.nivs_rt_sequence
def circular_call_a():
    circular_call_b()


@decorators.nivs_rt_sequence
def circular_call_b():
    circular_call_a()


@decorators.nivs_rt_sequence
def return_parameter(param):
    return param


class FunkyDecorator:
    def __init__(self, a, b):
        pass

    def __call__(self, f):
        return f


@decorators.nivs_rt_sequence
@FunkyDecorator(1, 2)
def return_parameter_invalid_decorator(param):
    return param


@decorators.NivsParam('no_param', DoubleValue(0), decorators.NivsParam.BY_VALUE)
def _return_param_wrong_param_name_pure_python(param):
    return param


@decorators.NivsParam("wrong", I32Value(5), decorators.NivsParam.BY_VALUE)
@decorators.nivs_rt_sequence
def return_parameter_with_decorator_wrong_name(param):
    return param.value


@decorators.NivsParam("param", I32Value(5), decorators.NivsParam.BY_VALUE)
@decorators.nivs_rt_sequence
def return_parameter_with_decorator(param):
    return param.value


@decorators.NivsParam("param", I32Value(5), decorators.NivsParam.BY_REF)
@decorators.nivs_rt_sequence
def return_parameter_with_decorator_byref(param):
    return param.value


@decorators.nivs_rt_sequence
@decorators.NivsParam("param", I32Value(5), decorators.NivsParam.BY_VALUE)
def return_parameter_with_decorator_inverted(param):
    return param.value


@decorators.NivsParam("x", I32Value(5), decorators.NivsParam.BY_VALUE)
@decorators.NivsParam("y", I32Value(5), decorators.NivsParam.BY_VALUE)
@decorators.NivsParam("z", I32Value(5), decorators.NivsParam.BY_REF)
@decorators.nivs_rt_sequence
def return_byref_in_z_sqrt_of_square_x_plus_square_y(x, y, z):
    z.value = sqrt(x.value ** 2 + y.value ** 2)


@decorators.nivs_rt_sequence
def return_arr_element(param):
    return param[0]


@decorators.nivs_rt_sequence
def return_arr_element_plus1_by_ref(param):
    param[0] += 1


@decorators.nivs_rt_sequence
def return_parameter_plus1_byref(param):
    param.value += 1
    return param.value


@decorators.NivsParam('param', DoubleValue(0), decorators.NivsParam.BY_VALUE)
@decorators.nivs_rt_sequence
def return_parameter_plus1_byvalue(param):
    param.value += 1
    return param.value


@decorators.NivsParam('param', DoubleValue(0), False)
@decorators.nivs_rt_sequence
def return_parameter_plus1_byref_bool(param):
    param.value += 1
    return param.value


@decorators.NivsParam('param', DoubleValue(0), True)
@decorators.nivs_rt_sequence
def return_parameter_plus1_byvalue_bool(param):
    param.value += 1
    return param.value


@decorators.nivs_rt_sequence
def call_return_constant_as_assignment():
    a = DoubleValue(0)
    a.value = return_constant()
    return a.value


@decorators.nivs_rt_sequence
def call_return_constant_as_expr():
    a = BooleanValue(0)
    return_constant()
    a.value = True
    return a.value


@decorators.nivs_rt_sequence
def call_return_parameter():
    a = DoubleValue(0)
    a.value = return_parameter(5)
    return a.value


@decorators.nivs_rt_sequence
def call_parameter_nivsdatatype():
    a = DoubleValue(5)
    return_parameter_plus1_byref(a)
    return a.value


@decorators.nivs_rt_sequence
def call_parameter_nivsdatatype_byvalue():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = return_parameter_plus1_byvalue(a)
    return b.value


@decorators.nivs_rt_sequence
def call_parameter_nivsdatatype_byvalue_untouched_orig():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = return_parameter_plus1_byvalue(a) + a.value
    return b.value


@decorators.nivs_rt_sequence
def call_parameter_nivsdatatype_byref_bool_ref():
    a = DoubleValue(5)
    return_parameter_plus1_byref_bool(a)
    return a.value


@decorators.nivs_rt_sequence
def call_parameter_nivsdatatype_byvalue_bool_ref():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = return_parameter_plus1_byvalue_bool(a)
    return b.value


@decorators.nivs_rt_sequence
def call_parameter_builtin_math():
    a = DoubleValue(-5)
    a.value = return_parameter(abs(5))
    return a.value


@decorators.nivs_rt_sequence
def call_parameter_array_elem():
    a = DoubleValueArray([1, 2, 3])
    b = DoubleValue(0)
    b.value = return_arr_element(a)
    return b.value


@decorators.nivs_rt_sequence
def call_parameter_array_elem_byref():
    a = DoubleValueArray([1, 2, 3])
    return a[1]


@decorators.nivs_rt_sequence
def call_parameter_with_decorator_diff_param_type_byvalue():
    a = DoubleValue(1.2)
    b = DoubleValue(0)
    b.value = return_parameter_with_decorator(a.value)
    return b.value


@decorators.nivs_rt_sequence
def call_parameter_with_decorator_diff_param_type_byref():
    a = DoubleValue(1.2)
    b = DoubleValue(0)
    b.value = return_parameter_with_decorator_byref(a.value)
    return b.value


@decorators.nivs_rt_sequence
def call_parameter_with_decorator():
    a = I32Value(1)
    b = I32Value(0)
    b.value = return_parameter_with_decorator(a.value)
    return b.value


@decorators.nivs_rt_sequence
def call_parameter_with_decorator_inverted():
    a = DoubleValue(1.2)
    b = DoubleValue(0)
    b.value = return_parameter_with_decorator_inverted(a.value)
    return b.value


@decorators.nivs_rt_sequence
def call_parameter_with_many_decorators():
    a = DoubleValue(3.1)
    b = DoubleValue(4.999)
    c = I32Value(0)
    return_byref_in_z_sqrt_of_square_x_plus_square_y(a, b, c)
    return c.value


@decorators.nivs_rt_sequence
def call_parameter_send_channel_ref_byvalue():
    a = DoubleValue('mychannel')
    a.value = 1.2
    return_parameter_plus1_byvalue(a)
    return a.value


@decorators.nivs_rt_sequence
def call_parameter_send_channel_ref_byref():
    a = DoubleValue('mychannel')
    a.value = 1.2
    return_parameter_plus1_byref(a)
    return a.value


@decorators.nivs_rt_sequence
def recursive_call():
    recursive_call()


@decorators.nivs_rt_sequence
def invalid_call():
    fake_call()  # noqa: F821 this is supposed to be an undefined call.


def test_param_wrong_name_python():
    from niveristand import errormessages
    with pytest.raises(VeristandError) as e:
        _return_param_wrong_param_name_pure_python(True)
    assert str(e.value) is errormessages.param_description_no_param


run_tests = [
    (return_constant, (), 5),
    (call_return_constant_as_assignment, (), return_constant()),
    (call_return_constant_as_expr, (), True),
    (call_return_parameter, (), 5),
    (call_parameter_nivsdatatype, (), 6),
    (call_parameter_nivsdatatype_byvalue, (), 6),
    (call_parameter_nivsdatatype_byvalue_untouched_orig, (), 11),
    (call_parameter_nivsdatatype_byref_bool_ref, (), 6),
    (call_parameter_nivsdatatype_byvalue_bool_ref, (), 6),
    (call_parameter_builtin_math, (), 5),
    (call_parameter_with_decorator, (), 1),
    (call_parameter_with_decorator_diff_param_type_byvalue, (), 1),
    (call_parameter_with_many_decorators, (), 5),
    (call_parameter_with_decorator_inverted, (), 1),
]

skip_tests = [
    (return_parameter_plus1_byref, (), "This call receives a parameter and it can't be faked without a caller."),
    (return_parameter_plus1_byvalue, (), "This call receives a parameter and it can't be faked without a caller."),
    (return_parameter_plus1_byref_bool, (), "This call receives a parameter and it can't be faked without a caller."),
    (return_parameter_plus1_byvalue_bool, (), "This call receives a parameter and it can't be faked without a caller."),
    (return_parameter, (), "This call receives a parameter and it can't be faked without a caller."),
    (return_parameter_with_decorator, (), "This call receives a parameter and it can't be faked without a caller."),
    (return_parameter_with_decorator_byref, (), "This call receives a parameter and it can't be faked."),
    (return_parameter_with_decorator_inverted, (), "This call receives a parameter and it can't be faked."),
    (return_byref_in_z_sqrt_of_square_x_plus_square_y, (), "This call receives a parameter and it can't be faked."),
    (return_arr_element, (), "This call receives a parameter and it can't be faked without a caller."),
    (return_arr_element_plus1_by_ref, (), "This call receives a parameter and it can't be faked without a caller."),
    (call_parameter_array_elem, (), "Subscript not implemented. Expected: 1"),
    (call_parameter_array_elem_byref, (), "Subscript not implemented. Expected: 2"),
    (call_parameter_send_channel_ref_byref, (), "Channel References not implemented. Expected:2.2"),
    (call_parameter_send_channel_ref_byvalue, (), "Channel References not implemented. Expected:1.2"),
]

fail_transform_tests = [
    (recursive_call, (), RuntimeError),
    (circular_call_a, (), RuntimeError),
    (circular_call_b, (), RuntimeError),
    (finite_recursion, (), RuntimeError),
    (invalid_call, (), TranslateError),
    (return_parameter_with_decorator_wrong_name, [5], TranslateError),
    (return_parameter_invalid_decorator, [1], TranslateError),
    (call_parameter_with_decorator_diff_param_type_byref, (), VeristandError),
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
        pytest.fail('ExpectedException not raised: ' + str(exception))


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
