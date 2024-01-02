#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    rsond = pd.read_csv('radiosond.txt', skiprows=5, delim_whitespace=True, na_values=['nd'])
    print(rsond.head())
    ax = plt.gca()
    ax.plot(rsond.Height, rsond.Temperature, 'r-', label='Temperature')
    ax.plot(rsond.Height, rsond.VapP, 'k--', label='Vapour Point')
    ax.plot(rsond.Height, rsond.Dewp, 'g:', label='Dew Point')
    ax.set_xlabel('Height (m)')
    ax.set_ylabel('Temperature $\\degree C$')
    ax.set_title('Radio Sond Data')
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()
