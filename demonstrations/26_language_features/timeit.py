#!/usr/bin/env python3

import time
import math


def timeit(func):
    def timed(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print('{} took {:6.2f} sec'.format(func.__name__, te-ts))
        return result

    return timed


@timeit
def squares(size):
    data = [float(n) for n in range(1,size+1)]
    return [math.sqrt(f**4/f**2) for f in data]


def main():
    squares(1000000)

if __name__ == '__main__':
    main()
