from niveristand.exceptions import VeristandNotImplementedError
from niveristand.translation import utils


def booloperator_transformer(node, resources):
    operator = _operator(node.op.__class__.__name__)
    if operator == "unknown":
        raise VeristandNotImplementedError()
    result = "( " + utils.generic_ast_node_transform(node.values[0], resources) + " "
    for o in node.values[1:]:
        op = utils.generic_ast_node_transform(o, resources)
        result += operator + " " + op + " "
    return result + ")"


def _operator(ast_operator):
    return {
        'And': "&&",
    }.get(ast_operator, "unknown")
