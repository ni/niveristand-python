from niveristand.translation import utils


def call_transformer(node, resources):
    node_str = str(utils.generic_ast_node_transform(node.func, resources)) + "("
    for arg in node.args:
        node_str += str(utils.generic_ast_node_transform(arg, resources))
    return node_str + ")"
