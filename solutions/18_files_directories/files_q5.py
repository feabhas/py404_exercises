#!/usr/bin/env python3

import os

def main():
    rm_list= []
    startdir = os.getcwd()
    for dirname, _, files in os.walk('.'):
        for filename in files:
            if filename.endswith('.txt'):
                path = os.path.join(startdir,  dirname,  filename)
                rm_list.append(path)
        for path in rm_list:
            print('Removing {}'.format(path))
            os.unlink(path)
    
if __name__ == '__main__':
    main()
