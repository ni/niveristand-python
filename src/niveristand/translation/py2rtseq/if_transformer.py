from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.translation import utils
from niveristand.translation.py2rtseq import validations


def if_transformer(node, resources):
    _validate_restrictions(node)
    test_condition = utils.generic_ast_node_transform(node.test, resources)
    parent_block = resources.get_current_block()
    if_else_statement = rtseqapi.add_if_else(parent_block, test_condition)
    for statement in node.body:
        resources.set_current_block(if_else_statement.IfTrue)
        utils.generic_ast_node_transform(statement, resources)
    for statement in node.orelse:
        resources.set_current_block(if_else_statement.IfFalse)
        utils.generic_ast_node_transform(statement, resources)
    resources.set_current_block(parent_block)


def _validate_restrictions(node):
    validations.check_try_in_node_body(node.body)
    validations.check_try_in_node_body(node.orelse)
