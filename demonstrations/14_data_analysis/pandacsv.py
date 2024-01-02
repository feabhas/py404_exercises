#!/usr/bin/env python3

import numpy as np
import pandas as pd

def main():
    airq = pd.read_csv('../../data/air-quality.csv', sep=',')
    print(airq.head())
    print(airq.columns)
    
    print(airq.CO)
    print(airq['CO'])
    print(airq[0:1])
    print(airq.loc[[0]])
    
    print(airq.CO >= 4.0)
    print(airq.mean(axis=0))
    print(airq > airq.mean(axis=0))
 
    # airq.CO[airq.CO >= 4.0] = 4.0
    # print(airq.CO)
    #
    # airq[airq==-200] = np.nan
    # print(airq)
    # print(airq.min(axis=0))
    #
    # airq = pd.read_csv('../../data/air-quality.csv', sep=',', na_values=['-200', '-', 'n/a'])
    # print(airq.head())

if __name__ == '__main__':
    main()