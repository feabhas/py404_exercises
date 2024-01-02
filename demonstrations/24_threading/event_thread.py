#!/usr/bin/env python3

import threading as thr
import time

class Reader:
    def read(self, event):
        with open('pep20.txt') as fp:
            self.zen = fp.readlines()
        event.set()
        event.clear()
        event.wait()
        # can write to shared again
        print('All done')

def main():
    event = thr.Event()
    reader = Reader()
    thread = thr.Thread(target=reader.read, args=(event,))
    thread.start()
    event.wait()
    print(''.join(reader.zen))
    time.sleep(2.0)
    # finished reading shared data
    event.set()
    thread.join()

if __name__ == '__main__':
    main()
