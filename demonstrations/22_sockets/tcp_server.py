#!/usr/bin/env python3

import select
import socket
import sys

PORT = 8888

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            print('socket created')
            server.bind(('', PORT))
            print('socket bind ok')
            server.listen(10)
            print('listening on port {}'.format(PORT))
            while True:
                try:
                    conn, addr = server.accept()
                    print('request from {}:{}'.format(addr[0], addr[1]))
                    request = conn.recv(4096)
                    print('received: {}'.format(request))
                    conn.sendall(b'from server: '+request)
                finally:
                    conn.close()

    except socket.error as ex:
        print('Error: {}'.format(ex), file=sys.stderr)
        sys.exit(1)

    except (KeyboardInterrupt, SystemExit):
        print('server closing down')

if __name__ == '__main__':
    main()
