#!/usr/bin/env python3

import time
from threading import Thread

class Target():
    def __init__(self, name):
        self.name = name

    def action(self, num):
        print('sleeping in {} {}'.format(self.name, num))
        time.sleep(2)
        print('done sleeping {} {}'.format(self.name, num))

def main():
    threads = []
    obj = Target('thread')
    for i in range(5):
        threads.append(Thread(target=obj.action, args=(i,)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
