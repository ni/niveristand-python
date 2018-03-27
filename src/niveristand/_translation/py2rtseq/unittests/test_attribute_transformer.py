import ast
from niveristand._translation.py2rtseq.attribute_transformer import attribute_transformer
from niveristand._translation.py2rtseq.utils import Resources
from niveristand.clientapi import DoubleValue


def test_datatype_value_works():
    tree = ast.parse("DoubleValue(0).value")
    # tree.body[0] is an Expr, and the attribute is the .value of that node.
    res = attribute_transformer(tree.body[0].value, Resources(None, '<test>'))
    assert res == str(DoubleValue(0))
