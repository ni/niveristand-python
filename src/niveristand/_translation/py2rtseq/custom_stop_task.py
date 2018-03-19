import ast
from niveristand import _errormessages
from niveristand.clientapi import realtimesequencedefinition
from niveristand.errors import TranslateError


def custom_stop_task(node, resources):
    _validate_restrictions(node)
    realtimesequencedefinition.add_stop_task(resources.get_current_block(), node.args[0].id)


def _validate_restrictions(node):
    if not isinstance(node.args[0], ast.Name):
        raise TranslateError(_errormessages.invalid_taskname_for_stop_task)
