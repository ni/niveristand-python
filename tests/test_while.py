import sys

from niveristand import decorators, exceptions, RealTimeSequence
from niveristand import realtimesequencetools
from niveristand.clientapi.datatypes import BooleanValue, DoubleValue, I32Value
import pytest
from testutilities import rtseqrunner, validation


@decorators.nivs_rt_sequence
def while_pass():
    while True:
        pass


@decorators.nivs_rt_sequence
def while_break():
    while True:
        break


@decorators.nivs_rt_sequence
def while_else_pass_fails():
    while True:
        pass
    else:
        pass


@decorators.nivs_rt_sequence
def while_invalid_boolean():
    while 1:
        pass


@decorators.nivs_rt_sequence
def while_invalid_boolean_const():
    while I32Value(0):
        pass


@decorators.nivs_rt_sequence
def while_invalid_boolean_var():
    a = I32Value(1)
    while a.value:
        pass


@decorators.nivs_rt_sequence
def while_nested():
    while True:
        while True:
            while True:
                pass


@decorators.nivs_rt_sequence
def while_one_statement():
    ret_var = I32Value(0)
    while ret_var.value == 0:
        ret_var.value = 1
    return ret_var.value


@decorators.nivs_rt_sequence
def while_multiple_statements():
    cond = BooleanValue(False)
    ret_var = I32Value(0)
    while cond.value is False:
        cond.value = True
        ret_var.value = 1
        ret_var.value = 2
        ret_var.value = 3
    return ret_var.value


@decorators.nivs_rt_sequence
def while_condition_variable():
    var = BooleanValue(True)
    while var.value:
        var.value = False
    return var.value


@decorators.nivs_rt_sequence
def while_condition_equal_operator():
    var = I32Value(1)
    while var.value == 1:
        var.value = 2
    return var.value


@decorators.nivs_rt_sequence
def while_condition_identity_operator():
    var = BooleanValue(True)
    ret = I32Value(0)
    while var.value is True:
        ret.value = 1
        var.value = False
    return ret.value


@decorators.nivs_rt_sequence
def while_condition_identity_not_operator():
    var = BooleanValue(True)
    ret = I32Value(0)
    while var.value is not False:
        ret.value = 1
        var.value = False
    return ret.value


@decorators.nivs_rt_sequence
def returns_true_if_lessthan_5(x):
    a = BooleanValue(True)
    if x >= 5:
        a.value = False
    return a.value


@decorators.nivs_rt_sequence
def while_condition_function_call():
    ret = DoubleValue(0)
    while returns_true_if_lessthan_5(ret.value):
        ret.value += 1
    return ret.value


@decorators.nivs_rt_sequence
def while_condition_complex_expression():
    a = DoubleValue(0)
    # the part before the or is true while a.value >= 6
    # the part after the or is true while a.value <6
    # so the last iteration should be a.value == 6
    while ((True and False) is ((a.value * 3) < 20)) or returns_true_if_lessthan_5(a.value - 1):
        a.value += 1
    return a.value


@decorators.nivs_rt_sequence
def while_try_catch_fail():
    while True:
        try:
            pass
        except Exception:
            pass
        finally:
            pass


@decorators.nivs_rt_sequence
def while_try_finally_fail():
    while True:
        try:
            pass
        finally:
            pass


@decorators.nivs_rt_sequence
def while_funcdef_fail():
    while True:
        def f1():
            pass
        f1()


@decorators.nivs_rt_sequence
def while_return_fail():
    a = BooleanValue(True)
    while True:
        return a.value


@decorators.nivs_rt_sequence
def while_false():
    a = I32Value(1)
    while False:
        a.value = 2
    return a.value


run_tests = [
    (while_one_statement, (), 1),
    (while_multiple_statements, (), 3),
    (while_condition_variable, (), False),
    (while_condition_equal_operator, (), 2),
    (while_condition_function_call, (), 5),
    (while_condition_identity_operator, (), 1),
    (while_condition_identity_not_operator, (), 1),
    (while_condition_complex_expression, (), 6),
    (while_false, (), 1),
]


transform_tests = run_tests + [
    (while_pass, (), 0),
    (while_nested, (), 0),
]


fail_transform_tests = [
    (while_invalid_boolean, (), exceptions.VeristandError),
    (while_invalid_boolean_const, (), exceptions.VeristandError),
    (while_invalid_boolean_var, (), exceptions.VeristandError),
    (while_else_pass_fails, (), exceptions.TranslateError),
    (while_break, (), exceptions.TranslateError),
    (while_try_catch_fail, (), exceptions.TranslateError),
    (while_try_finally_fail, (), exceptions.TranslateError),
    (while_return_fail, (), exceptions.TranslateError),
    (while_funcdef_fail, (), exceptions.TranslateError),
]


skip_tests = [
    (returns_true_if_lessthan_5, (), "Can't fake calling into this function."),
]


def idfunc(val):
    return val.__name__


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


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
