import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import HourLocator, DateFormatter

airq = pd.read_csv('air-quality.csv',
                   parse_dates={'Datetime': ['Date', 'Time']},
                   index_col='Datetime',
                   na_values='-200',
                   date_parser=lambda x: datetime.strptime(x, '%Y%m%d %H%M'))
airq.interpolate(inplace=True)

ax = plt.gca()
ax.plot(airq.index, airq.CO, marker='.')
ax.xaxis.set_major_locator(HourLocator(interval=3))
ax.xaxis.set_major_formatter(DateFormatter('%H:%M (%d-%b)'))
ax.set_title('CO concentrations $\\frac{mg}{m^3}$')
plt.gcf().autofmt_xdate()
plt.show()
