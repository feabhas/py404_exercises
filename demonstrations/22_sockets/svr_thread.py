#!/usr/bin/env python3

import socket
import sys
import threading as thr

PORT = 8888

def do_accept(conn):
    try:
        request = conn.recv(4096)
        conn.sendall(b'from server: ' + request)
    finally:
        conn.close()

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(('', PORT))
            server.listen(10)
            print('listening on port {}'.format(PORT))
            while True:
                conn, addr = server.accept()
                print('request from {}:{}'.format(addr[0], addr[1]))
                thread = thr.Thread(target=do_accept, args=(conn,))
                thread.daemon = True
                thread.start()

    except socket.error as ex:
        print('Error: {}'.format(ex), file=sys.stderr)
        sys.exit(1)

    except (KeyboardInterrupt, SystemExit):
        print('server closing down')


if __name__ == '__main__':
    main()
