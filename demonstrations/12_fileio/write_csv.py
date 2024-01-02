#!/usr/bin/env python3

import csv

def main():
    records = [
        ('Employee No', 'Employee Name', 'Role'),
        (123, 'Tom Watts', 'CEO'),
        (453, 'Davina Burlap', 'Director'),
        (456, 'Polly Sacks', 'Marketing'),
        (684, 'Richard Worthington', 'Sales')
    ]

    with open('employees.csv', 'w', newline='') as fp:
        writer = csv.writer(fp,  delimiter=':', quoting=csv.QUOTE_NONNUMERIC)
        for item in records:
            writer.writerow(item)

if __name__ == '__main__':
    main()
