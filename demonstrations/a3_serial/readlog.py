#!/usr/bin/env python3

import serial
import re, sys

search = re.compile('error|warning|fault', re.IGNORECASE)

def read_serial(port = 'COM1'):
    with serial.Serial(port, baudrate=9600) as ser:
        for n,line  in enumerate(ser,1):
            line = line.decode('utf-8').rstrip()
            match = search(line)
            if match:
                print('{:6d} {}'.format(n,line))

def main():
    try:
        read_serial('COM3')
    except serial.serialutil.SerialException as err:
        print(err, file=sys.stderr)

if __name__ == '__main__':
    main()
