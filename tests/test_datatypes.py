import sys

from niveristand import decorators
from niveristand import RealTimeSequence
from niveristand import realtimesequencetools
from niveristand.clientapi.datatypes.rtprimitives import BooleanValue
from niveristand.clientapi.datatypes.rtprimitives import BooleanValueArray
from niveristand.clientapi.datatypes.rtprimitives import DoubleValue
from niveristand.clientapi.datatypes.rtprimitives import DoubleValueArray
from niveristand.clientapi.datatypes.rtprimitives import I32Value
from niveristand.clientapi.datatypes.rtprimitives import I32ValueArray
from niveristand.clientapi.datatypes.rtprimitives import I64Value
from niveristand.clientapi.datatypes.rtprimitives import I64ValueArray
from niveristand.clientapi.datatypes.rtprimitives import U32Value
from niveristand.clientapi.datatypes.rtprimitives import U32ValueArray
from niveristand.clientapi.datatypes.rtprimitives import U64Value
from niveristand.clientapi.datatypes.rtprimitives import U64ValueArray
from niveristand.exceptions import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation


@decorators.nivs_rt_sequence
def boolean_type():
    a = BooleanValue(True)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_type1():
    a = BooleanValue(False)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_type2():
    a = BooleanValue(1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_type3():
    a = BooleanValue(0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_type_run():
    a = BooleanValue(True)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@decorators.nivs_rt_sequence
def boolean_type1_run():
    a = BooleanValue(False)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@decorators.nivs_rt_sequence
def boolean_type2_run():
    a = BooleanValue(1)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@decorators.nivs_rt_sequence
def boolean_type3_run():
    a = BooleanValue(0)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@decorators.nivs_rt_sequence
def illegal_boolean_type():
    a = BooleanValue("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_type():
    a = DoubleValue(5)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_type1():
    a = DoubleValue(5.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_type_run():
    a = DoubleValue(5)
    return a.value


@decorators.nivs_rt_sequence
def double_type1_run():
    a = DoubleValue(5.0)
    return a.value


@decorators.nivs_rt_sequence
def illegal_double_type():
    a = DoubleValue("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_type():
    a = I32Value(2)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_type_run():
    a = I32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def illegal_int32_type():
    a = I32Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_int32_type1():
    a = I32Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_overflow_error():
    a = I32Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_type():
    a = I64Value(2)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_type_run():
    a = I64Value(2)
    return a.value


@decorators.nivs_rt_sequence
def illegal_int64_type():
    a = I64Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_int64_type1():
    a = I64Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_overflow_error():
    a = I64Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_type():
    a = U32Value(2)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_type_run():
    a = U32Value(2)
    return a.value


@decorators.nivs_rt_sequence
def illegal_uint32_type():
    a = U32Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_uint32_type1():
    a = U32Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_overflow_error():
    a = U32Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_type():
    a = U64Value(2)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_type_run():
    a = U64Value(2)
    return a.value


@decorators.nivs_rt_sequence
def illegal_uint64_type():
    a = U64Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_uint64_type1():
    a = U64Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_overflow_error():
    a = U64Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_type_negative():
    a = BooleanValue(-1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_type_negative():
    a = DoubleValue(-5.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_type_negative():
    a = I32Value(-1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_type_negative():
    a = I64Value(-1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_type_negative():
    a = U32Value(-1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_type_negative():
    a = U64Value(-1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_type_negative_run():
    a = BooleanValue(-1)
    return a.value


@decorators.nivs_rt_sequence
def double_type_negative_run():
    a = DoubleValue(-5.0)
    return a.value


@decorators.nivs_rt_sequence
def int32_type_negative_run():
    a = I32Value(-1)
    return a.value


@decorators.nivs_rt_sequence
def int64_type_negative_run():
    a = I64Value(-1)
    return a.value


@decorators.nivs_rt_sequence
def uint32_type_negative_run():
    a = U32Value(-1)
    return a.value


@decorators.nivs_rt_sequence
def uint64_type_negative_run():
    a = U64Value(-1)
    return a.value


@decorators.nivs_rt_sequence
def boolean_array_one_element():
    a = BooleanValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_array_type():
    a = BooleanValueArray([True, False, 1, 0])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_array_empty():
    a = BooleanValueArray([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_array_one_element_run():
    a = BooleanValueArray([1])
    return a[0].value


@decorators.nivs_rt_sequence
def boolean_array_type_run():
    a = BooleanValueArray([True, False, 1, 0])
    return a[3].value


@decorators.nivs_rt_sequence
def boolean_array_invalid_type():
    a = BooleanValueArray([True, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_array_invalid_type1():
    a = BooleanValueArray([True, 'False'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_array_one_element():
    a = DoubleValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_array_type():
    a = DoubleValueArray([0, 1.0, 5.5])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_array_empty():
    a = DoubleValueArray([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_array_one_element_run():
    a = DoubleValueArray([1])
    return a[0].value


@decorators.nivs_rt_sequence
def double_array_type_run():
    a = DoubleValueArray([0, 1.0, 5.5])
    return a[2].value


@decorators.nivs_rt_sequence
def double_array_invalid_type():
    a = DoubleValueArray([5.5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_array_invalid_type1():
    a = DoubleValueArray([5.5, '5.5'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_array_one_element():
    a = I32ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_array_type():
    a = I32ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_array_empty():
    a = I32ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_array_one_element_run():
    a = I32ValueArray([1])
    return a[0].value


@decorators.nivs_rt_sequence
def int32_array_type_run():
    a = I32ValueArray([0, 1, 5])
    return a[2].value


@decorators.nivs_rt_sequence
def int32_array_invalid_type():
    a = I32ValueArray([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_array_invalid_type1():
    a = I32ValueArray([5, '-5'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_array_one_element():
    a = I64ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_array_type():
    a = I64ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_array_empty():
    a = I64ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_array_one_element_run():
    a = I64ValueArray([1])
    return a[0].value


@decorators.nivs_rt_sequence
def int64_array_type_run():
    a = I64ValueArray([0, 1, 5])
    return a[2].value


@decorators.nivs_rt_sequence
def int64_array_invalid_type():
    a = I64ValueArray([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_array_invalid_type1():
    a = I64ValueArray([5, '-5'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_array_one_element():
    a = U32ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_array_type():
    a = U32ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_array_empty():
    a = U32ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_array_one_element_run():
    a = U32ValueArray([1])
    return a[0].value


@decorators.nivs_rt_sequence
def uint32_array_type_run():
    a = U32ValueArray([0, 1, 5])
    return a[2].value


@decorators.nivs_rt_sequence
def uint32_array_invalid_type():
    a = U32ValueArray([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_array_invalid_type1():
    a = U32ValueArray([5, '5'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_array_negative_values():
    a = U32ValueArray([-5, -1])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_array_one_element():
    a = U64ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_array_type():
    a = U64ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_array_one_element_run():
    a = U64ValueArray([1])
    return a[0].value


@decorators.nivs_rt_sequence
def uint64_array_type_run():
    a = U64ValueArray([0, 1, 5])
    return a[2].value


@decorators.nivs_rt_sequence
def uint64_array_empty():
    a = U64ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_array_invalid_type():
    a = U64ValueArray([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_array_invalid_type1():
    a = U64ValueArray([5, '5'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_array_negative_values():
    a = U64ValueArray([-5, -1])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def invalid_return_type():
    return DoubleValueArray([5.0, 1])


@decorators.nivs_rt_sequence
def int32_max_value():
    a = I32Value(0x7FFFFFFF)
    return a.value


@decorators.nivs_rt_sequence
def int32_max_value_overflow():
    a = I32Value(0x80000000)
    return a.value


@decorators.nivs_rt_sequence
def int64_max_value():
    a = I64Value(0x7FFFFFFFFFFFFFFF)
    return a.value


@decorators.nivs_rt_sequence
def int64_max_value_overflow():
    a = I64Value(0x8000000000000000)
    return a.value


@decorators.nivs_rt_sequence
def uint32_max_value():
    a = U32Value(0x7FFFFFFF)
    return a.value


@decorators.nivs_rt_sequence
def uint32_max_value_overflow():
    a = U32Value(0x80000000)
    return a.value


@decorators.nivs_rt_sequence
def uint64_max_value():
    a = U64Value(0x7FFFFFFFFFFFFFFF)
    return a.value


@decorators.nivs_rt_sequence
def uint64_max_value_overflow():
    a = U64Value(0x8000000000000000)
    return a.value


@decorators.nivs_rt_sequence
def int32_array_overflow():
    a = I32ValueArray([0x80000000, 0x80000000])
    return a.value


@decorators.nivs_rt_sequence
def int64_array_overflow():
    a = I64ValueArray([0x8000000000000000, 0x8000000000000000])
    return a.value


@decorators.nivs_rt_sequence
def uint32_array_overflow():
    a = U32ValueArray([0x80000000, 0x80000000])
    return a.value


@decorators.nivs_rt_sequence
def uint64_array_overflow():
    a = U64ValueArray([0x8000000000000000, 0x8000000000000000])
    return a.value


transform_tests = [
    (boolean_type, ()),
    (boolean_type1, ()),
    (boolean_type2, ()),
    (boolean_type3, ()),
    (double_type, ()),
    (double_type1, ()),
    (int32_type, ()),
    (int64_type, ()),
    (uint32_type, ()),
    (uint64_type, ()),
    (boolean_array_type, ()),
    (double_array_type, ()),
    (int32_array_type, ()),
    (int64_array_type, ()),
    (uint32_array_type, ()),
    (uint64_array_type, ()),
    (boolean_array_empty, ()),
    (double_array_empty, ()),
    (int32_array_empty, ()),
    (int64_array_empty, ()),
    (uint32_array_empty, ()),
    (uint64_array_empty, ()),
    (boolean_array_one_element, ()),
    (double_array_one_element, ()),
    (int32_array_one_element, ()),
    (int64_array_one_element, ()),
    (uint32_array_one_element, ()),
    (uint64_array_one_element, ()),
    (boolean_type_negative, ()),
    (double_type_negative, ()),
    (int32_type_negative, ()),
    (int64_type_negative, ()),
    (uint32_array_negative_values, ()),
    (uint64_array_negative_values, ()),
]

run_tests = [
    (boolean_type_run, (), True),
    (boolean_type1_run, (), False),
    (boolean_type2_run, (), True),
    (boolean_type3_run, (), False),
    (double_type_run, (), 5.0),
    (double_type1_run, (), 5.0),
    (int32_type_run, (), 2),
    (int64_type_run, (), 2),
    (uint32_type_run, (), 2),
    (uint64_type_run, (), 2),
    (boolean_type_negative_run, (), True),
    (double_type_negative_run, (), -5.0),
    (int32_type_negative_run, (), -1),
    (int64_type_negative_run, (), -1),
    (int32_max_value, (), 0x7FFFFFFF),
    (int64_max_value, (), 0x7FFFFFFFFFFFFFFF),
    (uint32_max_value, (), 0x7FFFFFFF),
    (uint64_max_value, (), 0x7FFFFFFFFFFFFFFF),
    (boolean_array_type_run, (), False),
    (double_array_type_run, (), 5.5),
    (int32_array_type_run, (), 5),
    (int64_array_type_run, (), 5),
    (uint32_array_type_run, (), 5),
    (uint64_array_type_run, (), 5),
    (boolean_array_one_element_run, (), 1),
    (double_array_one_element_run, (), 1),
    (int32_array_one_element_run, (), 1),
    (int64_array_one_element_run, (), 1),
    (uint32_array_one_element_run, (), 1),
    (uint64_array_one_element_run, (), 1),
]

skip_tests = [

]

fail_transform_tests = [
    (illegal_boolean_type, TranslateError),
    (illegal_double_type, TranslateError),
    (illegal_int32_type, TranslateError),
    (illegal_int32_type1, TranslateError),
    (int32_overflow_error, OverflowError),
    (illegal_int64_type, TranslateError),
    (illegal_int64_type1, TranslateError),
    (int64_overflow_error, OverflowError),
    (illegal_uint32_type, TranslateError),
    (illegal_uint32_type1, TranslateError),
    (uint32_overflow_error, OverflowError),
    (illegal_uint64_type, TranslateError),
    (illegal_uint64_type1, TranslateError),
    (uint64_overflow_error, OverflowError),
    (boolean_array_invalid_type, TranslateError),
    (boolean_array_invalid_type1, TranslateError),
    (double_array_invalid_type, TranslateError),
    (double_array_invalid_type1, TranslateError),
    (int32_array_invalid_type, TranslateError),
    (int32_array_invalid_type1, TranslateError),
    (int64_array_invalid_type, TranslateError),
    (int64_array_invalid_type1, TranslateError),
    (uint32_array_invalid_type, TranslateError),
    (uint32_array_invalid_type1, TranslateError),
    (uint64_array_invalid_type, TranslateError),
    (uint64_array_invalid_type1, TranslateError),
    (invalid_return_type, TranslateError),
    (uint32_type_negative, OverflowError),
    (uint64_type_negative, OverflowError),
    (uint32_type_negative_run, OverflowError),
    (uint64_type_negative_run, OverflowError),
    (int32_max_value_overflow, OverflowError),
    (int64_max_value_overflow, OverflowError),
    (uint32_max_value_overflow, OverflowError),
    (uint64_max_value_overflow, OverflowError),
    (int32_array_overflow, OverflowError),
    (int64_array_overflow, OverflowError),
    (uint32_array_overflow, OverflowError),
    (uint64_array_overflow, OverflowError),
]


def idfunc(val):
    return val.__name__


@pytest.mark.parametrize("func_name, params", transform_tests, ids=idfunc)
def test_transform(func_name, params):
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


@pytest.mark.parametrize("func_name, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, expected_result):
    try:
        RealTimeSequence(func_name)
    except expected_result:
        pass
    except VeristandError as e:
        pytest.fail('Unexpected exception raised:' +
                    str(e.__class__) + ' while expected was: ' + expected_result.__name__)
    except Exception as exception:
        pytest.fail('ExpectedException not raised: ' + exception)


@pytest.mark.parametrize("func_name, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
