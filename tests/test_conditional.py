from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Int32
import pytest


pytestmark = pytest.mark.skip(reason='Not implemented yet')


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
    RealTimeSequence(if_else_pass)
    RealTimeSequence(if_elif_pass)
    RealTimeSequence(if_nested)


@decorators.nivs_rt_sequence
def if_one_statement():
    ret_var = Int32(0)
    if 1:
        ret_var.value = 1
    else:
        ret_var.value = 2
    return ret_var


@decorators.nivs_rt_sequence
def if_multiple_statements():
    ret_var = Int32(0)
    if 1:
        ret_var.value = 1
        ret_var.value = 2
        ret_var.value = 3
    elif 1:
        ret_var.value = 4
        ret_var.value = 5
    else:
        ret_var.value = 6
        ret_var.value = 7
        ret_var.value = 8

    return ret_var


def test_if_with_statements():
    RealTimeSequence(if_one_statement)
    RealTimeSequence(if_multiple_statements)


@decorators.nivs_rt_sequence
def if_condition_variable():
    var = Int32(0)
    if var.value:
        pass
    else:
        pass


@decorators.nivs_rt_sequence
def if_condition_equal_operator():
    var = Int32(0)
    if var.value == 1:
        pass
    else:
        pass


@decorators.nivs_rt_sequence
def if_condition_identity_operator():
    var = True
    if var is True:
        pass


@decorators.nivs_rt_sequence
def if_condition_identity_not_operator():
    var = True
    if var is not False:
        pass


def returns_true():
    return True


@decorators.nivs_rt_sequence
def if_condition_function_call():
    if returns_true() is True:
        pass


@decorators.nivs_rt_sequence
def if_condition_complex_expression():
    a = Int32(0)
    if (True and False) is not a.value * 1 < 10 or returns_true():
        pass


@decorators.nivs_rt_sequence
def if_elif_condition_complex_expression():
    a = Int32(0)
    if False:
        pass
    elif (True and False) is not a.value * 1 < 10 or returns_true():
        pass


def test_if_condition_statements():
    RealTimeSequence(if_condition_variable)
    RealTimeSequence(if_condition_equal_operator)
    RealTimeSequence(if_condition_identity_operator)
    RealTimeSequence(if_condition_identity_not_operator)
    RealTimeSequence(if_condition_function_call)
    RealTimeSequence(if_condition_complex_expression)
    RealTimeSequence(if_elif_condition_complex_expression)
