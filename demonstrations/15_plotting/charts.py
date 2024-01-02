#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    airq = pd.read_csv('data/air-quality.csv', sep=',', na_values=-200)
    ax = plt.gca()
    ax.scatter(airq.Time/100, airq.CO)
    plt.show()
 
    airq = pd.read_csv('data/air-quality.csv', sep=',', na_values=-200)
    t = airq.Time/100
    co = airq.CO[~np.isnan(airq.CO)]
    ax = plt.gca()
    ax.hist(co, bins=5, rwidth=0.8)
    plt.show()
 
    airq = pd.read_csv('data/air-quality.csv', sep=',', na_values=-200)
       
    index = np.arange(5)
    bar_width = 0.35
       
    nox = airq.Nox[:len(index)]
    no2 = airq.NO2[:len(index)]
       
    ax = plt.gca()
    ax.bar(index, nox, bar_width, color='b',
                label='Nox')
      
    ax.bar(index + bar_width, no2, bar_width, color='y',
                label='NO2')
    ax.set_xticks(index + bar_width / 2)
    labels = ['{:02d}:00'.format(t) for t in index]
    ax.set_xticklabels(labels)
    ax.legend()
    plt.show()

    airq = pd.read_csv('data/air-quality.csv', sep=',', na_values=-200)
    axl = plt.gca()
    plotl, = axl.plot(airq.CO, color='b')
    axl.set_ylabel("CO $\\frac{mg}{m^3}$", color='b')
    axr = axl.twinx()
    plotr, = axr.plot(airq.NO2, color='m')
    axr.set_ylabel("NO2 $\\frac{\\mu g}{m^3}$", color='m')
    axl.set_xlabel("time/hours")
    axl.legend((plotl,plotr), ('CO','NO2'), loc='upper left')
    axl.grid()
    axl.set_title("CO and NO2 Measurements")
    plt.show()

    airq = pd.read_csv('data/air-quality.csv', sep=',', na_values=-200)
    airq.NO2.plot(kind='line', label='NO2')
    airq.Nox.plot(kind='line', label='NOX')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()