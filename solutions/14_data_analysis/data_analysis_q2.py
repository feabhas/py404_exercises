#!/usr/bin/env python3

import numpy as np
import pandas as pd

def main():
    flint = pd.read_csv('flint-provenance.txt', skiprows=20, sep='\t')
    ca_max = flint.Ca.max()
    ca_max_locs = flint.Location[flint.Ca == ca_max]
    print('Maximum calcium value {}, found at locations {}'.format(
          ca_max, ', '.join(str(n) for n in ca_max_locs)
    ))

if __name__ == '__main__':
    main()
