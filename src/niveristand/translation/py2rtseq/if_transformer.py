import ast
from niveristand import errormessages, exceptions
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
    if validations.check_if_any_in_block(ast.Return, node.body) or \
            validations.check_if_any_in_block(ast.Return, node.orelse):
        raise exceptions.TranslateError(errormessages.return_unsupported_unless_last)
    if validations.check_if_any_in_block(ast.FunctionDef, node.body) or \
            validations.check_if_any_in_block(ast.FunctionDef, node.orelse):
        raise exceptions.TranslateError(errormessages.invalid_nested_funcdef)
