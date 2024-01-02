#!/usr/bin/env python3

def counter(seq, start=0):
    for value in seq:
        yield start, value
        start += 1

numbers = [5, 6, 2, 8, 3, 5]
for i, num in counter(numbers, 1):
    print('{}: {}'.format(i, num))

import serial

def serial_gen(port):
    with serial.Serial(port, 9600, timeout=1) as ser:
        bytes = ser.readline().rstrip()
        while bytes != b'***END***':
            yield [float(n) for n in bytes.split(b',')]
            bytes = ser.readline().rstrip()

for value in serial_gen('/dev/ttyUSB0'):
    print(value)

