#!/usr/bin/env python3

import serial, time

PORT='COM3'

def main():
    with serial.Serial(PORT, baudrate=115200, timeout=2.0) as ser:
        while True:
            line = ser.readline().strip()
            if line:
                try:
                    data = [float(s) for s in line.split()]
                    print(data)
                except ValueError:
                    print('Faulty line "{}"'.format(line))
            else:
                print('Timeout')


if __name__ == '__main__':
    main()

# alternate version reading binary data

import serial
import struct
import time

def read_binary_stats():
    results = []
    try:
        with serial.Serial(PORT, baudrate=115200, timeout=2.0) as ser:
            start = time.time()
            while True:
                buffer = ser.read(12)
                if buffer:
                    try:
                        data = struct.unpack('<3f', buffer)
                        results.append(data)
                    except ValueError:
                        pass
                else:
                    pass
    except KeyboardInterrupt:
        pass
    end = time.time()

    print('read {} lines in {:.2f} at {:.2f} lines/sec'.format(
        len(results), end-start, len(results)/(end-start)))