#!/usr/bin/env python3

import struct

FILE='hosts.dat'

DATA = [
    [ [ 127, 0, 0, 1], 'localhost'],
    [ [ 192, 168, 1, 1], 'server.local.net'],
    [ [ 192, 168, 1, 2], 'myhost.local.net'],
]

def main():
    with open(FILE, 'wb') as fp:
        for row in DATA:
            buffer = struct.pack('<4B64s', *row[0], row[1].encode())
            fp.write(buffer)
    
    hosts = {}       
    with open(FILE, 'rb') as fp:
        while True:
            buffer = fp.read(4)
            if buffer == b'':
                break
            addr = list(struct.unpack('<4B', buffer))
            name = struct.unpack('64s', fp.read(64))[0]
            name = name.decode('UTF-8').rstrip('\0x00')
            hosts[name] = addr
    for name,addr in sorted(hosts.items()):
        print('{:32s}: {}'.format(name, addr))

DATA_LIST = [
    [ [ 127, 0, 0, 1], 
        ['localhost', 'feabhas', 'loopback']],
    [ [ 192, 168, 1, 1], 
        ['server.local.net']],
    [ [ 192, 168, 1, 2], 
        ['myhost.local.net', 'feabhas.local.net']],
]

def main_list():
    with open(FILE, 'wb') as fp:
        for row in DATA_LIST:
            addr = struct.pack('4B', *row[0])
            fp.write(addr)
            fp.write(struct.pack('B', len(row[1])))
            for name in row[1]:
                fp.write(struct.pack('64p', name.encode()))
    
    hosts = {}       
    with open(FILE, 'rb') as fp:
        while True:
            buffer = fp.read(4)
            if buffer == b'':
                break
            addr = list(struct.unpack('4B', buffer))
            count, = struct.unpack('B', fp.read(1))
            for _ in range(count):
                name, = struct.unpack('64p', fp.read(64))
                name = name.decode('UTF-8')
                hosts[name] = addr
    for name,addr in sorted(hosts.items()):
        print('{:32s}: {}'.format(name, addr))
             
if __name__ == '__main__':
    #main()
    main_list()
