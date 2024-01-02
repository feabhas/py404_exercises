#!/usr/bin/env python3

import threading as thr
import time

class Target:
    def __init__(self, barrier):
        self.barrier = barrier

    def action(self, num):
        print('Thread {} ready'.format(num))
        self.barrier.wait()
        print('start sleeping in thread {}'.format(num))
        time.sleep(2)
        print('done sleeping in thread {}'.format(num))


def main():
    barrier = thr.Barrier(5)
    obj = Target(barrier)
    threads = []
    for i in range(barrier.parties):
        threads.append(thr.Thread(target=obj.action, args=(i,)))
        threads[-1].start()
    print('All threads started')
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
