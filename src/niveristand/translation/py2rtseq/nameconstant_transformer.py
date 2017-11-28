from niveristand import errormessages
from niveristand import exceptions


def nameconstant_transformer(node, resources):
    if node.value is True or node.value is False:
        return str(node.value).lower()
    else:
        raise exceptions.TranslateError(errormessages.name_constant_not_supported)
