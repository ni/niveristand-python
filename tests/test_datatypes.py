from niveristand import decorators
from niveristand import RealTimeSequence
from niveristand.datatypes.rtprimitives import Boolean
from niveristand.datatypes.rtprimitives import BooleanArray
from niveristand.datatypes.rtprimitives import Double
from niveristand.datatypes.rtprimitives import DoubleArray
from niveristand.datatypes.rtprimitives import Int32
from niveristand.datatypes.rtprimitives import Int32Array
from niveristand.datatypes.rtprimitives import Int64
from niveristand.datatypes.rtprimitives import Int64Array
from niveristand.datatypes.rtprimitives import UInt32
from niveristand.datatypes.rtprimitives import UInt32Array
from niveristand.datatypes.rtprimitives import UInt64
from niveristand.datatypes.rtprimitives import UInt64Array
from niveristand.exceptions import TranslateError, VeristandError
import pytest


@decorators.nivs_rt_sequence
def boolean_type():
    a = Boolean(True)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_type1():
    a = Boolean(False)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_type2():
    a = Boolean(1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_type3():
    a = Boolean(0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_boolean_type():
    a = Boolean("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_type():
    a = Double(5)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_type1():
    a = Double(5.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_double_type():
    a = Double("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_type():
    a = Int32(2)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_int32_type():
    a = Int32("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_int32_type1():
    a = Int32(1.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_overflow_error():
    a = Int32(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_type():
    a = Int64(2)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_int64_type():
    a = Int64("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_int64_type1():
    a = Int64(1.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_overflow_error():
    a = Int64(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_type():
    a = UInt32(2)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_uint32_type():
    a = UInt32("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_uint32_type1():
    a = UInt32(1.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_overflow_error():
    a = UInt32(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_type():
    a = UInt64(2)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_uint64_type():
    a = UInt64("Some string")  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def illegal_uint64_type1():
    a = UInt64(1.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_overflow_error():
    a = UInt64(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_type_negative():
    a = Boolean(-1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_type_negative():
    a = Double(-5.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_type_negative():
    a = Int32(-1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_type_negative():
    a = Int64(-1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_type_negative():
    a = UInt32(-1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_type_negative():
    a = UInt64(-1)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_array_type():
    a = BooleanArray([True, False, 1, 0])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_array_empty():
    a = BooleanArray([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def boolean_array_invalid_type():
    a = BooleanArray([True, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_array_type():
    a = DoubleArray([0, 1.0, 5.5])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_array_empty():
    a = DoubleArray([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_array_invalid_type():
    a = DoubleArray([5.5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_array_type():
    a = Int32Array([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_array_empty():
    a = Int32Array([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int32_array_invalid_type():
    a = Int32Array([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_array_type():
    a = Int64Array([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_array_empty():
    a = Int64Array([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def int64_array_invalid_type():
    a = Int64Array([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_array_type():
    a = UInt32Array([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_array_empty():
    a = UInt32Array([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_array_invalid_type():
    a = UInt32Array([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint32_array_negative_values():
    a = UInt32Array([-5, -1])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_array_type():
    a = UInt64Array([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_array_empty():
    a = UInt64Array([])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_array_invalid_type():
    a = UInt64Array([5, 'something'])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def uint64_array_negative_values():
    a = UInt64Array([-5, -1])  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def invalid_return_type():
    return DoubleArray([5.0, 1])


run_tests = [
    boolean_type,
    boolean_type1,
    boolean_type2,
    boolean_type3,
    double_type,
    double_type1,
    int32_type,
    int64_type,
    uint32_type,
    uint64_type,
    boolean_array_type,
    double_array_type,
    int32_array_type,
    int64_array_type,
    uint32_array_type,
    uint64_array_type,
]

skip_tests = [
    (boolean_type_negative, "Unary operator not implemented yet"),
    (double_type_negative, "Unary operator not implemented yet"),
    (int32_type_negative, "Unary operator not implemented yet"),
    (int64_type_negative, "Unary operator not implemented yet"),
    (uint32_type_negative, "Unary operator not implemented yet"),
    (uint64_type_negative, "Unary operator not implemented yet"),
    (boolean_array_empty, "DE14593"),
    (double_array_empty, "DE14593"),
    (int32_array_empty, "DE14593"),
    (int64_array_empty, "DE14593"),
    (uint32_array_empty, "DE14593"),
    (uint64_array_empty, "DE14593"),
    (uint32_array_negative_values, "Unary operator not implemented yet"),
    (uint64_array_negative_values, "Unary operator not implemented yet"),
]

fail_transform_tests = [
    (illegal_boolean_type, TranslateError),
    (illegal_double_type, TranslateError),
    (illegal_int32_type, TranslateError),
    (illegal_int32_type1, ValueError),
    (int32_overflow_error, OverflowError),
    (illegal_int64_type, TranslateError),
    (illegal_int64_type1, ValueError),
    (int64_overflow_error, OverflowError),
    (illegal_uint32_type, TranslateError),
    (illegal_uint32_type1, ValueError),
    (uint32_overflow_error, OverflowError),
    (illegal_uint64_type, TranslateError),
    (illegal_uint64_type1, ValueError),
    (uint64_overflow_error, OverflowError),
    (boolean_array_invalid_type, TranslateError),
    (double_array_invalid_type, TranslateError),
    (int32_array_invalid_type, TranslateError),
    (int64_array_invalid_type, TranslateError),
    (uint32_array_invalid_type, TranslateError),
    (uint64_array_invalid_type, TranslateError),
    (invalid_return_type, TranslateError),
]


def idfunc(val):
    return val.__name__


@pytest.mark.parametrize("func_name", run_tests, ids=idfunc)
def test_transform(func_name):
    RealTimeSequence(func_name)


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
