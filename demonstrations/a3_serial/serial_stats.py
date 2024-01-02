#!/usr/bin/env python3

import serial
import time
from sense_hat import SenseHat

PORT = '/dev/serial0'


def main():
    with serial.Serial(PORT, baudrate=115200) as ser:
        sense = SenseHat()
        while True:
            stats = b'%8.2f%8.2f%8.2f' % (
                sense.get_humidity(), sense.get_temperature(), sense.get_pressure())
            ser.write(stats)
            ser.write(b'\r\n')
            time.sleep(1.0)

if __name__ == '__main__':
    main()

# alternate version using binary data without time delay (faster)

import serial
import struct

def binary_stats():
    with serial.Serial(PORT, baudrate=115200) as ser:
        sense = SenseHat()
        while True:
            stats = struct.pack('<3f',
                sense.get_humidity(), sense.get_temperature(), sense.get_pressure())
            ser.write(stats)
