#!/usr/bin/env python3

import tempfile as tf
import sys
import subprocess as sp

def main():
    try:
        with tf.TemporaryFile('w+') as fp:
            proc = sp.Popen(['netstat', '-an'],
                            stdout=sp.PIPE, bufsize=1,
                            stderr=fp,
                            universal_newlines=True)
            for line in proc.stdout:
                print(line.rstrip())
            returncode = proc.wait()
            fp.seek(0)
            for err in fp:
                print(err, file=sys.stderr)
        if returncode != 0:
            raise sp.SubprocessError('Command failed: {}'.format(returncode))
    except sp.SubprocessError as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
