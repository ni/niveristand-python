from niveristand import exceptions
from niveristand import RealTimeSequence
import pytest
import testutilities.testfunctions as testfuncs


def test_transform_invalid_fucntion_fails():
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
