from niveristand.translation import utils


def functiondef_transformer(node, resources):
    for instruction in node.body:
        resources.set_current_block(resources.get_rtseq().Code.Main.Body)
        utils.generic_ast_node_transform(instruction, resources)
    return ""
