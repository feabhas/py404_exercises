#!/usr/bin/env python3

import serial, sys

port = 'COM1' if sys.platform=='win32' else '/dev/ttyUSB0'

with serial.Serial(port, baudrate=9600, timeout=3.0) as ser:
    while True:
        cmd = input('Board command: ')
        if not cmd:
            break
        ser.write(cmd.encode('UTF-8'))
        ser.write(b'\n')
        line = ser.read(120)
        print(line.decode('UTF-8'))
