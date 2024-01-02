#!/usr/bin/env python3

import queue
import threading as thr

def is_prime(n):
    if n> 2 and n % 2 == 0:
        return False
    for factor in range(3, int(n**0.5)+1, 2):
        if n % factor == 0:
            return False
    return True

def worker(q):
    while True:
        try:
            item = q.get()
            print('{} processing {} is {}'.format(
                thr.current_thread().getName(), item, 'prime' if is_prime(item) else 'not prime'))
        finally:
            q.task_done()

def create_pool(n, q):
    threads = []
    for i in range(n):
        t = thr.Thread(target=worker, args=(q,))
        t.daemon = True
        t.start()
        threads.append(t)
    return threads

def main():
    q = queue.Queue()
    threads = create_pool(3, q)
    for item in range(2, 14):
        q.put(item)
    q.join()


if __name__ == '__main__':
    main()
