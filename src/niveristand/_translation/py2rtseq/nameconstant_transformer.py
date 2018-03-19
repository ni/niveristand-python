from niveristand import _errormessages
from niveristand import errors


def nameconstant_transformer(node, resources):
    if node.value is True or node.value is False:
        return str(node.value).lower()
    else:
        raise errors.TranslateError(_errormessages.name_constant_not_supported)
