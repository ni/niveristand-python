"""Demonstrate common NI VeriStand Client API workflows.

Ensure the VeriStand Gateway is running before running this example.
On Linux, change the relative model path in "clientapi_example.nivssdf" from
"Model\EngineDemo_windows.vsmodel" to "Model\EngineDemo_linux.vsmodel".
"""

from __future__ import annotations

import os
import tempfile
import threading
import time

from niveristand import nivs_rt_sequence
from niveristand.realtimesequenceapi import realtimesequencetools
from niveristand.clientapi import Factory, SequenceCallInfo
from niveristand.clientapi.logging import (
    DataLoggingSpecification,
    FileConflictOperation,
    TdmsLogFile,
)
from niveristand.realtimesequenceapi.library import wait

GATEWAY = "localhost"
TARGET = "Controller"
USER_CHANNEL = "Targets/Controller/User Channels/User Channel"
ALARM_CHANNEL = "Targets/Controller/System Channels/Command Index"
EVENT_TIMEOUT_SECONDS = 10


def main():
    """The main portion of the script."""
    factory = Factory()
    workspace = factory.get_iworkspace2(GATEWAY)

    print("Deploying the system definition...")
    workspace.connect_to_system(get_asset("clientapi_example.nivssdf"), True, 120_000)

    try:
        print("Reading and writing channels...")
        use_channels(workspace)

        print("Monitoring channel value changes...")
        monitor_channel(factory, workspace)

        print("Reading alarms and monitoring alarm events...")
        monitor_alarms(factory, workspace)

        print("Reading models and monitoring parameter changes...")
        monitor_models(factory)

        print("Logging channel data...")
        log_data(factory)

        print("Running a stimulus profile session...")
        run_stimulus_profile(factory)
    finally:
        print("Undeploying the system definition...")
        workspace.disconnect_from_system("", True)


def get_asset(filename: str) -> str:
    """Return the path to an asset for this example."""
    return os.path.join(
        os.path.realpath(os.path.dirname(__file__)),
        "clientapi_example_assets",
        filename,
    )


def use_channels(workspace):
    """Read and write scalar channel values."""
    original_value = workspace.get_single_channel_value(USER_CHANNEL)
    print(f"Original value of user channel = {original_value}")

    workspace.set_single_channel_value(USER_CHANNEL, original_value + 1)
    time.sleep(2)
    updated_value = workspace.get_single_channel_value(USER_CHANNEL)
    print(f'Incremented value of "{USER_CHANNEL}": {updated_value}')

    workspace.set_single_channel_value(USER_CHANNEL, original_value)
    time.sleep(2)


def monitor_channel(factory, workspace):
    """Register for channel value change events."""
    channel_monitor = factory.get_channel_monitor(GATEWAY)

    def on_value_changed(sender, event_args):
        print(f"Channel value changed to {event_args.new_value.value[0]}")

    channel_monitor.register_channel_value_monitor(USER_CHANNEL, on_value_changed)
    try:
        value = workspace.get_single_channel_value(USER_CHANNEL)
        workspace.set_single_channel_value(USER_CHANNEL, value + 1)
        time.sleep(EVENT_TIMEOUT_SECONDS)
        workspace.set_single_channel_value(USER_CHANNEL, value)
        time.sleep(2)
    finally:
        channel_monitor.unregister_channel_value_monitor(USER_CHANNEL, on_value_changed)


def monitor_alarms(factory, workspace):
    """Read alarm data and register for alarm trigger events."""
    alarm_manager = factory.get_ialarm_manager2(GATEWAY)
    alarm_names = alarm_manager.get_alarm_list(TARGET)
    alarm_info = alarm_manager.get_multiple_alarms_data(TARGET, alarm_names, 5_000)
    for name, info in zip(alarm_names, alarm_info):
        print(f'Alarm "{name}": state={info.state}, priority={info.priority}')

    alarm_triggered = threading.Event()

    def on_alarm_triggered(target, event_args):
        print(
            f'Alarm "{event_args.alarm_name}" triggered on "{target}" '
            f"at value {event_args.value}"
        )
        alarm_triggered.set()

    alarm_manager.subscribe_on_alarm_trigger2_event(on_alarm_triggered)
    try:
        workspace.set_single_channel_value(ALARM_CHANNEL, 1)
        time.sleep(1)
        workspace.set_single_channel_value(ALARM_CHANNEL, -2)
        alarm_triggered.wait(EVENT_TIMEOUT_SECONDS)
    finally:
        alarm_manager.unsubscribe_on_alarm_trigger2_event(on_alarm_triggered)
        workspace.set_single_channel_value(ALARM_CHANNEL, 1)


def monitor_models(factory):
    """Read model state and register for model parameter change events."""
    model_manager = factory.get_imodel_manager2(GATEWAY)
    model_name = model_manager.get_model_list(TARGET)[0]
    model = factory.get_imodel(GATEWAY, TARGET, model_name)
    model_time, model_state = model.get_model_execution_state()
    print(f'Model "{model_name}": state={model_state}, time={model_time}')

    parameters = model_manager.get_parameters_list(TARGET)
    parameter_names, row_dimensions, column_dimensions = parameters
    parameter_dimensions = zip(parameter_names, row_dimensions, column_dimensions)
    parameter_name = None
    for name, rows, columns in parameter_dimensions:
        if rows == 1 and columns == 1:
            parameter_name = name
            break
    if parameter_name is None:
        raise RuntimeError("No scalar model parameter was found.")
    parameter_changed = threading.Event()

    def on_parameter_changed(sender, event_args):
        new_value = event_args.new_value.value[0]
        print(f'Parameter "{event_args.parameter_name}" changed to {new_value}')
        parameter_changed.set()

    original_value = model_manager.get_single_parameter_value(TARGET, parameter_name)
    changed_value = original_value + 1
    model_manager.register_for_parameter_value_change(
        TARGET, parameter_name, on_parameter_changed
    )
    try:
        model_manager.set_single_parameter_value(TARGET, parameter_name, changed_value)
        parameter_changed.wait(EVENT_TIMEOUT_SECONDS)
        model_manager.set_single_parameter_value(TARGET, parameter_name, original_value)
    finally:
        model_manager.unregister_for_parameter_value_change(
            TARGET, parameter_name, on_parameter_changed
        )


def log_data(factory):
    """Log a channel to a TDMS file."""
    log_path = os.path.join(tempfile.gettempdir(), "clientapi_example.tdms")
    log_file = TdmsLogFile(log_path, FileConflictOperation.OVERWRITE_EXISTING)
    channel_group = log_file.add_channel_group("Client API Example")
    channel_group.add_channel("User Channel", USER_CHANNEL)

    data_logging = factory.get_idata_logging(GATEWAY)
    data_logging.start_data_logging_session(
        "Client API Example", DataLoggingSpecification(log_file)
    )
    time.sleep(2)
    log_files = data_logging.stop_data_logging_session("Client API Example", True)
    print(f"Log files: {list(log_files)}")


@nivs_rt_sequence
def client_api_sequence():
    """Wait for one second on the VeriStand engine."""
    wait(1)


def run_stimulus_profile(factory):
    """Create, deploy, and run a stimulus profile session."""
    sequence_directory = tempfile.mkdtemp(prefix="niveristand_clientapi_")
    sequence_path = realtimesequencetools.save_py_as_rtseq(
        client_api_sequence, sequence_directory
    )
    sequence = SequenceCallInfo(sequence_path, TARGET, [], False, 1_000.0)
    session = factory.get_istimulus_profile_session(
        GATEWAY, "Client API Example", [sequence], "Client API example session"
    )
    session.deploy(False)
    try:
        sequence_control = session[session.sequence_names[0]]
        sequence_complete = threading.Event()

        def on_sequence_complete(sender, event_args):
            print(f"Sequence completed with error code {event_args.error.code}")
            sequence_complete.set()

        sequence_control.subscribe_sequence_complete_event(on_sequence_complete)
        try:
            sequence_control.run()
            sequence_complete.wait(EVENT_TIMEOUT_SECONDS)
        finally:
            sequence_control.unsubscribe_sequence_complete_event(on_sequence_complete)
    finally:
        session.undeploy()


if __name__ == "__main__":
    main()
