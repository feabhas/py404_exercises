#!/usr/bin/env python3

def printf(fmt, *args, **kwargs):
    print(fmt.format(*args), **kwargs)

def main():
    printf('Hello {}', 'world', end='...')

if __name__ == '__main__':
    main()
