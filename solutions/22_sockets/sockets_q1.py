#!/usr/bin/env python3
import socket
import random

HOST = ''
PORT = 8882

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
            udp.bind((HOST, PORT))
            uhost, uport = udp.getsockname()
            print('UDP bind at {}:{}'.format(uhost, uport))
            while True:
                data, address = udp.recvfrom(80)
                print('Received "{}" from {}:{}'.format(data[0], address[0], address[1]))
                n = random.randrange(data[0])
                udp.sendto(n.to_bytes(1, byteorder='little'), address)
    except KeyboardInterrupt:
        print('UDP shutdown')

if __name__ == '__main__':
    main()
