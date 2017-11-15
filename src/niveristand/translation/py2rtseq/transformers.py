import ast

from niveristand.translation.py2rtseq import default


TRANSFORMERS = {
    'Default': default.default_transformer,
}


def init_python_transformers():
    from niveristand.translation.py2rtseq import pass_transformer
    from niveristand.translation.py2rtseq import assign
    from niveristand.translation.py2rtseq import attribute
    from niveristand.translation.py2rtseq import call
    from niveristand.translation.py2rtseq import functiondef
    from niveristand.translation.py2rtseq import module
    from niveristand.translation.py2rtseq import name
    from niveristand.translation.py2rtseq import num
    from niveristand.translation.py2rtseq import return_transformer

    TRANSFORMERS[ast.Module.__name__] = module.module_transformer
    TRANSFORMERS[ast.FunctionDef.__name__] = functiondef.functiondef_transformer
    TRANSFORMERS[ast.Pass.__name__] = pass_transformer.pass_transformer
    TRANSFORMERS[ast.Assign.__name__] = assign.assign_transformer
    TRANSFORMERS[ast.Num.__name__] = num.num_transformer
    TRANSFORMERS[ast.Attribute.__name__] = attribute.attribute_transformer
    TRANSFORMERS[ast.Name.__name__] = name.name_transformer
    TRANSFORMERS[ast.Call.__name__] = call.call_transformer
    TRANSFORMERS[ast.Return.__name__] = return_transformer.return_transformer
