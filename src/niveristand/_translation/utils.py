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
            elif type(node.args[0]) is ast.UnaryOp or is_node_ast_num(node.args[0]):
                datavalue = get_element_value(node.args[0])
            elif type(node.args[0]) is ast.Name:
                if node.args[0].id in symbols._symbols:
                    datavalue = symbols._symbols[node.args[0].id]
                else:
                    raise TranslateError(_errormessages.init_var_invalid_type)
            elif is_node_ast_nameconstant(node.args[0]):
                node_value = get_value_from_nameconstant_node(node.args[0])
                if node_value is True or node_value is False:
                    datavalue = node_value
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
    elif is_node_ast_num(node):
        node_value = get_value_from_num_node(node)
        if isinstance(node_value, int):
            try:
                return_obj = _datatypes.I32Value(node_value)
            except OverflowError:
                return_obj = _datatypes.I64Value(node_value)
            return return_obj
        elif isinstance(node_value, float):
            return _datatypes.DoubleValue(node_value)
    elif is_node_ast_nameconstant(node):
        node_value = get_value_from_nameconstant_node(node)
        if node_value is None:
            raise TranslateError(_errormessages.init_var_invalid_type)
        return _datatypes.BooleanValue(node_value)
    raise TranslateError(_errormessages.init_var_invalid_type)


def get_element_value(node):
    if is_node_ast_num(node):
        return get_value_from_num_node(node)
    elif type(node) is ast.UnaryOp:
        return eval(generic_ast_node_transform(node, ()))
    elif type(node) is ast.Name:
        if node.id in symbols._symbols:
            return symbols._symbols[node.id]
        else:
            raise TranslateError(_errormessages.init_var_invalid_type)
    elif is_node_ast_nameconstant(node):
        return get_value_from_nameconstant_node(node)
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
    if is_node_ast_str(node):
        channel_name = get_value_from_str_node(node)
    else:
        raise errors.TranslateError(_errormessages.invalid_type_for_channel_ref)
    return channel_name


def is_node_ast_str(node):
    # Python 3.7
    if sys.version_info < (3, 8) and isinstance(node, ast.Str):
        return True
    # In Python 3.8, Str is Constant
    elif sys.version_info >= (3, 8) and isinstance(node, ast.Constant) \
            and isinstance(node.value, str):
        return True
    return False


def is_node_ast_num(node):
    # Python 3.7
    if sys.version_info < (3, 8) and isinstance(node, ast.Num):
        return True
    # In Python 3.8, Num is Constant
    elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float, complex)) \
            and str(node.value) not in ["True", "False", "None"]:
        return True
    return False


def is_node_ast_nameconstant(node):
    # Python 3.7
    if sys.version_info < (3, 8) and isinstance(node, ast.NameConstant):
        return True
    # In Python 3.8, NameConstant is Constant
    elif isinstance(node, ast.Constant) and node.value in [True, False, None] and \
            str(node.value) in ["True", "False", "None"]:
        return True
    return False


def get_value_from_str_node(node):
    if sys.version_info < (3, 8):
        return node.s
    else:
        return node.value


def get_value_from_num_node(node):
    if sys.version_info < (3, 8):
        return node.n
    else:
        return node.value


def get_value_from_nameconstant_node(node):
    return node.value
