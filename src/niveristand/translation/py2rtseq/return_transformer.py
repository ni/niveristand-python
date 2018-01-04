import ast

from niveristand import errormessages
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.datatypes.rtprimitives import ArrayType
from niveristand.exceptions import TranslateError
from niveristand.translation import utils


def return_transformer(node, resources):
    rtseq = resources.get_rtseq()
    expression = utils.generic_ast_node_transform(node.value, resources)
    if isinstance(node.value, (ast.Name, ast.Attribute)):
        src_var_name = utils.get_variable_name_from_node(node.value)
        if resources.has_variable(str(src_var_name)):
            rt_expression = expression
            return_default_value = resources.get_variable_py_value(src_var_name)
        else:
            raise TranslateError(errormessages.invalid_return_value)

    elif isinstance(node.value, (ast.Num, ast.Call)):
        return_default_value = utils.get_value_from_node(node.value, resources)
        if isinstance(return_default_value, ArrayType):
            raise TranslateError(errormessages.invalid_return_type)
        rt_expression = expression
    else:
        raise TranslateError(errormessages.invalid_return_value)
    var_name = rtseqapi.add_return_variable(rtseq, '__ret_var__', return_default_value)
    rtseqapi.add_assignment(resources.get_current_block(), var_name, rt_expression)
    return "return " + str(expression)
