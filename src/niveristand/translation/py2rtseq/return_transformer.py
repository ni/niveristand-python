import ast

from niveristand import errormessages
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.exceptions import TranslateError
from niveristand.internal import BLOCK, LOCAL_VAR_VALUE, LOCAL_VARIABLES, RTSEQ
from niveristand.translation import utils


def return_transformer(node, resources):
    rtseq = resources[RTSEQ]
    expression = utils.generic_ast_node_transform(node.value, resources)
    if isinstance(node.value, (ast.Name, ast.Attribute)):
        src_var_name = utils.get_variable_name_from_node(node.value)
        if str(src_var_name) in resources[LOCAL_VARIABLES]:
            rt_expression = expression
            node_value = resources[LOCAL_VARIABLES][src_var_name][LOCAL_VAR_VALUE]
        else:
            raise TranslateError(errormessages.init_var_invalid_type)

    elif isinstance(node.value, (ast.Num, ast.Call)):
        node_value = utils.get_value_from_node(node.value, resources)
        rt_expression = expression
    else:
        raise TranslateError(errormessages.init_var_invalid_type)
    var_name = rtseqapi.add_return_variable(rtseq, '__ret_var__', node_value)
    rtseqapi.add_assignment(resources[BLOCK], var_name, rt_expression)
    return "return " + str(expression)
