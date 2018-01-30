import ast
from niveristand import errormessages
from niveristand import exceptions
from niveristand.clientapi.datatypes import rtprimitives
from niveristand.translation import symbols, utils


def call_transformer(node, resources):
    if rtprimitives.is_channel_ref_type(node.func.id):
        if isinstance(node.args[0], ast.Str):
            identifier = resources.get_channel_ref_rtseq_name_from_channel_name(node.args[0].s)
        else:
            raise exceptions.TranslateError(errormessages.invalid_type_for_channel_ref)
        return identifier
    if rtprimitives.is_supported_data_type(node.func.id):
        # In case of a type declaration, return only the value because this is not
        # an actual sub-sequence call.
        return str(utils.generic_ast_node_transform(node.args[0], resources))
    if node.func.id in symbols._symbols:
        # In case of a builtin expression get it out from symbols and add any arguments it may have
        func_name = symbols._symbols[node.func.id]
    else:
        # It only can be a RT sequence call, so treat it accordingly
        func_name = str(utils.generic_ast_node_transform(node.func, resources))
        resources.add_referenced_sequence(func_name)
    node_str = func_name + "("
    for arg in node.args:
        node_str += str(utils.generic_ast_node_transform(arg, resources))
        node_str += " ,"
    if not node.args:
        return node_str + ")"
    else:
        # remove space and comma
        return node_str[:-2] + ")"
