import inspect
from niveristand import RealTimeSequence
import testutilities.testfunctions as testfuncs


def test_transform_empty():
    rtseq = RealTimeSequence(testfuncs.empty_func, "")
    assert (len(rtseq._seqs) == 1)


def test_transform_module():
    rtseq = RealTimeSequence(testfuncs, "")
    module_funcs = inspect.getmembers(testfuncs, predicate=inspect.isfunction)
    assert (len(rtseq._seqs) is len(module_funcs))


def test_transform_simple_local_assignment():
    testfunc = testfuncs.simple_local_assignment
    rtseq = RealTimeSequence(testfunc, "")
    assert (len(rtseq._seqs) is 1)
    assert (rtseq._seqs[testfunc.__name__].Variables.LocalVariables.Variables.Length is 1)
