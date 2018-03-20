import ast
from niveristand import _errormessages
from niveristand._translation import utils
from niveristand.clientapi import _datatypes, realtimesequencedefinition as rtseqapi
from niveristand.errors import TranslateError


def assign_transformer(node, resources):
    node_value = None
    initial_channel_ref_declaration = False
    lhs = node.targets[0]
    rtseq_var_name = utils.generic_ast_node_transform(lhs, resources)
    # the left hand side can only be a variable name or a name with an attribute (var.value)
    if isinstance(lhs, ast.Name):
        variable_name = utils.get_variable_name_from_node(lhs)
        # if the variable already exists this kind of assignment is invalid, use var.value instead
        if resources.has_variable(variable_name):
            raise TranslateError(_errormessages.variable_reassignment)
    elif isinstance(lhs, ast.Attribute):
        # in case of var[0].value get rid of the [0] part and search in the dictionary for var
        stripped_rtseq_var_name = rtseq_var_name[:rtseq_var_name.find("[")] if rtseq_var_name.find("[") != -1 \
            else rtseq_var_name
        variable_name = resources.get_variable_py_name(stripped_rtseq_var_name)
    else:
        raise TranslateError(_errormessages.variable_reassignment)
    rtseq = resources.get_rtseq()
    block = resources.get_current_block()
    if not resources.has_variable(variable_name):
        # new local variable
        node_value = utils.get_value_from_node(node.value, resources)
        if isinstance(node_value, (_datatypes.ChannelReference, _datatypes.VectorChannelReference)):
            initial_channel_ref_declaration = True
            channel_name = utils.get_channel_name(node.value.args[0])
            rtseq_var_name = rtseqapi.to_channel_ref_name(variable_name)
            resources.add_channel_ref(variable_name, channel_name, rtseq_var_name,
                                      isinstance(node_value, _datatypes.ArrayType))
        elif isinstance(node_value, _datatypes.DataType):
            rtseq_var_name = rtseqapi.add_local_variable(rtseq, variable_name, node_value)
            # add the local variable's accessor to the resources
            resources.add_variable(variable_name, node_value, rtseq_var_name)
            resources.add_variable(variable_name + ".value", node_value, rtseq_var_name)
        else:
            raise TranslateError(_errormessages.init_var_invalid_type)
    transformed_node_value = utils.generic_ast_node_transform(node.value, resources)
    rtseq_var_name = resources.get_variable_rtseq_name(variable_name) if not rtseq_var_name else rtseq_var_name
    if not initial_channel_ref_declaration:
        if isinstance(node_value, _datatypes.ArrayType):
            if transformed_node_value.count(',') > 0:
                value_list = transformed_node_value.split(',')
                for index, val in enumerate(value_list):
                    rtseqapi.add_assignment(block, rtseq_var_name + "[" + str(index) + "]", val)
        else:
            rtseqapi.add_assignment(block, rtseq_var_name, transformed_node_value)
