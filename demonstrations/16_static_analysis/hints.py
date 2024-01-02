#!/usr/bin/env python3
import typing

def add(a: float, b: float = 1) -> float:
    return a + b

n = add(5., 6.)

s = add('hello', 'world')

print(typing.get_type_hints(add))

def parse_ip(address: str) -> typing.List[int]:
    return [int(n) for n in address.split('.')]

addr = parse_ip('127.0.0.1')

def parse_kv(setting: str) -> typing.Tuple[str, int]:
    key, value = setting.split('=', maxsplit=1)
    return key.strip(), int(value)

k, v = parse_kv('base=16')


def read_word_frequency(filename: str) -> typing.Dict[str, int]:
    freq = {}
    # count frequency of words in file
    return freq


from typing import Optional

def parse_int(text: str) -> Optional[int]:
    try:
        return int(text)
    except ValueError:
        return None

print(parse_int('42'))
