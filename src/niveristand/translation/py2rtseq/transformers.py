import ast
from niveristand import datatypes
from niveristand import decorators
from niveristand import errormessages
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.exceptions import TranslateError
from niveristand.internal import BLOCK
from niveristand.internal import LOCAL_VARIABLES
from niveristand.internal import RTSEQ
from niveristand.translation import symbols
from niveristand.translation import utils


def _has_rtseq_decorator(func_node):
    for decorator in func_node.decorator_list:
        if (isinstance(decorator, ast.Name) and (decorator.id == decorators.nivs_rt_sequence.__name__)) or \
                (isinstance(decorator, ast.Attribute) and (
                    decorator.attr == decorators.nivs_rt_sequence.__name__)):
            return True
    return False


def generic_transform(node, resources):
    transformer_name = "_" + node.__class__.__name__ + "Transformer"
    transformer = getattr(TransformerFactory, transformer_name, TransformerFactory._DefaultTransformer)
    return transformer.transform(node, resources)


class DefaultTransformer:
    @staticmethod
    def transform(node, resources):
        raise TranslateError("Unexpected transform for node type %s" % node.__class__.__name__)


class ModuleTransformer:
    @staticmethod
    def transform(node, resources):
        rtseqfuncs = [rtf for rtf in ast.iter_child_nodes(node) if
                      type(rtf) is ast.FunctionDef and _has_rtseq_decorator(rtf)]
        for rtseqfunc in rtseqfuncs:
            generic_transform(rtseqfunc, resources)
        return ""


class FunctionDefTransformer:
    @staticmethod
    def transform(node, resources):
        resources[RTSEQ] = rtseqapi.create_real_time_sequence()
        resources[BLOCK] = resources[RTSEQ].Code.Main.Body
        for instruction in node.body:
            generic_transform(instruction, resources)
        return ""


class PassTransformer:
    @staticmethod
    def transform(node, resources):
        return ""


class AssignTransformer:
    @staticmethod
    def transform(node, resources):
        variable_name = generic_transform(node.targets[0], resources)
        node_value = generic_transform(node.value, resources)
        rtseq = resources[RTSEQ]
        block = resources[BLOCK]
        if variable_name not in resources[LOCAL_VARIABLES]:
            # new local variable
            if isinstance(node_value, datatypes.DataType):
                rtseq_var_name = utils.create_rtseq_variable(variable_name, node_value, rtseq)
                # add the local variable's accessor to the resources
                variable_name += ".value"
                resources[LOCAL_VARIABLES][variable_name] = rtseq_var_name
            else:
                raise TranslateError(errormessages.init_var_invalid_type)
        utils.add_assignment(block, resources[LOCAL_VARIABLES][variable_name], node_value)


class AttributeTransformer:
    @staticmethod
    def transform(node, resources):
        built_exp = generic_transform(node.value, resources) + '.' + node.attr
        if built_exp in symbols._symbols:
            return symbols._symbols[built_exp]
        return built_exp


class NumTransformer:
    @staticmethod
    def transform(node, resources):
        return node.n


class NameTransformer:
    @staticmethod
    def transform(node, resources):
        if node.id in symbols._symbols:
            return symbols._symbols[node.id]
        else:
            return node.id


class CallTransformer:
    @staticmethod
    def transform(node, resources):
        if node.func.id in datatypes.VALID_TYPES:
            datatype = datatypes.VALID_TYPES[node.func.id]
            datavalue = generic_transform(node.args[0], resources)
            return datatype(datavalue)
        node_str = str(generic_transform(node.func, resources)) + "("
        for arg in node.args:
            node_str += str(generic_transform(arg, resources))
        return node_str + ")"


class TransformerFactory:
    _DefaultTransformer = DefaultTransformer
    _ModuleTransformer = ModuleTransformer
    _FunctionDefTransformer = FunctionDefTransformer
    _PassTransformer = PassTransformer
    _AssignTransformer = AssignTransformer
    _NumTransformer = NumTransformer
    _AttributeTransformer = AttributeTransformer
    _NameTransformer = NameTransformer
    _CallTransformer = CallTransformer
