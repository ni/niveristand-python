import ast

from niveristand import errormessages
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.exceptions import TranslateError
from niveristand.internal import BLOCK, LOCAL_VAR_VALUE, LOCAL_VARIABLES, RT_SEQ_VAR_NAME, RTSEQ
from niveristand.translation import utils


def return_transformer(node, resources):
    rtseq = resources[RTSEQ]
    expression = utils.generic_ast_node_transform(node.value, resources)
    if str(expression) in resources[LOCAL_VARIABLES]:
        rt_expression = resources[LOCAL_VARIABLES][expression][RT_SEQ_VAR_NAME]
        node_value = resources[LOCAL_VARIABLES][expression][LOCAL_VAR_VALUE]
    elif isinstance(node.value, (ast.Num, ast.Call)):
        node_value = utils.get_value_from_node(node.value, resources)
        rt_expression = expression
    else:
        raise TranslateError(errormessages.init_var_invalid_type)
    var_name = rtseqapi.add_return_variable(rtseq, '__ret_var__', node_value)
    rtseqapi.add_assignment(resources[BLOCK], var_name, rt_expression)
    return "return " + str(expression)
