from niveristand.translation.py2rtseq.transformers import TRANSFORMERS


def generic_ast_node_transform(node, resources):
    transformer_name = node.__class__.__name__
    transformer = TRANSFORMERS.get(transformer_name, TRANSFORMERS['Default'])
    return transformer(node, resources)
