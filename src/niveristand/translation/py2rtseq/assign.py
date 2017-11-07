import ast
from niveristand import datatypes, errormessages
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.exceptions import TranslateError
from niveristand.internal import BLOCK, LOCAL_VARIABLES, RTSEQ
from niveristand.translation import utils


def assign_transformer(node, resources):
    variable_name = utils.generic_ast_node_transform(node.targets[0], resources)
    rtseq = resources[RTSEQ]
    block = resources[BLOCK]
    if variable_name not in resources[LOCAL_VARIABLES]:
        # new local variable
        node_value = _get_value_from_node(node.value, resources)
        if isinstance(node_value, datatypes.DataType):
            rtseq_var_name = _create_rtseq_variable(variable_name, node_value, rtseq)
            # add the local variable's accessor to the resources
            variable_name += ".value"
            resources[LOCAL_VARIABLES][variable_name] = rtseq_var_name
        else:
            raise TranslateError(errormessages.init_var_invalid_type)
    node_value = utils.generic_ast_node_transform(node.value, resources)
    _add_assignment(block, resources[LOCAL_VARIABLES][variable_name], node_value)


def _add_assignment(block, dest_name, source_name):
    rtseqapi.add_assignment(block, dest_name, source_name)


def _create_rtseq_variable(variable_name, value, rt_seq):
    variable_name = rtseqapi.add_local_variable(rt_seq, variable_name, value)
    return variable_name


def _get_value_from_node(node, resources):
    if not isinstance(node, ast.Call):
        raise TranslateError(errormessages.init_var_invalid_type)
    if node.func.id in datatypes.VALID_TYPES:
        datatype = datatypes.VALID_TYPES[node.func.id]
        datavalue = utils.generic_ast_node_transform(node.args[0], resources)
        return datatype(datavalue)
