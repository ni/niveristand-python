import ast
import sys
from niveristand import _errormessages, errors
from niveristand._translation import utils


def raise_if_try_in_node_body(statements):
    if check_if_any_in_block(ast_try(), statements):
        raise errors.TranslateError(_errormessages.try_only_in_top_level_func)


def ast_try():
    if sys.version_info > (3, 0):
        return ast.Try
    else:
        return ast.TryFinally


def check_if_any_in_block(ast_node, block):
    if any([isinstance(body_stmt, ast_node) for body_stmt in block]):
        return True
    return False


def check_if_looks_like_doc_block(node):
    return isinstance(node, ast.Expr) and isinstance(node.value, ast.Str)


def raise_if_invalid_bool_operand(node, resources):
    invalid_operand = False
    try:
        if not isinstance(utils.get_value_from_node(node, resources).value, bool):
            invalid_operand = True
    except errors.TranslateError:
        pass
    if invalid_operand:
        raise errors.TranslateError(_errormessages.invalid_operand_for_boolean_operator)


def raise_if_invalid_invert_operand(node, resources):
    invalid_operand = False
    try:
        if isinstance(utils.get_value_from_node(node, resources).value, (bool, float)):
            invalid_operand = True
    except errors.TranslateError:
        pass
    if invalid_operand:
        raise errors.TranslateError(_errormessages.invalid_operand_for_unary_invert_operator)
