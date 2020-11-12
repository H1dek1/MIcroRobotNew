#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from drawer import Drawer

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.size'] = 20

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
    fig = plt.figure(figsize=(12, 8), tight_layout=True)
    fig.subplots_adjust(hspace=0.3, wspace=0.6)
    gs = fig.add_gridspec(2, 12)
    ax0 = fig.add_subplot(gs[:, 0:4])
    ax1 = fig.add_subplot(gs[:, 4:8])
    ax2 = fig.add_subplot(gs[0, 8:12])
    ax3 = fig.add_subplot(gs[1, 8:12])

    #ax0 = fig.add_subplot(1, 4, 1)
    #ax1 = fig.add_subplot(1, 4, 2)
    #ax2 = fig.add_subplot(2, 2, 2)
    #ax3 = fig.add_subplot(2, 2, 4)
    """
    ax1
    """
    ax1.text(-1.0, 4.9, 'A', fontsize=30, horizontalalignment='center')
    ax2.text(-0.1, 17, 'B', fontsize=30, horizontalalignment='center')
    ax3.text(-0.1, 0.52, 'C', fontsize=30, horizontalalignment='center')
    properties(
            ax=ax1,
            equal_aspect=True,
            xlabel='$\it{x}/l$',
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
    #ax2.grid()
    xticks = np.arange(0, 3.0, 0.5)
    xticklabels = [str(n) for n in xticks]
    ax2.set_xticks(xticks)
    ax2.set_xticklabels(xticklabels)
    ax2.set_yticks([-np.pi, 0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi, 5*np.pi])
    ax2.set_yticklabels(['$-\\pi$', '0', '$\\pi$', '$2\\pi$', '$3\\pi$', '$4\\pi$', '$5\\pi$'])

    properties(
            ax=ax2,
            xlabel='$t*$',
            ylabel='$\\theta$',
            xlim=[0, 2.5],
            ylim=[-0.5*np.pi, 5.0*np.pi],
            )

    ax2.plot(theta[:, 0], theta[:, 1]-np.pi/2)

    """
    ax3
    """
    #ax3.grid()
    ax3.set_xticks(xticks)
    ax3.set_xticklabels(xticklabels)
    properties(
            ax=ax3,
            xlabel='$t*$',
            ylabel='$y/l$',
            xlim=[0, 2.5],
            ylim=[0, 0.5],
            )
    ax3.plot(traj[:, 0], traj[:, 1])
    fig.savefig('sample_fig.png')
    fig.savefig('sample_fig.eps')

def properties(
        ax, 
        equal_aspect=False,
        xlabel='$x$', ylabel='$y$',
        xlim=None, ylim=None,
        xticks=None, yticks=None,
        xticklabels=None, yticklabels=None):

    if equal_aspect == True: ax.set_aspect('equal')
    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)

    if xlim != None:
        ax.set_xlim(xlim)
    if ylim != None:
        ax.set_ylim(ylim)

    if xticks != None:
        ax.set_xticks(xticks)
        if xticklabels != None:
            ax.set_xticklabels(xticklabels)
    if yticks != None:
        ax.set_yticks(yticks)
        if yticklabels != None:
            ax.set_yticklabels(yticklabels)



if __name__ == '__main__':
    nums = [float(n) for n in sys.argv[1:]]
    main(nums)
