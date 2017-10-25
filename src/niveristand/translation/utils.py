import ast
from niveristand import exceptions as nivsexceptions
from niveristand.clientapi import realtimesequencedefinition as rtseqapi


def create_rtseq_variable(variable_name, ast_call_node, rt_seq):
    if type(ast_call_node) is ast.Num:
        node_value = ast_call_node.n
    elif type(ast_call_node) is ast.NameConstant:
        node_value = ast_call_node.value
    elif type(ast_call_node) is ast.Str:
        node_value = ast_call_node.s
    else:
        raise nivsexceptions.UnexpectedError("Unexpected assignment type %s"
                                         % type(ast_call_node))

    variable_name = rtseqapi.add_local_variable(rt_seq, variable_name, node_value)
    return variable_name
