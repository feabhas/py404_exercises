#!/usr/bin/env python3

def main():
    with open('file_read.py') as fp:
        for line in fp:
            print(line, end='')

    with open('file_read.py') as fp:
        for line in fp:
            line = line.rstrip()
            print(line)

    with open('populations.csv') as fp:
        lines = fp.readlines()
        print('There are {} records'.format(len(lines)-1))
        fp.seek(0)
        hdr = fp.readline().rstrip()
        print('headings: {}'.format(hdr))
        fp.seek(0)
        print(fp.read(18), end='')

if __name__ == '__main__':
    main()