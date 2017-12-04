import tempfile
from niveristand import decorators
from niveristand import realtimesequencetools
from testutilities import rtseqrunner


@decorators.nivs_rt_sequence
def simple():
    return 1.0


def test_run_simple():
    tempfolder = tempfile.mkdtemp()
    filename = realtimesequencetools.save_py_as_rtseq(simple, tempfolder)
    rtseq_result = rtseqrunner.run_rtseq_local(filename, [], [])
    py_result = simple()
    assert rtseq_result.Value == py_result


def test_call_assert_helper():
    rtseqrunner.assert_run_python_equals_rtseq(simple, 1.0)
