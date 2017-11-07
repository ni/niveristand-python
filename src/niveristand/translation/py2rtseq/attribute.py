from niveristand.translation import symbols, utils


def attribute_transformer(node, resources):
    built_exp = utils.generic_ast_node_transform(node.value, resources) + '.' + node.attr
    if built_exp in symbols._symbols:
        return symbols._symbols[built_exp]
    return built_exp
