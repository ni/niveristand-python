from niveristand import datatypes
from niveristand.translation import utils


def call_transformer(node, resources):
    if node.func.id in datatypes.VALID_TYPES:
        # In case of a type declaration, return only the value because this is not
        # an actual sub-sequence call.
        return str(utils.generic_ast_node_transform(node.args[0], resources))
    node_str = str(utils.generic_ast_node_transform(node.func, resources)) + "("
    for arg in node.args:
        node_str += str(utils.generic_ast_node_transform(arg, resources))
    return node_str + ")"
