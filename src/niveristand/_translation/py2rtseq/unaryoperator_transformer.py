import ast
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.errors import VeristandNotImplementedError


def unaryoperator_transformer(node, resources):
    operator = _operator(node.op.__class__.__name__)
    if operator == "unknown":
        raise VeristandNotImplementedError()
    if operator == '!':
        if isinstance(node.operand, ast.UnaryOp):
            validations.raise_if_invalid_bool_operand(node.operand.operand, resources)
        else:
            validations.raise_if_invalid_bool_operand(node.operand, resources)
    if operator == '~':
        validations.raise_if_invalid_invert_operand(node.operand, resources)
    operand = utils.generic_ast_node_transform(node.operand, resources)
    return "(" + operator + "(" + operand + ")" + ")"


def _operator(ast_operator):
    return{
        'USub': "-",
        'Not': "!",
        'Invert': "~",
    }.get(ast_operator, "unknown")
