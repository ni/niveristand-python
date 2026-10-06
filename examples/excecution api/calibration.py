"""Deploy TestScale and demonstrate polynomial channel calibration."""

import time
from pathlib import Path

from niveristand.clientapi import DeployOptions, Factory

GATEWAY_IP = "localhost"
DEPLOY_TIMEOUT_MS = 120_000
CALIBRATION_SETTLE_TIME_SECONDS = 1
THERMOCOUPLE_CHANNEL = "Targets/Controller/Hardware/Chassis/DAQ/Dev2/Analog Input/AI1"
DOUBLE_VALUE_COEFFICIENTS = [0.0, 2.0]


def main() -> None:
    factory = Factory()
    workspace = factory.get_iworkspace2(GATEWAY_IP)
    calibration = factory.get_icalibration2(GATEWAY_IP)

    calibration_assets = (
        Path(__file__).resolve().parents[1] / "clientapi_example_assets"
    )
    test_scale_sdf = calibration_assets / "TestScale.nivssdf"
    calibration_file = calibration_assets / "TestScale.nivscf"
    if not test_scale_sdf.is_file() or not calibration_file.is_file():
        raise FileNotFoundError(
            f"TestScale calibration assets not found in {calibration_assets}"
        )

    deploy_options = DeployOptions()
    deploy_options.deploy_system_definition = True
    deploy_options.calibration_file_path = str(calibration_file)
    deploy_options.timeout = DEPLOY_TIMEOUT_MS
    workspace.connect_to_system(str(test_scale_sdf), deploy_options)

    calibration_applied = False
    try:
        original_calibration = calibration.get_calibration(THERMOCOUPLE_CHANNEL)
        original_value = workspace.get_single_channel_value(THERMOCOUPLE_CHANNEL)
        print(
            f"Raw thermocouple value: {calibration.get_raw_value(THERMOCOUPLE_CHANNEL)}"
        )
        print(f"Value before calibration: {original_value}")

        calibration.set_calibration(THERMOCOUPLE_CHANNEL, DOUBLE_VALUE_COEFFICIENTS)
        calibration_applied = True
        time.sleep(CALIBRATION_SETTLE_TIME_SECONDS)

        calibrated_value = workspace.get_single_channel_value(THERMOCOUPLE_CHANNEL)
        print(f"Value after doubling calibration: {calibrated_value}")
    finally:
        try:
            if calibration_applied:
                if original_calibration:
                    calibration.set_calibration(
                        THERMOCOUPLE_CHANNEL, original_calibration
                    )
                else:
                    calibration.remove_calibration(THERMOCOUPLE_CHANNEL)
        finally:
            workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
