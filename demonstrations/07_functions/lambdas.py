#!/usr/bin/env python3


def main():
    words = 'This parrot is no more It has ceased to be'.split()

    print(sorted(words, key=lambda w: w.lower()))

    print(sorted(words, key=lambda w: len(w)))

    print(sorted(words, key=len))

    print(sorted(words, key=lambda w: (len(w), w.lower())))

if __name__ == '__main__':
    main()
