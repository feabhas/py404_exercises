import datetime
xmas = datetime.datetime(year=2014, day=25, month=12)
print(xmas)
today = datetime.datetime.today()
print(today)
delta_xmas = xmas - today
print(delta_xmas)
print(delta_xmas.days)
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)
print(today)
