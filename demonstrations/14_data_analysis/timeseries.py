import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import HourLocator, DateFormatter

airq = pd.read_csv('../../data/air-quality.csv',
                   parse_dates={'Datetime': ['Date', 'Time']},
                   index_col='Datetime',
                   na_values='-200',
                   date_parser=lambda x: datetime.strptime(x, '%Y%m%d %H%M'))
print('RH min: {}, max : {}'.format(airq.RH.min(), airq.RH.max()))

limit = 5.0
print(airq.CO > limit)
max_co_dates = airq[airq.CO >limit].index
print('Co exceeded {} on {}'.format(
       limit, max_co_dates.strftime('%d-%b-%Y %H:%M')))

print('CO exceeded average {} times'.format((airq.CO > airq.CO.mean()).sum()))

airq.interpolate(inplace=True)
print(airq.head())
airq.CO[airq.CO >= 4.0] = 4.0
print(airq.CO)
