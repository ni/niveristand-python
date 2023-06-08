"""Tests the generated python code."""
import pytest
from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    AlarmingStepFunction,
    BaseNode,
    Channel,
    CustomDeviceWaveform,
    DAQCM_Export_StartTrigger_On_Line,
    Target,
    Utilities,
    ValueSource,
)
from niveristand.systemstorage import (  # noqa: I100, E402
    WaveformTypeDataType,
)


def test_no_public_constructor_raises_value_error():
    "Runs the test described in the title."
    with pytest.raises(ValueError):
        BaseNode()


def test_incorrect_constructor_args_raises_type_error():
    "Runs the test described in the title."
    with pytest.raises(TypeError):
        Target("only name")


def test_const_field_returns_expected_value():
    "Runs the test described in the title."
    assert "Username" == Target.username_property_string


def test_static_field_returns_expected_value():
    "Runs the test described in the title."
    assert 2 == Channel.k_writable


def test_instance_field_returns_expected_value():
    "Runs the test described in the title."
    vs = ValueSource(73.5)
    assert (True, 73.5) == (vs.is_constant, vs.constant)


def test_static_property_returns_expected_value():
    "Runs the test described in the title."
    ver = Utilities.current_version
    assert ver.major >= 2020


def test_instance_property_returns_expected_value():
    "Runs the test described in the title."
    t = Target("my name", "Windows")
    assert "my name" == t.name


def test_instance_property_setter_sets_the_value():
    "Runs the test described in the title."
    t = Target("A", "Windows")
    t.description = "description here"
    assert "description here" == t.description


def test_static_method_returns_expected_value():
    "Runs the test described in the title."
    # value is a bit weird because this method actually starts at 1/1/1904 UTC
    assert 600527304999000000 == Utilities.double_to_date_time(99.9).Ticks


def test_instance_method_returns_expected_value():
    "Runs the test described in the title."
    t = Target("A", "Windows")
    assert "" == t.get_document_path()


def test_eq_type():
    "Runs the test described in the title."
    a1 = Target("A", "Windows")
    a2 = Target(a1._dotnet_instance)
    b = Target("B", "Windows")
    assert a1 == a2
    assert a1 != b


def test_eq_enum():
    "Runs the test described in the title."
    ea = AlarmingStepFunction.ENABLE_ALARM
    assert AlarmingStepFunction.ENABLE_ALARM == ea
    assert AlarmingStepFunction.DISABLE_ALARM != ea


def test_eq_enum_none_value():
    "Runs the test described in the title."
    trigger = DAQCM_Export_StartTrigger_On_Line.NONE
    assert DAQCM_Export_StartTrigger_On_Line.NONE == trigger
    assert DAQCM_Export_StartTrigger_On_Line.PFI_0 != trigger


def test_repr_type():
    "Runs the test described in the title."
    t = Target("A", "Windows")
    assert repr(t).startswith(
        "<niveristand.systemdefinitionapi.Target(name=A, node_path=A) object at 0x"
    )


def test_str_type():
    "Runs the test described in the title."
    t = Target("A", "Windows")
    assert str(t).startswith(
        "<niveristand.systemdefinitionapi.Target(name=A, node_path=A) object at 0x"
    )


def test_repr_enum():
    "Runs the test described in the title."
    ea = AlarmingStepFunction.ENABLE_ALARM
    assert "<niveristand.systemdefinitionapi.AlarmingStepFunction.ENABLE_ALARM: 2>" == repr(ea)


def test_str_enum():
    "Runs the test described in the title."
    ea = AlarmingStepFunction.ENABLE_ALARM
    assert "AlarmingStepFunction.ENABLE_ALARM" == str(ea)


def test_int_enum():
    "Runs the test described in the title."
    ea = AlarmingStepFunction.ENABLE_ALARM
    assert 2 == int(ea)


def test_property_returns_python_enum_repr_does_not_raise_error():
    "Runs the test described in the title."
    c = CustomDeviceWaveform("name", "not-a-GUID", WaveformTypeDataType.COMPLEX_DOUBLE)
    str(c.data_type)  # should not raise an error


@pytest.mark.skip(reason="TODO: is this worth the trouble of implementing?")
def test_property_returns_python_enum_with_proper_repr():
    "Runs the test described in the title."
    c = CustomDeviceWaveform("name", "not-a-GUID", WaveformTypeDataType.COMPLEX_DOUBLE)
    assert str(WaveformTypeDataType.COMPLEX_DOUBLE) == str(c.data_type)
