#!/usr/bin/env python3

def get_hosts(filename):
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            addr, host = line.split()
            fields = [int(s) for s in addr.split('.')]
            yield host, fields

def main():
    for host, addr in get_hosts('hosts.txt'):
        print('{:20} - {}'.format(host, addr))

if __name__ == '__main__':
    main()