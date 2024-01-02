#!/usr/bin/env python3
"""
Example use of modules and docstrings

Utility functions to classify IP addresses

:author: Feabhas
:date: Dec 2017
"""

def is_private(addr):
    """
    Identify if an IP address is private. A private address is one that
    begins with 10, 192.168 or in the range 172.16 to 172.31.

    :param addr: IP address as an array of 4 ints
    :return: true if address is private
    """
    if addr[0] == 10:
        return True
    elif addr[0] == 172 and 16 <= addr[1] < 32:
        return True
    elif addr[0:2] == [192, 168]:
        return True
    return False

def classify_ip(addr):
    """
    Identify the class of the IP address based on the value of the first field.

    :param addr:
    :return: tuple of address (list of int) and class
    """
    fields = [int(s) for s in addr.split('.')]
    if 0 <= fields[0] < 128:
        cls = 'A'
    elif 128 <= fields[0] < 192:
        cls = 'B'
    elif 192 <= fields[0] < 224:
        cls = 'C'
    elif 224 <= fields[0] < 240:
        cls = 'D'
    else:
        cls = 'E'
    return fields, cls

if __name__ == '__main__':
    addr, cls = classify_ip('192.168.1.1')
    print('{}: class {} {}'.format(
        '.'.join(str(n) for n in addr),
        cls,
        'is private' if is_private(addr) else ''))
