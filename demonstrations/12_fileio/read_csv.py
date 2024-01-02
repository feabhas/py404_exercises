#!/usr/bin/env python3

import csv

def main():
    with open('populations.csv', newline='') as fp:
        fp.readline()    # skip header text
        reader = csv.reader(fp, dialect=csv.excel, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            for col in row:
                print('{}:{} '.format(col, type(col).__name__), end='')
            print()

if __name__ == '__main__':
    main()
