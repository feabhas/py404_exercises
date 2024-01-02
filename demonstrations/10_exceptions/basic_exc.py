#!/usr/bin/env python3

def read_int():
    while True:
        try:
            response = input('Enter a number? ')
            return int(response)
        except ValueError:
            print('Invalid number: {}'.format(response))

def main():
    n = read_int()
    print('{} squared is {}'.format(n, n**2))
    
if __name__ == '__main__':
    main()
