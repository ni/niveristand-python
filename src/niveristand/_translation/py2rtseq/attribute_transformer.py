import ast
from niveristand import _errormessages, errors
from niveristand._translation import symbols, utils


def attribute_transformer(node, resources):
    var_name = utils.get_variable_name_from_node(node)
    if resources.has_variable(var_name):
        if isinstance(node.value, ast.Subscript):
            return utils.generic_ast_node_transform(node.value, resources)
        else:
            return resources.get_variable_rtseq_name(var_name)
    try:
        # Try to get the value of the node in case it's a DataType(x).value style.
        node_value = utils.get_value_from_node(node.value, resources)
        return str(node_value)
    except errors.TranslateError:
        # If we get a TranslateError it's because it wasn't a DataType(x).value, so move on.
        pass
    built_exp = utils.generic_ast_node_transform(node.value, resources) + '.' + node.attr
    if built_exp in symbols._symbols:
        return symbols._symbols[built_exp]
    else:
        raise errors.TranslateError(_errormessages.unknown_identifier % var_name)
