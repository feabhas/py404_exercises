#!/usr/bin/env python3

import socket

PORT = 8881
HOST = '127.0.0.1'

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.sendto(b'hello', (HOST, PORT))
        data, address = client.recvfrom(80)
        print('Response: {}'.format(data))

if __name__ == '__main__':
    main()
