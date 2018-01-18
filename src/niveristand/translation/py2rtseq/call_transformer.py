from niveristand.clientapi.datatypes import rtprimitives
from niveristand.translation import utils


def call_transformer(node, resources):
    if rtprimitives.is_supported_data_type(node.func.id):
        # In case of a type declaration, return only the value because this is not
        # an actual sub-sequence call.
        return str(utils.generic_ast_node_transform(node.args[0], resources))
    func_name = str(utils.generic_ast_node_transform(node.func, resources))
    resources.add_referenced_sequence(func_name)
    node_str = func_name + "("
    for arg in node.args:
        node_str += str(utils.generic_ast_node_transform(arg, resources))
    return node_str + ")"
