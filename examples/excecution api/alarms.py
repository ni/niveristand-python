"""Deploy Engine Demo and trigger the Engine Temperature Alert alarm."""

import os
import threading
import time

from niveristand.clientapi import Factory


GATEWAY_IP = "localhost"
TARGET = "Controller"
DEPLOY_TIMEOUT_MS = 120_000
EVENT_TIMEOUT_SECONDS = 120
PROCEDURE_SETTLE_TIME_SECONDS = 5
ALARM_NAME = "Engine Temperature Alert"
ENGINE_POWER = "Aliases/EnginePower"
DESIRED_RPM = "Aliases/DesiredRPM"
ENVIRONMENT_TEMPERATURE_PARAMETER = "Environment_Temperature"


def main() -> None:
    """Deploy Engine Demo, trigger its temperature alert, and clean up."""
    factory = Factory()
    workspace = factory.get_iworkspace2(GATEWAY_IP)
    alarm_manager = factory.get_ialarm_manager2(GATEWAY_IP)
    model_manager = factory.get_imodel_manager2(GATEWAY_IP)
    alarm_triggered = threading.Event()

    engine_demo_sdf = os.path.join(
        os.path.realpath(os.path.join(os.path.dirname(__file__), "..")),
        "clientapi_example_assets",
        "Engine Demo.nivssdf",
    )

    # NI VeriStand must be open so that the Gateway is available.
    workspace.connect_to_system(engine_demo_sdf, True, DEPLOY_TIMEOUT_MS)

    def on_alarm_triggered(target, event_args):
        """Signal when the Engine Temperature Alert alarm is triggered."""
        if event_args.alarm_name == ALARM_NAME:
            print(
                f'Alarm "{event_args.alarm_name}" triggered on "{target}" '
                f"at value {event_args.value}: {event_args.message}"
            )
            alarm_triggered.set()

    # Register before changing values so the alarm event cannot be missed.
    alarm_manager.subscribe_on_alarm_trigger2_event(on_alarm_triggered)
    try:
        # Run the engine at high RPM in a warm environment to exceed the critical
        # temperature limit continuously for the alarm's configured 30-second delay.
        workspace.set_single_channel_value(ENGINE_POWER, 1)
        workspace.set_single_channel_value(DESIRED_RPM, 10_000)
        model_manager.set_single_parameter_value(
            TARGET, ENVIRONMENT_TEMPERATURE_PARAMETER, 32
        )

        if not alarm_triggered.wait(EVENT_TIMEOUT_SECONDS):
            raise TimeoutError(f'Timed out waiting for alarm "{ALARM_NAME}".')

        # Allow the configured Safe Engine Shut Down procedure to ramp down the RPM
        # and reset engine power before restoring the original values.
        time.sleep(PROCEDURE_SETTLE_TIME_SECONDS)
    finally:
        alarm_manager.unsubscribe_on_alarm_trigger2_event(on_alarm_triggered)
        workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
