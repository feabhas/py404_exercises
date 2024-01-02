#!/usr/bin/env python3

import csv

FILE = '../../data/hosts.txt'

class Host:
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname

    def __str__(self):
        return '{}:{}'.format(
            self.hostname, self.ip)


def read_hosts(filename):
    hosts = []
    with open(filename) as fp:
        for entry in fp:
            entry = entry.strip()
            if entry.startswith('#') or not entry:
                continue
            fields = entry.split()
            if len(fields) != 2:
                continue
            hosts.append(Host(fields[0], fields[1]))
    return hosts


def main():
    hosts = read_hosts(FILE)
    for host in hosts:
        print(host)

if __name__ == '__main__':
    main()
