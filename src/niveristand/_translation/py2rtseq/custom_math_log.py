from niveristand._translation import utils


def custom_math_log(node, resources):
    if len(node.args) == 1:
        func = 'ln'
    else:
        func = 'log'

    node_str = func + "("
    for arg in node.args:
        node_str += str(utils.generic_ast_node_transform(arg, resources))
        node_str += " ,"
    if not node.args:
        return node_str + ")"
    else:
        # remove space and comma
        return node_str[:-2] + ")"
