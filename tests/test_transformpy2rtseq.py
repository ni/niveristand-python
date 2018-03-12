from niveristand import exceptions
from niveristand import RealTimeSequence
from niveristand.clientapi.datatypes import BooleanValue, BooleanValueArray, DoubleValue, DoubleValueArray
import pytest
import testutilities.testfunctions as testfuncs


def test_transform_invalid_function_fails():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(testfuncs)


def test_transform_func_without_decorator_fails():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(testfuncs.func_without_decorator)


def test_transform_empty():
    rtseq = RealTimeSequence(testfuncs.empty_func)
    assert rtseq._rtseq is not None
    assert rtseq._rtseq.Code.Main.Body.Statements.Length is 0
    assert rtseq._rtseq.Variables.LocalVariables.Variables.Length is 0


def test_transform_empty_with_two_decorators():
    rtseq = RealTimeSequence(testfuncs.empty_func_with_double_decorator)
    assert rtseq._rtseq is not None
    assert rtseq._rtseq.Code.Main.Body.Statements.Length is 0
    assert rtseq._rtseq.Variables.LocalVariables.Variables.Length is 0


def test_transform_simple_local_assignment():
    testfunc = testfuncs.simple_local_assignment
    rtseq = RealTimeSequence(testfunc)
    assert (rtseq._rtseq.Variables.LocalVariables.Variables.Length is 1)


def test_transform_pi_assign_to_local():
    testfunc = testfuncs.simple_assign_pi
    rtseq = RealTimeSequence(testfunc)
    assert(rtseq._rtseq.Variables.LocalVariables.Variables.Length is 1)
    assert(rtseq._rtseq.Code.Main.Body.Statements.Length is 3)


def test_untyped_declarations_fail():
    testfunc = testfuncs.assign_untyped
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(testfunc)


def test_return_var():
    testfunc = testfuncs.return_var
    rtseq = RealTimeSequence(testfunc)
    assert(isinstance(rtseq._rtseq.Variables.ReturnType.DefaultValue.Value, float))
    assert(rtseq._rtseq.Code.Main.Body.Statements.Length is 2)


def test_return_var_value():
    testfunc = testfuncs.return_var_value
    rtseq = RealTimeSequence(testfunc)
    assert(isinstance(rtseq._rtseq.Variables.ReturnType.DefaultValue.Value, float))
    assert(rtseq._rtseq.Code.Main.Body.Statements.Length is 2)


def test_undeclared_variable_fail():
    testfunc = testfuncs.return_var_invalid_value
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(testfunc)


def test_return_named_type():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(testfuncs.return_named_type)


def test_return_primitive_num():
    testfunc = testfuncs.return_primitive_num
    rtseq = RealTimeSequence(testfunc)
    assert(isinstance(rtseq._rtseq.Variables.ReturnType.DefaultValue.Value, float))
    assert(rtseq._rtseq.Code.Main.Body.Statements.Length is 1)


def test_return_var_pi():
    testfunc = testfuncs.return_var_pi
    rtseq = RealTimeSequence(testfunc)
    assert(isinstance(rtseq._rtseq.Variables.ReturnType.DefaultValue.Value, float))
    assert(rtseq._rtseq.Code.Main.Body.Statements.Length is 3)


def test_return_untyped_symbol():
    testfunc = testfuncs.return_untyped_symbol
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(testfunc)


def test_multiple_returns():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(testfuncs.multiple_returns)


def test_return_not_last():
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(testfuncs.return_not_last)


def test_default_value_bool_true():
    testfunc = testfuncs.return_true
    rtseq = RealTimeSequence(testfunc)
    assert rtseq._rtseq.Variables.LocalVariables.Variables[0].DefaultValue.Value is True


def test_default_value_bool_false():
    testfunc = testfuncs.return_false
    rtseq = RealTimeSequence(testfunc)
    assert rtseq._rtseq.Variables.LocalVariables.Variables[0].DefaultValue.Value is False


def test_boolean_array_return_type():
    ret = testfuncs.return_boolean_array()
    assert isinstance(ret, BooleanValueArray)
    assert isinstance(ret[0], BooleanValue)
    assert ret[0].value is True
    assert isinstance(ret[1], BooleanValue)
    assert ret[1].value is False


def test_double_array_return_type():
    ret = testfuncs.return_double_array()
    assert isinstance(ret, DoubleValueArray)
    assert isinstance(ret[0], DoubleValue)
    assert ret[0].value == 0.0
    assert isinstance(ret[3], DoubleValue)
    assert ret[3].value == 3.0


def test_a_value_value_assignment():
    testfunc = testfuncs.a_value_value_assignment
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(testfunc)


def test_a_value_value_assign_to():
    testfunc = testfuncs.a_value_value_assign_to
    with pytest.raises(exceptions.TranslateError):
        RealTimeSequence(testfunc)
