from niveristand.realtimesequenceapi import _errormessages
from niveristand.realtimesequenceapi._translation import symbols
from niveristand.realtimesequenceapi.errors import TranslateError


def name_transformer(node, resources):
    if node.id == "None":
        raise TranslateError(_errormessages.none_not_supported)
    if node.id in symbols._symbols:
        return symbols._symbols[node.id]
    elif resources.has_variable(node.id):
        return resources.get_variable_rtseq_name(node.id)
    else:
        return node.id
