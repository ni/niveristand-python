import inspect
from niveristand import _errormessages, errors
from niveristand.clientapi import realtimesequencedefinition


def custom_nivs_yield(node, resources):
    _validate_node()
    realtimesequencedefinition.add_yield(resources.get_current_block())
    return ""


def _validate_node():
    from niveristand._translation.py2rtseq import exp_transformer
    # There's only one valid way to call nivs_yield which is this call stack:
    # 0: _validate_node
    # 1: custom_nivs_yield
    # 2: call_transformer
    # 3: generic_ast_transform
    # 4: exp_transformer
    exp_frame = inspect.stack()[4]
    # Py27 doesn't have the 'function' element but in Py35 frame[3] is valid for backwards compatibility.
    # We can remove this nasty check if we drop 2.7
    func = exp_frame.function if 'function' in dir(exp_frame) else exp_frame[3]
    if func is not exp_transformer.exp_transformer.__name__:
        raise errors.TranslateError(_errormessages.invalid_nivs_yield)
