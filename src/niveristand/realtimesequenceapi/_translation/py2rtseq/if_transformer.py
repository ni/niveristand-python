import ast
from niveristand.realtimesequenceapi import _errormessages
from niveristand.realtimesequenceapi._translation import utils
from niveristand.realtimesequenceapi._translation.py2rtseq import validations
from niveristand.realtimesequenceapi.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.realtimesequenceapi import errors


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
    validations.raise_if_try_in_node_body(node.body)
    validations.raise_if_try_in_node_body(node.orelse)
    if validations.check_if_any_in_block(
        ast.Return, node.body
    ) or validations.check_if_any_in_block(ast.Return, node.orelse):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    if validations.check_if_any_in_block(
        ast.FunctionDef, node.body
    ) or validations.check_if_any_in_block(ast.FunctionDef, node.orelse):
        raise errors.TranslateError(_errormessages.invalid_nested_funcdef)
