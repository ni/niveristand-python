import ast
import sys
from niveristand import _errormessages
from niveristand._translation import utils
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.clientapi._datatypes import ArrayType
from niveristand.errors import TranslateError


def return_transformer(node, resources):
    _validate_restrictions(node)
    rtseq = resources.get_rtseq()
    expression = utils.generic_ast_node_transform(node.value, resources)
    stripped_expression = expression[:expression.find("[")] if expression.find("[") != -1 else expression
    if isinstance(node.value, (ast.Name, ast.Attribute, ast.Subscript)):
        src_var_name = utils.get_variable_name_from_node(node.value)
        if resources.has_variable(str(src_var_name)) and not resources.has_channel_ref(stripped_expression):
            rt_expression = expression
            return_default_value = resources.get_variable_py_value(src_var_name)
            # In case of "return var[0]" the default value is saved as a list, so make sure to not return list type
            # because those cannot be return variables.
            # The len check is there to not get index error in case of empty lists -> for that I don't know yet
            # what the solution is, so I will leave it like this (Arnold)
            if isinstance(return_default_value, ArrayType):
                if len(return_default_value.value):
                    return_default_value = return_default_value[0]
        else:
            raise TranslateError(_errormessages.invalid_return_value)
    elif isinstance(node.value, (ast.Num, ast.Call)):
        return_default_value = utils.get_value_from_node(node.value, resources)
        if isinstance(return_default_value, ArrayType):
            raise TranslateError(_errormessages.invalid_return_type)
        rt_expression = expression
    else:
        raise TranslateError(_errormessages.invalid_return_value)
    var_name = rtseqapi.add_return_variable(rtseq, '__ret_var__', return_default_value)
    rtseqapi.add_assignment(resources.get_current_block(), var_name, rt_expression)
    return "return " + str(expression)


def _validate_restrictions(node):
    valid_types = [ast.Num, ast.Attribute]
    if sys.version_info > (3, 0):
        valid_types.append(ast.NameConstant)
    if not isinstance(node.value, tuple(valid_types)):
        raise TranslateError(_errormessages.invalid_return_type)
