from niveristand.errors import TranslateError


def default_transformer(node, resources):
    raise TranslateError("Unexpected transform for node type %s" % node.__class__.__name__)
