import ast
import sys

from niveristand import _errormessages
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.errors import TranslateError


def try_transformer(node, resources):
    _validate_restrictions(node)
    for stmt in node.body:
        utils.generic_ast_node_transform(stmt, resources)
    resources.set_current_block(resources.get_rtseq().Code.CleanUp)
    for stmt in node.finalbody:
        utils.generic_ast_node_transform(stmt, resources)


def except_transformer(node, resources):
    raise TranslateError(_errormessages.invalid_try_except_orelse)


def _validate_restrictions(node):
    if sys.version_info > (3, 0):
        if node.handlers or node.orelse:
            raise TranslateError(_errormessages.invalid_try_except_orelse)
    if validations.check_if_any_in_block(ast.Return, node.body) or\
       validations.check_if_any_in_block(ast.Return, node.finalbody):
        raise TranslateError(_errormessages.return_not_supported_in_try_finally)
    validations.raise_if_try_in_node_body(node.body)
