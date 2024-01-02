#!/usr/bin/env python3

import os
import multiprocessing as mpr

def echo(pipe):
    msg = pipe.recv()
    print('pid={} msg={}'.format(os.getpid(), msg))
    pipe.send((os.getpid(), msg))
    pipe.close()


def main():
    pipe, child_pipe = mpr.Pipe()
    p = mpr.Process(target=echo, args=(child_pipe,))
    p.start()
    pipe.send([42, None, 'hello'])
    msg = pipe.recv()
    print('from child: {}'.format(msg))
    pipe.close()
    p.join()


if __name__ == '__main__':
    main()
