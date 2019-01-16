from niveristand import nivs_rt_sequence
from niveristand import NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import ChannelReference, DoubleValue


@NivsParam('p', DoubleValue(1.2), NivsParam.BY_REF)
@nivs_rt_sequence
def func1(p):
    return p.value


def test_func1_numeric():
    actual = realtimesequencetools.run_py_as_rtseq(func1, {"p": DoubleValue(2.3)})
    assert actual == 2.3


def test_func1_channel_reference():
    desired_rpm = ChannelReference('Aliases/DesiredRPM')
    desired_rpm.value = 100.101
    actual = realtimesequencetools.run_py_as_rtseq(func1, {"p": desired_rpm})
    assert actual == 100.101
