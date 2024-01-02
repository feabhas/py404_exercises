#!/usr/bin/env python3

import os
import queue
import threading

results = []
results_lock = threading.Lock()

def get_work():
    work = []
    for dirname, dirs, files in os.walk('..'):
        for filename in files:
            if filename.endswith('.py'):
                work.append(os.path.join(dirname, filename))
    return work

def line_counter(q):
    while True:
        try:
            filename = q.get()
            with open(filename) as fp:
                with results_lock:
                    results.append(len(fp.readlines()))
        finally:
            q.task_done()

def create_pool(n, q):
    pool = []
    for i in range(n):
        t = threading.Thread(target=line_counter, args=(q,))
        t.daemon = True
        t.start()
        pool.append(t)
    return pool

def main():
    files = get_work()
    q = queue.Queue()
    create_pool(5, q)
    for filename in files:
        q.put(filename)
    q.join()
    total = sum(results)
    print('There are {} lines in {} files'.format(total, len(files)))

if __name__ == '__main__':
    main()