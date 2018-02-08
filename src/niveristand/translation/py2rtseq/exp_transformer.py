from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.translation import utils


def exp_transformer(node, resources):
    exp = utils.generic_ast_node_transform(node.value, resources)
    if bool(exp):
        # Custom actions generate their own expressions and return None
        # so only add an expression if something was returned
        rtseqapi.add_expression(resources.get_current_block(), exp)
    return exp
