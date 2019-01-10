import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue
from niveristand.clientapi import BooleanValueArray
from niveristand.clientapi import DoubleValue
from niveristand.clientapi import DoubleValueArray
from niveristand.clientapi import I32Value
from niveristand.clientapi import I32ValueArray
from niveristand.clientapi import I64Value
from niveristand.clientapi import I64ValueArray
from niveristand.clientapi import RealTimeSequence
from niveristand.clientapi import U32Value
from niveristand.clientapi import U32ValueArray
from niveristand.clientapi import U64Value
from niveristand.clientapi import U64ValueArray
from niveristand.errors import TranslateError
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def boolean_type():
    a = BooleanValue(True)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type1():
    a = BooleanValue(False)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type2():
    a = BooleanValue(1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type3():
    a = BooleanValue(0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type_run():
    a = BooleanValue(True)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@nivs_rt_sequence
def boolean_type1_run():
    a = BooleanValue(False)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@nivs_rt_sequence
def boolean_type2_run():
    a = BooleanValue(1)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@nivs_rt_sequence
def boolean_type3_run():
    a = BooleanValue(0)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@nivs_rt_sequence
def illegal_boolean_type():
    a = BooleanValue("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_type():
    a = DoubleValue(5)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_type1():
    a = DoubleValue(5.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_type_run():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def double_type1_run():
    a = DoubleValue(5.0)
    return a.value


@nivs_rt_sequence
def illegal_double_type():
    a = DoubleValue("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_type():
    a = I32Value(2)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_type1():
    a = I32Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_type_run():
    a = I32Value(2)
    return a.value


@nivs_rt_sequence
def int32_type1_run():
    a = I32Value(1.0)
    return a.value


@nivs_rt_sequence
def illegal_int32_type():
    a = I32Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_overflow_error():
    a = I32Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_type():
    a = I64Value(2)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_type1():
    a = I64Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_type_run():
    a = I64Value(2)
    return a.value


@nivs_rt_sequence
def int64_type1_run():
    a = I64Value(1.0)
    return a.value


@nivs_rt_sequence
def illegal_int64_type():
    a = I64Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_overflow_error():
    a = I64Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_type():
    a = U32Value(2)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_type1():
    a = U32Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_type_run():
    a = U32Value(2)
    return a.value


@nivs_rt_sequence
def uint32_type1_run():
    a = U32Value(1.0)
    return a.value


@nivs_rt_sequence
def illegal_uint32_type():
    a = U32Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_overflow_error():
    a = U32Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_type():
    a = U64Value(2)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_type1():
    a = U64Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_type_run():
    a = U64Value(2)
    return a.value


@nivs_rt_sequence
def uint64_type1_run():
    a = U64Value(1.0)
    return a.value


@nivs_rt_sequence
def illegal_uint64_type():
    a = U64Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_overflow_error():
    a = U64Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type_negative():
    a = BooleanValue(-1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_type_negative():
    a = DoubleValue(-5.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_type_negative():
    a = I32Value(-1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_type_negative():
    a = I64Value(-1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_type_negative():
    a = U32Value(-1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_type_negative():
    a = U64Value(-1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type_negative_run():
    a = BooleanValue(-1)
    return a.value


@nivs_rt_sequence
def double_type_negative_run():
    a = DoubleValue(-5.0)
    return a.value


@nivs_rt_sequence
def int32_type_negative_run():
    a = I32Value(-1)
    return a.value


@nivs_rt_sequence
def int64_type_negative_run():
    a = I64Value(-1)
    return a.value


@nivs_rt_sequence
def uint32_type_negative_run():
    a = U32Value(-1)
    return a.value


@nivs_rt_sequence
def uint64_type_negative_run():
    a = U64Value(-1)
    return a.value


@nivs_rt_sequence
def boolean_array_one_element():
    a = BooleanValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_array_type():
    a = BooleanValueArray([True, False, 1, 0])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_array_empty():
    a = BooleanValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_array_one_element_run():
    a = BooleanValueArray([1])
    return a[0].value


@nivs_rt_sequence
def boolean_array_type_run():
    a = BooleanValueArray([True, False, 1, 0])
    return a[3].value


@nivs_rt_sequence
def boolean_array_invalid_type():
    a = BooleanValueArray([True, 'something'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_array_invalid_type1():
    a = BooleanValueArray([True, 'False'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_array_one_element():
    a = DoubleValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_array_type():
    a = DoubleValueArray([0, 1.0, 5.5])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_array_empty():
    a = DoubleValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_array_one_element_run():
    a = DoubleValueArray([1])
    return a[0].value


@nivs_rt_sequence
def double_array_type_run():
    a = DoubleValueArray([0, 1.0, 5.5])
    return a[2].value


@nivs_rt_sequence
def double_array_invalid_type():
    a = DoubleValueArray([5.5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_array_invalid_type1():
    a = DoubleValueArray([5.5, '5.5'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_array_one_element():
    a = I32ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_array_type():
    a = I32ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_array_empty():
    a = I32ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_array_one_element_run():
    a = I32ValueArray([1])
    return a[0].value


@nivs_rt_sequence
def int32_array_type_run():
    a = I32ValueArray([0, 1, 5])
    return a[2].value


@nivs_rt_sequence
def int32_array_invalid_type():
    a = I32ValueArray([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_array_invalid_type1():
    a = I32ValueArray([5, '-5'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_array_one_element():
    a = I64ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_array_type():
    a = I64ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_array_empty():
    a = I64ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_array_one_element_run():
    a = I64ValueArray([1])
    return a[0].value


@nivs_rt_sequence
def int64_array_type_run():
    a = I64ValueArray([0, 1, 5])
    return a[2].value


@nivs_rt_sequence
def int64_array_invalid_type():
    a = I64ValueArray([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_array_invalid_type1():
    a = I64ValueArray([5, '-5'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_one_element():
    a = U32ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_type():
    a = U32ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_empty():
    a = U32ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_one_element_run():
    a = U32ValueArray([1])
    return a[0].value


@nivs_rt_sequence
def uint32_array_type_run():
    a = U32ValueArray([0, 1, 5])
    return a[2].value


@nivs_rt_sequence
def uint32_array_invalid_type():
    a = U32ValueArray([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_invalid_type1():
    a = U32ValueArray([5, '5'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_negative_values():
    a = U32ValueArray([-5, -1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_one_element():
    a = U64ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_type():
    a = U64ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_one_element_run():
    a = U64ValueArray([1])
    return a[0].value


@nivs_rt_sequence
def uint64_array_type_run():
    a = U64ValueArray([0, 1, 5])
    return a[2].value


@nivs_rt_sequence
def uint64_array_empty():
    a = U64ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_invalid_type():
    a = U64ValueArray([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_invalid_type1():
    a = U64ValueArray([5, '5'])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_negative_values():
    a = U64ValueArray([-5, -1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def invalid_return_type():
    return DoubleValueArray([5.0, 1])


@nivs_rt_sequence
def int32_max_value():
    a = I32Value(0x7FFFFFFF)
    return a.value


@nivs_rt_sequence
def int32_max_value_overflow():
    a = I32Value(0x800000001)
    return a.value


@nivs_rt_sequence
def int64_max_value():
    a = I64Value(0x7FFFFFFFFFFFFFFF)
    return a.value


@nivs_rt_sequence
def int64_max_value_overflow():
    a = I64Value(0x80000000000000001)
    return a.value


@nivs_rt_sequence
def uint32_max_value():
    a = U32Value(0xFFFFFFFF)
    return a.value


@nivs_rt_sequence
def uint32_max_value_overflow():
    a = U32Value(0x800000001)
    return a.value


@nivs_rt_sequence
def uint64_max_value():
    a = U64Value(0xFFFFFFFFFFFFFFFF)
    return a.value


@nivs_rt_sequence
def uint64_max_value_overflow():
    a = U64Value(0x80000000000000001)
    return a.value


@nivs_rt_sequence
def int32_array_overflow():
    a = I32ValueArray([0x80000000, 0x80000000])
    return a.value


@nivs_rt_sequence
def int64_array_overflow():
    a = I64ValueArray([0x80000000000000001, 0x8000000000000000])
    return a.value


@nivs_rt_sequence
def uint32_array_overflow():
    a = U32ValueArray([0x800000001, 0x80000000])
    return a.value


@nivs_rt_sequence
def uint64_array_overflow():
    a = U64ValueArray([0x80000000000000001, 0x8000000000000000])
    return a.value


transform_tests = [
    (boolean_type, ()),
    (boolean_type1, ()),
    (boolean_type2, ()),
    (boolean_type3, ()),
    (double_type, ()),
    (double_type1, ()),
    (int32_type, ()),
    (int32_type1, ()),
    (int64_type, ()),
    (int64_type1, ()),
    (uint32_type, ()),
    (uint32_type1, ()),
    (uint64_type, ()),
    (uint64_type1, ()),
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
]

run_tests = [
    (boolean_type_run, (), True),
    (boolean_type1_run, (), False),
    (boolean_type2_run, (), True),
    (boolean_type3_run, (), False),
    (double_type_run, (), 5.0),
    (double_type1_run, (), 5.0),
    (int32_type_run, (), 2),
    (int32_type1_run, (), 1),
    (int64_type_run, (), 2),
    (int64_type1_run, (), 1),
    (uint32_type_run, (), 2),
    (uint32_type1_run, (), 1),
    (uint64_type_run, (), 2),
    (uint64_type1_run, (), 1),
    (boolean_type_negative_run, (), True),
    (double_type_negative_run, (), -5.0),
    (int32_type_negative_run, (), -1),
    (int64_type_negative_run, (), -1),
    (int32_max_value, (), 0x7FFFFFFF),
    (int64_max_value, (), 0x7FFFFFFFFFFFFFFF),
    (uint32_max_value, (), 0xFFFFFFFF),
    (uint64_max_value, (), 0xFFFFFFFFFFFFFFFF),
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

fail_transform_tests = [
    (illegal_boolean_type, TranslateError),
    (illegal_double_type, TranslateError),
    (illegal_int32_type, TranslateError),
    (int32_overflow_error, OverflowError),
    (illegal_int64_type, TranslateError),
    (int64_overflow_error, OverflowError),
    (illegal_uint32_type, TranslateError),
    (uint32_overflow_error, OverflowError),
    (illegal_uint64_type, TranslateError),
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
    (uint32_array_negative_values, OverflowError),
    (uint64_array_negative_values, OverflowError),
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
    try:
        return val.__name__
    except AttributeError:
        return str(val)


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
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])


def test_python_only_boolean():
    def return_true():
        return True

    def return_false():
        return False

    def return_one():
        return 1

    def return_string():
        return "string"
    # Boolean datatype creation from other boolean forms
    assert BooleanValue(True).value
    assert BooleanValue(return_true()).value
    assert BooleanValue(not return_false()).value
    assert BooleanValue(BooleanValue(True)).value
    assert BooleanValue(BooleanValue(True).value).value
    assert BooleanValue(BooleanValue(return_true())).value
    assert not BooleanValue(False).value
    assert not BooleanValue(return_false()).value
    assert not BooleanValue(not return_true()).value
    assert not BooleanValue(BooleanValue(False)).value
    assert not BooleanValue(BooleanValue(False).value).value
    assert not BooleanValue(BooleanValue(return_false())).value

    # Boolean datatype creation from numeric forms
    assert BooleanValue(1).value
    assert BooleanValue(return_one()).value
    assert BooleanValue(DoubleValue(1)).value
    assert BooleanValue(DoubleValue(1).value).value

    assert not BooleanValue(0).value
    assert not BooleanValue(DoubleValue(0).value).value
    assert not BooleanValue(DoubleValue(0)).value

    # Boolean datatype creation from expression
    assert BooleanValue(True and True).value
    assert not BooleanValue(False and True).value
    assert BooleanValue(5 < 10).value
    assert not BooleanValue(return_one() > 1).value

    # Boolean datatype creation from array
    assert BooleanValue(BooleanValueArray([True, False])[0]).value
    assert not BooleanValue(([True, False])[1]).value
    assert BooleanValue(BooleanValueArray([True, False])[0].value).value
    assert not BooleanValue(([True, False])[1]).value

    # Boolean datatype creation from strings
    assert BooleanValue('True').value
    assert not BooleanValue('False').value
    assert BooleanValue('true').value
    assert not BooleanValue('false').value

    # Boolean datatype creation that should fail
    with pytest.raises(TypeError):
        BooleanValue('string')
    with pytest.raises(TypeError):
        BooleanValue(object())
    with pytest.raises(TypeError):
        BooleanValue([])
    with pytest.raises(TypeError):
        BooleanValue(BooleanValueArray([True]))


def test_python_only_double():
    def return_true():
        return True

    def return_false():
        return False

    def return_non_zero():
        return 3.14

    def return_string():
        return "string"
    # Double datatype creation from boolean forms
    assert DoubleValue(True).value == 1.0
    assert DoubleValue(return_true()).value == 1.0
    assert DoubleValue(not return_false()).value == 1.0
    assert DoubleValue(DoubleValue(True)).value == 1.0
    assert DoubleValue(DoubleValue(True).value).value == 1.0
    assert DoubleValue(DoubleValue(return_true())).value == 1.0
    assert DoubleValue(False).value == 0.0
    assert DoubleValue(return_false()).value == 0.0
    assert DoubleValue(not return_true()).value == 0.0
    assert DoubleValue(DoubleValue(False)).value == 0.0
    assert DoubleValue(DoubleValue(False).value).value == 0.0
    assert DoubleValue(DoubleValue(return_false())).value == 0.0

    # Double datatype creation from numeric forms
    assert DoubleValue(3.14).value == 3.14
    assert DoubleValue(return_non_zero()).value == return_non_zero()
    assert DoubleValue(DoubleValue(3.14)).value == 3.14
    assert DoubleValue(DoubleValue(3.14).value).value == 3.14

    # Double datatype creation from expression
    assert DoubleValue(2.04 + 1.1).value == 3.14
    assert DoubleValue(False and True).value == 0.0
    assert DoubleValue(5 < 10).value == 1.0
    assert DoubleValue(return_non_zero() > 1).value == 1.0

    # Double datatype creation from array
    assert DoubleValue(DoubleValueArray([1.0, 3.14])[0]).value == 1.0
    assert DoubleValue([1.0, 3.14][1]).value == 3.14

    # Double datatype creation that should fail
    with pytest.raises(TypeError):
        DoubleValue('3.14')
    with pytest.raises(TypeError):
        DoubleValue('string')
    with pytest.raises(TypeError):
        DoubleValue(object())
    with pytest.raises(TypeError):
        DoubleValue([])
    with pytest.raises(TypeError):
        DoubleValue(DoubleValueArray([True]))


def test_python_only_i32():
    def return_true():
        return True

    def return_false():
        return False

    def return_non_zero():
        return 3

    def return_string():
        return "string"
    # I32 datatype creation from boolean forms
    assert I32Value(True).value == 1
    assert I32Value(return_true()).value == 1
    assert I32Value(not return_false()).value == 1
    assert I32Value(I32Value(True)).value == 1
    assert I32Value(I32Value(True).value).value == 1
    assert I32Value(I32Value(return_true())).value == 1
    assert I32Value(False).value == 0
    assert I32Value(return_false()).value == 0
    assert I32Value(not return_true()).value == 0
    assert I32Value(I32Value(False)).value == 0
    assert I32Value(I32Value(False).value).value == 0
    assert I32Value(I32Value(return_false())).value == 0

    # I32 datatype creation from numeric forms
    assert I32Value(3).value == 3
    assert I32Value(3.3).value == 3
    assert I32Value(DoubleValue(3.3)).value == 3
    assert I32Value(return_non_zero()).value == return_non_zero()
    assert I32Value(I32Value(3)).value == 3
    assert I32Value(I32Value(3).value).value == 3

    # I32 datatype creation from expression
    assert I32Value(2 + 1).value == 3
    assert I32Value(False and True).value == 0
    assert I32Value(5 < 10).value == 1
    assert I32Value(return_non_zero() > 1).value == 1

    # I32 datatype creation from array
    assert I32Value(I32ValueArray([1, 3])[0]).value == 1
    assert I32Value([1, 3][1]).value == 3

    # I32 datatype creation that should fail
    with pytest.raises(TypeError):
        I32Value('3')
    with pytest.raises(TypeError):
        I32Value('string')
    with pytest.raises(TypeError):
        I32Value(object())
    with pytest.raises(TypeError):
        I32Value([])
    with pytest.raises(TypeError):
        I32Value(I32ValueArray([True]))


def test_python_only_i64():
    def return_true():
        return True

    def return_false():
        return False

    def return_non_zero():
        return 3

    def return_string():
        return "string"
    # I64 datatype creation from boolean forms
    assert I64Value(True).value == 1
    assert I64Value(return_true()).value == 1
    assert I64Value(not return_false()).value == 1
    assert I64Value(I64Value(True)).value == 1
    assert I64Value(I64Value(True).value).value == 1
    assert I64Value(I64Value(return_true())).value == 1
    assert I64Value(False).value == 0
    assert I64Value(return_false()).value == 0
    assert I64Value(not return_true()).value == 0
    assert I64Value(I64Value(False)).value == 0
    assert I64Value(I64Value(False).value).value == 0
    assert I64Value(I64Value(return_false())).value == 0

    # I64 datatype creation from numeric forms
    assert I64Value(3).value == 3
    assert I64Value(3.3).value == 3
    assert I64Value(DoubleValue(3.3)).value == 3
    assert I64Value(return_non_zero()).value == return_non_zero()
    assert I64Value(I64Value(3)).value == 3
    assert I64Value(I64Value(3).value).value == 3

    # I64 datatype creation from expression
    assert I64Value(2 + 1).value == 3
    assert I64Value(False and True).value == 0
    assert I64Value(5 < 10).value == 1
    assert I64Value(return_non_zero() > 1).value == 1

    # I64 datatype creation from array
    assert I64Value(I64ValueArray([1, 3])[0]).value == 1
    assert I64Value([1, 3][1]).value == 3

    # I64 datatype creation that should fail
    with pytest.raises(TypeError):
        I64Value('3')
    with pytest.raises(TypeError):
        I64Value('string')
    with pytest.raises(TypeError):
        I64Value(object())
    with pytest.raises(TypeError):
        I64Value([])
    with pytest.raises(TypeError):
        I64Value(I64ValueArray([1]))


def test_python_only_u32():
    def return_true():
        return True

    def return_false():
        return False

    def return_non_zero():
        return 3

    def return_string():
        return "string"
    # U32 datatype creation from boolean forms
    assert U32Value(True).value == 1
    assert U32Value(return_true()).value == 1
    assert U32Value(not return_false()).value == 1
    assert U32Value(U32Value(True)).value == 1
    assert U32Value(U32Value(True).value).value == 1
    assert U32Value(U32Value(return_true())).value == 1
    assert U32Value(False).value == 0
    assert U32Value(return_false()).value == 0
    assert U32Value(not return_true()).value == 0
    assert U32Value(U32Value(False)).value == 0
    assert U32Value(U32Value(False).value).value == 0
    assert U32Value(U32Value(return_false())).value == 0

    # U32 datatype creation from numeric forms
    assert U32Value(3).value == 3
    assert U32Value(3.3).value == 3
    assert U32Value(DoubleValue(3.3)).value == 3
    assert U32Value(return_non_zero()).value == return_non_zero()
    assert U32Value(U32Value(3)).value == 3
    assert U32Value(U32Value(3).value).value == 3

    # U32 datatype creation from expression
    assert U32Value(2 + 1).value == 3
    assert U32Value(False and True).value == 0
    assert U32Value(5 < 10).value == 1
    assert U32Value(return_non_zero() > 1).value == 1

    # U32 datatype creation from array
    assert U32Value(U32ValueArray([1, 3])[0]).value == 1
    assert U32Value([1, 3][1]).value == 3

    # U32 datatype creation that should fail
    with pytest.raises(TypeError):
        U32Value('3')
    with pytest.raises(TypeError):
        U32Value('string')
    with pytest.raises(TypeError):
        U32Value(object())
    with pytest.raises(TypeError):
        U32Value([])
    with pytest.raises(TypeError):
        U32Value(U32ValueArray([1]))


def test_python_only_u64():
    def return_true():
        return True

    def return_false():
        return False

    def return_non_zero():
        return 3

    def return_string():
        return "string"
    # U64 datatype creation from boolean forms
    assert U64Value(True).value == 1
    assert U64Value(return_true()).value == 1
    assert U64Value(not return_false()).value == 1
    assert U64Value(U64Value(True)).value == 1
    assert U64Value(U64Value(True).value).value == 1
    assert U64Value(U64Value(return_true())).value == 1
    assert U64Value(False).value == 0
    assert U64Value(return_false()).value == 0
    assert U64Value(not return_true()).value == 0
    assert U64Value(U64Value(False)).value == 0
    assert U64Value(U64Value(False).value).value == 0
    assert U64Value(U64Value(return_false())).value == 0

    # U64 datatype creation from numeric forms
    assert U64Value(3).value == 3
    assert U64Value(3.3).value == 3
    assert U64Value(DoubleValue(3.3)).value == 3
    assert U64Value(return_non_zero()).value == return_non_zero()
    assert U64Value(U64Value(3)).value == 3
    assert U64Value(U64Value(3).value).value == 3

    # U64 datatype creation from expression
    assert U64Value(2 + 1).value == 3
    assert U64Value(False and True).value == 0
    assert U64Value(5 < 10).value == 1
    assert U64Value(return_non_zero() > 1).value == 1

    # U64 datatype creation from array
    assert U64Value(U64ValueArray([1, 3])[0]).value == 1
    assert U64Value([1, 3][1]).value == 3

    # U64 datatype creation that should fail
    with pytest.raises(TypeError):
        U64Value('3')
    with pytest.raises(TypeError):
        U64Value('string')
    with pytest.raises(TypeError):
        U64Value(object())
    with pytest.raises(TypeError):
        U64Value([])
    with pytest.raises(TypeError):
        U64Value(U64ValueArray([1]))
