from niveristand._translation import utils


def list_transformer(node, resources):
    list_string = ""
    if not node.elts:
        return list_string
    else:
        for element in node.elts:
            list_string += utils.generic_ast_node_transform(element, resources) + ","
        return list_string[:-1]
