#!/usr/bin/env python3

def menu(*args):
    for food in args:
        print(food)


menu('spam', 'eggs', 'bacon')

def selection(*args, **kwargs):
    for food in args:
        print(food)
    for food, choice in kwargs.items():
        if choice:
            print(food)

def main():
    selection('spam', 'eggs',
          bacon=False, sausage=True)

if __name__ == '__main__':
    main()