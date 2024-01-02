#!/usr/bin/env python3
import struct

def main():
    with open('records.dat', 'rb+') as fp:
        fp.seek(41, 0)
        buffer = fp.read(41)
        char, d0, d1, d2, d3, d4 = struct.unpack('<cddddd', buffer)
        print('row={} values={}'.format(char.decode("utf-8"),[d0, d1, d2, d3, d4]))

        fp.seek(-41, 1)
        buffer = fp.read(41)
        char = struct.unpack('<c', buffer[:1])[0].decode("utf-8")
        data = []
        for b in range(1, len(buffer), 8):
            data.append(struct.unpack('<d', buffer[b:b+8]))
        print('row={} values={}'.format(char, data))

if __name__ == '__main__':
    main()