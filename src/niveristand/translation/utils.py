import ast
import sys
from niveristand import datatypes, errormessages
from niveristand.datatypes import rtprimitives
from niveristand.exceptions import TranslateError
from niveristand.translation import symbols


def generic_ast_node_transform(node, resources):
    from niveristand.translation.py2rtseq.transformers import TRANSFORMERS
    transformer_name = node.__class__.__name__
    transformer = TRANSFORMERS.get(transformer_name, TRANSFORMERS['Default'])
    return transformer(node, resources)


def get_value_from_node(node, resources):
    if isinstance(node, ast.Call):
        call = generic_ast_node_transform(node.func, resources)
        node_id = call.split('.')[-1]
        if rtprimitives.is_supported_data_type(node_id):
            datatype = rtprimitives.get_class_by_name(node.func.id)
            if type(node.args[0]) is ast.Num:
                datavalue = node.args[0].n
            elif type(node.args[0]) is ast.Name:
                if node.args[0].id in symbols._symbols:
                    datavalue = symbols._symbols[node.args[0].id]
                else:
                    raise TranslateError(errormessages.init_var_invalid_type)
            # this is ugly, but NameConstant does not exist in 2.7 and we need to evaluate the system version
            # otherwise the 2.7 version will error out by not recognizing the NameConstant attribute
            elif sys.version_info >= (3, 5) and type(node.args[0]) is ast.NameConstant:
                if node.args[0].value is True or node.args[0].value is False:
                    datavalue = node.args[0].value
                else:
                    raise TranslateError(errormessages.init_var_invalid_type)
            elif type(node.args[0]) is ast.List:
                datavalue = [get_element_value(element) for element in node.args[0].elts]
            else:
                raise TranslateError(errormessages.init_var_invalid_type)
            return datatype(datavalue)
    elif isinstance(node, ast.Num):
        if isinstance(node.n, int):
            return datatypes.Int32(node.n)
        elif isinstance(node.n, float):
            return datatypes.Double(node.n)
    raise TranslateError(errormessages.init_var_invalid_type)


def get_element_value(node):
    if type(node) is ast.Num:
        return node.n
    elif type(node) is ast.Name:
        if node.id in symbols._symbols:
            return symbols._symbols[node.id]
        else:
            raise TranslateError(errormessages.init_var_invalid_type)
    # this is ugly, but NameConstant does not exist in 2.7 and we need to evaluate the system version
    # otherwise the 2.7 version will error out by not recognizing the NameConstant attribute
    elif sys.version_info >= (3, 5) and type(node) is ast.NameConstant:
        return node.value
    else:
        raise TranslateError(errormessages.init_var_invalid_type)


def get_variable_name_from_node(node):
    full_name = ''
    cur_node = node
    while isinstance(cur_node, ast.Attribute):
        full_name = '.' + cur_node.attr + full_name
        cur_node = cur_node.value
    if isinstance(cur_node, ast.Name):
        full_name = cur_node.id + full_name
    return full_name
