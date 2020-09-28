import ast
import sys

from niveristand import _errormessages
from niveristand import errors
from niveristand._translation import symbols
from niveristand.clientapi import _datatypes
from niveristand.clientapi._datatypes import rtprimitives
from niveristand.errors import TranslateError


def generic_ast_node_transform(node, resources):
    from niveristand._translation.py2rtseq.transformers import TRANSFORMERS
    transformer_name = node.__class__.__name__
    transformer = TRANSFORMERS.get(transformer_name, TRANSFORMERS['Default'])
    return transformer(node, resources)


def get_value_from_node(node, resources):
    if isinstance(node, ast.Call):
        call = generic_ast_node_transform(node.func, resources)
        node_id = call.split('.')[-1]
        if rtprimitives.is_supported_data_type(node_id):
            datatype = rtprimitives.get_class_by_name(node.func.id)
            if rtprimitives.is_channel_ref_type(datatype.__name__):
                if rtprimitives.is_array_type(datatype.__name__):
                    datavalue = [0.0]
                else:
                    datavalue = 0.0
            # In Python 3.8, Num is Constant
            elif type(node.args[0]) in (ast.Num, ast.UnaryOp) or \
                    check_ast_constant_num(node.args[0]):
                datavalue = get_element_value(node.args[0])
            elif type(node.args[0]) is ast.Name:
                if node.args[0].id in symbols._symbols:
                    datavalue = symbols._symbols[node.args[0].id]
                else:
                    raise TranslateError(_errormessages.init_var_invalid_type)
            # In Python 3.8, NameConstant is Constant
            elif type(node.args[0]) is ast.NameConstant or \
                    check_ast_constant_nameconstant(node.args[0]):
                if node.args[0].value is True or node.args[0].value is False:
                    datavalue = node.args[0].value
                else:
                    raise TranslateError(_errormessages.init_var_invalid_type)
            elif type(node.args[0]) is ast.List:
                datavalue = [get_element_value(element) for element in node.args[0].elts]
            else:
                raise TranslateError(_errormessages.init_var_invalid_type)
            return datatype(datavalue)
    elif isinstance(node, ast.Name):
        if node.id in ['True', 'False']:
            return _datatypes.BooleanValue(node.id)
    # In Python 3.8, NameConstant is Constant
    elif isinstance(node, ast.NameConstant) or \
            check_ast_constant_nameconstant(node):
        if node.value is None:
            raise TranslateError(_errormessages.init_var_invalid_type)
        return _datatypes.BooleanValue(node.value)
    # Python 3.7
    elif sys.version_info < (3, 8) and isinstance(node, ast.Num):
        if isinstance(node.n, int):
            try:
                return_obj = _datatypes.I32Value(node.n)
            except OverflowError:
                return_obj = _datatypes.I64Value(node.n)
            return return_obj
        elif isinstance(node.n, float):
            return _datatypes.DoubleValue(node.n)
    # In Python 3.8, Num is Constant
    elif check_ast_constant_num(node):
        if isinstance(node.value, int):
            try:
                return_obj = _datatypes.I32Value(node.value)
            except OverflowError:
                return_obj = _datatypes.I64Value(node.value)
            return return_obj
        elif isinstance(node.value, float):
            return _datatypes.DoubleValue(node.value)
    raise TranslateError(_errormessages.init_var_invalid_type)


def get_element_value(node):
    # Python 3.7
    if sys.version_info < (3, 8) and type(node) is ast.Num:
        return node.n
    # In Python 3.8, Num is Constant
    elif check_ast_constant_num(node):
        return node.value
    elif type(node) is ast.UnaryOp:
        return eval(generic_ast_node_transform(node, ()))
    elif type(node) is ast.Name:
        if node.id in symbols._symbols:
            return symbols._symbols[node.id]
        else:
            raise TranslateError(_errormessages.init_var_invalid_type)
    # In Python 3.8, NameConstant is Constant
    elif type(node) is ast.NameConstant or check_ast_constant_nameconstant(node):
        return node.value
    else:
        raise TranslateError(_errormessages.init_var_invalid_type)


def get_variable_name_from_node(node):
    full_name = ''
    cur_node = node
    while isinstance(cur_node, ast.Attribute):
        full_name = '.' + cur_node.attr + full_name
        cur_node = cur_node.value
    if isinstance(cur_node, ast.Name):
        full_name = cur_node.id + full_name
    if isinstance(cur_node, ast.Subscript):
        full_name = get_variable_name_from_node(cur_node.value) + full_name
    return full_name


def get_channel_name(node):
    if sys.version_info < (3, 8) and type(node) is ast.Str:
        channel_name = node.s
    elif check_ast_constant_str(node):
        channel_name = node.value
    else:
        raise errors.TranslateError(_errormessages.invalid_type_for_channel_ref)
    return channel_name


def check_ast_constant_str(node):
    return isinstance(node, ast.Constant) and isinstance(node.value, str)


def check_ast_constant_num(node):
    return isinstance(node, ast.Constant) and isinstance(node.value, (int, float, complex)) \
        and str(node.value) not in ["True", "False", "None"]


def check_ast_constant_nameconstant(node):
    return isinstance(node, ast.Constant) and node.value in [True, False, None] \
        and str(node.value) in ["True", "False", "None"]
