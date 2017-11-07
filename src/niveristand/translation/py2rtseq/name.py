from niveristand.translation import symbols


def name_transformer(node, resources):
    if node.id in symbols._symbols:
        return symbols._symbols[node.id]
    else:
        return node.id
