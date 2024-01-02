#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 8883

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        message = b'5,256'
        sock.sendall(message)
        while True:
            reply = sock.recv(80).rstrip()
            if len(reply) == 0:
                break
            for row in reply.decode('utf8').split('\r\n'):
                print(row)

if __name__ == '__main__':
    main()