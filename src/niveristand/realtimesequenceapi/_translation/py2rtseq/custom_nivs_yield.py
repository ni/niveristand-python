import inspect
from niveristand.realtimesequenceapi import _errormessages
from niveristand.realtimesequenceapi.clientapi import realtimesequencedefinition
from niveristand.realtimesequenceapi import errors


def custom_nivs_yield(node, resources):
    _validate_node()
    realtimesequencedefinition.add_yield(resources.get_current_block())
    return ""


def _validate_node():
    from niveristand.realtimesequenceapi._translation.py2rtseq import exp_transformer

    # There's only one valid way to call nivs_yield which is this call stack:
    # 0: _validate_node
    # 1: custom_nivs_yield
    # 2: call_transformer
    # 3: generic_ast_transform
    # 4: exp_transformer
    exp_frame = inspect.stack()[4]
    func = exp_frame.function
    if func is not exp_transformer.exp_transformer.__name__:
        raise errors.TranslateError(_errormessages.invalid_nivs_yield)
