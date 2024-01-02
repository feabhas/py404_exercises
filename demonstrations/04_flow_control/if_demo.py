#!/usr/bin/env python3

num = input('Enter a number: ')
num = int(num)
if num % 2 == 0:
    print('Even number!')
else:
    print('Odd number')

if num < 0:
    print('Negative number')
elif num == 0:
    print('You put in zero!')
else:
    print('Positive number')

