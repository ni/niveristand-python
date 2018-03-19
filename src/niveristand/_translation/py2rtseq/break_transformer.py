from niveristand import _errormessages, errors


def break_transformer(node, resources):
    raise errors.TranslateError(_errormessages.break_unsupported)
