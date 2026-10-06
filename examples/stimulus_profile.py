"""Deploy and run an existing RT sequence"""

import os
import time

from niveristand import VeriStandException
from niveristand.clientapi import Factory, SequenceCallInfo, SequenceState
from niveristand.data import BooleanValue

GATEWAY_IP = "localhost"
TARGET = "Controller"
DEPLOY_TIMEOUT_MS = 120_000
EVENT_TIMEOUT_SECONDS = 300
POLL_INTERVAL_SECONDS = 1
SESSION_NAME = "Demo Session"


def main() -> None:
    """Deploy Engine Demo, run the sequence, and clean up."""
    factory = Factory()
    workspace = factory.get_iworkspace2(GATEWAY_IP)

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

    workspace.connect_to_system(engine_demo_sdf, True, DEPLOY_TIMEOUT_MS)

    sequence_path = os.path.join(
        os.path.expanduser("~public"),
        "Documents",
        "National Instruments",
        "NI VeriStand 2026",
        "Examples",
        "Stimulus Profile",
        "Engine Demo",
        "Stimulus Profiles",
        "Engine Demo Return Value",
        "Engine Demo Return Value.nivsseq",
    )
    try:
        sequence = SequenceCallInfo(sequence_path, TARGET, [], False, 1_000.0)
        session = factory.get_istimulus_profile_session(
            GATEWAY_IP,
            SESSION_NAME,
            [sequence],
            "Run the Engine Demo sequence and read its return value",
        )
        session.deploy(False)
        try:
            control = session[session.sequence_names[0]]
            control.run()

            while control.state != SequenceState.STOPPED:
                temperature = workspace.get_single_channel_value("Aliases/EngineTemp")
                print(f"Engine temperature: {temperature:.2f} C")
                time.sleep(POLL_INTERVAL_SECONDS)

            return_value: BooleanValue = control.get_return_value()
            print(f"Engine Temperature < 110: {return_value.value}")
        finally:
            session.undeploy()
    except VeriStandException as error:
        print(error)
        print(error.resolved_error_message)
    finally:
        workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
