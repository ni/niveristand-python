import ast
from niveristand import errormessages, exceptions
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.translation import utils
from niveristand.translation.py2rtseq import validations


def while_transformer(node, resources):
    _validate_restrictions(node, resources)
    test_condition = utils.generic_ast_node_transform(node.test, resources)
    parent_block = resources.get_current_block()
    while_statement = rtseqapi.add_while(parent_block, test_condition)
    for statement in node.body:
        resources.set_current_block(while_statement.Body)
        utils.generic_ast_node_transform(statement, resources)
    resources.set_current_block(parent_block)


def _validate_restrictions(node, resources):
    if node.orelse:
        raise exceptions.TranslateError(errormessages.unsupported_orelse_while)
    if validations.check_if_any_in_block(ast.Return, node.body):
        raise exceptions.TranslateError(errormessages.return_unsupported_unless_last)
    if validations.check_if_any_in_block(ast.FunctionDef, node.body):
        raise exceptions.TranslateError(errormessages.invalid_nested_funcdef)
    validations.check_try_in_node_body(node.body)
