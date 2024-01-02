#!/usr/bin/env python3
import sys

def main():
    with open('data.txt', 'w') as fp:
        fp.writelines(['hello\n', 'world\n'])
        for n in (1, 2, 3, 4):
            fp.write(str(n))
            fp.write('\n')
        print('\n'.join(sys.path), file=fp)

if __name__ == '__main__':
    main()