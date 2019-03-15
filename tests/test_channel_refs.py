from niveristand import errors, realtimesequencetools
from niveristand.clientapi import RealTimeSequence
import pytest
from testutilities import rtseqrunner, testfunctions
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Expression  # noqa: E501, I100 We need these C# imports to be out of order.


def test_channel_ref_type_string():
    rtseq = RealTimeSequence(testfunctions.channel_ref_type_string)
    assert rtseq._rtseq.Variables.LocalVariables.Variables.Length is 0
    assert rtseq._rtseq.Variables.ChannelReferences.Channels.Length is 1
    assert rtseq._rtseq.Variables.ChannelReferences.Channels[0].Channel.Channel \
        == "Aliases/DesiredRPM"


def test_channel_ref_setter():
    rtseq = RealTimeSequence(testfunctions.channel_ref_setter)
    assert rtseq._rtseq.Code.Main.Body.Statements.Length is 1
    expression = Expression('ch_a = 5')
    assert rtseq._rtseq.Code.Main.Body.Statements[0].Equals(expression)


def test_channel_ref_return():
    testfunc = testfunctions.channel_ref_return
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfunc)


def test_channel_ref_run():
    result = rtseqrunner.run_rtseq_in_VM(testfunctions.channel_ref_validate_getter)
    assert result == 5


def test_channel_ref_run_python():
    result = testfunctions.channel_ref_validate_getter()
    assert result == 5


def test_channel_ref_invalid_channel_set():
    with pytest.raises(errors.VeristandError):
        testfunctions.channel_ref_invalid_channel_set()


def test_channel_ref_invalid_channel_get():
    with pytest.raises(errors.VeristandError):
        testfunctions.channel_ref_invalid_channel_get()


def test_channel_ref_invalid_channel_transform():
    # Transforming sequences with invalid channels should work, because they are not validated. This is, because users
    # need to be able to transform without a deployed system definition and therefore we are not checking through the
    # C# API the validity of a channel. This will be improved in the future to differentiate between the two cases.
    rtseq = RealTimeSequence(testfunctions.channel_ref_invalid_channel_transform)
    assert rtseq._rtseq.Code.Main.Body.Statements.Length is 0
    assert rtseq._rtseq.Variables.ChannelReferences.Channels.Length is 1


def test_channel_ref_array_type_string():
    rtseq = RealTimeSequence(testfunctions.channel_ref_array_type_string)
    assert rtseq._rtseq.Variables.LocalVariables.Variables.Length is 0
    assert rtseq._rtseq.Variables.ChannelReferences.Channels.Length is 1
    assert rtseq._rtseq.Variables.ChannelReferences.Channels[0].Channel.Channel \
        == "Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a"


def test_channel_ref_array_setter():
    rtseq = RealTimeSequence(testfunctions.channel_ref_array_setter)
    assert rtseq._rtseq.Code.Main.Body.Statements.Length is 1
    expression = Expression('ch_a[0] = 5')
    assert rtseq._rtseq.Code.Main.Body.Statements[0].Equals(expression)


def test_channel_ref_array_return():
    testfunc = testfunctions.channel_ref_array_return
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfunc)


def test_channel_ref_for_vector_channel():
    with pytest.raises(errors.VeristandError):
        realtimesequencetools.run_py_as_rtseq(testfunctions.channel_ref_for_vector_channel)

@pytest.mark.skip
def test_channel_ref_array_run():
    result = rtseqrunner.run_rtseq_in_VM(testfunctions.channel_ref_array_validate_getter)
    assert result == 5


@pytest.mark.skip
def test_channel_ref_array_run_python():
    result = testfunctions.channel_ref_array_validate_getter()
    assert result == 5
