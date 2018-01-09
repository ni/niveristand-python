from niveristand.exceptions import VeristandNotImplementedError
from niveristand.translation import utils


def compareoperator_transformer(node, resources):
    left = utils.generic_ast_node_transform(node.left, resources)
    result = "((" + left + ") "
    for op, comparator in zip(node.ops, node.comparators):
        operator = _operator(op.__class__.__name__)
        if operator == "unknown":
            raise VeristandNotImplementedError()
        right = utils.generic_ast_node_transform(comparator, resources)
        result += operator + " (" + right + ")"
    result += ")"
    return result


def _operator(ast_operator):
    return{
        'Eq': "==",
        'Gt': ">",
        'Lt': "<",
    }.get(ast_operator, "unknown")
