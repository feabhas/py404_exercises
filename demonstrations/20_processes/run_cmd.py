#!/usr/bin/env python3

import sys
import subprocess as sp


def main():
    try:
        cp = sp.run('netstat -an', shell=True)
        cp.check_returncode()
    except sp.SubprocessError as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)



if __name__ == '__main__':
    main()
