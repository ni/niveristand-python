import ast
from niveristand import _errormessages, errors
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.clientapi import realtimesequencedefinition as rtseqapi


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
        raise errors.TranslateError(_errormessages.unsupported_orelse_while)
    if validations.check_if_any_in_block(ast.Return, node.body):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    if validations.check_if_any_in_block(ast.FunctionDef, node.body):
        raise errors.TranslateError(_errormessages.invalid_nested_funcdef)
    validations.raise_if_try_in_node_body(node.body)
