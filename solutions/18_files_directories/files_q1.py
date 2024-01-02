#!/usr/bin/env python3

import os

def main():
    mydirname = os.getcwd()
    mydir = os.listdir('.')

    print("Directory: {}".format(mydirname))
    for file in mydir:
        print(file)
    
if __name__ == '__main__':
    main()
