import ast

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
    if not isinstance(node.args[0], (ast.UnaryOp, ast.Num)):
        raise TranslateError(_errormessages.invalid_error_code_for_generate_error)
    if not isinstance(node.args[1], ast.Str):
        raise TranslateError(_errormessages.invalid_message_for_generate_error)
    if not isinstance(node.args[2], ast.Attribute):
        raise TranslateError(_errormessages.invalid_action_for_generate_error)
