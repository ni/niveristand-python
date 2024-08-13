"""Create an empty system definition."""
from __future__ import annotations

import os
import sys

sys.path.append(r"C:\Program Files\National Instruments\VeriStand 2024")
from niveristand import VeriStandSdfError  # noqa: E402
from niveristand.systemdefinitionapi import (  # noqa: E402
    AcquisitionMode,
    AlarmMode,
    AlarmPriority,
    AlarmState,
    Alias,
    AliasFolder,
    CANPort,
    DAQAnalogInput,
    DAQAnalogOutput,
    DAQCounterEdge,
    DAQDevice,
    DAQDeviceInputConfiguration,
    DAQDigitalInput,
    DAQDigitalOutput,
    DAQDIOPort,
    DAQFrequencyMeasurement,
    DAQInternalChannel,
    DAQMeasurementType,
    DAQPulseGeneration,
    DAQTaskAI,
    DAQTriggerDigitalEdge,
    DAQWaveformAnalogInput,
    Database,
    DataFileReplay,
    DataLoggingFile,
    DirectionType,
    FileType,
    LINPort,
    LowpassFilter,
    Model,
    PolynomialScale,
    Procedure,
    SampleMode,
    SetVariableStepFunction,
    SignalBasedFrame,
    SystemDefinition,
    XNETTermination,
)


def main(filepath=None):
    """The main portion of the script."""
    try:
        print("Creating System Definition...")
        if not filepath:
            filepath = os.path.join(os.path.dirname(__file__), "combined.nivssdf")
        system_definition = create_system_definition(filepath)

        print("Adding and populating DAQ Devices... ")
        add_daq(system_definition)

        print("Adding and populating XNET Devices... ")
        add_can(system_definition)
        add_lin(system_definition)

        print("Adding and populating Simulation Models... ")
        add_models(system_definition)

        print("Adding user channels, alarms, procedures, aliases, etc... ")
        add_remaining(system_definition)

        save_system_definition(system_definition)
    except BaseException as e:
        if isinstance(e, VeriStandSdfError):
            print(f"\nVeriStandSdfError: {str(e)}", end="")
        elif str(type(e)) == "<class 'NationalInstruments.VeriStand.VeriStandException'>":
            # VeriStandSdfError gives better error messages
            print(f"\nVeriStandException: {VeriStandSdfError(e.Code)}", end="")
        # re-raise the exception to print the stack trace to the console
        raise


def get_asset(filename: str) -> str:
    """Returns the path to an asset for this example."""
    return os.path.join(
        os.path.realpath(os.path.dirname(__file__)), "sysdef_example_assets", filename
    )


def create_system_definition(filepath: str, ip_address: str = "localhost") -> SystemDefinition:
    """Creates the system definition."""
    filename = os.path.basename(filepath)
    is_local = ip_address == "localhost" or ip_address == "127.0.0.1"
    target_type = "Windows" if is_local else "Linux_x64"
    system_definition = SystemDefinition(
        filename,
        "This is an example System Definition file created using the System Definition API",
        "System Definition API",
        "1.0.0.0",
        "Controller",
        target_type,
        filepath,
    )

    target = system_definition.root.get_targets().get_target_list()[0]
    if not is_local:
        target.ip_address = ip_address
    return system_definition


def add_daq(system_definition: SystemDefinition):
    """Adds a DAQ device to the system definition."""
    daq_device = DAQDevice(
        "Dev1",
        "This is a DAQ Device created using the System Definition Offline API.",
        DAQDeviceInputConfiguration.DEFAULT,
    )
    target = system_definition.root.get_targets().get_target_list()[0]
    chassis = target.get_hardware().get_chassis_list()[0]
    chassis.get_daq().add_device(daq_device)

    # Analog Input Channels
    analog_inputs = daq_device.create_analog_inputs()
    analog_inputs.add_analog_input(
        DAQAnalogInput("AI0", 1, DAQMeasurementType.ANALOG_INPUT_TEMPERATURE_THERMOCOUPLE)
    )
    analog_inputs.add_analog_input(
        DAQAnalogInput("AI1", 0, DAQMeasurementType.ANALOG_INPUT_VOLTAGE)
    )

    # Analog Output Channels
    analog_outputs = daq_device.create_analog_outputs()
    analog_outputs.add_analog_output(
        DAQAnalogOutput("AO0", 0, DAQMeasurementType.ANALOG_OUTPUT_VOLTAGE)
    )

    # Digital Input Channels
    digital_inputs = daq_device.create_digital_inputs()
    daq_input_port = DAQDIOPort(0, False)
    digital_inputs.add_dio_port(daq_input_port)
    daq_input_port.add_digital_input(DAQDigitalInput("DI0", False, 0, 0))
    daq_input_port.add_digital_input(DAQDigitalInput("DI1", False, 1, 0))

    # Digital Output Channels
    digital_outputs = daq_device.create_digital_outputs()
    daq_output_port = DAQDIOPort(1, False)
    digital_outputs.add_dio_port(daq_output_port)
    daq_output_port.add_digital_output(DAQDigitalOutput("DO4", False, 4, 1))

    # Counter Channels
    counters = daq_device.create_counters()
    counters.add_counter(
        DAQFrequencyMeasurement("FreqIn", "", 0, 0.0, 1.0, 0.0, DAQCounterEdge.FALLING)
    )
    counters.add_counter_output(DAQPulseGeneration("PWMOut", "", 1))

    # Internal Channels
    internal_channels = daq_device.create_internal_channels()
    internal_channels.add_internal_channel(DAQInternalChannel("Channel 0", 0.0))

    # Waveform Tasks
    daq_device_waveform = DAQDevice("Dev2", "", DAQDeviceInputConfiguration.DEFAULT)
    chassis.get_daq().add_device(daq_device_waveform)
    daq_tasks = chassis.get_daq().get_tasks()
    waveform_task = DAQTaskAI("Task1", 1000, AcquisitionMode.CONTINUOUS)
    waveform_task.get_triggers().start_trigger = DAQTriggerDigitalEdge(
        "PFI0", DirectionType.FALLING
    )
    daq_tasks.add_task(waveform_task)
    analog_waveform_input = DAQWaveformAnalogInput(
        "AI2", 0, DAQMeasurementType.ANALOG_INPUT_CURRENT
    )
    waveform_analog_inputs = daq_device_waveform.create_analog_inputs()
    waveform_analog_inputs.sample_mode = SampleMode.WAVEFORM
    waveform_analog_inputs.add_waveform_analog_input(analog_waveform_input)
    waveform_analog_inputs.waveform_analog_input_task = waveform_task

    # Polynomial Scale
    coefficients = [1.0]
    reverse_coefficients = []
    scale = PolynomialScale("MyScale", coefficients, reverse_coefficients, "")
    system_definition.root.get_scales().add_scale(scale)
    daq_device.get_analog_input_section().get_analog_input_list()[0].scale = scale


def add_can(system_definition: SystemDefinition):
    """Adds the CAN section to the system definition."""
    target = system_definition.root.get_targets().get_target_list()[0]
    chassis = target.get_hardware().get_chassis_list()[0]
    chassis.get_xnet().enable_xnet()  # enable XNET if we haven't already

    target.get_user_channels().add_new_user_channel("MyXnetUserChannel", "", "", 1.0)
    user_channel = target.get_user_channels().get_user_channel_list()[0]

    # CAN Database
    can = chassis.get_xnet().get_can()
    can_database = Database("NIXNET_example")
    target.get_xnet_databases().add_database(can_database)

    # CAN Cluster
    can_cluster = "CAN_Cluster"
    can_port = CANPort("CAN 1", 1, can_database, can_cluster, 125000)
    can_port.termination = XNETTermination.ON
    can.add_can_port(can_port)

    # Frame Variables
    cyclic_frame = "CANCyclicFrame1"
    cyclic_frame_signals = ["CANCyclicSignal1", "CANCyclicSignal2"]
    event_frame = "CANEventFrame1"
    event_frame_signals = ["CANEventSignal1", "CANEventSignal2"]

    # CAN Incoming Frames
    incoming_cyclic_frame = SignalBasedFrame(
        cyclic_frame, 64, can_database, can_cluster, 8, 0.1, False, cyclic_frame_signals
    )
    can_port.get_incoming().get_single_point().add_signal_based_frame(incoming_cyclic_frame)
    for signal in cyclic_frame_signals:
        incoming_cyclic_frame.create_signal_based_signal(signal, "", "volts", 0.0)

    incoming_event_frame = SignalBasedFrame(
        event_frame, 66, can_database, can_cluster, 8, 0.1, False, event_frame_signals
    )
    can_port.get_incoming().get_single_point().add_signal_based_frame(incoming_event_frame)
    for signal in event_frame_signals:
        incoming_event_frame.create_signal_based_signal(signal, "", "volts", 0.0)

    incoming_cyclic_frame.create_frame_information()

    incoming_data_logging = DataLoggingFile(
        "log", "file", os.path.dirname(system_definition.document_type.document_file_path)
    )
    incoming_data_logging.data_logging_file_type = FileType.TDMS
    can_port.get_incoming().get_raw_frame_data_logging().add_data_logging_file(
        incoming_data_logging
    )
    can_port.get_incoming().get_raw_frame_data_logging().get_data_logging_file_list()[
        0
    ].trigger_channel = user_channel

    # CAN Outgoing Frames
    outgoing_cyclic_frame = SignalBasedFrame(
        cyclic_frame, 64, can_database, can_cluster, 8, 0.1, False, cyclic_frame_signals
    )
    can_port.get_outgoing().get_cyclic().add_signal_based_frame(outgoing_cyclic_frame)
    for signal in cyclic_frame_signals:
        outgoing_cyclic_frame.create_signal_based_signal(signal, "", "volts", 0.0)

    outgoing_event_frame = SignalBasedFrame(
        event_frame, 64, can_database, can_cluster, 8, 0.1, False, event_frame_signals
    )
    can_port.get_outgoing().get_event_triggered().add_signal_based_frame(outgoing_event_frame)
    for signal in event_frame_signals:
        outgoing_event_frame.create_signal_based_signal(signal, "", "volts", 0.0)

    outgoing_cyclic_frame.create_frame_faulting(True, True)
    outgoing_cyclic_frame.get_frame_faulting().get_skip_cyclic_frames().trigger_channel = (
        user_channel
    )
    outgoing_cyclic_frame.get_frame_faulting().get_transmit_time().set_trigger_channel(user_channel)

    outgoing_data_replay = DataFileReplay("replay", get_asset("fake.tdms"))
    can_port.get_outgoing().get_data_replay().add_data_file_replay(outgoing_data_replay)
    can_port.get_outgoing().get_data_replay().get_data_file_replay_list()[
        0
    ].trigger_channel = user_channel


def add_lin(system_definition: SystemDefinition):
    """Adds a LIN section to the system definition."""
    target = system_definition.root.get_targets().get_target_list()[0]
    chassis = target.get_hardware().get_chassis_list()[0]
    chassis.get_xnet().enable_xnet()  # enable XNET if we haven't already

    # LIN Database
    lin = chassis.get_xnet().get_lin()
    lin_database = Database("NIXNET_exampleLDF")
    target.get_xnet_databases().add_database(lin_database)

    # LIN Cluster
    lin_cluster = "Cluster"
    lin_port = LINPort("LIN 1", 1, lin_database, lin_cluster, 125000, "SlowSchedule")
    lin.add_lin_port(lin_port)

    # LIN Incoming Frame
    incoming_signals = ["SlaveSignal3_U8", "SlaveSignal4_U8"]
    incoming_frame = SignalBasedFrame(
        "Slave1Frame2", 5, lin_database, lin_cluster, 8, 0.1, False, incoming_signals
    )
    lin_port.get_incoming().get_single_point().add_signal_based_frame(incoming_frame)
    for signal in incoming_signals:
        incoming_frame.create_signal_based_signal(signal, "", "volts", 0.0)

    # LIN Outgoing Frame
    outgoing_signals = ["MasterSignal3_U8", "MasterSignal4_U8"]
    outgoing_frame = SignalBasedFrame(
        "MasterFrame2", 3, lin_database, lin_cluster, 8, 0.1, False, outgoing_signals
    )
    lin_port.get_outgoing().get_unconditional().add_signal_based_frame(outgoing_frame)
    for signal in outgoing_signals:
        outgoing_frame.create_signal_based_signal(signal, "", "volts", 0.0)


def add_models(system_definition: SystemDefinition):
    """Adds models to the system definition."""
    target = system_definition.root.get_targets().get_target_list()[0]
    simulation_models = target.get_simulation_models()

    random_model = Model("RandomFMU", "", get_asset("RandomFMU.fmu"), 0, 1, 0, True, True, True)
    simulation_models.get_models().add_model(random_model)

    sinewave_model = Model(
        "SinewaveFMU", "", get_asset("SinewaveFMU.fmu"), 0, 1, 0, True, True, True
    )
    simulation_models.get_models().add_model(sinewave_model)


def add_remaining(system_definition: SystemDefinition):
    """Add other items to the system definition."""
    target = system_definition.root.get_targets().get_target_list()[0]
    chassis = target.get_hardware().get_chassis_list()[0]

    # User Channel
    target.get_user_channels().add_new_user_channel("MyUserChannel", "", "", 1.0)
    user_channel = target.get_user_channels().get_user_channel_list()[1]

    # Procedure
    procedure = Procedure("MyProcedure", "")
    procedure.add_new_dwell("Dwell Step", "Dwell for 3 seconds.", 3)
    procedure.add_new_set_variable(
        "Counting Step", "", user_channel, SetVariableStepFunction.ADD, user_channel, 1
    )
    target.get_procedures().add_procedure(procedure)

    # Calculated Channel
    lpf_calculated_channel = LowpassFilter("MyLowpassFilterChannel", "", user_channel, 50, 1)
    target.get_calculated_channels().add_calculated_channel(lpf_calculated_channel)

    # Alarm
    target.get_alarms().add_new_alarm(
        "MyAlarm",
        "",
        user_channel,
        2,
        1,
        procedure,
        AlarmMode.NORMAL,
        AlarmState.ENABLED,
        AlarmPriority.LOW,
        0,
        "",
    )

    # Alias
    alias = Alias("MyUserChannelAlias", "", user_channel)
    alias_folder = AliasFolder("MyAliasFolder", "")
    system_definition.root.get_aliases().add_alias_folder(alias_folder)
    system_definition.root.get_aliases().get_alias_folder_list()[0].add_alias(alias)

    # FPGA
    chassis.get_fpga().add_fpga_device(
        get_asset("PXIe-7867R Analog, PWM, Digital Lines.fpgaconfig")
    )


def save_system_definition(system_definition: SystemDefinition):
    """Saves the system definition."""
    filepath = system_definition.document_type.document_file_path
    saved, error = system_definition.save_system_definition_file()
    if saved:
        print(f'System Definition saved to "{filepath}"')
    else:
        raise FileNotFoundError(f'Unable to save System Definition to "{filepath}": {error}')


if __name__ == "__main__":
    main()
