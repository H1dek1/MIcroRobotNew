#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from drawer import Drawer

def main():
    data = np.loadtxt('../result/result.txt', skiprows=2)
    #params = np.loadtxt('../result/result.txt')
    params = np.zeros(5)
    drawer = Drawer(
            #dt=params[0],
            dt=1.0e-2,
            #a=params[1],
            a=0.3,
            alpha=params[2],
            beta=params[3],
            gamma=params[4])
    
    fig, axes = plt.subplots(1, 1, figsize=(6.4, 4.8))
    axes.set_aspect('equal')
    drawer.drawCapture(data=data, ax=axes, time=0)
    fig.savefig('sample.png')


if __name__ == '__main__':
    main()
