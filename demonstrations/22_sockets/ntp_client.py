#!/usr/bin/env python3

import socket
import struct
from datetime import datetime

TIMEOUT = 3
NTP_PORT = 123
NTP_OFFSET = 2208988800
NTP_REQ = b'\x1b' + 47 * b'\0'

def get_time(server):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.settimeout(TIMEOUT)
        client.sendto(NTP_REQ, (server, NTP_PORT))
        data, address = client.recvfrom(48)
        if not data:
            raise UserWarning('No data from: {}'.format(server))
        ntp_time, = struct.unpack('>I',data[40:44])
        return datetime.fromtimestamp(ntp_time-NTP_OFFSET)

def main():
    ntp = get_time('0.pool.ntp.org')
    print('NTP time: {:%d-%b-%Y %H:%M:%S}'.format(ntp))

if __name__ == '__main__':
    main()
