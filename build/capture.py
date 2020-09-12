#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from drawer import Drawer

def main():
    draw_times = [0., 20]
    data = np.loadtxt('../result/result.txt', skiprows=2)
    params = np.loadtxt('../result/params.txt', skiprows=1)
    drawer = Drawer(
            dt=params[0],
            a=params[1],
            alpha=params[2],
            beta=params[3],
            gamma=params[4])
    
    fig, axes = plt.subplots(1, 1, figsize=(6.4, 4.8))
    axes.set_aspect('equal')

    for time in draw_times:
        drawer.draw_swimmer(data=data, ax=axes, time=time)
        #drawer.draw_ext_field(data=data, ax=axes, time=0)
    fig.savefig('sample.png')


if __name__ == '__main__':
    main()
