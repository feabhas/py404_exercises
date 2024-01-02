#!/usr/bin/env python3

name = input('Enter your first and last name? ')

first, last = name.split()

print('Hello {} {}'.format(first.capitalize(), last.capitalize()))

