#!/usr/bin/env python3

from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import HourLocator, YearLocator, DateFormatter
from matplotlib.dates import date2num

def main():
    mojo = pd.read_csv('pump-sensor-mojo.txt',
                       parse_dates={'Datetime': ['Date', 'Time']},
                       index_col='Datetime',
                       date_parser=lambda x: datetime.strptime(x, '%m/%d/%y %H:%M'))
    print(mojo.head())
    max_flow = mojo.Flow.max()
    time_max_flow = mojo[mojo.Flow==max_flow].index
    print('Maximum flow was {} at: {}'.format(
        max_flow, ','.join(t for t in time_max_flow.strftime('%d-%b-%Y %H:%M'))
    ))

if __name__ == '__main__':
    main()
