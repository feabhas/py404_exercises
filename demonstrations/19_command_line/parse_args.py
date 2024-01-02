#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-n', '--number', action='store_const',
                        default=0, const=1)
    parser.add_argument('-f', '--file', nargs=1, default='config.py')
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()