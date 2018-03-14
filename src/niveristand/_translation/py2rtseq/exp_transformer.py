from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.clientapi import realtimesequencedefinition as rtseqapi


def exp_transformer(node, resources):
    if validations.check_if_looks_like_doc_block(node):
        exp = ""
    else:
        exp = utils.generic_ast_node_transform(node.value, resources)
    if bool(exp):
        # Custom actions generate their own expressions and return None
        # so only add an expression if something was returned
        rtseqapi.add_expression(resources.get_current_block(), exp)
    return exp
