"""Tests the generated python code all different `out` types."""
from typing import Any, Sequence, Tuple

from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    Dictionary,
    Target,
    UserChannel,
    Utilities,
)


def test_out_bool_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_boolean("my_key", True)
    assert (True, True) == d.get_boolean("my_key")  # Does not throw Type Error


def test_out_double_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_double("my_key", 1.5)
    assert (True, 1.5) == d.get_double("my_key")  # Does not throw Type Error


def test_out_uint16_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_u16("my_key", 65535)
    assert (True, 65535) == d.get_u16("my_key")  # Does not throw Type Error


def test_out_uint32_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_u32("my_key", 4294967295)
    assert (True, 4294967295) == d.get_u32("my_key")  # Does not throw Type Error


def test_out_uint64_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_u64("my_key", 18446744073709551615)
    assert (True, 18446744073709551615) == d.get_u64("my_key")  # Does not throw Type Error


def test_out_int16_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_i16("my_key", -32768)
    assert (True, -32768) == d.get_i16("my_key")  # Does not throw Type Error


def test_out_int32_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_i32("my_key", -2147483648)
    assert (True, -2147483648) == d.get_i32("my_key")  # Does not throw Type Error


def test_out_int64_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_i64("my_key", -9223372036854775808)
    assert (True, -9223372036854775808) == d.get_i64("my_key")  # Does not throw Type Error


def test_out_str_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_string("my_key", "my_value")
    assert (True, "my_value") == d.get_string("my_key")  # Does not throw Type Error


def test_differs_only_by_out_str():
    "Runs the test described in the title."
    path = r"C:\dev\Some Project\my file.xml"
    expected = (r"C:\dev\Some Project", "my file.xml")
    assert expected == Utilities.strip_path(path)  # Does not throw Type Error


def _assert_dictionary_array(expected_array: Sequence[Any], actual_result: Tuple[bool, Any]):
    assert 2 == len(actual_result)
    assert actual_result[0]
    assert [type(x) for x in expected_array] == [type(x) for x in actual_result[1]]
    assert expected_array == [x for x in actual_result[1]]


def test_out_sequence_of_bool_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [True, True]
    d.add_boolean_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_boolean_array("my_key"))


def test_out_sequence_of_double_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [1.5, 1.5]
    d.add_double_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_double_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_uint16_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [65535, 65535]
    d.add_u16_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_u16_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_uint32_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [4294967295, 4294967295]
    d.add_u32_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_u32_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_uint64_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [18446744073709551615, 18446744073709551615]
    d.add_u64_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_u64_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_int16_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [-32768, -32768]
    d.add_i16_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_i16_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_int32_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [-2147483648, -2147483648]
    d.add_i32_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_i32_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_int64_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [-9223372036854775808, -9223372036854775808]
    d.add_i64_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_i64_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_str_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = ["my_value", "my_value"]
    d.add_string_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_string_array("my_key"))  # Does not throw Type Error


def test_out_BaseNode_param():  # noqa N802 (references class names)
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    u = UserChannel("uc1", "description", "volts", 3.3)
    ucs = t.get_user_channels()
    ucs.add_user_channel(u)
    assert (True, ucs) == u.get_parent()
