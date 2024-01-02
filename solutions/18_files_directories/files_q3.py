#!/usr/bin/env python3

import os
import glob

def main():
    FILENAME = "TestFile"
    # cd to TestDirectory
    os.chdir('TestDirectory')

    mydir = glob.glob('*.txt')
    for file in mydir:
        print(file)
  
if __name__ == '__main__':
    main()
