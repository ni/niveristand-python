from niveristand import errormessages
from niveristand import exceptions as nivsexceptions
import numpy


class DataType:
    def __init__(self, value, description="", units=""):
        self._validate(value)
        self.__value = self._validate(value)

    def __str__(self):
        return str(self.value)

    def _validate(self, value):
        return True

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
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class ArrayType(DataType):
    def _validate(self, value):
        True


class Boolean(DataType):
    def _validate(self, value):
        try:
            return bool(value)
        except TypeError:
            raise nivsexceptions.TranslateError(errormessages.init_var_invalid_type)


class DoubleArray(ArrayType):
    def _validate(self, value):
        try:
            if not value:
                original_elements = []
            else:
                original_elements = value.split(',')
            element_list = []
            for element in original_elements:
                element_list.append(Double(element))
            return element_list
        except TypeError:
            raise nivsexceptions.TranslateError(errormessages.init_var_invalid_type)


class Double(DataType):
    def _validate(self, value):
        try:
            return float(value)
        except TypeError:
            raise nivsexceptions.TranslateError(errormessages.init_var_invalid_type)


class Int32(DataType):
    def _validate(self, value):
        try:
            return int(value)
        except TypeError:
            raise nivsexceptions.TranslateError(errormessages.init_var_invalid_type)


class Int64(DataType):
    def _validate(self, value):
        try:
            return numpy.int64(value)
        except TypeError:
            raise nivsexceptions.TranslateError(errormessages.init_var_invalid_type)


class UInt32(DataType):
    def _validate(self, value):
        try:
            return numpy.uint32(value)
        except TypeError:
            raise nivsexceptions.TranslateError(errormessages.init_var_invalid_type)


class UInt64(DataType):
    def _validate(self, value):
        try:
            return numpy.uint64(value)
        except TypeError:
            raise nivsexceptions.TranslateError(errormessages.init_var_invalid_type)


VALID_TYPES = {
    ArrayType.__name__: ArrayType,
    Boolean.__name__: Boolean,
    Double.__name__: Double,
    DoubleArray.__name__: DoubleArray,
    Int32.__name__: Int32,
    Int64.__name__: Int64,
    UInt32.__name__: UInt32,
    UInt64.__name__: UInt64
}