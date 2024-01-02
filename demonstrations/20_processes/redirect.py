#!/usr/bin/env python3

import sys
import subprocess as sp

def main():
    try:
        cp = sp.run(['netstat', '-an'],
                    stdout=sp.PIPE, stderr=sp.PIPE,
                    universal_newlines=True)
        cp.check_returncode()
        for line in cp.stdout.split('\n'):
            print(line)
        for errs in cp.stderr.split('\n'):
            print(line, file=sys.stderr)
    except sp.SubprocessError as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
