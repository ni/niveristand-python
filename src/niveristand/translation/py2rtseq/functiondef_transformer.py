import ast
from niveristand.clientapi.datatypes import DoubleValue
from niveristand.translation import utils


def functiondef_transformer(node, resources):
    for param in node.args.args:
        arg_name, def_value, by_value = _arg_to_param(param, resources)
        resources.add_parameter(arg_name, def_value, by_value)
    for instruction in node.body:
        resources.set_current_block(resources.get_rtseq().Code.Main.Body)
        utils.generic_ast_node_transform(instruction, resources)
    return ""


def _arg_to_param(node, resources):
    if type(node) is ast.Name:
        arg_name = utils.generic_ast_node_transform(node, resources)
    elif type(node) is ast.arg:
        arg_name = node.arg

    # default values for now
    by_value = False
    def_value = DoubleValue(0)
    return arg_name, def_value, by_value
