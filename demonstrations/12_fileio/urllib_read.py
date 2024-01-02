#!/usr/bin/env python3

import urllib.request as request

with request.urlopen('http://www.feabhas.com') as resp:
    for line in resp:
        print(line.decode('UTF-8'), end='')
