#!/usr/bin/env python3

b = 0
while b <= 3:
    x = 0
    print('Outer {}'.format(b))
    while x <= 5:
        print('Inner {}'.format(x))
        x += 1
    b += 1

for b in range(4):
    print('Outer {}'.format(b))
    for x in range(6):
        print('Inner {}'.format(x))
