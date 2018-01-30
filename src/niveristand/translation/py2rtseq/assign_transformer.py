from niveristand import errormessages
from niveristand.clientapi import datatypes, realtimesequencedefinition as rtseqapi
from niveristand.exceptions import TranslateError
from niveristand.translation import utils


def assign_transformer(node, resources):
    node_value = None
    initial_channel_ref_declaration = False
    variable_name = utils.get_variable_name_from_node(node.targets[0])
    rtseq = resources.get_rtseq()
    block = resources.get_current_block()
    if not resources.has_variable(variable_name):
        # new local variable
        node_value = utils.get_value_from_node(node.value, resources)
        if isinstance(node_value, datatypes.ChannelReference):
            initial_channel_ref_declaration = True
            channel_name = utils.get_channel_name(node.value.args[0])
            rtseq_var_name = rtseqapi.to_channel_ref_name(variable_name)
            resources.add_channel_ref(variable_name, channel_name, rtseq_var_name)
        elif isinstance(node_value, datatypes.DataType):
            rtseq_var_name = rtseqapi.add_local_variable(rtseq, variable_name, node_value)
            # add the local variable's accessor to the resources
            resources.add_variable(variable_name, node_value, rtseq_var_name)
            resources.add_variable(variable_name + ".value", node_value, rtseq_var_name)
        else:
            raise TranslateError(errormessages.init_var_invalid_type)
    transformed_node_value = utils.generic_ast_node_transform(node.value, resources)
    rtseq_var_name = resources.get_variable_rtseq_name(variable_name)
    if not initial_channel_ref_declaration:
        if isinstance(node_value, datatypes.ArrayType):
            if transformed_node_value.count(',') > 0:
                value_list = transformed_node_value.split(',')
                for index, val in enumerate(value_list):
                    rtseqapi.add_assignment(block, rtseq_var_name + "[" + str(index) + "]", val)
        else:
            rtseqapi.add_assignment(block, rtseq_var_name, transformed_node_value)
