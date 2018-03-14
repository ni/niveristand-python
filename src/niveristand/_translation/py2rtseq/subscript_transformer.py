from niveristand._translation import utils


def subscript_transformer(node, resources):
    variable_name = utils.get_variable_name_from_node(node)
    rtseq_var_name = resources.get_variable_rtseq_name(variable_name)
    index = utils.generic_ast_node_transform(node.slice, resources)
    return rtseq_var_name + "[" + index + "]"
