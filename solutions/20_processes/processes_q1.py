#!/usr/bin/env python3

import os, sys
import subprocess

CMD = ['ls','-l'] if sys.platform != 'win32' else ['cmd','/c','dir']

def main():
    cp = subprocess.run(CMD)
    cp.check_returncode()

if __name__ == '__main__':
    main()