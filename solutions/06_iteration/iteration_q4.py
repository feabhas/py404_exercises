#!/usr/bin/env python3

max_primes = int(input("Enter number of primes: "))

primes = [2, 3]

candidate = primes[-1]
while len(primes) < max_primes:
    candidate += 2
    is_prime = True
    for prime in primes:
        if candidate % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(candidate)

print('The first {} primes are: {}'.format(max_primes, ', '.join(str(p) for p in primes)))

