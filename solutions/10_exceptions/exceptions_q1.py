#!/usr/bin/env python3

def classify_ip(addr):
    fields = [int(s) for s in addr.split('.')]
    if len(fields) != 4:
        raise UserWarning("Address {} must have four dot separated fields".format(addr))
    for n in fields:
        if n < 0 or n > 255:
            raise UserWarning('Invalid number {} found in {}'.format(n, fields))

    if 0 <= fields[0] < 128:
        return 'A'
    elif 128 <= fields[0] < 192:
        return 'B'
    elif 192 <= fields[0] < 224:
        return 'C'
    elif 224 <= fields[0] < 240:
        return 'D'
    return 'E'

def main():
    while True:
        addr = input('IP addr (blank to stop)? ')
        if not addr:
            break
        print('{}: class {}'.format(addr, classify_ip(addr)))

if __name__ == '__main__':
    main()
