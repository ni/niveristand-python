import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def if_pass():
    if True:
        pass


@nivs_rt_sequence
def if_else_pass():
    if True:
        pass
    else:
        pass


@nivs_rt_sequence
def if_invalid_boolean():
    if 1:
        pass


@nivs_rt_sequence
def if_invalid_boolean_const():
    if I32Value(0):
        pass


@nivs_rt_sequence
def if_invalid_boolean_var():
    a = I32Value(1)
    if a.value:
        pass


@nivs_rt_sequence
def if_elif_pass():
    if True:
        pass
    elif True:
        pass
    else:
        pass


@nivs_rt_sequence
def if_nested():
    if True:
        if True:
            if True:
                pass
            else:
                if True:
                    pass
                else:
                    pass
        elif True:
            pass
        else:
            pass
    else:
        pass


@nivs_rt_sequence
def if_one_statement():
    ret_var = I32Value(0)
    if True:
        ret_var.value = 1
    else:
        ret_var.value = 2
    return ret_var.value


@nivs_rt_sequence
def if_multiple_statements():
    ret_var = I32Value(0)
    if True:
        ret_var.value = 1
        ret_var.value = 2
        ret_var.value = 3
    elif False:
        ret_var.value = 4
        ret_var.value = 5
    else:
        ret_var.value = 6
        ret_var.value = 7
        ret_var.value = 8

    return ret_var.value


@nivs_rt_sequence
def if_condition_variable():
    var = BooleanValue(0)
    if var.value:
        var.value = True
    else:
        var.value = False
    return var.value


@nivs_rt_sequence
def if_condition_equal_operator():
    var = I32Value(1)
    if var.value == 1:
        var.value = 2
    else:
        var.value = 3
    return var.value


@nivs_rt_sequence
def if_condition_identity_operator():
    var = BooleanValue(True)
    ret = I32Value(0)
    if var.value is True:
        ret.value = 1
    return ret.value


@nivs_rt_sequence
def if_condition_identity_not_operator():
    var = BooleanValue(True)
    ret = I32Value(0)
    if var is not False:
        ret.value = 1
    return ret.value


@nivs_rt_sequence
def _returns_true():
    a = BooleanValue(True)
    return a.value


@nivs_rt_sequence
def if_condition_function_call():
    ret = I32Value(0)
    if _returns_true():
        ret.value = 1
    return ret.value


@nivs_rt_sequence
def if_condition_complex_expression():
    a = I32Value(0)
    if (True and False) is not _returns_true() or a.value < 10:
        a.value = 1
    return a.value


@nivs_rt_sequence
def if_elif_condition_complex_expression():
    a = I32Value(0)
    if False:
        a.value = 1
    elif (True and False) is not _returns_true() or a.value < 10:
        a.value = 2
    return a.value


@nivs_rt_sequence
def if_try_catch_fails():
    if True:
        try:
            pass
        except Exception:
            pass
        finally:
            pass


@nivs_rt_sequence
def if_try_finally_fails():
    if True:
        try:
            pass
        finally:
            pass


@nivs_rt_sequence
def if_else_try_finally_fails():
    if True:
        pass
    else:
        try:
            pass
        finally:
            pass


@nivs_rt_sequence
def if_elif_try_finally_fails():
    if True:
        pass
    elif True:
        try:
            pass
        finally:
            pass
    else:
        pass


@nivs_rt_sequence
def if_return_fails():
    a = BooleanValue(True)
    if True:
        return a.value


@nivs_rt_sequence
def if_else_return_fails():
    a = BooleanValue(True)
    if True:
        pass
    else:
        return a.value


@nivs_rt_sequence
def if_elif_return_fails():
    a = BooleanValue(True)
    if False:
        pass
    elif True:
        return a.value
    else:
        pass


@nivs_rt_sequence
def if_funcdef_fails():
    if True:
        def func():
            pass


@nivs_rt_sequence
def if_else_funcdef_fails():
    if False:
        pass
    else:
        def func():
            pass


@nivs_rt_sequence
def if_elif_funcdef_fails():
    if False:
        pass
    elif True:
        def func():
            pass
    else:
        pass


run_tests = [
    (if_one_statement, (), 1),
    (if_multiple_statements, (), 3),
    (if_condition_variable, (), False),
    (if_condition_equal_operator, (), 2),
    (if_condition_function_call, (), 1),
    (if_condition_identity_operator, (), 1),
    (if_condition_identity_not_operator, (), 1),
    (if_condition_complex_expression, (), 1),
    (if_elif_condition_complex_expression, (), 2),
]


transform_tests = run_tests + [
    (if_pass, (), 0),
    (if_else_pass, (), 0),
    (if_elif_pass, (), 0),
    (if_nested, (), 0),
]


fail_transform_tests = [
    (if_invalid_boolean, (), VeristandError),
    (if_invalid_boolean_const, (), VeristandError),
    (if_invalid_boolean_var, (), VeristandError),
    (if_return_fails, (), TranslateError),
    (if_elif_return_fails, (), TranslateError),
    (if_else_return_fails, (), TranslateError),
    (if_try_catch_fails, (), TranslateError),
    (if_try_finally_fails, (), TranslateError),
    (if_elif_try_finally_fails, (), TranslateError),
    (if_else_try_finally_fails, (), TranslateError),
    (if_funcdef_fails, (), TranslateError),
    (if_elif_funcdef_fails, (), TranslateError),
    (if_else_funcdef_fails, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", transform_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
