from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations


def ifexp_transformer(node, resources):
    validations.raise_if_invalid_if_test(node.test)
    test = utils.generic_ast_node_transform(node.test, resources)
    body = utils.generic_ast_node_transform(node.body, resources)
    orelse = utils.generic_ast_node_transform(node.orelse, resources)
    return "(" + test + ") ? (" + body + ") : (" + orelse + ")"
