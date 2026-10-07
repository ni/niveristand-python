"""Deploy Engine Demo and demonstrate single and multiple channel access."""

import os
import threading
import time

from niveristand import VeriStandException
from niveristand.clientapi import Factory

VERISTAND_YEAR = 2026
GATEWAY_IP = "localhost"
DEPLOY_TIMEOUT_MS = 120_000
WRITE_SETTLE_TIME_SECONDS = 2
EVENT_TIMEOUT_SECONDS = 10
DESIRED_RPM = "Aliases/DesiredRPM"
MULTIPLE_CHANNELS = [DESIRED_RPM, "Aliases/EnginePower"]


def main() -> None:
    try:
        factory = Factory()
        workspace = factory.get_iworkspace2(GATEWAY_IP)

        # NI VeriStand must be open so that the Gateway is available.
        engine_demo_sdf = os.path.join(
            os.path.expanduser("~public"),
            "Documents",
            "National Instruments",
            f"NI VeriStand {VERISTAND_YEAR}",
            "Examples",
            "Stimulus Profile",
            "Engine Demo",
            "Engine Demo.nivssdf",
        )
        # Deploy Engine Demo through the running VeriStand Gateway.
        workspace.connect_to_system(engine_demo_sdf, True, DEPLOY_TIMEOUT_MS)

        # Read, write, and verify the Engine Demo Desired RPM channel.
        original_desired_rpm = workspace.get_single_channel_value(DESIRED_RPM)
        print(f"Original Desired RPM: {original_desired_rpm}")
        workspace.set_single_channel_value(DESIRED_RPM, original_desired_rpm + 1)
        time.sleep(WRITE_SETTLE_TIME_SECONDS)
        updated_desired_rpm = workspace.get_single_channel_value(DESIRED_RPM)
        print(f"Desired RPM after write: {updated_desired_rpm}\n")

        # Read, write, and verify multiple Engine Demo channels at once.
        original_multiple_values = list(
            workspace.get_multiple_channel_values(MULTIPLE_CHANNELS)
        )
        print(
            f"Original values: {dict(zip(MULTIPLE_CHANNELS, original_multiple_values))}"
        )
        workspace.set_multiple_channel_values(MULTIPLE_CHANNELS, [2_000.0, 1.0])
        time.sleep(WRITE_SETTLE_TIME_SECONDS)
        updated_multiple_values = list(
            workspace.get_multiple_channel_values(MULTIPLE_CHANNELS)
        )
        print(
            f"Values after write: {dict(zip(MULTIPLE_CHANNELS, updated_multiple_values))}\n"
        )

        # Monitor Desired RPM and print its updated value from the callback.
        channel_monitor = factory.get_channel_monitor(GATEWAY_IP)
        value_changed = threading.Event()

        def on_value_changed(sender, event_args):
            print(f"Channel value changed to {event_args.new_value.value[0]}\n")
            value_changed.set()

        original_desired_rpm = workspace.get_single_channel_value(DESIRED_RPM)
        channel_monitor.register_channel_value_monitor(DESIRED_RPM, on_value_changed)
        workspace.set_single_channel_value(DESIRED_RPM, original_desired_rpm + 1)
        if not value_changed.wait(EVENT_TIMEOUT_SECONDS):
            raise TimeoutError("Timed out waiting for the channel value change event.")
    except VeriStandException as error:
        print(error.resolved_error_message)
    except Exception as exc:
        print(exc)
    finally:
        channel_monitor.unregister_channel_value_monitor(DESIRED_RPM, on_value_changed)

        # Undeploy Engine Demo
        workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
