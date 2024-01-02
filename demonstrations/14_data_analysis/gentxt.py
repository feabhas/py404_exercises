#!/usr/bin/env python3
import numpy as np

def main():
    airq = np.genfromtxt('air-quality.csv', delimiter=',', skip_header=1)
    print(airq.shape)
    print(airq[1])


if __name__ == '__main__':
    main()