import sys
from niveristand import nivs_rt_sequence
from niveristand.clientapi import RealTimeSequence
from niveristand.library import multitask, task
import pytest
from testutilities import validation


@nivs_rt_sequence
def docstring_func_single_line():
    """Single-line doc."""
    pass


@nivs_rt_sequence
def docstring_func_parameters(arg1, arg2):
    """Test parameters docstring.

    :param arg1: first argument
    :param arg2: second argument
    """
    pass


@nivs_rt_sequence
def docstring_func_multi_line():
    """Begin doc.

    This is more doc
    that is in multiple strings.
    """
    pass


@nivs_rt_sequence
def docstring_func_in_code():
    """Begin doc.

    This is more doc
    that is in multiple strings.
    """
    pass
    """ More doc strings"""
    pass


@nivs_rt_sequence
def docstring_try():
    """Begin doc.

    This is more doc
    that is in multiple strings.
    """
    try:
        pass
    finally:
        pass


@nivs_rt_sequence
def docstring_multitask():
    """Test multitask docstring."""
    with multitask() as mt:
        @task(mt)
        def func1():
            """Test task docstring in func1."""
            pass

        @task(mt)
        def func2():
            """Test task docstring in func2.

            Multi-line comment here.
            """
            pass
    pass


@nivs_rt_sequence
def docstring_try_inside():
    """Begin doc.

    This is more doc
    that is in multiple strings.
    """
    try:
        """More docs"""
        pass
    finally:
        pass


transform_tests = [
    (docstring_func_in_code, (), None),
    (docstring_func_multi_line, (), None),
    (docstring_func_parameters, (), None),
    (docstring_func_single_line, (), None),
    (docstring_multitask, (), None),
    (docstring_try, (), None),
    (docstring_try_inside, (), None),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", transform_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
