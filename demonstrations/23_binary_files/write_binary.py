#!/usr/bin/env python3
import struct

def main():
    values = [1.0, 1.5, 2.0, 4.0, 5.0]
    with open('records.dat', 'wb') as fp:
        data = struct.pack('<5d', *values)
        fp.write(b'A')
        fp.write(data)
        data = struct.pack('<'+'d'*len(values), *[v**2 for v in values])
        fp.write(b'B')
        fp.write(struct.pack('<i', len(values)))
        fp.write(data)

if __name__ == '__main__':
    main()