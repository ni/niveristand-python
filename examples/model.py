"""Deploy Engine Demo and demonstrate reading and monitoring models."""

import os
import threading
from typing import Any

from niveristand import VeriStandException
from niveristand.clientapi import Factory, ParameterValueChangeEventArgs

GATEWAY_IP = "localhost"
TARGET = "Controller"
DEPLOY_TIMEOUT_MS = 120_000
EVENT_TIMEOUT_SECONDS = 10
MODEL_PARAMETER = "Environment_Temperature"


def main() -> None:
    factory = Factory()
    workspace = factory.get_iworkspace2(GATEWAY_IP)

    # NI VeriStand must be open so that the Gateway is available.
    engine_demo_sdf = os.path.join(
        os.path.expanduser("~public"),
        "Documents",
        "National Instruments",
        "NI VeriStand 2026",
        "Examples",
        "Stimulus Profile",
        "Engine Demo",
        "Engine Demo.nivssdf",
    )
    # Deploy Engine Demo through the running VeriStand Gateway.
    workspace.connect_to_system(engine_demo_sdf, True, DEPLOY_TIMEOUT_MS)
    # Read the first model's current execution state.
    model_manager = factory.get_imodel_manager2(GATEWAY_IP)
    model_name = model_manager.get_model_list(TARGET)[0]
    model = factory.get_imodel(GATEWAY_IP, TARGET, model_name)

    model_time, model_state = model.get_model_execution_state()
    print(f'Model "{model_name}": state = {model_state}, time = {model_time}')

    # Monitor an Engine Demo scalar model parameter and print its new value from the callback.
    parameter_changed = threading.Event()

    def on_parameter_value_changed(
        sender: Any, event_args: ParameterValueChangeEventArgs
    ):
        new_value = event_args.new_value.value[0]
        print(
            f'Parameter "{event_args.parameter_name}" changed to {new_value} via callback'
        )
        parameter_changed.set()

    original_value = model_manager.get_single_parameter_value(TARGET, MODEL_PARAMETER)
    changed_value = original_value + 1

    model_manager.register_for_parameter_value_change(
        TARGET, MODEL_PARAMETER, on_parameter_value_changed
    )
    try:
        model_manager.set_single_parameter_value(TARGET, MODEL_PARAMETER, changed_value)
        if not parameter_changed.wait(EVENT_TIMEOUT_SECONDS):
            raise TimeoutError(
                "Timed out waiting for the parameter value change event."
            )
    except VeriStandException as error:
        print(error)
        print(error.resolved_error_message)
    finally:
        model_manager.unregister_for_parameter_value_change(
            TARGET, MODEL_PARAMETER, on_parameter_value_changed
        )

        # Undeploy Engine Demo
        workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
