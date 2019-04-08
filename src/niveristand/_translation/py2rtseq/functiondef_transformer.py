import ast
from collections import namedtuple
import sys
from niveristand import _decorators, _errormessages, errors
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.clientapi._datatypes import BooleanValue, DoubleValue


def functiondef_transformer(node, resources):
    if validations.check_if_looks_like_doc_block(node.body[0]):
        node.body = node.body[1:]
    _validate_restrictions(node)
    for param in node.args.args:
        p = _init_args(param, resources)
        resources.add_parameter(p.name, p.def_value, p.by_value)
    for decorator in [dec for dec in node.decorator_list if type(dec) is ast.Call]:
        # the NivsParam decorator is a class, so it gets used like this:
        # @NivsParam(param_name, DataType(default), BY_REF)
        # which in ast terms is treated as an ast.Call. So, we look for those and convert to args.
        p = _decorator_to_arg(decorator, resources)
        resources.update_parameter(p.name, p.def_value, p.by_value)
    # reparenting should happen in each transformer that contains nested blocks
    resources.set_current_block(resources.get_rtseq().Code.Main.Body)
    for instruction in node.body:
        utils.generic_ast_node_transform(instruction, resources)
    return ""


_param = namedtuple('_param', 'name def_value by_value')


def _init_args(node, resources):
    # default values for now
    by_value = False
    def_value = DoubleValue(0)
    if type(node) is ast.Name:
        arg_name = utils.generic_ast_node_transform(node, resources)
    elif 'arg' in dir(ast) and type(node) is ast.arg:
        arg_name = node.arg
    return _param(arg_name, def_value, by_value)


def _decorator_to_arg(node, resources):
    arg_name = def_value = by_value = None
    if not len(node.args) == 3:
        raise errors.TranslateError(_errormessages.invalid_param_decorator)
    # this is a decorator param definition. First parameter is the string for the name.
    if isinstance(node.args[0], ast.Str):
        arg_name = node.args[0].s
    # second is the default value
    try:
        def_value = utils.get_value_from_node(node.args[1], resources)
    except errors.TranslateError:
        # def_value won't get assigned anything if an error occurs, which will trigger the exception later.
        pass
    # third is whether to pass by ref or by value
    valid_types = [ast.Name, ast.Attribute]
    if isinstance(node.args[2], tuple(valid_types)):
        by_value_str = utils.get_variable_name_from_node(node.args[2])
        by_value_str = getattr(_decorators.NivsParam, by_value_str.split('.')[-1], by_value_str)
        by_value = BooleanValue(by_value_str).value
    elif 'NameConstant' in dir(ast) and isinstance(node.args[2], ast.NameConstant):
        by_value = node.args[2].value

    if arg_name is None or def_value is None or by_value is None:
        raise errors.TranslateError(_errormessages.invalid_param_decorator)
    return _param(arg_name, def_value, by_value)


def _validate_restrictions(node):
    if validations.check_if_any_in_block(ast.FunctionDef, node.body):
        raise errors.TranslateError(_errormessages.invalid_function_definition)
    if sys.version_info > (3, 0):
        # py35 restrictions
        if node.returns is not None \
                or len(node.args.kwonlyargs) != 0 \
                or len(node.args.kw_defaults) != 0 \
                or node.args.vararg is not None \
                or node.args.kwarg is not None \
                or len(node.args.defaults) != 0:
            raise errors.TranslateError(_errormessages.invalid_function_definition)
    else:
        # py27 restrictions
        if node.args.vararg is not None \
                or node.args.kwarg is not None \
                or len(node.args.defaults) != 0:
            raise errors.TranslateError(_errormessages.invalid_function_definition)
    if validations.check_if_any_in_block(validations.ast_try(), node.body):
        if not isinstance(node.body[0], validations.ast_try()):
            raise errors.TranslateError(_errormessages.try_must_be_first_stmt)
        if len(node.body) > 2:
            raise errors.TranslateError(_errormessages.invalid_stmt_after_try)
        elif len(node.body) == 2:
            if not isinstance(node.body[1], ast.Return):
                raise errors.TranslateError(_errormessages.invalid_stmt_after_try)
    return_statements = [statement for statement in node.body if isinstance(statement, ast.Return)]
    if len(return_statements) > 1:
        raise errors.TranslateError(_errormessages.multiple_return_statements)
    if validations.check_if_any_in_block(ast.Return, node.body[:-1]):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    for decorator in node.decorator_list:
        decorator_name_node = decorator.func if isinstance(decorator, ast.Call) else decorator
        decorator_name = utils.get_variable_name_from_node(decorator_name_node)
        decorator_name = decorator_name.split(".")[-1]
        _raise_if_invalid_decorator(decorator_name)


def _raise_if_invalid_decorator(attribute):
    if not (attribute in _decorators._VALID_DECORATORS):
        raise errors.TranslateError(_errormessages.invalid_decorator)
