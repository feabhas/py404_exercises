#!/usr/bin/env python3

import os
import concurrent.futures as cf

def get_work():
    work = []
    for dirname, dirs, files in os.walk('..'):
        for filename in files:
            if filename.endswith('.py'):
                work.append(os.path.join(dirname, filename))
    return work


def line_counter(filename):
    print('pid={} msg={}'.format(os.getpid(), filename))
    with open(filename) as fp:
        total = len(fp.readlines())
    return total

def main():
    files = get_work()
    with cf.ProcessPoolExecutor(max_workers=3) as executor:
        futures = []
        for filename in files:
            futures.append(executor.submit(line_counter, filename))
    total = 0
    for future in futures:
        total += future.result()

    print('There are {} lines in {} files'.format(total, len(files)))

if __name__ == '__main__':
    main()