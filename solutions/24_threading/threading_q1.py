#!/usr/bin/env python3

import os

def get_work():
    work = []
    for dirname, dirs, files in os.walk('..'):
        for filename in files:
            if filename.endswith('.py'):
                work.append(os.path.join(dirname, filename))
    return work


def main():
    files = get_work()
    total = 0
    for filename in files:
        with open(filename) as fp:
            total += len(fp.readlines())
    print('There are {} lines in {} files'.format(total, len(files)))

if __name__ == '__main__':
    main()