import ast
from niveristand import errormessages, exceptions
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.translation import utils


def while_transformer(node, resources):
    _validate_transformer(node, resources)
    test_condition = utils.generic_ast_node_transform(node.test, resources)
    parent_block = resources.get_current_block()
    while_statement = rtseqapi.add_while(parent_block, test_condition)
    for statement in node.body:
        resources.set_current_block(while_statement.Body)
        utils.generic_ast_node_transform(statement, resources)
    resources.set_current_block(parent_block)


def _validate_transformer(node, resources):
    if node.orelse:
        raise exceptions.TranslateError(errormessages.unsupported_orelse_while)
    if any([isinstance(body_node, ast.Return) for body_node in node.body]):
        raise exceptions.TranslateError(errormessages.return_unsupported_unless_last)
