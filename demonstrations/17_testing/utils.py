#!/usr/bin/env python3

from typing import Union

def parse_number(text: str) -> Union[int, float]:
    text = text.strip()
    if '.' in text:
        return float(text)
    elif text.startswith('0x'):
        return int(text, base=16)
    else:
        return int(text)
