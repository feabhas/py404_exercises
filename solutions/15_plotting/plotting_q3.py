#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    rsond = pd.read_csv('radiosond.txt', skiprows=5, delim_whitespace=True, na_values=['nd'])
    ax = plt.gca()
    pres, = ax.plot(rsond.Height, rsond.Pressure, 'g-')
    bx = ax.twinx()
    rh, = bx.plot(rsond.Height, rsond.RH, 'r-')
    ax.set_xlabel ('Height')
    ax.set_ylabel('Pressure')
    bx.set_ylabel('RH')
    ax.set_title('Radio Sond Data')
    ax.legend((pres, rh), ('Pressure', 'Relative Humidity'), loc='upper right')
    plt.show()


if __name__ == '__main__':
    main()
