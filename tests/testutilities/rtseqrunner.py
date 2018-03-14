import os
import tempfile
import clr
from niveristand import realtimesequencetools
from niveristand.clientapi._datatypes import DataType
import pytest
import testutilities.configutilities as configutilities


rtseq_dll_path = os.path.join(configutilities.getbinariesfolder(),
                              "NationalInstruments.VeriStand.RealTimeSequenceUtilities.dll")


def _check_can_run_local():
    if not os.path.isfile(rtseq_dll_path):
        pytest.skip("RealTimeSequenceRunner assembly not present.")


def run_rtseq_local(filepath, channel_names=[], channel_values=[], deltat=1):
    _check_can_run_local()
    clr.AddReference(rtseq_dll_path)
    from NationalInstruments.VeriStand.RealTimeSequenceUtilities import RealTimeSequenceRunner

    res = RealTimeSequenceRunner.Run(filepath, channel_names, channel_values, float(deltat))
    return res


def assert_run_python_equals_rtseq(func, expected):
    tempfolder = tempfile.mkdtemp()
    filename = realtimesequencetools.save_py_as_rtseq(func, tempfolder)
    rtseq_result = run_rtseq_local(filename)
    py_result = func()
    if isinstance(py_result, DataType):
        py_result = py_result.value
    assert py_result == expected
    assert rtseq_result.Value == py_result


def run_rtseq_in_VM(func, deltat=1):
    from NationalInstruments.VeriStand.Data import VoidValue
    filename = realtimesequencetools.save_py_as_rtseq(func, None)
    rtseq_result = run_rtseq_local(filename, deltat=deltat)
    if isinstance(rtseq_result, VoidValue):
        return None
    return rtseq_result.Value
