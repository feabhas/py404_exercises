#!/usr/bin/env python3
import socket

HOST = ''
PORT = 8881

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
            udp.bind((HOST, PORT))
            uhost, uport = udp.getsockname()
            print('UDP bind at {}:{}'.format(uhost, uport))
            while True:
                data, address = udp.recvfrom(80)
                print('Received "{}" from {}:{}'.format(data, address[0], address[1]))
                udp.sendto(b'echo: ' + data, address)
    except KeyboardInterrupt:
        print('UDP shutdown')

if __name__ == '__main__':
    main()
