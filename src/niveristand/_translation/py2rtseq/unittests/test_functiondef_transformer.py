import ast
import inspect
from niveristand import errors
from niveristand._translation.py2rtseq import functiondef_transformer
from niveristand._translation.py2rtseq import utils
import pytest


def functiondef_with_default(i=1):
    return i


def functiondef_with_args(*args):
    return args


def functiondef_with_kwargs(**kwargs):
    return kwargs


def functiondef_nested():
    def functiondef_inside():
        pass
    pass

# def functiondef_with_kwarg_default(*args, kwarg=1):
#    return kwarg


def invalid_decorator(func):
    return func


class InvalidDecoratorClass:
    def __call__(self, f):
        return f

    @staticmethod
    def invalid_decorator_as_attribute(func):
        return func


@invalid_decorator
def functiondef_invalid_decorator():
    pass


@InvalidDecoratorClass()
def functiondef_invalid_decorator2():
    pass


@InvalidDecoratorClass.invalid_decorator_as_attribute
def functiondef_invalid_decorator3():
    pass


invalid_func_tests = [
    functiondef_with_default,
    functiondef_with_args,
    functiondef_with_kwargs,
    functiondef_nested,
    #  functiondef_with_kwarg_default,
    functiondef_invalid_decorator,
    functiondef_invalid_decorator2,
    functiondef_invalid_decorator3,
]


def idfunc(val):
    return val.__name__


@pytest.mark.parametrize("func", invalid_func_tests, ids=idfunc)
def test_functiondef_transformer_fails(func):
    _fail_function_helper(func)


def _fail_function_helper(func):
    node = (ast.parse(inspect.getsource(func)))
    node = node.body[0]
    with pytest.raises(errors.TranslateError):
        functiondef_transformer.functiondef_transformer(node, utils.Resources(None, '<test>'))
