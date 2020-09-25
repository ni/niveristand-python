import ast
import sys

from niveristand import _errormessages
from niveristand._translation import utils
from niveristand.clientapi import ErrorAction
from niveristand.clientapi import realtimesequencedefinition
from niveristand.errors import TranslateError


def custom_generate_error(node, resources):
    _validate_restrictions(node)
    try:
        error_code = eval(utils.generic_ast_node_transform(node.args[0], resources))
    except NameError:
        raise TranslateError(_errormessages.invalid_error_code_for_generate_error)
    message = node.args[1].s
    action = ErrorAction[node.args[2].attr]
    realtimesequencedefinition.add_generate_error(resources.get_current_block(), error_code, message, action.value)
    return ""


def _validate_restrictions(node):
    # Python 3.7
    if sys.version_info < (3, 8) and not isinstance(node.args[0], (ast.UnaryOp, ast.Num)):
        raise TranslateError(_errormessages.invalid_error_code_for_generate_error)
    # In Python 3.8, Num is Constant
    elif not utils.check_ast_constant_num(node.args[0]) and not isinstance(node.args[0], ast.UnaryOp):
        raise TranslateError(_errormessages.invalid_error_code_for_generate_error)
    # In Python 3.8, Str is Constant
    if not isinstance(node.args[1], ast.Str) or not utils.check_ast_constant_str(node.args[1]):
        raise TranslateError(_errormessages.invalid_message_for_generate_error)
    if not isinstance(node.args[2], ast.Attribute):
        raise TranslateError(_errormessages.invalid_action_for_generate_error)
