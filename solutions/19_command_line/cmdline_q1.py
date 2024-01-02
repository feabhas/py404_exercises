#!/usr/bin/env python3

import sys

USAGE = """Usage: q1.py filename
print out number of lines in a file
"""

def main():
    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as fp:
        total = len(fp.readlines())
    print('File {} has {} lines'.format(filename, total))


if __name__ == '__main__':
    main()