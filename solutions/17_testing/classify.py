#!/usr/bin/env python3
"""
Example IP address classification funtion

Used to illustrate static and unit testing.
:author: Feabhas
:date: Jan 2018
"""

def classify_ip(addr: str) -> str:
    """
    Identify the class of the IP address based on the value of the first field.

    :param addr:
    :return: tuple of address (list of int) and class
    """
    fields = [int(s) for s in addr.split('.')]
    if len(fields) != 4:
        raise UserWarning("Address {} must have four dot separated fields".format(addr))
    for num in fields:
        if num < 0 or num > 255:
            raise UserWarning('Invalid number {} found in {}'.format(num, fields))

    if 0 <= fields[0] < 128:
        return 'A'
    elif 128 <= fields[0] < 192:
        return 'B'
    elif 192 <= fields[0] < 224:
        return 'C'
    elif 224 <= fields[0] < 240:
        return 'D'
    return 'E'
