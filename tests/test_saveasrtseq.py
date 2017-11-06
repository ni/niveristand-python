import os
import shutil
import tempfile
from niveristand import realtimesequencetools as rtseq
import pytest
import testutilities.testfunctions as testfuncs


def test_save_creates_file():
    try:
        tempfolder = tempfile.mkdtemp()
        rtseq.save_py_as_rtseq(testfuncs.empty_func, tempfolder)
        exp_path = os.path.join(tempfolder, testfuncs.empty_func.__name__ + ".nivsseq")
        assert os.path.isfile(exp_path)
    finally:
        shutil.rmtree(tempfolder, ignore_errors=True)


def test_save_invalid_folder_throws():
    tempfolder = tempfile.mkdtemp()
    shutil.rmtree(tempfolder, ignore_errors=True)
    with pytest.raises(IOError):
        rtseq.save_py_as_rtseq(testfuncs.empty_func, tempfolder)


def _save_debug_helper(func):
    """Save a sequence so it can be inspected manually."""
    tempfolder = tempfile.mkdtemp()
    print(tempfolder)
    rtseq.save_py_as_rtseq(func, tempfolder)


if __name__ == '__main__':
    _save_debug_helper(testfuncs.simple_assign_pi)
