#!/usr/bin/env python3

import os, sys
import subprocess as sp

def linux_fields(line):
    fields = line.split()
    if len(fields) != 9:
        return None, None
    filename = fields[8]
    date = ' '.join(fields[5:8])
    return filename, date

def windows_fields(line):
    fields = line.split()
    if len(fields) != 4 or ':' not in fields[1]:
        return None, None
    filename = fields[3]
    date = ' '.join(fields[:2])
    return filename, date

CMD = ['ls', '-l'] if sys.platform != 'win32' else ['cmd','/c','dir']
get_fields = linux_fields if sys.platform != 'win32' else windows_fields

def main():
    proc = sp.Popen(CMD, stdout=sp.PIPE, bufsize=1, universal_newlines=True)
    print('Directory: {}'.format(os.getcwd()))
    for line in proc.stdout:
        filename, date = get_fields(line)
        if filename is None:
            continue
        print('{:20} {}'.format(filename, date))
    returncode = proc.wait()
    if returncode != 0:
        raise sp.SubprocessError('Command "{}" failed: {}'.format(CMD, returncode))


if __name__ == '__main__':
    main()

