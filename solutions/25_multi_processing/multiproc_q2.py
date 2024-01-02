#!/usr/bin/env python3

import os
import multiprocessing as mpr

def get_work():
    work = []
    for dirname, dirs, files in os.walk('..'):
        for filename in files:
            if filename.endswith('.py'):
                work.append(os.path.join(dirname, filename))
    return work


def line_counter(pipe):
    filename = pipe.recv()
    print('pid={} msg={}'.format(os.getpid(), filename))
    with open(filename) as fp:
        total = len(fp.readlines())
    pipe.send(total)
    pipe.close()

def start_counter(filename):
    pipe, child_pipe = mpr.Pipe()
    p = mpr.Process(target=line_counter, args=(child_pipe,))
    p.start()
    pipe.send(filename)
    return p, pipe


def main():
    files = get_work()
    procs = []
    for filename in files:
        procs.append(start_counter(filename))
    total = 0
    for proc, pipe in procs:
        n = pipe.recv()
        print('from child: {}'.format(n))
        proc.join()
        total += n

    print('There are {} lines in {} files'.format(total, len(files)))

if __name__ == '__main__':
    main()