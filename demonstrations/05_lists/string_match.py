#!/usr/bin/env python3

args = input('Enter a command: ').split()

match args:
    case ['quit']:
        exit()
    case['show', 'env']:
        print(f'show the environment')
    case ['list', folder]:
        print(f'listing folder {folder}')
    case ['copy', src, dst]:
        print(f'copying from {src} to {dst}')
    case _:
        print('unknown command')
