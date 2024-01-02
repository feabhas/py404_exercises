#!/usr/bin/env python3

import serial, sys

port = 'COM1' if sys.platform=='win32' else '/dev/ttyUSB0'

with serial.Serial(port, baudrate=9600) as ser:
    for n,line  in enumerate(ser,1):
        line = line.decode('utf-8').rstrip()
        print('{:6d} {}'.format(n, line))
