from niveristand._translation import utils


def ifexp_transformer(node, resources):
    test = utils.generic_ast_node_transform(node.test, resources)
    body = utils.generic_ast_node_transform(node.body, resources)
    orelse = utils.generic_ast_node_transform(node.orelse, resources)
    return "(" + test + ") ? (" + body + ") : (" + orelse + ")"
