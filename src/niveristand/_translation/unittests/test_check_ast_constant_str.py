import ast
from niveristand._translation import utils


def test_true_check_returns_false_bool():
    node = ast.Constant(value=True)
    res = utils.check_ast_constant_str(node)
    assert res is False


def test_false_check_returns_false_bool():
    node = ast.Constant(value=False)
    res = utils.check_ast_constant_str(node)
    assert res is False


def test_none_check_returns_false_bool():
    node = ast.Constant(value=None)
    res = utils.check_ast_constant_str(node)
    assert res is False


def test_int_check_returns_false_bool():
    node = ast.Constant(value=0)
    res = utils.check_ast_constant_str(node)
    assert res is False


def test_float_check_returns_false_bool():
    node = ast.Constant(value=1.0)
    res = utils.check_ast_constant_str(node)
    assert res is False


def test_str_0_check_returns_true_bool():
    node = ast.Constant(value="0")
    res = utils.check_ast_constant_str(node)
    assert res is True


def test_str_true_check_returns_true_bool():
    node = ast.Constant(value="True")
    res = utils.check_ast_constant_str(node)
    assert res is True



def test_str_false_check_returns_true_bool():
    node = ast.Constant(value="False")
    res = utils.check_ast_constant_str(node)
    assert res is True


def test_str_none_check_returns_true_bool():
    node = ast.Constant(value="None")
    res = utils.check_ast_constant_str(node)
    assert res is True


def test_str_0_check_returns_true_bool():
    node = ast.Constant(value="0")
    res = utils.check_ast_constant_str(node)
    assert res is True


def test_str_1_check_returns_true_bool():
    node = ast.Constant(value="1")
    res = utils.check_ast_constant_str(node)
    assert res is True


def test_str_empty_check_returns_true_bool():
    node = ast.Constant(value="")
    res = utils.check_ast_constant_str(node)
    assert res is True
