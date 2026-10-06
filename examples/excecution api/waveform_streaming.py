"""Start and register for waveform data published by the VeriStand Gateway.

This example prompts for a System Definition file that contains waveforms and a
waveform path from that System Definition. It deploys the System Definition and
prints the streamed waveform data.

NOTE: This example expects the NI VeriStand gateway to be localhost.
"""

import os
import time

from niveristand.clientapi import DeployOptions, Factory
from niveristand.clientapi.waveformstreaming import (
    StreamAllData,
    WaveformDataDBLEventArgs,
    WaveformStreamSpecification,
)

GATEWAY_IP = "localhost"
DEPLOY_TIMEOUT_MS = 120_000
STREAM_DURATION_SECONDS = 30


def main() -> None:
    sdf_path = os.path.abspath(
        os.path.expandvars(
            os.path.expanduser(input("System definition path: ").strip())
        )
    )
    if not os.path.isfile(sdf_path):
        raise FileNotFoundError(f'System definition file not found: "{sdf_path}"')

    waveform_path = input("Waveform path: ").strip()
    if not waveform_path:
        raise ValueError("A waveform path is required.")

    factory = Factory()
    workspace = factory.get_iworkspace2(GATEWAY_IP)
    # Deploy the selected system definition through the VeriStand Gateway.
    deploy_options = DeployOptions()
    deploy_options.deploy_system_definition = True
    deploy_options.timeout = DEPLOY_TIMEOUT_MS
    workspace.connect_to_system(sdf_path, deploy_options)

    try:
        # Register for DBL waveform data and stream at the acquisition rate.
        waveform_streaming = factory.get_iwaveform_streaming(GATEWAY_IP)
        specification = WaveformStreamSpecification(waveform_path)
        specification.stream_data_at_acquisition_rate = True
        specification.stream_condition = StreamAllData()
        specifications = [specification]

        def on_waveform_data(
            sender: object, event_args: WaveformDataDBLEventArgs
        ) -> None:
            samples = event_args.data
            print(
                f"Received {len(samples)} samples: "
                f"offset={event_args.offset_from_start_in_samples}, "
                f"dt={event_args.dt}, data={samples}"
            )

        registered = False
        streaming = False
        try:
            waveform_streaming.register_for_dbl_waveform_data(
                specifications, on_waveform_data
            )
            registered = True
            waveform_streaming.start_streaming_waveforms(specifications)
            streaming = True
            time.sleep(STREAM_DURATION_SECONDS)
        finally:
            if streaming:
                waveform_streaming.stop_streaming_waveforms(specifications)
            if registered:
                waveform_streaming.unregister_for_dbl_waveform_data(
                    specifications, on_waveform_data
                )
    finally:
        workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
