from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Int32
import pytest
from testutilities import rtseqrunner


@decorators.nivs_rt_sequence
def if_pass():
    if True:
        pass


@decorators.nivs_rt_sequence
def if_else_pass():
    if 1:
        pass
    else:
        pass


@decorators.nivs_rt_sequence
def if_elif_pass():
    if 1:
        pass
    elif 1:
        pass
    else:
        pass


@decorators.nivs_rt_sequence
def if_nested():
    if 1:
        if 1:
            if 1:
                pass
            else:
                if 1:
                    pass
                else:
                    pass
        elif 1:
            pass
        else:
            pass
    else:
        pass


def test_if_pass():
    RealTimeSequence(if_pass)


@pytest.mark.skip("DE14610")
def test_if_else_pass():
    RealTimeSequence(if_else_pass)
    RealTimeSequence(if_elif_pass)
    RealTimeSequence(if_nested)


@decorators.nivs_rt_sequence
def if_one_statement():
    ret_var = Int32(0)
    if True:
        ret_var.value = 1
    else:
        ret_var.value = 2
    return ret_var.value


@decorators.nivs_rt_sequence
def if_multiple_statements():
    ret_var = Int32(0)
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


def test_if_with_statements():
    RealTimeSequence(if_one_statement)
    RealTimeSequence(if_multiple_statements)


def test_run_with_statements():
    rtseqrunner.assert_run_python_equals_rtseq(if_one_statement, 1)
    rtseqrunner.assert_run_python_equals_rtseq(if_multiple_statements, 3)


@decorators.nivs_rt_sequence
def if_condition_variable():
    var = Int32(0)
    if var.value:
        var.value = 1
    else:
        var.value = 2
    return var.value


@decorators.nivs_rt_sequence
def if_condition_equal_operator():
    var = Int32(0)
    if var.value == 1:
        var.value = 1
    else:
        var.value = 2


@decorators.nivs_rt_sequence
def if_condition_identity_operator():
    var = True
    ret = Int32(0)
    if var is True:
        ret.value = 1
    return ret.value


@decorators.nivs_rt_sequence
def if_condition_identity_not_operator():
    var = True
    ret = Int32(0)
    if var is not False:
        pass
    return ret.value


def returns_true():
    return True


@decorators.nivs_rt_sequence
def if_condition_function_call():
    ret = Int32(0)
    if returns_true() is True:
        ret.value = 1
    return ret.value


@decorators.nivs_rt_sequence
def if_condition_complex_expression():
    a = Int32(0)
    if (True and False) is not a.value * 1 < 10 or returns_true():
        a.value = 1
    return a.value


@decorators.nivs_rt_sequence
def if_elif_condition_complex_expression():
    a = Int32(0)
    if False:
        a.value = 1
    elif (True and False) is not a.value * 1 < 10 or returns_true():
        a.value = 2
    return a.value


@pytest.mark.skip("Complex expressions not implemented yet")
def test_if_condition_statements():
    RealTimeSequence(if_condition_variable)
    RealTimeSequence(if_condition_equal_operator)
    RealTimeSequence(if_condition_identity_operator)
    RealTimeSequence(if_condition_identity_not_operator)
    RealTimeSequence(if_condition_function_call)
    RealTimeSequence(if_condition_complex_expression)
    RealTimeSequence(if_elif_condition_complex_expression)


@pytest.mark.skip("Complex expressions not implemented yet")
def test_run_if_condition_statements():
    rtseqrunner.assert_run_python_equals_rtseq(if_condition_variable, 2)
    rtseqrunner.assert_run_python_equals_rtseq(if_condition_equal_operator, 2)
    rtseqrunner.assert_run_python_equals_rtseq(if_condition_identity_operator, 1)
    rtseqrunner.assert_run_python_equals_rtseq(if_condition_identity_not_operator, 0)
    rtseqrunner.assert_run_python_equals_rtseq(if_condition_function_call, 1)
    rtseqrunner.assert_run_python_equals_rtseq(if_condition_complex_expression, 0)
    rtseqrunner.assert_run_python_equals_rtseq(if_elif_condition_complex_expression, 0)
