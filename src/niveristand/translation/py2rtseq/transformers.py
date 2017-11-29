import ast
import sys
from niveristand.translation.py2rtseq import assign_transformer
from niveristand.translation.py2rtseq import attribute_transformer
from niveristand.translation.py2rtseq import binaryoperator_transformer
from niveristand.translation.py2rtseq import call_transformer
from niveristand.translation.py2rtseq import default_transformer
from niveristand.translation.py2rtseq import functiondef_transformer
from niveristand.translation.py2rtseq import if_transformer
from niveristand.translation.py2rtseq import module_transformer
from niveristand.translation.py2rtseq import name_transformer
from niveristand.translation.py2rtseq import nameconstant_transformer
from niveristand.translation.py2rtseq import num_transformer
from niveristand.translation.py2rtseq import pass_transformer
from niveristand.translation.py2rtseq import return_transformer


TRANSFORMERS = {
    'Default': default_transformer.default_transformer,
    ast.Assign.__name__: assign_transformer.assign_transformer,
    ast.Attribute.__name__: attribute_transformer.attribute_transformer,
    ast.Call.__name__: call_transformer.call_transformer,
    ast.FunctionDef.__name__: functiondef_transformer.functiondef_transformer,
    ast.If.__name__: if_transformer.if_transformer,
    ast.Module.__name__: module_transformer.module_transformer,
    ast.Name.__name__: name_transformer.name_transformer,
    ast.Num.__name__: num_transformer.num_transformer,
    ast.Pass.__name__: pass_transformer.pass_transformer,
    ast.Return.__name__: return_transformer.return_transformer,
    ast.BinOp.__name__: binaryoperator_transformer.binaryoperator_transformer,
}

if sys.version_info >= (3, 5):
    TRANSFORMERS[ast.NameConstant.__name__] = nameconstant_transformer.nameconstant_transformer
