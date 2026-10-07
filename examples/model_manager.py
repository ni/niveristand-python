"""Deploy Sinewave Delay, read model signals, and monitor parameter changes."""

import os
import threading
from typing import Any

from niveristand import VeriStandException
from niveristand.clientapi import Factory, ParameterValueChangeEventArgs

VERISTAND_YEAR = 2026
GATEWAY_IP = "localhost"
TARGET = "Controller"
MODEL_NAME = "sinewave"
SIGNAL_INDEXES = [0]
DEPLOY_TIMEOUT_MS = 120_000
EVENT_TIMEOUT_SECONDS = 10
MODEL_PARAMETER = "Amplitude"


def main() -> None:
    try:
        factory = Factory()
        workspace = factory.get_iworkspace2(GATEWAY_IP)

        # NI VeriStand must be open so that the Gateway is available.
        sinewave_delay_sdf = os.path.join(
            os.path.expanduser("~public"),
            "Documents",
            "National Instruments",
            f"NI VeriStand {VERISTAND_YEAR}",
            "Examples",
            "Sinewave Delay",
            "Sinewave Delay.nivssdf",
        )
        # Deploy Sinewave Delay through the running VeriStand Gateway.
        workspace.connect_to_system(sinewave_delay_sdf, True, DEPLOY_TIMEOUT_MS)

        model_manager = factory.get_imodel_manager2(GATEWAY_IP)
        model_names = model_manager.get_model_list(TARGET)
        print(f"Models: {', '.join(model_names)}")
        model = factory.get_imodel(GATEWAY_IP, TARGET, MODEL_NAME)

        model_time, model_state = model.get_model_execution_state()
        print(f'Model "{MODEL_NAME}": state = {model_state}, time = {model_time}')

        values = model_manager.get_signal_values(TARGET, MODEL_NAME, SIGNAL_INDEXES)
        for value in values:
            print(f"Signal: {value}")

        parameter_changed = threading.Event()

        def on_parameter_value_changed(
            sender: Any, event_args: ParameterValueChangeEventArgs
        ) -> None:
            new_value = event_args.new_value.value[0]
            print(
                f'Parameter "{event_args.parameter_name}" changed to {new_value} via callback'
            )
            parameter_changed.set()

        original_value = model_manager.get_single_parameter_value(
            TARGET, MODEL_PARAMETER
        )
        print(f'Parameter "{MODEL_PARAMETER}": current value = {original_value}')

        changed_value = original_value + 1

        model_manager.register_for_parameter_value_change(
            TARGET, MODEL_PARAMETER, on_parameter_value_changed
        )

        model_manager.set_single_parameter_value(TARGET, MODEL_PARAMETER, changed_value)
        if not parameter_changed.wait(EVENT_TIMEOUT_SECONDS):
            raise TimeoutError(
                "Timed out waiting for the parameter value change event."
            )

    except VeriStandException as error:
        print(error.resolved_error_message)
    except Exception as exc:
        print(exc)
    finally:
        model_manager.unregister_for_parameter_value_change(
            TARGET, MODEL_PARAMETER, on_parameter_value_changed
        )
        # Undeploy Sinewave Delay.
        workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
