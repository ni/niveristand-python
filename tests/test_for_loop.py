import sys
from niveristand import decorators, RealTimeSequence
from niveristand.clientapi.datatypes import DoubleValue, DoubleValueArray, I32Value
from niveristand.exceptions import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation


@decorators.nivs_rt_sequence
def return_constant():
    return 10


@decorators.nivs_rt_sequence
def increment_param_by_ref(param):
    param.value = param.value + 1


@decorators.nivs_rt_sequence
def for_loop_variable_array():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for x in b:
        a.value += x.value
    return a.value


@decorators.nivs_rt_sequence
def for_loop_variable_array1():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for x in b.value:
        a.value += x.value
    return a.value


@decorators.nivs_rt_sequence
def for_loop_modify_collection():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    for x in a.value:
        x.value += 1
    return a[0].value


@decorators.nivs_rt_sequence
def for_loop_modify_elements():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    for x in a.value:
        increment_param_by_ref(x)
    return a[0].value


@decorators.nivs_rt_sequence
def for_loop_constant_array():
    a = DoubleValue(0)
    for x in [1, 2, 3, 4, 5]:
        a.value += x
    return a.value


@decorators.nivs_rt_sequence
def for_loop_range():
    a = DoubleValue(0)
    for x in range(10):
        a.value += x
    return a


@decorators.nivs_rt_sequence
def for_loop_range_with_start():
    a = DoubleValue(0)
    for x in range(2, 10):
        a.value += x
    return a


@decorators.nivs_rt_sequence
def for_loop_range_with_step():
    a = DoubleValue(0)
    for x in range(2, 10, 2):
        a.value += x
    return a


@decorators.nivs_rt_sequence
def for_loop_range_with_variable():
    a = DoubleValue(0)
    b = I32Value(10)
    for x in range(b.value):
        a.value += x
    return a


@decorators.nivs_rt_sequence
def for_loop_range_with_call():
    a = DoubleValue(0)
    for x in range(return_constant()):
        a.value += x
    return a


@decorators.nivs_rt_sequence
def for_loop_iterate_on_array():
    a = DoubleValueArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(10):
        a[0].value += a[i].value
    return a[0].value


@decorators.nivs_rt_sequence
def for_loop_else():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for x in b.value:
        a.value += x
    else:
        a.value = -1
    return a.value


@decorators.nivs_rt_sequence
def nested_for_loop():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for i in range(5):
        for j in b.value:
            a[i].value += j.value
    return a[3].value


@decorators.nivs_rt_sequence
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


@decorators.nivs_rt_sequence
def looping_over_invalid_var():
    a = DoubleValue(0)
    for x in a.value:
        a.value += x
    return a.value


run_tests = [
    (return_constant, (), 10),
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
]


skip_tests = [
    (for_loop_constant_array, (), "Constant parsing not supported in SPE."),
    (increment_param_by_ref, (), "This call receives a parameter and it can't be faked without a caller."),
]

fail_transform_tests = [
    (for_loop_else, (), TranslateError),
    (for_loop_range_with_start, (), TranslateError),
    (for_loop_range_with_step, (), TranslateError),
    (looping_over_invalid_var, (), TranslateError),
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
