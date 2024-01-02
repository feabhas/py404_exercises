import datetime
now = datetime.datetime.now()
print(now.strftime('Today is %A the %d of %b, %Y'))

from datetime import datetime
logfile = 'data-20140101-10:15.log'
logdate = datetime.strptime(logfile, 'data-%Y%m%d-%H:%M.log')
print(f'{logdate:%a, %d-%b-%Y %H:%M}')
