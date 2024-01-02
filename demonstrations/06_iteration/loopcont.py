#!/usr/bin/env python3

while True:
    answer = input('command? ')
    if answer == 'quit':
        break
     if answer == 'pass':
        continue    
    print('Your command was', answer)