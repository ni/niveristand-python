import math
from math import pi
from niveristand import decorators
from niveristand.clientapi.datatypes import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.clientapi.datatypes import BooleanValueArray, DoubleValueArray


def func_without_decorator():
    pass


@decorators.nivs_rt_sequence
def empty_func():
    pass


@decorators.nivs_rt_sequence
@decorators.nivs_rt_sequence
def empty_func_with_double_decorator():
    pass


@decorators.nivs_rt_sequence
def simple_local_assignment():
    a = I32Value(5)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def simple_float_local_assignment():
    a = DoubleValue(5.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def simple_assign_pi():
    a = DoubleValue(0.0)  # noqa: F841 it's ok for this variable to never be used
    a.value = math.pi
    a.value = pi


@decorators.nivs_rt_sequence
def assign_untyped():
    a = math.pi  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def return_var():
    a = DoubleValue(5)
    return a


@decorators.nivs_rt_sequence
def return_var_value():
    a = DoubleValue(5)
    return a.value


@decorators.nivs_rt_sequence
def return_var_invalid_value():
    a = DoubleValue(5)
    return a.value.value


@decorators.nivs_rt_sequence
def return_named_type():
    return DoubleValue(5)


@decorators.nivs_rt_sequence
def return_primitive_num():
    return 5.0


@decorators.nivs_rt_sequence
def return_var_pi():
    a = DoubleValue(5)
    a.value = math.pi
    return a


@decorators.nivs_rt_sequence
def return_untyped_symbol():
    return math.pi


@decorators.nivs_rt_sequence
def return_true():
    a = BooleanValue(True)
    return a.value


@decorators.nivs_rt_sequence
def return_false():
    a = BooleanValue(False)
    return a.value


@decorators.nivs_rt_sequence
def return_boolean_array():
    a = BooleanValueArray([True, False])
    return a


@decorators.nivs_rt_sequence
def return_double_array():
    a = DoubleValueArray([0, 1, 2, 3])
    return a


@decorators.nivs_rt_sequence
def channel_ref_type_string():
    a = ChannelReference("Aliases/DesiredRPM")  # noqa: F841 it's ok not to be used


@decorators.nivs_rt_sequence
def channel_ref_setter():
    a = ChannelReference("Aliases/DesiredRPM")
    a.value = 5


@decorators.nivs_rt_sequence
def channel_ref_return():
    a = ChannelReference("Aliases/DesiredRPM")
    a.value = 5.0
    return a.value


@decorators.nivs_rt_sequence
def channel_ref_validate_getter():
    a = ChannelReference("Aliases/DesiredRPM")
    a.value = 5.0
    b = DoubleValue(0)
    b.value = a.value
    return b.value
