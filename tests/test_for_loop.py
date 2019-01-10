import sys
from niveristand import nivs_rt_sequence, NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import ChannelReference, DoubleValue, DoubleValueArray, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import arraysize, localhost_wait
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def _return_constant():
    return 10


@nivs_rt_sequence
def _increment_param_by_ref(param):
    param.value = param.value + 1


@nivs_rt_sequence
def for_loop_variable_array():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for x in b:
        a.value += x.value
    return a.value


@nivs_rt_sequence
def for_loop_variable_array1():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for x in b.value:
        a.value += x.value
    return a.value


@nivs_rt_sequence
def for_loop_modify_collection():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    for x in a.value:
        x.value += 1
    return a[0].value


@nivs_rt_sequence
def for_loop_modify_elements():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    for x in a.value:
        _increment_param_by_ref(x)
    return a[0].value


@nivs_rt_sequence
def for_loop_constant_array():
    a = DoubleValue(0)
    for x in [1, 2, 3, 4, 5]:
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_range():
    a = DoubleValue(0)
    for x in range(10):
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_range_with_start():
    a = DoubleValue(0)
    for x in range(2, 10):
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_range_with_step():
    a = DoubleValue(0)
    for x in range(2, 10, 2):
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_range_with_variable():
    a = DoubleValue(0)
    b = I32Value(10)
    for x in range(b.value):
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_range_with_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference('Aliases/DesiredRPM')
    b.value = 10.0
    localhost_wait(0.2)
    for x in range(b.value):
        a.value += x
    return a


@nivs_rt_sequence
def for_loop_range_with_call():
    a = DoubleValue(0)
    for x in range(_return_constant()):
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_iterate_on_array():
    a = DoubleValueArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(10):
        a[0].value += a[i].value
    return a[0].value


@nivs_rt_sequence
def for_loop_else():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for x in b.value:
        a.value += x
    else:
        a.value = -1
    return a.value


@nivs_rt_sequence
def nested_for_loop():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for i in range(5):
        for j in b.value:
            a[i].value += j.value
    return a[3].value


@nivs_rt_sequence
def nested_for_loop_body():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for i in range(5):
        for j in b.value:
            if j.value % 2 == 0:
                a[i].value += j.value
            else:
                a[i].value -= j.value
    return a[3].value


@nivs_rt_sequence
def looping_over_invalid_var():
    a = DoubleValue(0)
    for x in a.value:
        a.value += x
    return a.value


@nivs_rt_sequence
def for_return_in_body():
    for i in range(5):
        return i


@nivs_rt_sequence
def for_try_in_body():
    for i in range(5):
        try:
            pass
        finally:
            pass


@nivs_rt_sequence
def for_funcdef_in_body():
    for i in range(5):
        def func():
            pass
        pass


@nivs_rt_sequence
@NivsParam('array', DoubleValueArray([0]), NivsParam.BY_REF)
def _average(array):
    average_var = DoubleValue(0)
    for x in array:
        average_var.value += x.value
    average_var.value /= arraysize(array.value)
    return average_var.value


@nivs_rt_sequence
def call_average():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    res = DoubleValue(0)
    res.value = _average(a)
    return res.value


run_tests = [
    (for_loop_variable_array, (), 15),
    (for_loop_variable_array1, (), 15),
    (for_loop_modify_collection, (), 2),
    (for_loop_modify_elements, (), 2),
    (for_loop_range, (), 45),
    (for_loop_range_with_variable, (), 45),
    (for_loop_range_with_call, (), 45),
    (for_loop_iterate_on_array, (), 45),
    (nested_for_loop, (), 19),
    (nested_for_loop_body, (), 1),
    (call_average, (), 3),
]

fail_transform_tests = [
    (for_loop_else, (), TranslateError),
    (for_loop_range_with_start, (), TranslateError),
    (for_loop_range_with_step, (), TranslateError),
    (looping_over_invalid_var, (), TranslateError),
    (for_return_in_body, (), TranslateError),
    (for_try_in_body, (), TranslateError),
    (for_funcdef_in_body, (), TranslateError),
    (for_loop_range_with_channel_ref, (), VeristandError),
    (for_loop_constant_array, (), VeristandError),
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
