#!/usr/bin/env python3

import time
import threading

class ThreadedClass(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = thread_num

    def run(self):
        print('sleeping in thread {}'.format(self.num))
        time.sleep(2)
        print('done sleeping from {}'.format(self.num))

def main():
    threads = []
    for i in range(5):
        threads.append(ThreadedClass(num=i))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
