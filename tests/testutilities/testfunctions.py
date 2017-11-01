import math
from math import pi
from niveristand import decorators


@decorators.nivs_rt_sequence
def empty_func():
    pass


@decorators.nivs_rt_sequence
def simple_local_assignment():
    a = 5  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def simple_float_local_assignment():
    a = 5.0  # noqa: F841 it's ok for this variable to never be used


@decorators.nivs_rt_sequence
def simple_assign_pi():
    a = math.pi  # noqa: F841 it's ok for this variable to never be used
    b = pi  # noqa: F841 it's ok for this variable to never be used
