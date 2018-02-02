from niveristand import errormessages, exceptions


def break_transformer(node, resources):
    raise exceptions.TranslateError(errormessages.break_unsupported)
