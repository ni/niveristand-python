"""Deploy Calibration Demo and demonstrate polynomial channel calibration."""

import os
import time

from niveristand import VeriStandException
from niveristand.clientapi import DeployOptions, Factory

GATEWAY_IP = "localhost"
DEPLOY_TIMEOUT_MS = 120_000
CALIBRATION_SETTLE_TIME_SECONDS = 1
THERMOCOUPLE_CHANNEL = "Targets/Controller/Hardware/Chassis/DAQ/Dev2/Analog Input/AI1"
DOUBLE_VALUE_COEFFICIENTS = [0.0, 2.0]


def main() -> None:
    try:
        factory = Factory()
        workspace = factory.get_iworkspace2(GATEWAY_IP)
        calibration = factory.get_icalibration2(GATEWAY_IP)

        calibration_demo_sdf =  os.path.join(
            os.path.realpath(os.path.dirname(__file__)), "calibration assets", "Calibration Demo.nivssdf"
        )
        calibration_file =  os.path.join(
            os.path.realpath(os.path.dirname(__file__)), "calibration assets", "Calibration Demo.nivscf"
        )

        deploy_options = DeployOptions()
        deploy_options.deploy_system_definition = True
        deploy_options.calibration_file_path = str(calibration_file)
        deploy_options.timeout = DEPLOY_TIMEOUT_MS
        workspace.connect_to_system(str(calibration_demo_sdf), deploy_options)

        calibration_applied = False
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
    except VeriStandException as error:
        print(error.resolved_error_message)
    except Exception as exc:
        print(exc)
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
