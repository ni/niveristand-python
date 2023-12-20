"""Tests the generated python code for method overload resolution."""
import os

import pytest
from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    SystemDefinition,
)


def test_save_system_definition_file_same_filename():
    "Runs the test described in the title."
    try:
        sdf_path = os.path.join(os.path.dirname(__file__), "test-original.nivssdf")
        if os.path.exists(sdf_path):
            os.remove(sdf_path)

        sdf = SystemDefinition("name", "", "", "", "", "Windows", sdf_path)

        assert not os.path.exists(sdf_path)
        sdf.save_system_definition_file()
        assert os.path.exists(sdf_path)
    except Exception as e:
        if type(e).__name__ == "DllNotFoundException":
            pytest.skip("VeriStand installation or vsdev required for NIVeriStand_util.dll")
        else:
            raise


# AB#2583012: save_system_definition_file is not respecting file path argument
def test_save_system_definition_file_different_filename():
    "Runs the test described in the title."
    try:
        original_sdf_path = os.path.join(os.path.dirname(__file__), "test-original.nivssdf")
        alternate_sdf_path = os.path.join(os.path.dirname(__file__), "test-alternate.nivssdf")
        if os.path.exists(original_sdf_path):
            os.remove(original_sdf_path)
        if os.path.exists(alternate_sdf_path):
            os.remove(alternate_sdf_path)

        sdf = SystemDefinition("name", "", "", "", "", "Windows", original_sdf_path)

        sdf.save_system_definition_file(alternate_sdf_path)
        assert os.path.exists(alternate_sdf_path)
        assert not os.path.exists(original_sdf_path)
    except Exception as e:
        if type(e).__name__ == "DllNotFoundException":
            pytest.skip("VeriStand installation or vsdev required for NIVeriStand_util.dll")
        else:
            raise
