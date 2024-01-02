#!/usr/bin/env python3

import os

def main():
    for dirname, dirs, files in os.walk('..'):
        print('Files in {}'.format(dirname))
        for filename in files:
            print(os.path.join(dirname, filename))

if __name__ == '__main__':
    main()