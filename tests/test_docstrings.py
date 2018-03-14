import sys
from niveristand import _decorators, RealTimeSequence
from niveristand.library._tasks import multitask
import pytest
from testutilities import validation


@_decorators.nivs_rt_sequence
def docstring_func_single_line():
    """Single-line doc."""
    pass


@_decorators.nivs_rt_sequence
def docstring_func_parameters(arg1, arg2):
    """Test parameters docstring.

    :param arg1: first argument
    :param arg2: second argument
    """
    pass


@_decorators.nivs_rt_sequence
def docstring_func_multi_line():
    """Begin doc.

    This is more doc
    that is in multiple strings.
    """
    pass


@_decorators.nivs_rt_sequence
def docstring_func_in_code():
    """Begin doc.

    This is more doc
    that is in multiple strings.
    """
    pass
    """ More doc strings"""
    pass


@_decorators.nivs_rt_sequence
def docstring_try():
    """Begin doc.

    This is more doc
    that is in multiple strings.
    """
    try:
        pass
    finally:
        pass


@_decorators.nivs_rt_sequence
def docstring_multitask():
    """Test multitask docstring."""
    with multitask() as mt:
        @_decorators.task(mt)
        def func1():
            """Test task docstring in func1."""
            pass

        @_decorators.task(mt)
        def func2():
            """Test task docstring in func2.

            Multi-line comment here.
            """
            pass
    pass


@_decorators.nivs_rt_sequence
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


skip_tests = [
]

transform_tests = [
    (docstring_func_in_code, (), None),
    (docstring_func_multi_line, (), None),
    (docstring_func_parameters, (), None),
    (docstring_func_single_line, (), None),
    (docstring_multitask, (), None),
    (docstring_try, (), None),
    (docstring_try_inside, (), None),
]

fail_tests = [
]


def idfunc(val):
    return val.__name__


@pytest.mark.parametrize("func_name, params, expected_result", transform_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", fail_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
