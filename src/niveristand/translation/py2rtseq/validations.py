import ast
import sys
from niveristand import errormessages, exceptions


def check_try_in_node_body(statements):
    if check_if_any_in_block(ast_try(), statements):
        raise exceptions.TranslateError(errormessages.try_only_in_top_level_func)


def ast_try():
    if sys.version_info > (3, 0):
        return ast.Try
    else:
        return ast.TryFinally


def check_if_any_in_block(ast_node, block):
    if any([isinstance(body_stmt, ast_node) for body_stmt in block]):
        return True
    return False


def looks_like_doc_block(node):
    return isinstance(node, ast.Expr) and isinstance(node.value, ast.Str)
