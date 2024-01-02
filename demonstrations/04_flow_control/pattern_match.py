#!/usr/bin/env python3

num = input('Enter a number: ')
num = int(num)

match num:
    case 0:
        print('none')
    case 1:
        print('one')
    case 2 | 3 | 4 | 5:
        print('handful')
    case _:
        print('many')


command = input('Enter a command: ').strip()

match command:
    case 'quit':
        exit()
    case 'bonjour' | 'guten tag' | 'ciao':
        print('good day')
    case _:
        print('unknown command')
