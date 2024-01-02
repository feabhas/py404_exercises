#!/usr/bin/env python3

import os

def main():
    for dirname in ['../starter','../demo']: #sys.stdin:
        dirname = dirname.strip()
        print(dirname)
        for f in os.listdir(dirname):
            print('  {}'.format(f))
        print()
      
if __name__ == '__main__':
    main()
