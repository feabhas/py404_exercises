#!/usr/bin/env python3

import time
import serial

with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
    ser.sendBreak();        # reset board
    time.sleep(1.0);
    ser.write(b'+TEMP')     # Query temperature
    line = ser.read(80)
    print(line)
