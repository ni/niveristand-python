from niveristand._translation import utils
from niveristand.errors import VeristandNotImplementedError


def binaryoperator_transformer(node, resources):
    operator = _operator(node.op.__class__.__name__)
    if operator == "unknown":
        raise VeristandNotImplementedError()
    left = utils.generic_ast_node_transform(node.left, resources)
    right = utils.generic_ast_node_transform(node.right, resources)
    return "((" + left + ") " + operator + " (" + right + "))"


def _operator(ast_operator):
    return{
        'Add': "+",
        'Sub': "-",
        'Mult': "*",
        'Div': "/",
        'Pow': "**",
        'Mod': "%",
        'BitAnd': "&",
        'BitOr': "|",
        'BitXor': "^",
        'LShift': "<<",
        'RShift': ">>",
    }.get(ast_operator, "unknown")
