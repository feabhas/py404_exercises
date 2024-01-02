#!/usr/bin/env python3

import multiprocessing as mpr
import queue, os, time

def is_prime(n):
    if n> 2 and n % 2 == 0:
        return False
    for factor in range(3, int(n**0.5)+1, 2):
        if n % factor == 0:
            return False
    return True

def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('{:6d} processing {} is {}'.format(
            os.getpid(), item, 'prime' if is_prime(item) else 'not prime'))

def create_workers(n, q):
    processes = []
    for i in range(n):
        p = mpr.Process(target=worker, args=(q,))
        p.start()
        processes.append(p)
    return processes

def main():
    q = mpr.Queue()
    processes = create_workers(3, q)
    for item in range(2, 14):
        q.put(item)
    for _ in range(len(processes)):
        q.put(None)
    q.close()
    for proc in processes:
        proc.join()


if __name__ == '__main__':
    main()
