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
    data = np.loadtxt('../result/result.txt', skiprows=int(2))
    params = np.loadtxt('../result/params.txt', skiprows=1)
    theta = np.loadtxt('../result/theta1out.txt')
    traj = np.loadtxt('../result/zout.txt')
    drawer = Drawer(
            dt=params[0],
            a=params[1],
            alpha=params[2],
            beta=params[3],
            gamma=params[4])
    
    fig = plt.figure(figsize=(16, 10), tight_layout=True)
    gs = fig.add_gridspec(2, 3)
    ax0 = fig.add_subplot(gs[0, :])
    ax1 = fig.add_subplot(gs[1, 0:2])
    ax2 = fig.add_subplot(gs[1, 2])
    ax3 = ax2.twinx()
    ax4_mini = fig.add_axes([0.610, 0.32, 0.3, 0.18])
    """
    ax4_mini
    """
    ax4_mini.set_aspect('equal')
    ax4_mini.set_xlim(-0.8, 1.6)
    ax4_mini.set_ylim(-1.2, 1.2)
    ax4_mini.tick_params(labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False,
            bottom=False,
            left=False)

    center = np.array([0, 0])
    direct = 0
    ratio = 1
    #drawing
    #pos_1 = [ratio * -0.5, 0]
    #pos_2 = [ratio * 0.5, 0]
    #pos_3 = [0, ratio * np.sqrt(3)/2]
    
    pos_1 = center + [-0.5*np.sin(direct),  0.5*np.cos(direct)]
    pos_2 = center + [ 0.5*np.sin(direct), -0.5*np.cos(direct)]
    pos_3 = center + [np.sqrt(3)/2 * np.cos(direct), np.sqrt(3)/2 * np.sin(direct)]
    ##particle
    perm1 = patches.Circle(xy=(pos_1[0], pos_1[1]), radius=ratio * 0.3, fc='gray')
    perm2 = patches.Circle(xy=(pos_2[0], pos_2[1]), radius=ratio * 0.3, fc='gray')
    para = patches.Circle(xy=(pos_3[0], pos_3[1]), radius=ratio * 0.15, fc='orange')
    ax4_mini.add_patch(perm1)
    ax4_mini.add_patch(perm2)
    ax4_mini.add_patch(para)
    ##vectors
    theta_1 = direct + np.pi/5
    theta_2 = direct - np.pi/5
    abso = 0.25
    ax4_mini.quiver(pos_1[0], pos_1[1], abso*np.cos(theta_1), abso*np.sin(theta_1), pivot='mid', scale=1.0, width=2.7e-2, headwidth=3.0, headlength=4.2, headaxislength=3.6, color='black', zorder=2)
    ax4_mini.quiver(pos_2[0], pos_2[1], abso*np.cos(theta_2), abso*np.sin(theta_2), pivot='mid', scale=1.0, width=2.7e-2, headwidth=3.0, headlength=4.2, headaxislength=3.6, color='black', zorder=2)
    
    ##frames
    ax4_mini.plot([pos_1[0], pos_2[0]], [pos_1[1], pos_2[1]], 'k-', lw=3, zorder=0)
    ax4_mini.plot([pos_2[0], pos_3[0]], [pos_2[1], pos_3[1]], 'k-', lw=3, zorder=0)
    ax4_mini.plot([pos_3[0], pos_1[0]], [pos_3[1], pos_1[1]], 'k-', lw=3, zorder=0)
    
    ax4_mini.plot([pos_1[0], pos_1[0]+1], [pos_1[1], pos_1[1]], linestyle='--', color='k', lw=1, zorder=5)
    ax4_mini.plot([pos_1[0], pos_1[0]+np.cos(theta_1)], [pos_1[1], pos_1[1]+np.sin(theta_1)], linestyle='--', color='k', lw=1, zorder=5)
    arrow_dict0 = dict(arrowstyle = '->, head_width=0.15, head_length=0.3', connectionstyle='arc3, rad=0.2', color='k', linestyle='--', shrinkA=0, shrinkB=0)
    ax4_mini.annotate('',
            xy=(pos_1[0]+0.65*np.cos(theta_1), pos_1[1]+0.65*np.sin(theta_1)),
            xytext=(pos_1[0]+0.65, pos_1[1]),
            arrowprops=arrow_dict0,
            color='k',
            zorder=4)
    
    ax4_mini.plot([pos_2[0], pos_2[0]+1], [pos_2[1], pos_2[1]], linestyle='--', color='k', lw=1, zorder=5)
    ax4_mini.plot([pos_2[0], pos_2[0]+np.cos(theta_2)], [pos_2[1], pos_2[1]+np.sin(theta_2)], linestyle='--', color='k', lw=1, zorder=5)
    arrow_dict1 = dict(arrowstyle = '->, head_width=0.15, head_length=0.3', connectionstyle='arc3, rad=-0.2', color='k', linestyle='--', shrinkA=0, shrinkB=0)
    ax4_mini.annotate('',
            xy=(pos_2[0]+0.65*np.cos(theta_2), pos_2[1]+0.65*np.sin(theta_2)),
            xytext=(pos_2[0]+0.65, pos_2[1]),
            arrowprops=arrow_dict1,
            color='k',
            zorder=4)
    ax4_mini.text(pos_1[0]+0.9*np.cos(theta_1/2), pos_1[1]+0.9*np.sin(theta_1/2), r'$\theta$', fontsize=20, horizontalalignment='center', verticalalignment='center')
    ax4_mini.text(pos_2[0]+0.9*np.cos(theta_2/2), pos_2[1]+0.9*np.sin(theta_2/2), r'$\theta$', fontsize=20, horizontalalignment='center', verticalalignment='center')
    



    """
    ax0
    """
    #times = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    #times = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
    #times = np.array([0.0, 0.4, 0.45, 0.50, 0.55, 0.60])
    times = np.array([0.0, 0.4, 0.44, 0.48, 0.52, 0.56, 0.60,
        0.80, 0.84, 0.88, 0.92, 0.96, 1.00])
    positions = np.array([
        [ 0.0, 3.0], 
        [ 3.0, 3.0], 
        [ 6.0, 3.0], 
        [ 9.0, 3.0],
        [12.0, 3.0],
        [15.0, 3.0],
        [18.0, 3.0],
        #[ 0.0, 0.0], 
        [ 3.0, 0.0], 
        [ 6.0, 0.0], 
        [ 9.0, 0.0],
        [12.0, 0.0],
        [15.0, 0.0],
        [18.0, 0.0]])

    ax0.set_xlim(-1.0, 20.0)
    ax0.set_ylim(-1.5, 4.0)
    ax0.set_aspect('equal')
    #ax0.axis('off')
    ax0.tick_params(
            labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False,
            bottom=False,
            left=False)
    
    for i in range(len(times)):
        swimmer_stamps(ax=ax0, time=times[i], data=data, dt=params[0], position=positions[i])

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

    label_time = np.array([0, 20])
    for i in range(len(draw_times)):
        drawer.draw_swimmer(data=data, ax=ax1, time=draw_times[i], label_time=label_time[i])
        #drawer.draw_ext_field(data=data, ax=axes, time=0)

    ax1.set_ylim(-1, 1)
    ax1.quiver(1.5, 0, 1.3, 0, color='r', angles='xy', scale_units='xy', scale=1, 
            width=2.0e-2, headwidth=3.0, headlength=4, headaxislength=4, zorder=2)
    """
    ax2
    """
    #ax2.grid()
    xticks = np.arange(0, 3.0, 0.5)
    xticklabels = [str(n) for n in xticks]
    ax2.set_xticks(xticks)
    ax2.set_xticklabels(xticklabels, fontsize=25)
    ax2.set_yticks([0, 2*np.pi, 4*np.pi, 6*np.pi])
    ax2.set_yticklabels([r'$0$', r'$2\pi$', r'$4\pi$', r'$6\pi$'], fontsize=25)

    properties(
            ax=ax2,
            xlabel=r'$t^*$',
            ylabel=r'$\theta$',
            xlim=[0, 2.5],
            ylim=[-0.5*np.pi, 6.0*np.pi],
            )

    ax2.plot(theta[:, 0], theta[:, 1]-5*2*np.pi, color="red", label=r'$\theta$')

    """
    ax3
    """
    #ax3.grid()
    ax3.set_xticks(xticks)
    ax3.set_xticklabels(xticklabels, fontsize=25)
    properties(
            ax=ax3,
            xlabel=r'$t^*$',
            ylabel=r'$x/\ell$',
            xlim=[0, 2.5],
            ylim=[-0.05, 0.5],
            )
    ax3.plot(traj[:, 0], traj[:, 1], color="blue", ls='--', label=r'$x/\ell$')
    handler1, label1 = ax2.get_legend_handles_labels()
    handler2, label2 = ax3.get_legend_handles_labels()
    ax3.legend(handler1 + handler2, label1 + label2, loc=4, borderaxespad=0.2, fontsize=20)
    fig.savefig('papers/figure_1.png')
    fig.savefig('papers/figure_1.eps')
    #plt.show()

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

def swimmer_stamps(ax, time, data, dt, position):
    theta1 = data[int(time/dt), 5]
    theta2 = data[int(time/dt), 6]
    para_max = np.sqrt(data[:,7]**2 + data[:,8]**2).max()
    para_u = data[int(time/dt), 7] / para_max
    para_v = data[int(time/dt), 8] / para_max
    
    center = position
    perm1  = center + np.array([0, 0.5])
    perm2  = center - np.array([0, 0.5])
    para   = center + np.array([np.sqrt(3)/2, 0])
    #schemes
    ax.plot([perm1[0], perm2[0]], [perm1[1], perm2[1]], color='k', lw=3.5e+0, zorder=0)
    ax.plot([perm1[0], para[0]], [perm1[1], para[1]],   color='k', lw=3.5e+0, zorder=0)
    ax.plot([perm2[0], para[0]], [perm2[1], para[1]],   color='k', lw=3.5e+0, zorder=0)
    #particles
    circle_1 = patches.Circle(xy=perm1, radius=0.3,  fc='gray',   ec='gray',   fill=True, zorder=1)
    circle_2 = patches.Circle(xy=perm2, radius=0.3,  fc='gray',   ec='gray',   fill=True, zorder=1)
    circle_3 = patches.Circle(xy=para,  radius=0.15, fc='orange', ec='orange', fill=True, zorder=1)
    ax.add_patch(circle_1)
    ax.add_patch(circle_2)
    ax.add_patch(circle_3)
    #vector
    ax.quiver(perm1[0], perm1[1], 0.6*np.cos(theta1), 0.6*np.sin(theta1),
            color='k', angles='xy', scale_units='xy', scale=1, pivot='mid', 
            width=3.0e-3, zorder=2)
    ax.quiver(perm2[0], perm2[1], 0.6*np.cos(theta2), 0.6*np.sin(theta2),
            color='k', angles='xy', scale_units='xy', scale=1, pivot='mid', 
            width=3.0e-3, zorder=2)
    ax.quiver(para[0], para[1], 0.6*para_u, 0.6*para_v,
            color='k', angles='xy', scale_units='xy', scale=1, pivot='mid', 
            width=3.0e-3, zorder=2)
    #time
    ax.text(center[0]-0.1, center[1]-1.2, r'$t^*={}$'.format(format(time, '.2f')), horizontalalignment='left', verticalalignment='center', fontsize=20)


if __name__ == '__main__':
    nums = [float(n) for n in sys.argv[1:]]
    main(nums)
