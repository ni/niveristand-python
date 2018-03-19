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
    built_exp = utils.generic_ast_node_transform(node.value, resources) + '.' + node.attr
    if built_exp in symbols._symbols:
        return symbols._symbols[built_exp]
    else:
        raise errors.TranslateError(_errormessages.unknown_identifier % var_name)
