#!/usr/bin/env python3

import threading as thr
import time

def hello(msg):
    print(msg)

t = thr.Timer(3, function=hello, args=('Hello world!',))
t.start()

# 3 seconds later...

