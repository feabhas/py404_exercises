#!/usr/bin/env python3

import threading as thr

def is_prime(n):
    if n> 2 and n % 2 == 0:
        return False
    for factor in range(3, int(n**0.5)+1, 2):
        if n % factor == 0:
            return False
    return True

results = []
results_lock = thr.Lock()

def action(num):
    with results_lock:
        results.append((num, is_prime(num)))

def main():
    threads = []
    for n in range(2, 14):
        threads.append(thr.Thread(target=action, args=(n,)))
        threads[-1].start()
    for t in threads:
        t.join()
    for n, prime in results:
        print('{} is {}'.format(n, 'prime' if prime else 'not prime'))

if __name__ == '__main__':
    main()
