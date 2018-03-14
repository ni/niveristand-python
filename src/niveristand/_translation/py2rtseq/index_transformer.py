from niveristand._translation import utils


def index_transformer(node, resources):
    index = utils.generic_ast_node_transform(node.value, resources)
    return index
