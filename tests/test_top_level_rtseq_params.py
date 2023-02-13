from niveristand import nivs_rt_sequence
from niveristand import NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import (
    ChannelReference,
    DoubleValue,
    DoubleValueArray,
    RealTimeSequence,
)
from niveristand.errors import VeristandError
import pytest


@NivsParam("p", DoubleValue(1.2), NivsParam.BY_REF)
@nivs_rt_sequence
def func1(p):
    return p.value


@NivsParam("p", DoubleValueArray([1.2, 2.3]), NivsParam.BY_VALUE)
@nivs_rt_sequence
def func2(p):
    return p[0].value


def test_run_py_as_rtseq_numeric_param():
    actual = realtimesequencetools.run_py_as_rtseq(func1, {"p": DoubleValue(2.3)})
    assert actual == 2.3


def test_run_py_as_rtseq_channel_reference_param():
    desired_rpm = ChannelReference("Aliases/DesiredRPM")
    desired_rpm.value = 100.101
    actual = realtimesequencetools.run_py_as_rtseq(func1, {"p": desired_rpm})
    assert actual == 100.101


def test_run_py_as_rtseq_invalid_extra_parameter():
    with pytest.raises(VeristandError):
        realtimesequencetools.run_py_as_rtseq(
            func1, {"p": DoubleValue(2.3), "pp": DoubleValue(3.4)}
        )


def test_run_py_as_rtseq_missing_by_ref_parameter():
    with pytest.raises(VeristandError):
        realtimesequencetools.run_py_as_rtseq(func1, {})


def test_run_py_as_rtseq_missing_by_value_parameter():
    actual = realtimesequencetools.run_py_as_rtseq(func2, {})
    assert actual == 1.2


def test_run_py_as_rtseq_wrong_parameter_data_type():
    with pytest.raises(VeristandError):
        realtimesequencetools.run_py_as_rtseq(func2, {"p": DoubleValue(2.3)})


def test_realtimesequence_numeric_param():
    rtseq = RealTimeSequence(func1)
    actual = rtseq.run({"p": DoubleValue(2.3)})
    actual.wait_for_result()
    assert actual.ret_val == 2.3


def test_realtimesequence_channel_reference_param():
    desired_rpm = ChannelReference("Aliases/DesiredRPM")
    desired_rpm.value = 100.101
    rtseq = RealTimeSequence(func1)
    actual = rtseq.run({"p": desired_rpm})
    actual.wait_for_result()
    assert actual.ret_val == 100.101


def test_realtimesequence_invalid_extra_parameter():
    rtseq = RealTimeSequence(func1)
    with pytest.raises(VeristandError):
        rtseq.run({"p": DoubleValue(2.3), "pp": DoubleValue(3.4)})


def test_realtimesequence_missing_by_ref_parameter():
    rtseq = RealTimeSequence(func1)
    with pytest.raises(VeristandError):
        rtseq.run({})


def test_realtimesequence_missing_by_value_parameter():
    rtseq = RealTimeSequence(func2)
    actual = rtseq.run({})
    actual.wait_for_result()
    assert actual.ret_val == 1.2


def test_realtimesequence_wrong_parameter_data_type():
    rtseq = RealTimeSequence(func2)
    with pytest.raises(VeristandError):
        rtseq.run({"p": DoubleValue(2.3)})
