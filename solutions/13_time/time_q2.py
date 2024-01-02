"""
Alternate exercises for chapter 11 Time

Created on 24 Oct 2017

@author: martin
"""
from datetime import datetime, timedelta


def main():
    today = datetime.today()
    xmas = datetime(today.year+1 if (today.month==12 and today.day>25) 
                                 else today.year, 
                                 12, 25)
    tdelta = xmas-today
    print('{} days to Xmas ({:%d-%b-%Y})'.format(tdelta.days, xmas))
    print('Xmas falls on a {:%A}'.format(xmas))

if __name__ == '__main__':
    main()
