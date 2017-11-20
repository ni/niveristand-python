import ast
from niveristand import datatypes, errormessages
from niveristand.exceptions import TranslateError


def generic_ast_node_transform(node, resources):
    from niveristand.translation.py2rtseq.transformers import TRANSFORMERS
    transformer_name = node.__class__.__name__
    transformer = TRANSFORMERS.get(transformer_name, TRANSFORMERS['Default'])
    return transformer(node, resources)


def get_value_from_node(node, resources):
    if isinstance(node, ast.Call):
        call = generic_ast_node_transform(node.func, resources)
        node_id = call.split('.')[-1]
        if node_id in datatypes.VALID_TYPES:
            datatype = datatypes.VALID_TYPES[node.func.id]
            datavalue = generic_ast_node_transform(node.args[0], resources)
            return datatype(datavalue)
    elif isinstance(node, ast.Num):
        if isinstance(node.n, int):
            return datatypes.Int32(node.n)
        elif isinstance(node.n, float):
            return datatypes.Double(node.n)
    raise TranslateError(errormessages.init_var_invalid_type)
