#!/usr/bin/env python3

import os

def main():
    DIRNAME = 'TestDirectory'
    FILENAME = "TestFile"

    os.mkdir(DIRNAME)
    os.chdir(DIRNAME)
    with open(FILENAME, 'w') as fd:
        pass

    mydirname = os.getcwd()
    mydir = os.listdir('.')
    print("Directory: {}".format(mydirname))
    for file in mydir:
        print(file)

if __name__ == '__main__':
    main()
