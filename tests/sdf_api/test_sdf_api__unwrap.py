"""Tests the generated python code for AB#2359562: Unwrap wrapped types..."""
import pytest
from niveristand.systemstorage import (  # noqa: I100, E402
    ChannelType,
    OnNodeChangeEventArgs,
    WaveformTypeDataType,
)
from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    Alias,
    CallProcedure,
    Channel,
    ConditionStepComparison,
    CustomDeviceChannel,
    CustomDeviceWaveform,
    LookupTable,
    LUTValue,
    PolynomialScale,
    Procedure,
    SetMultipleVariables,
    Target,
    UserChannel,
)
from niveristand.systemdefinitionapi.modelsupport import (
    VsModelFeatureSet,
    VsModelJsonFileDescriptor,
    VsModelParameter,
)

_random_guid = "1de25881-7f05-49de-90d2-ff0720ee77e2"


def test_property_settter_enum_passed():
    "Runs the test described in the title."
    c = CustomDeviceWaveform("name", _random_guid, WaveformTypeDataType.COMPLEX_DOUBLE)
    assert c.data_type == WaveformTypeDataType.COMPLEX_DOUBLE
    c.data_type = WaveformTypeDataType.DOUBLE
    assert c.data_type == WaveformTypeDataType.DOUBLE


def test_property_setter_does_not_unwrap_primitive_element():
    "Runs the test described in the title."
    c = CustomDeviceChannel("cdc", "775506CE-1485-13A6-56A13E7139081FC2")
    assert _random_guid != c.type_guid
    c.type_guid = _random_guid
    assert _random_guid == c.type_guid


def test_property_setter_unwraps_veristand_elements():
    "Runs the test described in the title."
    a = Alias("alias", "", "unset_path")
    uc = UserChannel("uc1", "", "V", 3.3)
    a.linked_channel = uc
    assert uc == a.linked_channel


@pytest.mark.skip(reason="somewhat difficult to support List<T>, only used in model support")
def test_property_setter_unwraps_to_dotnet_generic_list_of_veristand_elements():
    "Runs the test described in the title."
    v = VsModelJsonFileDescriptor()
    params = [VsModelParameter(), VsModelParameter()]
    v.parameters = params
    pass  # no type error


def test_property_setter_unwraps_sequence_of_veristand_elements():
    "Runs the test described in the title."
    scaled = [3.5, 9.0]
    values = [LUTValue(), LUTValue()]
    values[0].scaled = scaled[0]
    values[1].scaled = scaled[1]
    lt = LookupTable("name")
    lt.lookup_table_values = values
    # instances returned aren't the same as passed in, so we can't compare LUTValues directly
    assert scaled == [x.scaled for x in lt.lookup_table_values]


def test_property_setter_passes_empty_sequence_of_veristand_elements():
    "Runs the test described in the title."
    lt = LookupTable("name")
    lt.lookup_table_values = []
    assert 0 == len(lt.lookup_table_values)


@pytest.mark.skip(reason="TODO: implement test? Only matters for Inport and Outport")
def test_property_setter_passes_2d_dotnet_array():
    "Runs the test described in the title."
    raise NotImplementedError()


@pytest.mark.skip(reason="TODO: implement test? Only matters for Inport and Outport")
def test_property_setter_2d_array_given_sequence_raises_type_error():
    "Runs the test described in the title."
    raise NotImplementedError()


def test_method_enum_passed():
    "Runs the test described in the title."
    p = Procedure("name", "desc")
    cp = CallProcedure("cp1", "first", p)
    assert p.add_command(cp)
    assert p.add_new_condition("name", "", p, ConditionStepComparison.EQUAL, 3.5, cp)


def test_method_unwraps_only_veristand_elements():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    u = UserChannel("uc1", "description", "volts", 3.3)
    assert t.get_user_channels().add_user_channel(u)


def test_method_unwraps_sequence_of_veristand_elements():
    "Runs the test described in the title."
    p = Procedure("name", "desc")
    cps = [CallProcedure("cp1", "first", p), CallProcedure("cp2", "second", p)]
    for cp in reversed(cps):
        assert p.add_command(cp)
    assert p.reorder_command_list(cps)
    assert cps == p.get_command_list()


@pytest.mark.skip(reason="TODO: is this worth the trouble of implementing?")
def test_method_unwraps_ienumerable_of_veristand_elements():
    "Runs the test described in the title."
    # would use Model.import_parameters() or SystemDefinitionExtensions.get_descendant_channels()
    raise NotImplementedError()


def test_method_passes_empty_sequence_of_veristand_elements():
    "Runs the test described in the title."
    p = Procedure("name", "desc")
    assert 0 == len(p.get_command_list())
    assert p.reorder_command_list([])
    assert 0 == len(p.get_command_list())


def test_constructor_enum_passed():
    "Runs the test described in the title."
    CustomDeviceWaveform("name", _random_guid, WaveformTypeDataType.COMPLEX_DOUBLE)
    pass  # Should not raise TypeError


def test_constructor_mix_of_primitive_and_veristand_types_are_properly_passed():
    "Runs the test described in the title."
    uc = UserChannel("uc1", "", "V", 3.3)
    a = Alias("alias", "", uc)
    assert "alias" == a.node_path
    assert uc == a.linked_channel


def test_constructor_does_not_unwrap_primitive_element():
    "Runs the test described in the title."
    coeff = [1.5, 2.25, 3.5]
    reverse_coeff = [9.75, 7.5, -1.5]
    scale = PolynomialScale("name", coeff, reverse_coeff, "unit")
    assert coeff == list(scale.polynomial_coeff)
    assert reverse_coeff == list(scale.reverse_polynomial_coeff)


def test_constructor_unwraps_sequence_of_veristand_elements():
    "Runs the test described in the title."
    channels = [UserChannel("uc1", "", "V", 3.3), Channel(ChannelType("test", "test"))]
    values = [1.25, 2.5]
    vars = SetMultipleVariables("name", "desc", channels, values)
    assert channels == vars.channels
    assert values == [x for x in vars.values]


def test_constructor_passes_empty_sequence_of_veristand_elements():
    "Runs the test described in the title."
    vars = SetMultipleVariables("name", "desc", [], [])
    assert 0 == len(vars.channels)
    assert 0 == len(vars.values)


@pytest.mark.skip(reason="somewhat difficult, only used for one constructor we don't care about")
def test_constructor_unwraps_four_tuple_version():
    "Runs the test described in the title."
    # mostly testing that the constructor does not throw
    fs = VsModelFeatureSet((1, 2, 3, 4))
    assert fs.supports_non_virtual_bus
    assert not fs.generated_using_latest_addon_version


def test_constructor_does_not_unwrap_four_tuple_if_not_version():
    "Runs the test described in the title."
    non_version_tuple = (1, 2, 3, 4)
    args = OnNodeChangeEventArgs("action", non_version_tuple)
    assert non_version_tuple == tuple(args.m_data)
