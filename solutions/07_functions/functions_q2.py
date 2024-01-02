#!/usr/bin/env python3

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
        print('{}: class {}'.format('.'.join(str(n) for n in addr), cls))

if __name__ == '__main__':
    main()
