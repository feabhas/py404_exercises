#!/usr/bin/env python3

def counter(seq, start=0):
    for value in seq:
        yield start, value
        start += 1


def main():
    numbers = [5, 6, 2, 8, 3, 5]
    for i, num in counter(numbers, 1):
        print('{}: {}'.format(i, num))

if __name__ == '__main__':
    main()
