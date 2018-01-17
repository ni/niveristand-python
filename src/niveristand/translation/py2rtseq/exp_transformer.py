from niveristand.translation import utils


def exp_transformer(node, resources):
    return utils.generic_ast_node_transform(node.value, resources)
