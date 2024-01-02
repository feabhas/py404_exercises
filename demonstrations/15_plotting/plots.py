#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main():
    t = np.linspace(0.0, 2.0, 100)
    ax = plt.gca()
    ax.plot(np.exp(-t) * np.sin(2 * np.pi * t))
    plt.show()

    t = np.linspace(0.0, 2.0, 35)
    ax = plt.gca()
    ax.plot(t, np.exp(-t)*np.sin(2*np.pi*t), 'r--x')
    ax.plot(t, np.exp(-t)*np.sin(3*np.pi*t), ls=':', color='b', marker='o')
    ax.plot(t, np.exp(-t), '-', color='k', lw=2)
    ax.plot(t, -np.exp(-t), '-', color='#888888', lw=2)
    plt.show()
   
    t = np.linspace(0.0, 2.0, 35)
    ax = plt.gca()
    ax.plot(t, np.exp(-t)*np.sin(2*np.pi*t), 'b--.')
    ax.set_xlabel('time')
    ax.set_ylabel('$sin(2 \\pi t) e ^ -t$')
    ax.set_title('Damped Oscillation', fontsize=12, fontweight='bold')
    plt.show()

    t = np.linspace(0.0, 2.0, 100)
    ax = plt.gca()
    ax.plot(t, np.exp(-t)*np.sin(2*np.pi*t), label='$sin(2 \\pi t) e ^ -t$')
    ax.plot(t, np.exp(-t)*np.sin(3*np.pi*t), label='$sin(3 \\pi t) e ^ -t$')
    ax.legend(loc=(0.5, 0.75))
    plt.savefig('damped.png')
    plt.show()
    
if __name__ == '__main__':
    main()