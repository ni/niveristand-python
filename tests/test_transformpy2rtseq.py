from niveristand import exceptions
from niveristand import RealTimeSequence
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


def test_return_named_type():
    testfunc = testfuncs.return_named_type
    rtseq = RealTimeSequence(testfunc)
    assert(isinstance(rtseq._rtseq.Variables.ReturnType.DefaultValue.Value, float))
    assert(rtseq._rtseq.Code.Main.Body.Statements.Length is 1)


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
