from niveristand.internal import LOCAL_VARIABLES, RT_SEQ_VAR_NAME
from niveristand.translation import symbols, utils


def attribute_transformer(node, resources):
    var_name = utils.get_variable_name_from_node(node)
    if var_name in resources[LOCAL_VARIABLES]:
        return resources[LOCAL_VARIABLES][var_name][RT_SEQ_VAR_NAME]
    built_exp = utils.generic_ast_node_transform(node.value, resources) + '.' + node.attr
    if built_exp in symbols._symbols:
        return symbols._symbols[built_exp]
    else:
        return built_exp
