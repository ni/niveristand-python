"""Deploy Engine Demo and demonstrate single and multiple channel faults."""

import os
import time

from niveristand.clientapi import Factory

GATEWAY_IP = "localhost"
DEPLOY_TIMEOUT_MS = 120_000
FAULT_SETTLE_TIME_SECONDS = 1
ENGINE_RPM_INPUT = (
    "Targets/Controller/Simulation Models/Models/Engine Demo/Inports/command_RPM"
)
ENGINE_ON_INPUT = (
    "Targets/Controller/Simulation Models/Models/Engine Demo/Inports/command_EngineOn"
)
ENGINE_RPM_FAULT = 2_500.0
MULTIPLE_FAULT_CHANNELS = [ENGINE_RPM_INPUT, ENGINE_ON_INPUT]
MULTIPLE_FAULT_VALUES = [3_000.0, 1.0]


def main() -> None:
    factory = Factory()
    workspace = factory.get_iworkspace2(GATEWAY_IP)

    engine_demo_sdf = os.path.join(
        os.path.realpath(os.path.join(os.path.dirname(__file__), "..")),
        "clientapi_example_assets",
        "Engine Demo.nivssdf",
    )
    # NI VeriStand must be open so that the Gateway is available.
    workspace.connect_to_system(engine_demo_sdf, True, DEPLOY_TIMEOUT_MS)

    channel_fault = factory.get_ichannel_fault(GATEWAY_IP)
    try:
        # Set one fault and verify both its status and the resulting channel value.
        channel_fault.set_fault_value(ENGINE_RPM_INPUT, ENGINE_RPM_FAULT)
        time.sleep(FAULT_SETTLE_TIME_SECONDS)
        faulted, fault_value = channel_fault.get_fault_value(ENGINE_RPM_INPUT)
        rpm_input_value = workspace.get_single_channel_value(ENGINE_RPM_INPUT)
        print(f"RPM input faulted: {faulted}, fault value: {fault_value}")
        print(f"RPM input channel value while faulted: {rpm_input_value}")
        print(f"Current fault list: {channel_fault.get_fault_list()}")

        # Clear the individual fault and verify it is no longer active.
        channel_fault.clear_fault(ENGINE_RPM_INPUT)
        time.sleep(FAULT_SETTLE_TIME_SECONDS)
        faulted, fault_value = channel_fault.get_fault_value(ENGINE_RPM_INPUT)
        print(f"RPM input faulted after clear: {faulted}, value: {fault_value}")

        # Demonstrate setting and clearing faults for multiple model inputs.
        channel_fault.set_multiple_faults(
            MULTIPLE_FAULT_CHANNELS, MULTIPLE_FAULT_VALUES
        )
        time.sleep(FAULT_SETTLE_TIME_SECONDS)
        print(f"Multiple faults: {channel_fault.get_fault_list()}")
        channel_fault.clear_multiple_faults(MULTIPLE_FAULT_CHANNELS)
        time.sleep(FAULT_SETTLE_TIME_SECONDS)
        print(f"Fault list after clearing: {channel_fault.get_fault_list()}")
    finally:
        workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
