import math
from math import pi
from niveristand import _decorators
from niveristand.clientapi._datatypes import BooleanValue, BooleanValueArray, ChannelReference, DoubleValue, \
    DoubleValueArray, I32Value, VectorChannelReference
from niveristand.library.primitives import localhost_wait


def func_without_decorator():
    pass


@_decorators.nivs_rt_sequence
def empty_func():
    pass


@_decorators.nivs_rt_sequence
@_decorators.nivs_rt_sequence
def empty_func_with_double_decorator():
    pass


@_decorators.nivs_rt_sequence
def simple_local_assignment():
    a = I32Value(5)  # noqa: F841 it's ok for this variable to never be used


@_decorators.nivs_rt_sequence
def simple_float_local_assignment():
    a = DoubleValue(5.0)  # noqa: F841 it's ok for this variable to never be used


@_decorators.nivs_rt_sequence
def simple_assign_pi():
    a = DoubleValue(0.0)  # noqa: F841 it's ok for this variable to never be used
    a.value = math.pi
    a.value = pi


@_decorators.nivs_rt_sequence
def assign_untyped():
    a = math.pi  # noqa: F841 it's ok for this variable to never be used


@_decorators.nivs_rt_sequence
def return_var():
    a = DoubleValue(5)
    return a.value


@_decorators.nivs_rt_sequence
def return_var_value():
    a = DoubleValue(5)
    return a.value


@_decorators.nivs_rt_sequence
def return_var_invalid_value():
    a = DoubleValue(5)
    return a.value.value


@_decorators.nivs_rt_sequence
def return_named_type():
    return DoubleValue(5)


@_decorators.nivs_rt_sequence
def return_primitive_num():
    return 5.0


@_decorators.nivs_rt_sequence
def return_var_pi():
    a = DoubleValue(5)
    a.value = math.pi
    return a.value


@_decorators.nivs_rt_sequence
def return_untyped_symbol():
    return math.pi


@_decorators.nivs_rt_sequence
def return_true():
    a = BooleanValue(True)
    return a.value


@_decorators.nivs_rt_sequence
def return_false():
    a = BooleanValue(False)
    return a.value


@_decorators.nivs_rt_sequence
def return_boolean_array():
    a = BooleanValueArray([True, False])
    return a


@_decorators.nivs_rt_sequence
def return_double_array():
    a = DoubleValueArray([0, 1, 2, 3])
    return a


@_decorators.nivs_rt_sequence
def multiple_returns():
    a = DoubleValue(5)
    return a.value
    b = DoubleValue(5)
    return b.value


@_decorators.nivs_rt_sequence
def return_not_last():
    a = DoubleValue(5)
    return a.value
    a.value += 1


@_decorators.nivs_rt_sequence
def channel_ref_type_string():
    a = ChannelReference("Aliases/DesiredRPM")  # noqa: F841 it's ok not to be used


@_decorators.nivs_rt_sequence
def channel_ref_setter():
    a = ChannelReference("Aliases/DesiredRPM")
    a.value = 5


@_decorators.nivs_rt_sequence
def channel_ref_return():
    a = ChannelReference("Aliases/DesiredRPM")
    a.value = 5.0
    localhost_wait()
    return a.value


@_decorators.nivs_rt_sequence
def channel_ref_validate_getter():
    a = ChannelReference("Aliases/DesiredRPM")
    a.value = 5.0
    localhost_wait()
    b = DoubleValue(0)
    b.value = a.value
    return b.value


@_decorators.nivs_rt_sequence
def channel_ref_invalid_channel_set():
    a = ChannelReference("InvalidName")
    a.value = 5


@_decorators.nivs_rt_sequence
def channel_ref_invalid_channel_get():
    a = ChannelReference("InvalidName")
    b = DoubleValue(0)
    b.value = a.value


@_decorators.nivs_rt_sequence
def channel_ref_invalid_channel_transform():
    a = ChannelReference("InvalidName")  # noqa: F841 it's ok not to be used


@_decorators.nivs_rt_sequence
def channel_ref_array_type_string():
    a = VectorChannelReference("Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a")  # noqa: F841


@_decorators.nivs_rt_sequence
def channel_ref_array_setter():
    a = VectorChannelReference("Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a")
    a[0].value = 5


@_decorators.nivs_rt_sequence
def channel_ref_array_return():
    a = VectorChannelReference("Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a")
    a[0].value = 5.0
    localhost_wait()
    return a[0].value


@_decorators.nivs_rt_sequence
def channel_ref_for_vector_channel():
    a = ChannelReference('Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a')
    a.value = 50


@_decorators.nivs_rt_sequence
def channel_ref_array_validate_getter():
    a = VectorChannelReference("Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a")
    a[3].value = 5.0
    localhost_wait()
    b = DoubleValue(0)
    b.value = a[3].value
    return b.value


@_decorators.nivs_rt_sequence
def a_value_value_assignment():
    a = DoubleValue(0)
    a.value = a.value.value
    return a.value


@_decorators.nivs_rt_sequence
def a_value_value_assign_to():
    a = DoubleValue(0)
    a.value.value = 1
    return a.value
