"""Tests the generated python code for method overload resolution."""
import pytest
from niveristand import VeriStandSdfError  # noqa: I100, E402
from niveristand.systemstorage import ChannelType  # noqa: I100, E402
from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    Alarm,
    AlarmMode,
    AlarmPriority,
    AlarmState,
    Dictionary,
    Procedure,
    Target,
    UserChannel,
    Utilities,
)


def test_out_empty_sequence_resolves():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_string_array("my_key", [])
    actual = d.get_string_array("my_key")  # Does not throw Type Error
    assert 2 == len(actual)
    assert actual[0]
    assert not len(actual[1])


def test_error_out_parameter_given_success_condition_does_not_throw():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    u = UserChannel("uc1", "description", "volts", 3.3)
    assert t.get_user_channels().add_user_channel(u)


def test_error_out_parameter_given_error_condition_throws_error():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    try:
        t.get_user_channels().add_user_channel(None)
        raise AssertionError("Did not throw")
    except Exception as e:
        assert VeriStandSdfError == type(e)  # noqa: E721 - we want to directly compare types
        assert "-307676 (InputParameterInvalid): Input UserChannel cannot be null." == str(e)


def _add_new_alarm(target: Target):
    return target.get_alarms().add_new_alarm(
        "MyAlarm",
        "desc",
        UserChannel("uc1", "description", "volts", 3.3),
        2.5,
        1,
        Procedure("name", "desc"),
        AlarmMode.NORMAL,
        AlarmState.ENABLED,
        AlarmPriority.LOW,
        0,
        "tripped!",
    )


def test_add_new_alarm_given_success_condition_does_not_throw():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    a = _add_new_alarm(t)
    # if we call the `out Error` overload we'll get back an Alarm and not a bool
    assert Alarm == type(a)  # noqa: E721 - we want to directly compare types


def test_add_new_alarm_given_error_condition_throws_error():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    try:
        _add_new_alarm(t)
        _add_new_alarm(t)
        raise AssertionError("Did not throw")
    except Exception as e:
        assert VeriStandSdfError == type(e)  # noqa: E721 - we want to directly compare types


def test_non_final_out_error_param():
    "Runs the test described in the title."
    try:
        Utilities.deserialize_slsc("does_not_exist", ChannelType("test", "test"))
        raise AssertionError("Did not throw")
    except Exception as e:
        assert VeriStandSdfError == type(e)  # noqa: E721 - we want to directly compare types


def test_get_node_errors_given_success_condition_returns_empty_list():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    # an empty list counts as `false` in if statements but isn't None in case folks expect a list
    assert [] == t.get_node_errors()


@pytest.mark.skip(reason="TODO: is it worth implementing this test?")
def test_get_node_errors_given_error_condition_throws_error():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    try:
        t.get_node_errors()
        raise AssertionError("Did not throw")
    except Exception as e:
        assert VeriStandSdfError == type(e)  # noqa: E721 - we want to directly compare types


def test_method_overload_only_differs_by_str_out_parameter_false_case():
    "Runs the test described in the title."
    c = ChannelType("test", "test")
    assert (False, "") == c.get_dependent_node_value_str("none")


def test_method_overload_only_differs_by_str_out_parameter_true_case():
    "Runs the test described in the title."
    c1 = ChannelType("base", "base")
    c2 = ChannelType("dependent", "dependent")
    c1.set_dependent_node_value("test", c2)
    assert (True, "dependent") == c1.get_dependent_node_value_str("test")


def test_method_overload_only_differs_by_BaseNode_out_parameter_false_case():  # noqa N802 (references class names)
    "Runs the test described in the title."
    c = ChannelType("test", "test")
    assert (False, None) == c.get_dependent_node_value_basenodetype("none")


def test_method_overload_only_differs_by_BaseNode_out_parameter_true_case():  # noqa N802 (references class names)
    "Runs the test described in the title."
    c1 = ChannelType("base", "base")
    c2 = ChannelType("dependent", "dependent")
    c1.set_dependent_node_value("test", c2)
    result_bool, result_node = c1.get_dependent_node_value_basenodetype("test")
    assert result_bool
    assert ChannelType == type(result_node)
    assert (c2.name, c2.node_path) == (result_node.name, result_node.node_path)
