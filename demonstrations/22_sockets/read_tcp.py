#!/usr/bin/env python3

import socket
import sys

HOST = 'www.feabhas.com'
PORT = 80
REQUEST = b'GET / HTTP/1.1\r\nHost: feabhas.com\r\n\r\n'

def main():
    try:
        addr = socket.gethostbyname('www.feabhas.com')
        print('Feabhas is {}'.format(addr))
        name, aliases, ips = socket.gethostbyaddr(addr)
        print(name, aliases, ips)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            svr_name, svr_port = sock.getpeername()
            client_name, client_port = sock.getsockname()
            print('Connected local port {} to remote port {}'.format(client_port, svr_port))
            sock.sendall(REQUEST)
            reply = sock.recv(4096)
            for line in reply.split(b'\r\n'):
                print(line.decode('UTF-8'))
    except socket.error as ex:
        raise UserWarning ('Cannot connect to {}: {}'.format(HOST, ex))

if __name__ == '__main__':
    main()