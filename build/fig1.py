#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from drawer import Drawer

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 25
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

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
    
    fig = plt.figure(figsize=(14, 4), tight_layout=True)
    gs = fig.add_gridspec(1, 3)
    ax1 = fig.add_subplot(gs[0, 0:2])
    ax2 = fig.add_subplot(gs[0, 2])
    ax3 = ax2.twinx()

    """
    ax1
    """
    properties(
            ax=ax1,
            equal_aspect=True,
            xlabel=r'$x/\ell$',
            ylabel=r'$y/\ell$',
            #xlim=[-1, 1],
            #ylim=[-1, 4],
            )

    for time in draw_times:
        drawer.draw_swimmer(data=data, ax=ax1, time=time)
        #drawer.draw_ext_field(data=data, ax=axes, time=0)

    ax1.set_ylim(-1, 1)
    """
    ax2
    """
    #ax2.grid()
    xticks = np.arange(0, 3.0, 0.5)
    xticklabels = [str(n) for n in xticks]
    ax2.set_xticks(xticks)
    ax2.set_xticklabels(xticklabels, fontsize=25)
    ax2.set_yticks([0, 2*np.pi, 4*np.pi])
    ax2.set_yticklabels([r'$0$', r'$2\pi$', r'$4\pi$'], fontsize=25)

    properties(
            ax=ax2,
            xlabel=r'$t^*$',
            ylabel=r'$\theta$',
            xlim=[0, 2.5],
            ylim=[-0.5*np.pi, 5.0*np.pi],
            )

    ax2.plot(theta[:, 0], theta[:, 1], color="red", label=r'$\theta$')

    """
    ax3
    """
    #ax3.grid()
    ax3.set_xticks(xticks)
    ax3.set_xticklabels(xticklabels, fontsize=25)
    properties(
            ax=ax3,
            xlabel=r'$t^*$',
            ylabel=r'$y/\ell$',
            xlim=[0, 2.5],
            ylim=[-0.05, 0.5],
            )
    ax3.plot(traj[:, 0], traj[:, 1], color="blue", ls='--', label=r'$y$')
    handler1, label1 = ax2.get_legend_handles_labels()
    handler2, label2 = ax3.get_legend_handles_labels()
    ax3.legend(handler1 + handler2, label1 + label2, loc=4, borderaxespad=0.2, fontsize=20)
    fig.savefig('papers/figure_1.png')
    fig.savefig('papers/figure_1.eps')
    plt.show()

def properties(
        ax, 
        equal_aspect=False,
        xlabel=r'$x$', ylabel=r'$y$',
        xlim=None, ylim=None,
        xticks=None, yticks=None,
        xticklabels=None, yticklabels=None):

    if equal_aspect == True: ax.set_aspect('equal')
    ax.set_xlabel(xlabel, fontsize=25)
    ax.set_ylabel(ylabel, fontsize=25)

    if xlim != None:
        ax.set_xlim(xlim)
    if ylim != None:
        ax.set_ylim(ylim)

    if xticks != None:
        ax.set_xticks(xticks)
        if xticklabels != None:
            ax.set_xticklabels(xticklabels, fontsize=25)
    if yticks != None:
        ax.set_yticks(yticks)
        if yticklabels != None:
            ax.set_yticklabels(yticklabels, fontsize=25)



if __name__ == '__main__':
    nums = [float(n) for n in sys.argv[1:]]
    main(nums)
