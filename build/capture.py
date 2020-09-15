#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from drawer import Drawer

def main(nums):
    draw_times = nums
    data = np.loadtxt('../result/result.txt', skiprows=2)
    params = np.loadtxt('../result/params.txt', skiprows=1)
    theta = np.loadtxt('../result/theta1out.txt')
    traj = np.loadtxt('../result/zout.txt')
    drawer = Drawer(
            dt=params[0],
            a=params[1],
            alpha=params[2],
            beta=params[3],
            gamma=params[4])
    
    #fig = plt.figure(tight_layout=True)
    fig = plt.figure(figsize=(10, 8), tight_layout=True)
    fig.subplots_adjust(hspace=0.3, wspace=0.6)
    gs = fig.add_gridspec(2, 3)
    ax1 = fig.add_subplot(gs[:, 0])
    ax2 = fig.add_subplot(gs[0, 1:3])
    ax3 = fig.add_subplot(gs[1, 1:3])
    """
    ax1
    """
    properties(
            ax=ax1,
            equal_aspect=True,
            xlabel='$x/l$',
            ylabel='$y/l$',
            #xlim=[-1, 1],
            #ylim=[-1, 4],
            )

    for time in draw_times:
        drawer.draw_swimmer(data=data, ax=ax1, time=time)
        #drawer.draw_ext_field(data=data, ax=axes, time=0)

    """
    ax2
    """
    ax2.grid()
    xticks = np.arange(0, 2.5, 0.5)
    xticklabels = [str(n) for n in xticks]
    ax2.set_xticks(xticks)
    ax2.set_xticklabels(xticklabels, fontsize=15)
    ax2.set_yticks([-np.pi, 0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
    ax2.set_yticklabels(['$-\\pi$', '0', '$\\pi$', '$2\\pi$', '$3\\pi$', '$4\\pi$'], fontsize=15)

    properties(
            ax=ax2,
            xlabel='$t*$',
            ylabel='$\\theta$',
            xlim=[0, 2.5],
            ylim=[-0.5*np.pi, 4.5*np.pi],
            )

    ax2.plot(theta[:, 0], theta[:, 1]-np.pi/2)

    """
    ax3
    """
    ax3.set_xticks(xticks)
    ax3.set_xticklabels(xticklabels, fontsize=15)
    properties(
            ax=ax3,
            xlabel='$t*$',
            ylabel='$y$',
            xlim=[0, 2.5],
            ylim=[0, 0.5],
            )
    ax3.plot(traj[:, 0], traj[:, 1])
    fig.savefig('sample.png')

def properties(
        ax, 
        equal_aspect=False,
        xlabel='$x$', ylabel='$y$',
        xlim=None, ylim=None,
        xticks=None, yticks=None,
        xticklabels=None, yticklabels=None):

    if equal_aspect == True: ax.set_aspect('equal')
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)

    if xlim != None:
        ax.set_xlim(xlim)
    if ylim != None:
        ax.set_ylim(ylim)

    if xticks != None:
        ax.set_xticks(xticks)
        if xticklabels != None:
            ax.set_xticklabels(xticklabels, fontsize=15)
    if yticks != None:
        ax.set_yticks(yticks)
        if yticklabels != None:
            ax.set_yticklabels(yticklabels, fontsize=15)



if __name__ == '__main__':
    nums = [float(n) for n in sys.argv[1:]]
    main(nums)
