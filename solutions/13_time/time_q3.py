#!/usr/bin/env python3

from datetime import datetime, timedelta

def main():
    filenames = [
        '01022017.log', '02012017.log', 
        '03032017.log', '03122016.log'
    ]
    sortdict = dict()
    for filename in filenames:
        sortdict[datetime.strptime(filename, '%d%m%Y.log')] = filename
    dates = [filename for dt,filename in sorted(sortdict.items())]
    print(dates)
 

if __name__ == '__main__':
    main()
