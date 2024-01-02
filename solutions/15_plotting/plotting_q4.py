#!/usr/bin/env python3

from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, DateFormatter

def main():
    mojo = pd.read_csv('pump-sensor-mojo.txt',
                       parse_dates={'Datetime': ['Date', 'Time']},
                       index_col='Datetime',
                       date_parser=lambda x: datetime.strptime(x, '%m/%d/%y %H:%M'))

    ax = plt.gca()
    plt.plot(mojo.index, mojo.Flow)
    ax.xaxis.set_major_locator(DayLocator())
    ax.xaxis.set_major_formatter(DateFormatter('%d-%b-%Y'))
    ax.set_ylabel('Flow rate m/s')
    ax.set_title('Mojo Flow Rate')
    plt.gcf().autofmt_xdate()
    plt.show()

if __name__ == '__main__':
    main()
