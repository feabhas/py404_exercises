#!/usr/bin/env python3

import random

numbers = (
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10)
)

guess = int(input('Guess on of my three numbers? '))

if guess in numbers:
    print('good guess: {} is in {}'.format(guess, sorted(numbers)))
else:
    print('sorry {} is not in {}'.format(guess, sorted(numbers)))

