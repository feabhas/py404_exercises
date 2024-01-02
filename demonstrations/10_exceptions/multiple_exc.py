#!/usr/bin/env python3

import sys

def read_int():
    while True:
        try:
            response = input('Enter a number? ')
            return int(response)
        except ValueError:
            print('Invalid number: {}'.format(response))

def main():
    try:
        n = read_int()
        print('{} squared is {}'.format(n, n**2))
    except (EOFError, KeyboardInterrupt) as err:
        print('\n{}'.format(err), file=sys.stderr)
        sys.exit(1)
    
if __name__ == '__main__':
    main()
