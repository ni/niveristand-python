import ast
import sys
from niveristand._translation import utils


def test_true_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=True)
        res = utils.is_node_ast_num(node)
        assert res is False
    assert True


def test_false_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=False)
        res = utils.is_node_ast_num(node)
        assert res is False
    assert True


def test_none_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=None)
        res = utils.is_node_ast_num(node)
        assert res is False
    assert True


def test_str_0_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="0")
        res = utils.is_node_ast_num(node)
        assert res is False
    assert True


def test_str_1_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="1.0")
        res = utils.is_node_ast_num(node)
        assert res is False


def test_str_true_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="True")
        res = utils.is_node_ast_num(node)
        assert res is False


def test_str_false_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="False")
        res = utils.is_node_ast_num(node)
        assert res is False


def test_str_none_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="None")
        res = utils.is_node_ast_num(node)
        assert res is False


def test_str_empty_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="")
        res = utils.is_node_ast_num(node)
        assert res is False


def test_int_0_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=0)
        res = utils.is_node_ast_num(node)
        assert res is True


def test_int_1_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=1)
        res = utils.is_node_ast_num(node)
        assert res is True


def test_float_0_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=0.0)
        res = utils.is_node_ast_num(node)
        assert res is True


def test_float_1_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=1.0)
        res = utils.is_node_ast_num(node)
        assert res is True


def test_complex_1_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=1j)
        res = utils.is_node_ast_num(node)
        assert res is True


def test_complex_2_3_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=complex(2, 3))
        res = utils.is_node_ast_num(node)
        assert res is True
