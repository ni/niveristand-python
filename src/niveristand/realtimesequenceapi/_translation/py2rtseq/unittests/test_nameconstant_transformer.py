import ast
from niveristand.realtimesequenceapi import errors
from niveristand.realtimesequenceapi._translation.py2rtseq import nameconstant_transformer
import pytest


def test_true_node_returns_true_string():
    node = ast.Constant(value=True)
    res = nameconstant_transformer.nameconstant_transformer(node, None)
    assert res == "true"


def test_false_node_returns_false_string():
    node = ast.Constant(value=False)
    res = nameconstant_transformer.nameconstant_transformer(node, None)
    assert res == "false"


def test_none_node_throws():
    node = ast.Constant(value=None)
    with pytest.raises(errors.TranslateError):
        nameconstant_transformer.nameconstant_transformer(node, None)
