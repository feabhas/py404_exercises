#!/usr/bin/env python3

import re

def capitals(m):
    text = m.group()
    return text[:1].upper()+text[1:]

def main():
    page = """
python is n interpreted programming language.
created by Guido van Rossum and first released in 1991.
python uses whitespace indentation to delimit code blocks.
"""
    output = re.sub('([a-z][^.]+.)*', capitals, page)
    print(output)

if __name__ == '__main__':
    main()