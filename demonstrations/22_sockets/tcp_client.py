#!/usr/bin/env python3

import socket
import sys

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(('127.0.0.1', 8888))
            message = b'Hello world\r\n'
            sock.sendall(message)
            reply = sock.recv(4096)
            for line in reply.rstrip().split(b'\r\n'):
                print(line.decode('UTF-8'))

    except socket.error as ex:
        print('Error: {}'.format(ex), file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()