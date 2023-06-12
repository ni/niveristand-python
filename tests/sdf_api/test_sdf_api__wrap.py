"""Tests the generated python code for return value wrapping."""
import pytest
from niveristand.systemstorage import (  # noqa: I100, E402
    AliasType,
    ChannelType,
    VersionType,
    WaveformTypeDataType,
)
from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    AlarmPriority,
    Alias,
    BaseNode,
    Channel,
    CustomDeviceChannel,
    CustomDeviceWaveform,
    Dictionary,
    DictionaryElement,
    NodeIDUtil,
    PolynomialScale,
    SetMultipleVariables,
    SLSCChassis,
    SystemDefinition,
    SystemDefinitionExtensions,
    Target,
    UserChannel,
    UserChannels,
    Utilities,
    ValueSource,
)

_random_guid = "1de25881-7f05-49de-90d2-ff0720ee77e2"
_alias_guid = "2c11e122-dad9-44da-989c-a66ff203fa31"


def test_enum_returns_its_value():
    "Runs the test described in the title."
    m = AlarmPriority.MEDIUM
    assert AlarmPriority == type(m)  # noqa: E721 - we want to directly compare types
    assert m == AlarmPriority.MEDIUM
    assert "<niveristand.systemdefinitionapi.AlarmPriority.MEDIUM: 1>" == repr(m)


def test_nested_enum_returns_its_value():
    "Runs the test described in the title."
    hia = SLSCChassis.SLSCChassisIDType.HOSTNAME_IP_ADDRESS
    ect = SLSCChassis.SLSCChassisType.E12001_CHASSIS_TYPE
    outer_type = "niveristand.systemdefinitionapi.SLSCChassis"
    assert f"<{outer_type}.SLSCChassisIDType.HOSTNAME_IP_ADDRESS: 1>" == repr(hia)
    assert f"<{outer_type}.SLSCChassisType.E12001_CHASSIS_TYPE: 0>" == repr(ect)


def test_property_base_type_return_value_returns_derived_type():
    "Runs the test described in the title."
    vs = ValueSource(UserChannel("uc1", "", "V", 3.3))
    assert UserChannel == type(vs.channel)  # noqa: E721 - we want to directly compare types


def test_property_sequence_of_base_type_return_value_returns_derived_types():
    "Runs the test described in the title."
    channels = [UserChannel("uc1", "", "V", 3.3), Channel(ChannelType("test", "test"))]
    vars = SetMultipleVariables("name", "desc", channels, [1.25, 2.5])
    assert [type(x) for x in channels] == [type(x) for x in vars.channels]


def test_property_return_of_primitive_element_is_not_wrapped():
    "Runs the test described in the title."
    u = UserChannel("uc1", "description", "volts", 3.3)
    assert "uc1" == u.name


def test_property_return_of_sequence_of_primitive_elements_none_are_wrapped():
    "Runs the test described in the title."
    coeff = [1.5, 2.25, 3.5]
    reverse_coeff = [9.75, 7.5, -1.5]
    scale = PolynomialScale("name", coeff, reverse_coeff, "unit")
    assert coeff == list(scale.polynomial_coeff)
    assert reverse_coeff == list(scale.reverse_polynomial_coeff)


def test_property_return_of_sequence_of_veristand_elements_all_are_wrapped():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_boolean("a", True)
    d.add_i16("bb", 12345)
    d.add_double("ccc", 34.5)
    elements = d.elem
    assert 3 == len(elements)
    for e in elements:
        assert DictionaryElement == type(e)


def test_property_returns_python_enum():
    "Runs the test described in the title."
    c = CustomDeviceWaveform("name", _random_guid, WaveformTypeDataType.COMPLEX_DOUBLE)
    assert WaveformTypeDataType.COMPLEX_DOUBLE == c.data_type


def test_property_returns_version():
    "Runs the test described in the title."
    sdf = SystemDefinition(
        "name", "desc", "creator", "", "Controller", "Windows", r"C:\does_not_exist"
    )
    assert (2020, 0, 0, 0) == sdf.version
    assert "(2020, 0, 0, 0)" == str(sdf.version)


@pytest.mark.skip(reason="TODO: implement test? Only matters for Inport and Outport")
def test_property_returns_2d_array():
    "Runs the test described in the title."
    raise NotImplementedError()


def test_method_base_type_return_value_returns_derived_type():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    u = UserChannel("uc1", "description", "volts", 3.3)
    ucs = t.get_user_channels()
    ucs.add_user_channel(u)
    assert ucs == SystemDefinitionExtensions.get_parent(u)
    assert (True, ucs) == u.get_parent()


def test_method_sequence_of_base_type_return_value_returns_derived_types():
    "Runs the test described in the title."
    alias_core = AliasType("name", _alias_guid)
    alias = NodeIDUtil.id_to_base_node(alias_core.id)
    assert Alias == type(alias)


def test_method_return_of_primitive_element_is_not_wrapped():
    "Runs the test described in the title."
    u = UserChannel("uc1", "description", "volts", 3.3)
    assert "" == u.get_document_path()


def test_method_return_of_veristand_element_is_wrapped():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    uc = t.get_user_channels()
    assert UserChannels == type(uc)


def test_method_return_of_sequence_of_primitive_elements_none_are_wrapped():
    "Runs the test described in the title."
    b = [True, False, False, True]
    d = Dictionary()
    d.add_boolean_array("bools", b)
    actual_success, actual_array = d.get_boolean_array("bools")
    assert (True, b) == (actual_success, list(actual_array))


def test_method_return_of_sequence_of_veristand_elements_all_are_wrapped():
    "Runs the test described in the title."
    c = CustomDeviceChannel("cdc", "775506CE-1485-13A6-56A13E7139081FC2")
    d1, d2 = Dictionary(), Dictionary()
    d1.add_boolean("a", True)
    d2.add_i16("bb", 12345)
    c.set_dictionary_array_property("dict", [d1, d2])
    actual = c.get_dictionary_array_property("dict")
    assert 2 == len(actual)
    assert (True, [Dictionary, Dictionary]) == (actual[0], [type(x) for x in actual[1]])
    assert [("a", True), ("bb", 12345)] == [(de.key, de.item) for d in actual[1] for de in d.elem]


def test_method_void_return_primitive_out_only_out_returned():
    "Runs the test described in the title."
    a = AliasType("name", _alias_guid)
    assert ([], []) == a.get_node_properties()


def test_method_return_of_ienumerable_of_veristand_elements_all_are_wrapped():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    results = SystemDefinitionExtensions.get_descendant_channels(t)
    assert len(results)
    assert all(isinstance(result, BaseNode) for result in results)
    assert list == type(results)


def test_method_returns_version():
    "Runs the test described in the title."
    vt = VersionType()
    vt.major = 3
    vt.minor = 2
    vt.fix = 1
    vt.build = 456
    v = Utilities.version_type_to_version(vt)
    assert (3, 2, 1, 456) == v
    assert "(3, 2, 1, 456)" == str(v)
