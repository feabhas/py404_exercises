#!/usr/bin/env python3

import argparse
import sys

EUSAGE = """Usage: q1.py filename
print out number of lines in a file
"""

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", help="Count the number of lines", action="store_true")
    parser.add_argument("-p", "--print", help="Print the lines", action="store_true")
    parser.add_argument('filename', nargs='+')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    for filename in args.filename:
        with open(filename) as fp:
            lines = fp.readlines()
        if args.count:
            print('File {} has {} lines'.format(filename, len(lines)))
        elif args.print:
            print(''.join(lines))


if __name__ == '__main__':
    main()

