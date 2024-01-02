#!/usr/bin/env python3


def is_private(addr):

    if addr[0] == 10:
        return True
    elif addr[0] == 172 and 16 <= addr[1] < 32:
        return True
    elif addr[0:2] == [192, 168]:
        return True
    return False

def classify_ip(addr):
    fields = [int(s) for s in addr.split('.')]
    if 0 <= fields[0] < 128:
        cls = 'A'
    elif 128 <= fields[0] < 192:
        cls = 'B'
    elif 192 <= fields[0] < 224:
        cls = 'C'
    elif 224 <= fields[0] < 240:
        cls = 'D'
    else:
        cls = 'E'
    return fields, cls

def main():
    while True:
        line = input('IP addr (blank to stop)? ')
        if not line:
            break
        addr, cls = classify_ip(line)
        print('{}: class {} {}'.format(
              '.'.join(str(n) for n in addr),
              cls,
              'is private' if is_private(addr) else ''))

if __name__ == '__main__':
    main()
