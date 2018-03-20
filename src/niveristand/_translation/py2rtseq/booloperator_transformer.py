from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.errors import VeristandNotImplementedError


def booloperator_transformer(node, resources):
    operator = _operator(node.op.__class__.__name__)
    if operator == "unknown":
        raise VeristandNotImplementedError()
    for value in node.values:
        validations.raise_if_invalid_bool_operand(value, resources)
    result = "( " + utils.generic_ast_node_transform(node.values[0], resources) + " "
    for o in node.values[1:]:
        op = utils.generic_ast_node_transform(o, resources)
        result += operator + " " + op + " "
    return result + ")"


def _operator(ast_operator):
    return {
        'And': "&&",
        'Or': "||",
    }.get(ast_operator, "unknown")
