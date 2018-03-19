from niveristand._translation import utils
from niveristand.errors import VeristandNotImplementedError


def unaryoperator_transformer(node, resources):
    operator = _operator(node.op.__class__.__name__)
    if operator == "unknown":
        raise VeristandNotImplementedError()
    operand = utils.generic_ast_node_transform(node.operand, resources)
    return "(" + operator + "(" + operand + ")" + ")"


def _operator(ast_operator):
    return{
        'USub': "-",
        'Not': "!",
        'Invert': "~",
    }.get(ast_operator, "unknown")
