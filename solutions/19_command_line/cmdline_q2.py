#!/usr/bin/env python3

import argparse
import sys

EUSAGE = """Usage: q1.py filename
print out number of lines in a file
"""

def get_filename():
    parser = argparse.ArgumentParser()
    # parser.add_argument("url", help="URL to fetch", type=str)
    # parser.add_argument("-t", "--tags", help="Depth of headers to display", type=int)
    parser.add_argument('filename')
    args = parser.parse_args()
    return args.filename


def main():
    filename = get_filename()
    with open(filename) as fp:
        total = len(fp.readlines())
    print('File {} has {} lines'.format(filename, total))


if __name__ == '__main__':
    main()

