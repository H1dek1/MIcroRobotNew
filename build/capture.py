#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from drawer import Drawer

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.size'] = 25

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
    fig = plt.figure(figsize=(20, 12), tight_layout=True)
    fig.subplots_adjust(hspace=0.4, wspace=0.0)
    gs = fig.add_gridspec(6, 13)
    ax0 = fig.add_subplot(gs[0:4, 0:4])
    ax01 = fig.add_subplot(gs[2:6, 0:4])
    ax1 = fig.add_subplot(gs[:, 4:7])
    ax2 = fig.add_subplot(gs[0:3, 7:13])
    ax3 = fig.add_subplot(gs[3:6, 7:13])

    #ax0 = fig.add_subplot(1, 4, 1)
    #ax1 = fig.add_subplot(1, 4, 2)
    #ax2 = fig.add_subplot(2, 2, 2)
    #ax3 = fig.add_subplot(2, 2, 4)
    #ax01.axis('off')
    """
    ax0
    """
    # visual set
    ratio = 2.0
    ax0.set_xlim([-2.0, 2.0])
    ax0.set_ylim([-2.5, 2.5])
    ax0.set_aspect('equal')
    ax0.axis('off')
    
    #drawing
    pos_1 = [ratio * -0.5, 0]
    pos_2 = [ratio * 0.5, 0]
    pos_3 = [0, ratio * np.sqrt(3)/2]
    ##particle
    perm1 = patches.Circle(xy=(pos_1[0], pos_1[1]), radius=ratio * 0.3, fc='gray')
    perm2 = patches.Circle(xy=(pos_2[0], pos_2[1]), radius=ratio * 0.3, fc='gray')
    para = patches.Circle(xy=(pos_3[0], pos_3[1]), radius=ratio * 0.3, fc='orange')
    ax0.add_patch(perm1)
    ax0.add_patch(perm2)
    ax0.add_patch(para)
    ##vectors
    ax0.quiver(pos_1[0], pos_1[1], 0.25*np.cos(3*np.pi/4), ratio*0.16*np.sin(3*np.pi/4), pivot='mid', scale=1, width=2.0e-2, headwidth=3, headlength=4, headaxislength=3, color='black', zorder=2)
    ax0.quiver(pos_2[0], pos_2[1], 0.25*np.cos(np.pi/4), ratio*0.16*np.sin(np.pi/4), pivot='mid', scale=1, width=2.0e-2, headwidth=3, headlength=4, headaxislength=3, color='black', zorder=2)
    
    ##frames
    ax0.plot([pos_1[0], pos_2[0]], [pos_1[1], pos_2[1]], 'k-', lw=5, zorder=3)
    ax0.plot([pos_2[0], pos_3[0]], [pos_2[1], pos_3[1]], 'k-', lw=5, zorder=3)
    ax0.plot([pos_3[0], pos_1[0]], [pos_3[1], pos_1[1]], 'k-', lw=5, zorder=3)
    
    ##measures
    R = 0.4*ratio
    init = 1*np.pi/5
    fini = 4*np.pi/5
    arrow_dict1 = dict(arrowstyle = '->, head_width=0.3, head_length=0.4', connectionstyle='arc3, rad=0.5', color='k')
    arrow_dict2 = dict(arrowstyle = '->, head_width=0.3, head_length=0.4', connectionstyle='arc3, rad=-0.5', color='k')
    ax0.annotate('',
            xy=(pos_1[0] + R*np.cos(np.pi/2+fini), pos_1[1] + R*np.sin(np.pi/2+fini)),
            xytext=(pos_1[0] + R*np.cos(np.pi/2+init), pos_1[1] + R*np.sin(np.pi/2+init)),
            arrowprops=arrow_dict1,
            color='k',
            zorder=4)
    ax0.annotate('',
            xy=(pos_2[0] + R*np.cos(np.pi/2-fini), pos_2[1] + R*np.sin(np.pi/2-fini)),
            xytext=(pos_2[0] + R*np.cos(np.pi/2-init), pos_1[1] + R*np.sin(np.pi/2-init)),
            arrowprops=arrow_dict2,
            color='k',
            zorder=4)
    #ax.plot([0, 0], [0, np.sqrt(3)/2], ls='dashed', color='k', lw=1, zorder=4)
    
    ax0.plot([pos_2[0], pos_2[0]], [pos_2[1], pos_2[1]-1.2], linestyle='--', color='k', lw=1, zorder=5)
    ax0.plot([pos_1[0], pos_1[0]], [pos_1[1], pos_1[1]-1.2], linestyle='--', color='k', lw=1, zorder=5)
    ax0.plot([pos_2[0]-ratio*0.3, pos_2[0]-ratio*0.3], [pos_2[1], pos_2[1]-1.0], linestyle='--', color='k', lw=1, zorder=5)
    arrow_dict3 = dict(arrowstyle = '<->, head_width=0.2, head_length=0.4', connectionstyle='arc3', color='k', shrinkA=0, shrinkB=0, linestyle='--')
    
    
    ax0.annotate('',
            xy=(pos_1[0], pos_1[1]-1.1),
            xytext=(pos_2[0], pos_2[1]-1.1),
            arrowprops=arrow_dict3,
            color='k',
            zorder=4)
    ax0.text(0, pos_1[1]-1.1, '$l$', fontsize=25, horizontalalignment='center', verticalalignment='bottom')
    ax0.annotate('',
            xy=(pos_2[0]-ratio*0.3, pos_1[1]-0.9),
            xytext=(pos_2[0], pos_2[1]-0.9),
            arrowprops=arrow_dict3,
            color='k',
            zorder=4)
    ax0.text((2*pos_2[0]-ratio*0.3)/2, pos_2[1]-0.9, '$a$', fontsize=25, horizontalalignment='center', verticalalignment='bottom')
    





    """
    ax1
    """
    ax0.text(-2.0, 2.8, 'A', fontsize=30, horizontalalignment='center')
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
    ax2.set_xticklabels(xticklabels, fontsize=25)
    ax2.set_yticks([-np.pi, 0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi, 5*np.pi])
    ax2.set_yticklabels(['$-\\pi$', '0', '$\\pi$', '$2\\pi$', '$3\\pi$', '$4\\pi$', '$5\\pi$'], fontsize=25)

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
    ax3.set_xticklabels(xticklabels, fontsize=25)
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
