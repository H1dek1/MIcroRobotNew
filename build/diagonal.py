#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main():
    data = np.loadtxt("../result/phases.txt", skiprows=2)
    ext_angle = data[:,6]
    pos_x = data[:,4]
    pos_y = data[:,5]
    swimmer_angle = np.arctan2(pos_y, pos_x)

    fig, ax = plt.subplots(1, 1)
    ax.plot(ext_angle, swimmer_angle)
    plt.show()

if __name__ == '__main__':
    main()
