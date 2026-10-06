"""Deploy Sinewave Delay and read a model signal value."""

import os

from niveristand.clientapi import Factory

GATEWAY_IP = "localhost"
TARGET = "Controller"
MODEL_NAME = "sinewave"
DEPLOY_TIMEOUT_MS = 120_000
# Index 0 is the only output port (Out1) of the sinewave model.
SIGNAL_INDEXES = [0]


def main() -> None:
    factory = Factory()
    workspace = factory.get_iworkspace2(GATEWAY_IP)

    # NI VeriStand must be open so that the Gateway is available.
    sinewave_delay_sdf = os.path.join(
        os.path.realpath(os.path.join(os.path.dirname(__file__), "..")),
        "clientapi_example_assets",
        "Sinewave Delay.nivssdf",
    )
    # Deploy Sinewave Delay through the running VeriStand Gateway.
    workspace.connect_to_system(sinewave_delay_sdf, True, DEPLOY_TIMEOUT_MS)
    try:
        model_manager = factory.get_imodel_manager2(GATEWAY_IP)
        values = model_manager.get_signal_values(TARGET, MODEL_NAME, SIGNAL_INDEXES)
        for index, value in zip(SIGNAL_INDEXES, values):
            print(f"Signal {index}: {value}")
    finally:
        # Undeploy Sinewave Delay.
        workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
