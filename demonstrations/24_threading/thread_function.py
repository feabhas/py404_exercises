#!/usr/bin/env python3

import time
import threading as thr

def action(num):
    print('sleeping in thread {}'.format(num))
    time.sleep(2)
    print('done sleeping from {}'.format(num))

def main():
    threads = []
    for i in range(5):
        threads.append(thr.Thread(target=action, args=(i,)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
