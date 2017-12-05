from niveristand import datatypes, errormessages
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.exceptions import TranslateError
from niveristand.internal import BLOCK, LOCAL_VAR_VALUE, LOCAL_VARIABLES, RT_SEQ_VAR_NAME, RTSEQ
from niveristand.translation import utils


def assign_transformer(node, resources):
    node_value = None
    variable_name = utils.get_variable_name_from_node(node.targets[0])
    rtseq = resources[RTSEQ]
    block = resources[BLOCK]
    if variable_name not in resources[LOCAL_VARIABLES]:
        # new local variable
        node_value = utils.get_value_from_node(node.value, resources)
        if isinstance(node_value, datatypes.DataType):
            rtseq_var_name = rtseqapi.add_local_variable(rtseq, variable_name, node_value)
            # add the local variable's accessor to the resources
            local_var = {RT_SEQ_VAR_NAME: rtseq_var_name, LOCAL_VAR_VALUE: node_value}
            resources[LOCAL_VARIABLES][variable_name] = local_var
            resources[LOCAL_VARIABLES][variable_name + ".value"] = local_var
        else:
            raise TranslateError(errormessages.init_var_invalid_type)
    transformed_node_value = utils.generic_ast_node_transform(node.value, resources)
    rtseq_var_name = resources[LOCAL_VARIABLES][variable_name][RT_SEQ_VAR_NAME]
    if isinstance(node_value, datatypes.ArrayType):
        value_list = transformed_node_value.split(',')
        for index, val in enumerate(value_list):
            rtseqapi.add_assignment(block, rtseq_var_name + "[" + str(index) + "]", val)
    else:
        rtseqapi.add_assignment(block, rtseq_var_name, transformed_node_value)
