#!/usr/bin/env python3

from typing import List

def parse_ip(addr: str) -> List[int]:
    return [int(s) for s in addr.split('.')]


def main() -> None:
    a = parse_ip(1)
    b = parse_ip('192.168.1.1')
    b[0] = 193
    b[0] = 'a'


if __name__ == '__main__':
    main()
