import ast

from niveristand import _decorators
from niveristand._translation import utils


def module_transformer(node, resources):
    rtseqfuncs = [rtf for rtf in ast.iter_child_nodes(node) if
                  type(rtf) is ast.FunctionDef and _has_rtseq_decorator(rtf)]
    for rtseqfunc in rtseqfuncs:
        utils.generic_ast_node_transform(rtseqfunc, resources)
    return ""


def _has_rtseq_decorator(func_node):
    for decorator in func_node.decorator_list:
        if (isinstance(decorator, ast.Name) and (decorator.id == _decorators.nivs_rt_sequence.__name__)) or \
                (isinstance(decorator, ast.Attribute) and (
                    decorator.attr == _decorators.nivs_rt_sequence.__name__)):
            return True
    return False
