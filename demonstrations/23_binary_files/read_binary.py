#!/usr/bin/env python3
import struct

def main():
    with open('records.dat', 'rb') as fp:
        row = fp.read(41)
        print(row)

        char = chr(row[0])
        #char = row[0:1].decode('utf8')
        data = struct.unpack('<ddddd', row[1:])
        print('Row {}: {}'.format(char, data))

        char = fp.read(1).decode('utf8')
        length, = struct.unpack('<i', fp.read(4))
        data = struct.unpack('<'+'d'*length, fp.read(length*8))
        print('Row {}: {}'.format(char, data))


if __name__ == '__main__':
    main()