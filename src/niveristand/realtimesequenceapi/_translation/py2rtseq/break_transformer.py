from niveristand.realtimesequenceapi import _errormessages
from niveristand.realtimesequenceapi import errors


def break_transformer(node, resources):
    raise errors.TranslateError(_errormessages.break_unsupported)
