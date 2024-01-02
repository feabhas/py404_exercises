#!/usr/bin/env python3

my_list
["I'm", 'a', 'list', 'of', 'strings']
print(my_list[0])
print(my_list[-1])
print(my_list[:-2])
tail = my_list[2:]
print(tail)
print(len(tail))

print(' SPLIT-ME-ON-THE-HYPHEN'.split('-'))
print(' - '.join(['JOIN','WORDS','LIKE','THIS']))

details = 'John', 'Smith', 49
print(details)
fname, lname, age = details
num, den = divmod(3.14159, 1)
