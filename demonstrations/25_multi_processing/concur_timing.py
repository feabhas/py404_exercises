#!/usr/bin/env python3
"""
Concurrency timing example

Sample timings on a 4-core Windows 10 workstation

SCALE = 5000

sequential 416.2783889770508
threading 406.96760416030884
multiprocessing 159.20711588859558

SCALE = 10000

sequential 1009.5904223918915
threading 964.6052610874176
multiprocessing 415.51235914230347

"""
import time
import threading as thr
import multiprocessing as mpr
import queue

SCALE = 100

def do_work(values):
    half = len(values)//2
    roots = 0.
    for n in values[:half]:
        roots += n ** 0.5
    for n in values[half:]:
        roots += n ** 0.5
    return roots

RANGES = [
    range(     0*SCALE, 100000*SCALE),
    range(100000*SCALE, 200000*SCALE),
    range(200000*SCALE, 300000*SCALE),
    range(300000*SCALE, 400000*SCALE),
]

def seq_work(values):
    _ = do_work(values)

def seq():
    start = time.time()
    for r in RANGES:
        seq_work(r)
    end = time.time()
    print("sequential", end-start)

def thr_work(q):
    values = q.get()
    _ = do_work(values)
    q.task_done()

def threads():
    q = queue.Queue()
    threads = []
    for _ in range(4):
        t = thr.Thread(target=thr_work, args=(q,))
        t.start()
        threads.append(t)
    time.sleep(2)
    start = time.time()
    for r in RANGES:
        q.put(r)
    q.join()
    end = time.time()
    for t in threads:
        t.join()
    print('threading', end - start)


def mpr_work(q):
    values = q.get()
    _ = do_work(values)


def processes():
    q = mpr.Queue()
    procs = []
    for _ in range(4):
        p = mpr.Process(target=mpr_work, args=(q,))
        p.start()
        procs.append(p)
    time.sleep(2)
    start = time.time()
    for r in RANGES:
        q.put(r)
    q.close()
    for p in procs:
        p.join()
    end = time.time()
    print("multiprocessing", end - start)

import concurrent.futures as cf

def future_work(values):
    return do_work(values)

def futures():
    with cf.ProcessPoolExecutor(max_workers=4) as executor:
        futures = []
        start = time.time()
        for r in RANGES:
            future = executor.submit(future_work, r)
            futures.append(future)
    for future in futures:
        _ = future.result()
    end = time.time()
    print("executor tasks", end - start)

def main():
    seq()
    threads()
    processes()
    #futures()

if __name__ == '__main__':
    main()