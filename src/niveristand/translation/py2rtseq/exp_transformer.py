from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.translation import utils


def exp_transformer(node, resources):
    exp = utils.generic_ast_node_transform(node.value, resources)
    rtseqapi.add_expression(resources.get_current_block(), exp)
    return exp
