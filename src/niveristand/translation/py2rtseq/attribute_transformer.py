from niveristand.translation import symbols, utils


def attribute_transformer(node, resources):
    var_name = utils.get_variable_name_from_node(node)
    if resources.has_variable(var_name):
        return resources.get_variable_rtseq_name(var_name)
    built_exp = utils.generic_ast_node_transform(node.value, resources) + '.' + node.attr
    if built_exp in symbols._symbols:
        return symbols._symbols[built_exp]
    else:
        return built_exp
