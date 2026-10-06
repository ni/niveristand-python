"""Deploy Engine Demo and receive streamed channel data over UDP."""

import os
import socket

from niveristand.clientapi import ByteOrder, Factory, UDPDataPacket

GATEWAY_IP = "localhost"
DEPLOY_TIMEOUT_MS = 120_000
CLIENT_PORT = 51_000
STREAM_RATE_HZ = 100.0
RECEIVE_TIMEOUT_SECONDS = 10
PACKET_COUNT = 10
CHANNELS = [
    "Targets/Controller/System Channels/HP Loop Duration",
    "Targets/Controller/System Channels/LP Loop Duration",
]


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

    try:
        # Configure a unicast UDP stream for the selected Engine Demo channels.
        stream_session = workspace.get_iudp_channel_stream_session(CHANNELS)
        stream_session.multicast = False
        stream_session.max_rate = STREAM_RATE_HZ
        stream_session.client_port = CLIENT_PORT
        stream_session.byte_order = ByteOrder.LITTLE_ENDIAN

        receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        receiver.bind(("", CLIENT_PORT))
        receiver.settimeout(RECEIVE_TIMEOUT_SECONDS)
        stream_deployed = False
        try:
            address, port, max_packet_size, channel_ids, packet_ids = (
                stream_session.deploy_udp_channel_stream_session()
            )
            stream_deployed = True

            # Print the stream metadata and received samples for inspection.
            print(f"Receiving UDP channel data at {address}:{port}")
            for channel, channel_id, packet_id in zip(
                CHANNELS, channel_ids, packet_ids
            ):
                print(
                    f'Channel "{channel}": channel ID={channel_id}, '
                    f"packet ID={packet_id}"
                )
            channel_names_by_id = dict(zip(channel_ids, CHANNELS))

            for packet_number in range(1, PACKET_COUNT + 1):
                packet, sender = receiver.recvfrom(max_packet_size)
                data_packet = UDPDataPacket.deserialize(
                    packet, ByteOrder.LITTLE_ENDIAN
                )
                print(
                    f"\nPacket {packet_number} | ID={data_packet.packet_id} | "
                    f"t0={data_packet.t0:g} | dt={data_packet.dt:g} | "
                    f"offset={data_packet.sample_offset} | {len(packet)} bytes | "
                    f"from {sender[0]}:{sender[1]}"
                )
                for channel_id, samples in zip(
                    data_packet.channel_ids, data_packet.data
                ):
                    label = (
                        "Timestamps"
                        if channel_id == 0
                        else channel_names_by_id.get(
                            channel_id, f"Unknown channel {channel_id}"
                        )
                    )
                    formatted_samples = ", ".join(f"{sample:g}" for sample in samples)
                    print(f"  [{channel_id}] {label}: {formatted_samples}")
        except socket.timeout as error:
            raise TimeoutError("Timed out waiting for UDP channel data.") from error
        finally:
            if stream_deployed:
                stream_session.undeploy_udp_channel_stream_session()
            receiver.close()
    finally:
        # Undeploy Engine Demo after the UDP stream session is stopped.
        workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
