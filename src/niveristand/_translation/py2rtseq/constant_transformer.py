from niveristand import _errormessages
from niveristand import errors


def constant_transformer(node, resources):
    if node.value is True or node.value is False:
        return str(node.value).lower()
    elif isinstance(node.value, (int, float, complex)) and str(node.value) not in ("True", "False", "None"):
        return str(node.value)
    elif isinstance(node.value, str):
        return node.value
    else:
        raise errors.TranslateError(_errormessages.constant_not_supported)
