from niveristand.exceptions import TranslateError
import ast
import niveristand.decorators as decorators
from niveristand.translation import utils
from niveristand.clientapi import realtimesequencedefinition as rtseqapi


def _has_rtseq_decorator(func_node):
    for decorator in func_node.decorator_list:
        if (isinstance(decorator, ast.Name) and (decorator.id == decorators.nivs_rt_sequence.__name__)) or \
                (isinstance(decorator, ast.Attribute) and (
                    decorator.attr == decorators.nivs_rt_sequence.__name__)):
            return True
    return False


def generic_transform(node, rtseq, block):
    transformer_name = "_" + node.__class__.__name__ + "Transformer"
    transformer = getattr(TransformerFactory, transformer_name, TransformerFactory._DefaultTransformer)
    return transformer.transform(node, rtseq, block)


class DefaultTransformer:
    @staticmethod
    def transform(node, rtseq, block):
        raise TranslateError("Unexpected transform for node type %s" % node.__class__.__name__)

    @staticmethod
    def get_string_expression(node):
        raise TranslateError("Unexpected get_string_expression node type %s" % node.__class__.__name__)


class ModuleTransformer:
    @staticmethod
    def transform(node, rtseq_container, block):
        rtseqfuncs = [rtf for rtf in ast.iter_child_nodes(node) if
                      type(rtf) is ast.FunctionDef and _has_rtseq_decorator(rtf)]
        for rtseqfunc in rtseqfuncs:
            seq = rtseqapi.create_real_time_sequence()
            generic_transform(rtseqfunc, seq, None)
            rtseq_container[rtseqfunc.name] = seq
        return ""


class FunctionDefTransformer:
    @staticmethod
    def transform(node, rtseq, block):
        for instruction in node.body:
            generic_transform(instruction, rtseq, rtseq.Code.Main.Body)
        return rtseq


class PassTransformer:
    @staticmethod
    def transform(node, rtseq, block):
        return rtseq


class AssignTransformer:
    @staticmethod
    def transform(node, rtseq, block):
        if isinstance(node.targets[0], ast.Name):
            # new local variable
            variable_name = node.targets[0].id
            utils.create_rtseq_variable(variable_name, node.value, rtseq)


class TransformerFactory:
    _DefaultTransformer = DefaultTransformer
    _ModuleTransformer = ModuleTransformer
    _FunctionDefTransformer = FunctionDefTransformer
    _PassTransformer = PassTransformer
    _AssignTransformer = AssignTransformer
