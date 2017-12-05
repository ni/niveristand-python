from niveristand import decorators
from niveristand import exceptions
from niveristand import RealTimeSequence
from niveristand.datatypes.rtprimitives import Boolean
from niveristand.datatypes.rtprimitives import Double
from niveristand.datatypes.rtprimitives import DoubleArray
from niveristand.datatypes.rtprimitives import Int32
from niveristand.datatypes.rtprimitives import Int64
from niveristand.datatypes.rtprimitives import UInt32
from niveristand.datatypes.rtprimitives import UInt64
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


def test_boolean_type():
    RealTimeSequence(boolean_type)
    RealTimeSequence(boolean_type1)
    RealTimeSequence(boolean_type2)
    RealTimeSequence(boolean_type3)


@decorators.nivs_rt_sequence
def illegal_boolean_type():
    a = Boolean("Some string")  # noqa: F841 it's ok for this variable to never be used


def test_illegal_boolean_type():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(illegal_boolean_type)


@decorators.nivs_rt_sequence
def double_type():
    a = Double(5)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def double_type1():
    a = Double(5.0)  # noqa: F841 it's ok for this variable to never be used


def test_double_type():
    RealTimeSequence(double_type)
    RealTimeSequence(double_type1)


@decorators.nivs_rt_sequence
def illegal_double_type():
    a = Double("Some string")  # noqa: F841 it's ok for this variable to never be used


def test_illegal_double_type():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(illegal_double_type)


@decorators.nivs_rt_sequence
def int32_type():
    a = Int32(2)  # noqa: F841 it's ok for this variable to never be used


def test_int32_type():
    RealTimeSequence(int32_type)


@decorators.nivs_rt_sequence
def illegal_int32_type():
    a = Int32("Some string")  # noqa: F841 it's ok for this variable to never be used


def test_illegal_int32_type():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(illegal_int32_type)


@decorators.nivs_rt_sequence
def illegal_int32_type1():
    a = Int32(1.0)  # noqa: F841 it's ok for this variable to never be used


def test_illegal_int32_type1():
    with pytest.raises(ValueError):
        RealTimeSequence(illegal_int32_type1)


@decorators.nivs_rt_sequence
def int64_type():
    a = Int64(2)  # noqa: F841 it's ok for this variable to never be used


def test_int64_type():
    RealTimeSequence(int64_type)


@decorators.nivs_rt_sequence
def illegal_int64_type():
    a = Int64("Some string")  # noqa: F841 it's ok for this variable to never be used


def test_illegal_int64_type():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(illegal_int64_type)


@decorators.nivs_rt_sequence
def illegal_int64_type1():
    a = Int64(1.0)  # noqa: F841 it's ok for this variable to never be used


def test_illegal_int64_type1():
    with pytest.raises(ValueError):
        RealTimeSequence(illegal_int64_type1)


@decorators.nivs_rt_sequence
def uint32_type():
    a = UInt32(2)  # noqa: F841 it's ok for this variable to never be used


def test_uint32_type():
    RealTimeSequence(uint32_type)


@decorators.nivs_rt_sequence
def illegal_uint32_type():
    a = UInt32("Some string")  # noqa: F841 it's ok for this variable to never be used


def test_illegal_uint32_type():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(illegal_uint32_type)


@decorators.nivs_rt_sequence
def illegal_uint32_type1():
    a = UInt32(1.0)  # noqa: F841 it's ok for this variable to never be used


def test_illegal_uint32_type1():
    with pytest.raises(ValueError):
        RealTimeSequence(illegal_uint32_type1)


@decorators.nivs_rt_sequence
def uint64_type():
    a = UInt64(2)  # noqa: F841 it's ok for this variable to never be used


def test_uint64_type():
    RealTimeSequence(uint64_type)


@decorators.nivs_rt_sequence
def illegal_uint64_type():
    a = UInt64("Some string")  # noqa: F841 it's ok for this variable to never be used


def test_illegal_uint64_type():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(illegal_uint64_type)


@decorators.nivs_rt_sequence
def illegal_uint64_type1():
    a = UInt64(1.0)  # noqa: F841 it's ok for this variable to never be used


def test_illegal_uint64_type1():
    with pytest.raises(ValueError):
        RealTimeSequence(illegal_uint64_type1)


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


@pytest.mark.skip(reason="Unary operator not implemented yet")
def test_datatypes_negative():
    RealTimeSequence(boolean_type_negative)
    RealTimeSequence(double_type_negative)
    RealTimeSequence(int32_type_negative)
    RealTimeSequence(int64_type_negative)
    RealTimeSequence(uint32_type_negative)
    RealTimeSequence(uint64_type_negative)


@decorators.nivs_rt_sequence
def double_array_type():
    a = DoubleArray([0, 1.0, 5.5])  # noqa: F841 it's ok for this variable to never be used


def test_double_array_type():
    RealTimeSequence(double_array_type)


@decorators.nivs_rt_sequence
def double_array_empty():
    a = DoubleArray([])  # noqa: F841 it's ok for this variable to never be used


def test_double_array_empty():
    RealTimeSequence(double_array_empty)


@decorators.nivs_rt_sequence
def double_array_invalid_type():
    a = DoubleArray([5.5, 'something'])  # noqa: F841 it's ok for this variable to never be used


def test_double_array_invalid_type():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(double_array_invalid_type)
