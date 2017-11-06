import math
from math import pi
from niveristand import decorators
from niveristand.datatypes import Double
from niveristand.datatypes import Int32


def func_without_decorator():
    pass


@decorators.nivs_rt_sequence
def empty_func():
    pass


@decorators.nivs_rt_sequence
def simple_local_assignment():
    a = Int32(5)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def simple_float_local_assignment():
    a = Double(5.0)  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def simple_assign_pi():
    a = Double(0.0)  # noqa: F841 it's ok for this variable to never be used
    a.value = math.pi
    a.value = pi


@decorators.nivs_rt_sequence
def assign_untyped():
    a = 0  # noqa: F841 it's ok for this variable to never be used
