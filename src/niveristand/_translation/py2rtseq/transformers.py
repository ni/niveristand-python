import ast
import sys
from niveristand._translation.py2rtseq import assign_transformer
from niveristand._translation.py2rtseq import attribute_transformer
from niveristand._translation.py2rtseq import augassign_transformer
from niveristand._translation.py2rtseq import binaryoperator_transformer
from niveristand._translation.py2rtseq import booloperator_transformer
from niveristand._translation.py2rtseq import break_transformer
from niveristand._translation.py2rtseq import call_transformer
from niveristand._translation.py2rtseq import compareoperator_transformer
from niveristand._translation.py2rtseq import default_transformer
from niveristand._translation.py2rtseq import exp_transformer
from niveristand._translation.py2rtseq import for_transformer
from niveristand._translation.py2rtseq import functiondef_transformer
from niveristand._translation.py2rtseq import if_transformer
from niveristand._translation.py2rtseq import ifexp_transformer
from niveristand._translation.py2rtseq import index_transformer
from niveristand._translation.py2rtseq import list_transformer
from niveristand._translation.py2rtseq import module_transformer
from niveristand._translation.py2rtseq import name_transformer
from niveristand._translation.py2rtseq import nameconstant_transformer
from niveristand._translation.py2rtseq import num_transformer
from niveristand._translation.py2rtseq import pass_transformer
from niveristand._translation.py2rtseq import return_transformer
from niveristand._translation.py2rtseq import subscript_transformer
from niveristand._translation.py2rtseq import try_transformer
from niveristand._translation.py2rtseq import unaryoperator_transformer
from niveristand._translation.py2rtseq import while_transformer
from niveristand._translation.py2rtseq import with_transformer


TRANSFORMERS = {
    'Default': default_transformer.default_transformer,
    ast.Assign.__name__: assign_transformer.assign_transformer,
    ast.Attribute.__name__: attribute_transformer.attribute_transformer,
    ast.AugAssign.__name__: augassign_transformer.augassign_transformer,
    ast.BinOp.__name__: binaryoperator_transformer.binaryoperator_transformer,
    ast.BoolOp.__name__: booloperator_transformer.booloperator_transformer,
    ast.Break.__name__: break_transformer.break_transformer,
    ast.Call.__name__: call_transformer.call_transformer,
    ast.Compare.__name__: compareoperator_transformer.compareoperator_transformer,
    ast.Expr.__name__: exp_transformer.exp_transformer,
    ast.For.__name__: for_transformer.for_transformer,
    ast.FunctionDef.__name__: functiondef_transformer.functiondef_transformer,
    ast.If.__name__: if_transformer.if_transformer,
    ast.IfExp.__name__: ifexp_transformer.ifexp_transformer,
    ast.Index.__name__: index_transformer.index_transformer,
    ast.List.__name__: list_transformer.list_transformer,
    ast.Module.__name__: module_transformer.module_transformer,
    ast.Name.__name__: name_transformer.name_transformer,
    ast.Num.__name__: num_transformer.num_transformer,
    ast.Pass.__name__: pass_transformer.pass_transformer,
    ast.Return.__name__: return_transformer.return_transformer,
    ast.Subscript.__name__: subscript_transformer.subscript_transformer,
    ast.UnaryOp.__name__: unaryoperator_transformer.unaryoperator_transformer,
    ast.While.__name__: while_transformer.while_transformer,
    ast.With.__name__: with_transformer.with_transformer,
}

if sys.version_info >= (3, 5):
    TRANSFORMERS[ast.NameConstant.__name__] = nameconstant_transformer.nameconstant_transformer
    TRANSFORMERS[ast.Try.__name__] = try_transformer.try_transformer
else:
    TRANSFORMERS[ast.TryFinally.__name__] = try_transformer.try_transformer
    TRANSFORMERS[ast.TryExcept.__name__] = try_transformer.except_transformer
