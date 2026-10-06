"""Deploy Engine Demo and receive streamed channel data over UDP."""

import os
import socket
import struct

from niveristand import VeriStandException
from niveristand.clientapi import ByteOrder, Factory

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


def deserialize(packet: bytes, byte_order: ByteOrder) -> tuple:
    """Return (packet_id, t0, dt, channel_ids, data, sample_offset) for one UDP datagram."""
    if byte_order == ByteOrder.LITTLE_ENDIAN:
        prefix = "<"
    elif byte_order == ByteOrder.BIG_ENDIAN:
        prefix = ">"
    elif byte_order == ByteOrder.NATIVE_HOST_ORDER:
        prefix = "="
    else:
        raise ValueError(f"Unsupported byte order {byte_order}.")
    offset = 0

    def read(fmt: str) -> tuple:
        nonlocal offset
        values = struct.unpack_from(prefix + fmt, packet, offset)
        offset += struct.calcsize(prefix + fmt)
        return values

    try:
        packet_id, t0, dt, channel_count = read("iddi")
        channel_ids = list(read(f"{channel_count}i"))
        rows, columns = read("ii")
        values = read(f"{rows * columns}d")
        (sample_offset,) = read("Q")
    except struct.error as error:
        raise ValueError(f"Invalid UDP data packet: {error}") from None
    data = [list(values[row * columns : (row + 1) * columns]) for row in range(rows)]
    return packet_id, t0, dt, channel_ids, data, sample_offset


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
                packet_id, t0, dt, packet_channel_ids, data, sample_offset = (
                    deserialize(packet, ByteOrder.NATIVE_HOST_ORDER)
                )
                print(
                    f"\nPacket {packet_number} | ID={packet_id} | "
                    f"t0={t0:g} | dt={dt:g} | "
                    f"offset={sample_offset} | {len(packet)} bytes | "
                    f"from {sender[0]}:{sender[1]}"
                )
                for channel_id, samples in zip(packet_channel_ids, data):
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
    except VeriStandException as error:
        print(error)
        print(error.resolved_error_message)
    finally:
        # Undeploy Engine Demo after the UDP stream session is stopped.
        workspace.disconnect_from_system("", True)


if __name__ == "__main__":
    main()
