#!/usr/bin/env python3

def main():
    try:
        n = int(input('Enter a number? '))
    except ValueError:
        raise UserWarning('Invalid number entered')


if __name__ == '__main__':
    main()