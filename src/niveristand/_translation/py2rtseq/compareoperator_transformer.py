from niveristand import _errormessages
from niveristand._translation import utils
from niveristand.errors import TranslateError, VeristandNotImplementedError


def compareoperator_transformer(node, resources):
    left = utils.generic_ast_node_transform(node.left, resources)
    result = "((" + left + ") "
    if len(node.ops) > 1:
        raise TranslateError(_errormessages.cascaded_comparison_operators_not_allowed)
    operator = _operator(node.ops[0].__class__.__name__)
    if operator == "unknown":
        raise VeristandNotImplementedError()
    right = utils.generic_ast_node_transform(node.comparators[0], resources)
    result += operator + " (" + right + ")"
    result += ")"
    return result


def _operator(ast_operator):
    return{
        'Eq': "==",
        'NotEq': "!=",
        'Gt': ">",
        'GtE': ">=",
        'Lt': "<",
        'LtE': "<=",
        'Is': "==",
        'IsNot': "!=",
    }.get(ast_operator, "unknown")
