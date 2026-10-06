"""Deploy Engine Demo and log channels to TDMS and text files."""

import os
import time

from niveristand.clientapi import Factory
from niveristand.clientapi.logging import (
    DataLoggingSpecification,
    Delimiter,
    FileConflictOperation,
    TdmsLogFile,
    TextLogFile,
)

GATEWAY_IP = "localhost"
DEPLOY_TIMEOUT_MS = 120_000
LOG_RATE_HZ = 10.0
LOG_DURATION_SECONDS = 10
TDMS_SESSION_NAME = "Engine Demo TDMS Logging"
TEXT_SESSION_NAME = "Engine Demo Text Logging"
CHANNELS = {
    "System Time": "Targets/Controller/System Channels/System Time",
    "Engine Temperature": "Aliases/EngineTemp",
    "Desired RPM": "Aliases/DesiredRPM",
    "Actual RPM": "Aliases/ActualRPM",
}


def main() -> None:
    factory = Factory()
    workspace = factory.get_iworkspace2(GATEWAY_IP)

    # NI VeriStand must be open so that the Gateway is available.
    engine_demo_sdf = os.path.join(
        os.path.realpath(os.path.join(os.path.dirname(__file__), "..")),
        "execution_api_assets",
        "Engine Demo.nivssdf",
    )
    # Deploy Engine Demo through the running VeriStand Gateway.
    workspace.connect_to_system(engine_demo_sdf, True, DEPLOY_TIMEOUT_MS)

    # Create TDMS and tab-delimited text logs beside this example.
    log_directory = os.path.realpath(os.path.dirname(__file__))
    tdms_path = os.path.join(log_directory, "engine_demo_tdms_log.tdms")
    text_path = os.path.join(log_directory, "engine_demo_text_log.txt")

    tdms_file = TdmsLogFile(tdms_path, FileConflictOperation.OVERWRITE_EXISTING)
    channel_group = tdms_file.add_channel_group("Engine Demo")
    text_file = TextLogFile(
        text_path,
        FileConflictOperation.OVERWRITE_EXISTING,
        Delimiter.TAB,
        6,
    )
    for channel_name, channel_path in CHANNELS.items():
        channel_group.add_channel(channel_name, channel_path)
        text_file.add_channel(channel_name, channel_path, True)

    tdms_specification = DataLoggingSpecification(tdms_file)
    tdms_specification.log_data_at_target_rate = False
    tdms_specification.custom_rate = LOG_RATE_HZ
    text_specification = DataLoggingSpecification(text_file)
    text_specification.log_data_at_target_rate = False
    text_specification.custom_rate = LOG_RATE_HZ

    data_logging = factory.get_idata_logging(GATEWAY_IP)
    started_sessions = []
    try:
        data_logging.start_data_logging_session(TDMS_SESSION_NAME, tdms_specification)
        started_sessions.append(TDMS_SESSION_NAME)
        data_logging.start_data_logging_session(TEXT_SESSION_NAME, text_specification)
        started_sessions.append(TEXT_SESSION_NAME)
        # Capture the selected Engine Demo channels for the requested duration.
        time.sleep(LOG_DURATION_SECONDS)
    finally:
        for session_name in reversed(started_sessions):
            data_logging.stop_data_logging_session(session_name, True)

        # Undeploy Engine Demo after both logging sessions are stopped.
        workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
