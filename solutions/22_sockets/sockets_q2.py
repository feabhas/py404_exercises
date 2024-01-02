#!/usr/bin/env python3

import socket

PORT = 8882
HOST = '127.0.0.1'

LIMIT = b'\x80'

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.sendto(LIMIT, (HOST, PORT))
        data, address = client.recvfrom(80)
        print('Sent {},  reply: {}'.format(LIMIT[0], data[0]))

if __name__ == '__main__':
    main()
