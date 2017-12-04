from niveristand.internal import LOCAL_VARIABLES, RT_SEQ_VAR_NAME
from niveristand.translation import symbols


def name_transformer(node, resources):
    if node.id in symbols._symbols:
        return symbols._symbols[node.id]
    elif node.id in resources[LOCAL_VARIABLES]:
        return resources[LOCAL_VARIABLES][node.id][RT_SEQ_VAR_NAME]
    else:
        return node.id
