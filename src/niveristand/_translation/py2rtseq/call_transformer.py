import ast
from niveristand import _errormessages
from niveristand import errors
from niveristand._translation import custom_action_symbols, symbols, utils
from niveristand.clientapi._datatypes import rtprimitives


def call_transformer(node, resources):
    if rtprimitives.is_channel_ref_type(node.func.id):
        if isinstance(node.args[0], ast.Str):
            identifier = resources.get_channel_ref_rtseq_name_from_channel_name(node.args[0].s)
        else:
            raise errors.TranslateError(_errormessages.invalid_type_for_channel_ref)
        return identifier
    if rtprimitives.is_supported_data_type(node.func.id):
        if rtprimitives.is_scalar_type(node.func.id):
            return _transform_data_type_scalar(node)
        elif isinstance(node.args[0], ast.List):
            return _transform_datatype_non_scalar(node, resources)
        else:
            raise errors.TranslateError(_errormessages.init_var_invalid_type)
    if node.func.id in custom_action_symbols._custom_action_symbols:
        # Custom action symbols are basically transformers for functions that don't have
        # their own ast node. Invoke them here
        return custom_action_symbols._custom_action_symbols[node.func.id](node, resources)
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


def _transform_datatype_non_scalar(node, resources):
    data_value_str = utils.generic_ast_node_transform(node.args[0], resources)
    return data_value_str


def _transform_data_type_scalar(node):
    # In case of data type creation or declaration, create the appropriate value (for example Double(3)
    # needs to return "3.0", not "3".)
    data_type = rtprimitives.get_class_by_name(node.func.id)
    data_value_str = str(data_type(utils.get_element_value(node.args[0])).value)
    # we need to check the symbols dictionary because of named constants. Using Boolean(True)
    # needs to return "true" not "True"
    if data_value_str in symbols._symbols:
        data_value_str = symbols._symbols[data_value_str]
    return data_value_str
