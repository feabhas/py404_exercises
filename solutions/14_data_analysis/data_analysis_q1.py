#!/usr/bin/env python3

import numpy as np
import pandas as pd

def main():
    flint = pd.read_csv('flint-provenance.txt', skiprows=20, sep='\t')
    print(flint.head())

    print('Max iron concentration is {:.2f}'.format(flint.Fe.max()))
    print('Min copper concentration is {:.2f}'.format(flint.Cu.min()))
    print('Average zinc concentration is {:.2f}'.format(flint.Zn.mean()))

    loc2 = flint[flint.Location==2]
    print('There are {} flints from location 2'.format(loc2.shape[0]))
    ratio_na_k = loc2.Na/loc2.K
    print('Sodium to Potassium ratio for location 2 flints: {}'.format(
          ', '.join(str(n) for n in ratio_na_k.values.round(2))))


if __name__ == '__main__':
    main()
