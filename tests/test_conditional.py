from niveristand import decorators, exceptions, RealTimeSequence
from niveristand.datatypes import Boolean, Int32
import pytest
from testutilities import rtseqrunner


@decorators.nivs_rt_sequence
def if_pass():
    if True:
        pass


@decorators.nivs_rt_sequence
def if_else_pass():
    if True:
        pass
    else:
        pass


@decorators.nivs_rt_sequence
def if_invalid_boolean():
    if 1:
        pass


@decorators.nivs_rt_sequence
def if_invalid_boolean_const():
    if Int32(0):
        pass


@decorators.nivs_rt_sequence
def if_invalid_boolean_var():
    a = Int32(1)
    if a.value:
        pass


@decorators.nivs_rt_sequence
def if_elif_pass():
    if True:
        pass
    elif True:
        pass
    else:
        pass


@decorators.nivs_rt_sequence
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


@decorators.nivs_rt_sequence
def if_condition_variable():
    var = Boolean(0)
    if var.value:
        var.value = True
    else:
        var.value = False
    return var.value


@decorators.nivs_rt_sequence
def if_condition_equal_operator():
    var = Boolean(0)
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


run_tests = [
    (if_one_statement, (), 1),
    (if_multiple_statements, (), 3),
    (if_condition_variable, (), False),
]


transform_tests = run_tests + [
    (if_pass, (), 0),
    (if_else_pass, (), 0),
    (if_elif_pass, (), 0),
    (if_nested, (), 0),
]


fail_transform_tests = [
    (if_invalid_boolean, (), exceptions.VeristandError),
    (if_invalid_boolean_const, (), exceptions.VeristandError),
    (if_invalid_boolean_var, (), exceptions.VeristandError)
]


skip_tests = [
    (if_condition_equal_operator, (), "Operator not implemented yet"),
    (if_condition_identity_operator, (), "Operator not implemented yet"),
    (if_condition_identity_not_operator, (), "Operator not implemented yet"),
    (if_condition_complex_expression, (), "Operator not implemented yet"),
    (if_elif_condition_complex_expression, (), "Operator not implemented yet"),
    (if_condition_function_call, (), "Function calls not implemented yet"),
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
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    try:
        RealTimeSequence(func_name)
    except expected_result:
        pass
    except exceptions.VeristandError as e:
        pytest.fail('Unexpected exception raised:' +
                    str(e.__class__) + ' while expected was: ' + expected_result.__name__)
    except Exception as exception:
        pytest.fail('ExpectedException not raised: ' + exception)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)
