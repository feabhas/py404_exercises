"""
Alternate exercises for chapter 11 Time

Created on 24 Oct 2017

@author: martin
"""
from datetime import datetime, timedelta

def main():
    filename = 'system-y2017d24m10.log'
    filedate = datetime.strptime(filename, 'system-y%Yd%dm%m.log')
    print('File date is {:%d-%b-%Y}'.format(filedate))
    print('Next date is {:%d-%b-%Y}'.format(filedate+timedelta(days=1)))

if __name__ == '__main__':
    main()
