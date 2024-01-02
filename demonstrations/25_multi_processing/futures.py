#!/usr/bin/env python3

import concurrent.futures as cf

def is_prime(n):
    if n> 2 and n % 2 == 0:
        return False
    for factor in range(3, int(n**0.5)+1, 2):
        if n % factor == 0:
            return False
    return True

def main():
    with cf.ProcessPoolExecutor(max_workers=3) as executor:
        futures = []
        for n in range(2, 14):
            future = executor.submit(is_prime, n)
            futures.append((n, future))
    for n, future in futures:
        prime = future.result()
        print('{} is {}'.format(n, 'prime' if prime else 'not prime'))

if __name__ == '__main__':
    main()