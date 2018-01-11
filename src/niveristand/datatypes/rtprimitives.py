from NationalInstruments.VeriStand.Data import BooleanValue
from NationalInstruments.VeriStand.Data import BooleanValueArray
from NationalInstruments.VeriStand.Data import DoubleValue
from NationalInstruments.VeriStand.Data import DoubleValueArray
from NationalInstruments.VeriStand.Data import I32Value
from NationalInstruments.VeriStand.Data import I32ValueArray
from NationalInstruments.VeriStand.Data import I64Value
from NationalInstruments.VeriStand.Data import I64ValueArray
from NationalInstruments.VeriStand.Data import U32Value
from NationalInstruments.VeriStand.Data import U32ValueArray
from NationalInstruments.VeriStand.Data import U64Value
from NationalInstruments.VeriStand.Data import U64ValueArray
from niveristand import errormessages
from niveristand import exceptions as nivsexceptions
import numpy


def get_class_by_name(name):
    return VALID_TYPES[name]


def is_supported_data_type(name):
    return name in VALID_TYPES


def is_supported_return_type(name):
    return name in VALID_RETURN_TYPES


class DataType:
    def __init__(self, value, description="", units=""):
        self._data_value = self._to_data_value(value)

    def __str__(self):
        return str(self._data_value)

    def _to_data_value(self, value):
        raise nivsexceptions.TranslateError(errormessages.invalid_type_to_convert)

    @staticmethod
    def _is_compatible_with_datatype(other):
        return isinstance(other, (int, float, numpy.int32, numpy.int64, numpy.long))

    def __add__(self, other):
        if isinstance(other, DataType):
            return self.value + other.value
        elif isinstance(other, (int, float)):
            return self.value + other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, DataType):
            return self.value - other.value
        elif isinstance(other, (int, float)):
            return self.value - other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __rsub__(self, other):
        if isinstance(other, DataType):
            return other.value - self.value
        elif isinstance(other, (int, float)):
            return other - self.value
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __mul__(self, other):
        if isinstance(other, DataType):
            return self.value * other.value
        elif isinstance(other, (int, float)):
            return self.value * other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __divmod__(self, other):
        if isinstance(other, DataType):
            return self.value / other.value
        elif isinstance(other, (int, float)):
            return self.value / other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __rdivmod__(self, other):
        if isinstance(other, DataType):
            return other.value / self.value
        elif isinstance(other, (int, float)):
            return other / self.value
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __floordiv__(self, other):
        if isinstance(other, DataType):
            return self.value // other.value
        elif isinstance(other, (int, float)):
            return self.value // other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __rfloordiv__(self, other):
        if isinstance(other, DataType):
            return other.value // self.value
        elif isinstance(other, (int, float)):
            return other // self.value
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __truediv__(self, other):
        if isinstance(other, DataType):
            return self.value / other.value
        elif isinstance(other, (int, float)):
            return self.value / other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __rtruediv__(self, other):
        if isinstance(other, DataType):
            return other.value / self.value
        elif isinstance(other, (int, float)):
            return other / self.value
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __div__(self, other):
        if isinstance(other, DataType):
            return self.value / other.value
        elif isinstance(other, (int, float)):
            return self.value / other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __rdiv__(self, other):
        if isinstance(other, DataType):
            return other.value / self.value
        elif isinstance(other, (int, float)):
            return other / self.value

    def __pow__(self, power, modulo=None):
        if isinstance(power, DataType):
            return self.value ** power.value
        elif isinstance(power, (int, float)):
            return self.value ** power
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __rpow__(self, other):
        if isinstance(other, DataType):
            return other.value ** self.value
        elif isinstance(other, (int, float)):
            return other ** self.value
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __mod__(self, other):
        if isinstance(other, DataType):
            return self.value % other.value
        elif isinstance(other, (int, float, numpy.int32, numpy.int64, numpy.long)):
            return self.value % other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __rmod__(self, other):
        if isinstance(other, DataType):
            return other.value % self.value
        elif isinstance(other, (int, float, numpy.int32, numpy.int64, numpy.long)):
            return other % self.value
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __and__(self, other):
        if isinstance(other, (Int32, Int64)):
            return self.value & other.value
        elif isinstance(other, (int, numpy.long, numpy.int32, numpy.int64)):
            return self.value & other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __rand__(self, other):
        return self.__and__(other)

    def __eq__(self, other):
        if isinstance(other, DataType):
            return self.value == other.value
        elif isinstance(other, (int, float, bool, numpy.bool_)):
            return self.value == other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __ne__(self, other):
        if isinstance(other, DataType):
            return self.value != other.value
        elif self._is_compatible_with_datatype(other):
            return self.value != other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __gt__(self, other):
        if isinstance(other, DataType):
            return self.value > other.value
        elif self._is_compatible_with_datatype(other):
            return self.value > other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __ge__(self, other):
        if isinstance(other, DataType):
            return self.value >= other.value
        elif self._is_compatible_with_datatype(other):
            return self.value >= other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    def __lt__(self, other):
        if isinstance(other, DataType):
            return self.value < other.value
        elif self._is_compatible_with_datatype(other):
            return self.value < other
        else:
            raise nivsexceptions.VeristandError(errormessages.invalid_type_for_operator)

    @property
    def value(self):
        return self._data_value.Value

    @value.setter
    def value(self, value):
        self._data_value = self._to_data_value(value)


class ArrayType(DataType):
    def _to_data_value(self, value):
        raise nivsexceptions.TranslateError(errormessages.invalid_type_to_convert)


class Boolean(DataType):
    def _to_data_value(self, value):
        if type(value) is int or type(value) is float:
            value = bool(value)
        return BooleanValue(value)


class BooleanArray(ArrayType):
    def _to_data_value(self, value):
        return BooleanValueArray(value)


class Double(DataType):
    def _to_data_value(self, value):
        if type(value) is int:
            value = numpy.float(value)
        return DoubleValue(value)


class DoubleArray(ArrayType):
    def _to_data_value(self, value):
        return DoubleValueArray(value)


class Int32(DataType):
    def _to_data_value(self, value):
        value = numpy.int32(value)
        return I32Value(value)


class Int32Array(ArrayType):
    def _to_data_value(self, value):
        return I32ValueArray(value)


class Int64(DataType):
    def _to_data_value(self, value):
        value = numpy.int64(value)
        return I64Value(value)


class Int64Array(ArrayType):
    def _to_data_value(self, value):
        return I64ValueArray(value)


class UInt32(DataType):
    def _to_data_value(self, value):
        value = numpy.uint32(value)
        return U32Value(value)


class UInt32Array(ArrayType):
    def _to_data_value(self, value):
        return U32ValueArray(value)


class UInt64(DataType):
    def _to_data_value(self, value):
        value = numpy.uint64(value)
        return U64Value(value)


class UInt64Array(ArrayType):
    def _to_data_value(self, value):
        return U64ValueArray(value)


VALID_TYPES = {
    ArrayType.__name__: ArrayType,
    Boolean.__name__: Boolean,
    BooleanArray.__name__: BooleanArray,
    Double.__name__: Double,
    DoubleArray.__name__: DoubleArray,
    Int32.__name__: Int32,
    Int32Array.__name__: Int32Array,
    Int64.__name__: Int64,
    Int64Array.__name__: Int64Array,
    UInt32.__name__: UInt32,
    UInt32Array.__name__: UInt32Array,
    UInt64.__name__: UInt64,
    UInt64Array.__name__: UInt64Array
}

VALID_RETURN_TYPES = {
    Boolean.__name__: Boolean,
    Double.__name__: Double,
    Int32.__name__: Int32,
    Int64.__name__: Int64,
    UInt32.__name__: UInt32,
    UInt64.__name__: UInt64
}
