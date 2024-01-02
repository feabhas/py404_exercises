#!/usr/bin/env python3

import time
import threading as thr

class Target():
    def __init__(self, limit):
        self.semaphore = thr.BoundedSemaphore(limit)

    def action(self, num):
        with self.semaphore:
            print('sleeping in thread {}'.format(num))
            time.sleep(2)
            print('done sleeping in thread {}'.format(num))

def main():
    threads = []
    obj = Target(2)
    for i in range(5):
        threads.append(thr.Thread(target=obj.action, args=(i,)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
