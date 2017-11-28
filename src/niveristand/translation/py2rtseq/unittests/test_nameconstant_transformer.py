import ast
import sys
from niveristand import exceptions
from niveristand.translation.py2rtseq import nameconstant_transformer
import pytest


def test_true_node_returns_true_string():
    if sys.version_info >= (3, 5):
        node = ast.NameConstant(value=True)
        res = nameconstant_transformer.nameconstant_transformer(node, None)
        assert res == "true"


def test_false_node_returns_false_string():
    if sys.version_info >= (3, 5):
        node = ast.NameConstant(value=False)
        res = nameconstant_transformer.nameconstant_transformer(node, None)
        assert res == "false"


def test_none_node_throws():
    if sys.version_info >= (3, 5):
        node = ast.NameConstant(value=None)
        with pytest.raises(exceptions.TranslateError):
            nameconstant_transformer.nameconstant_transformer(node, None)
