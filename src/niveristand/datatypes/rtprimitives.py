from distutils.util import strtobool
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
        self._value = self._validate(value)
        self._data_value = self._to_data_value()

    def __str__(self):
        return str(self.value)

    def _validate(self, value):
        try:
            return self._translate_value(value)
        except TypeError:
            raise nivsexceptions.TranslateError(errormessages.init_var_invalid_type)

    def _translate_value(self, value):
        return None

    def _to_data_value(self):
        raise nivsexceptions.TranslateError(errormessages.invalid_type_to_convert)

    def __add__(self, other):
        if isinstance(other, DataType):
            return self.value + other.value
        elif isinstance(other, (int, float)):
            return self.value + other
        else:
            raise nivsexceptions.TranslateError(errormessages.invalid_type_for_operator)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, DataType):
            return self.value - other.value
        elif isinstance(other, (int, float)):
            return self.value - other
        else:
            raise nivsexceptions.TranslateError(errormessages.invalid_type_for_operator)

    def __rsub__(self, other):
        return self.__sub__(other)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def data_value(self):
        return self._data_value

    @data_value.setter
    def data_value(self, value):
        self._data_value = value


class ArrayType(DataType):
    def _validate(self, value):
        try:
            if not value:
                original_elements = []
            else:
                original_elements = value.split(',')
            element_list = [self._translate_value(element) for element in original_elements]
            return element_list
        except TypeError:
            raise nivsexceptions.TranslateError(errormessages.init_var_invalid_type)

    def _to_data_value(self):
        raise nivsexceptions.TranslateError(errormessages.invalid_type_to_convert)


class Boolean(DataType):
    def _translate_value(self, value):
        return bool(value)

    def _to_data_value(self):
        return BooleanValue(self.value)


class BooleanArray(ArrayType):
    def _translate_value(self, value):
        return Boolean(strtobool(value))

    def _to_data_value(self):
        value_list = [BooleanValue(element_value.value) for element_value in self.value]
        return BooleanValueArray(value_list)


class Double(DataType):
    def _translate_value(self, value):
        return float(value)

    def _to_data_value(self):
        return DoubleValue(self.value)


class DoubleArray(ArrayType):
    def _translate_value(self, value):
        return Double(value)

    def _to_data_value(self):
        value_list = [DoubleValue(element_value.value) for element_value in self.value]
        return DoubleValueArray(value_list)


class Int32(DataType):
    def _translate_value(self, value):
        return numpy.int32(value)

    def _to_data_value(self):
        return I32Value(self.value)


class Int32Array(ArrayType):
    def _translate_value(self, value):
        return Int32(value)

    def _to_data_value(self):
        value_list = [I32Value(element_value.value) for element_value in self.value]
        return I32ValueArray(value_list)


class Int64(DataType):
    def _translate_value(self, value):
        return numpy.int64(value)

    def _to_data_value(self):
        return I64Value(self.value)


class Int64Array(ArrayType):
    def _translate_value(self, value):
        return Int64(value)

    def _to_data_value(self):
        value_list = [I64Value(element_value.value) for element_value in self.value]
        return I64ValueArray(value_list)


class UInt32(DataType):
    def _translate_value(self, value):
        return numpy.uint32(value)

    def _to_data_value(self):
        return U32Value(self.value)


class UInt32Array(ArrayType):
    def _translate_value(self, value):
        return UInt32(value)

    def _to_data_value(self):
        value_list = [U32Value(element_value.value) for element_value in self.value]
        return U32ValueArray(value_list)


class UInt64(DataType):
    def _translate_value(self, value):
        return numpy.uint64(value)

    def _to_data_value(self):
        return U64Value(self.value)


class UInt64Array(ArrayType):
    def _translate_value(self, value):
        return UInt64(value)

    def _to_data_value(self):
        value_list = [U64Value(element_value.value) for element_value in self.value]
        return U64ValueArray(value_list)


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
