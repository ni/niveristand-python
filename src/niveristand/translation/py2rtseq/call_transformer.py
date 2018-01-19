from niveristand.clientapi.datatypes import rtprimitives
from niveristand.translation import symbols, utils


def call_transformer(node, resources):
    if rtprimitives.is_supported_data_type(node.func.id):
        # In case of a type declaration, return only the value because this is not
        # an actual sub-sequence call.
        return str(utils.generic_ast_node_transform(node.args[0], resources))
    if node.func.id in symbols._symbols:
        # In case of a builtin expression get it out from symbols and add any arguments it may have
        func_name = symbols._symbols[node.func.id]
        node_str = func_name + "("
        for arg in node.args:
            node_str += str(utils.generic_ast_node_transform(arg, resources))
            node_str += " ,"
        if not node.args:
            return node_str + ")"
        else:
            # remove space and comma
            return node_str[:-2] + ")"
    else:
        # It only can be a RT sequence call, so treat it accordingly
        func_name = str(utils.generic_ast_node_transform(node.func, resources))
        resources.add_referenced_sequence(func_name)
        return func_name + "()"  # TODO: implement argument parsing in case of rtseq call: check if only variables
        # are passed and they are valid
