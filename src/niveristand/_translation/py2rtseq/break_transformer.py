from niveristand import _errormessages, _exceptions


def break_transformer(node, resources):
    raise _exceptions.TranslateError(_errormessages.break_unsupported)
