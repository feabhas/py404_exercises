#!/usr/bin/env python3

import random

def middle(n):
    return (n//10)%10

def main():
    random.seed(1)
    codes = random.sample(range(100,1000), k=20)
    print(sorted(codes, key=middle))
    print(sorted(codes, key=lambda n: (n//10)%10))
    print(sorted(codes, key=lambda n: ((n//10)%10, n//100, n%10)))

if __name__ == '__main__':
    main()