from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.internal import BLOCK
from niveristand.translation import utils


def if_transformer(node, resources):
    test_condition = utils.generic_ast_node_transform(node.test, resources)
    parent_block = resources[BLOCK]
    if_else_statement = rtseqapi.add_if_else(parent_block, test_condition)
    for statement in node.body:
        resources[BLOCK] = if_else_statement.IfTrue
        utils.generic_ast_node_transform(statement, resources)
    for statement in node.orelse:
        resources[BLOCK] = if_else_statement.IfFalse
        utils.generic_ast_node_transform(statement, resources)
    resources[BLOCK] = parent_block
