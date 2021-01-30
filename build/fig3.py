#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.size'] = 20
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

def main():
    data = np.loadtxt("../diagonal_phases/phases_a0.4.txt", skiprows=2)
    ext_angle = data[:,6] * (np.pi/180)
    pos_x = data[:,4]
    pos_y = data[:,5]
    length = np.sqrt(pos_x **2 + pos_y **2)
    swimmer_angle = np.arctan2(pos_y, pos_x)

    fig = plt.figure(figsize=(16, 10), tight_layout=True)
    gs = fig.add_gridspec(5, 2)
    ax0 = fig.add_subplot(gs[0:2, 0])
    ax1 = fig.add_subplot(gs[0:2, 1])
    ax3 = fig.add_subplot(gs[2:5, 0])
    ax2 = fig.add_subplot(gs[2:5, 1])

    #ax2_mini = fig.add_axes([0.220, 0.41, 0.3, 0.16])
    #ax3_mini = fig.add_axes([0.695, 0.41, 0.3, 0.16])

    ax2_mini = fig.add_axes([0.035, 0.16, 0.3, 0.18])
    ax3_mini = fig.add_axes([0.517, 0.16, 0.3, 0.18])
    """
    ax0
    """
    # visual set
    ratio = 1.0
    ax0.set_xlim([-3.3, 5.0])
    ax0.set_ylim([-1.0, 2.5])
    ax0.set_xlabel(r'$x/\ell$')
    ax0.set_ylabel(r'$y/\ell$')
    ax0.set_aspect('equal')
    #ax0.axis('off')
    
    #center position and direction
    phi = np.pi/8
    center = np.array([4*np.cos(phi), 4*np.sin(phi)])
    direct = np.pi/8
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
    ax0.add_patch(perm1)
    ax0.add_patch(perm2)
    ax0.add_patch(para)
    ##vectors
    theta_1 = direct + np.pi/4
    theta_2 = direct - np.pi/3
    ax0.quiver(pos_1[0], pos_1[1], 0.08*np.cos(theta_1), 0.08*np.sin(theta_1), pivot='mid', scale=1.5, width=0.5e-2, headwidth=3.0, headlength=4, headaxislength=4, color='black', zorder=2)
    ax0.quiver(pos_2[0], pos_2[1], 0.08*np.cos(theta_2), 0.08*np.sin(theta_2), pivot='mid', scale=1.5, width=0.5e-2, headwidth=3.0, headlength=4, headaxislength=4, color='black', zorder=2)
    
    ##frames
    ax0.plot([pos_1[0], pos_2[0]], [pos_1[1], pos_2[1]], 'k-', lw=3, zorder=0)
    ax0.plot([pos_2[0], pos_3[0]], [pos_2[1], pos_3[1]], 'k-', lw=3, zorder=0)
    ax0.plot([pos_3[0], pos_1[0]], [pos_3[1], pos_1[1]], 'k-', lw=3, zorder=0)
    
    
    ext_x = -2.5
    ext_y =  0.0
    ext_u = 0.8*np.cos(np.pi/6)
    ext_v = 0.8*np.sin(np.pi/6)
    ax0.plot([ext_x, ext_x+1.2], [ext_y, ext_y], linestyle='--', color='k', lw=1, zorder=5)
    ax0.plot([ext_x, ext_x+1.2*np.cos(np.pi/6)], [ext_y, ext_y+1.2*np.sin(np.pi/6)], linestyle='--', color='k', lw=1, zorder=5)
#    ax0.quiver(ext_x, ext_y, ext_u, ext_v, pivot='mid', scale=6, width=8.0e-3, headwidth=3, headlength=5, headaxislength=4, color='black', zorder=2)
    arrow_dict4 = dict(arrowstyle = '<->, head_width=0.10, head_length=0.4', color='k', linestyle='-', shrinkA=0, shrinkB=0, lw=2.0e+0)
    ax0.annotate('',
            xy=(ext_x+ext_u/2, ext_y+ext_v/2),
            xytext=(ext_x-ext_u/2, ext_y-ext_v/2),
            arrowprops=arrow_dict4,
            color='k',
            zorder=4)
    ##measures
    R = 0.6*ratio
    arrow_dict2 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=0.25', color='k', linestyle='--', shrinkA=0, shrinkB=0)
    arrow_dict3 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=0.25', color='k', linestyle='--', shrinkA=0, shrinkB=0)
    ax0.annotate('',
            xy=(    ext_x + 1.0*np.cos(np.pi/6), ext_y + 1.0*np.sin(np.pi/6)),
            xytext=(ext_x + 1.0*np.cos(0),       ext_y + 1.0*np.sin(0)),
            arrowprops=arrow_dict3,
            color='k',
            zorder=4)
    ax0.text(ext_x-0.2, ext_y+0.4, r'$\mathbf{B}^{\rm ext}$', fontsize=20, horizontalalignment='center', verticalalignment='center')
    ax0.text(ext_x+1.6*np.cos(np.pi/12), ext_y+1.6*np.sin(np.pi/12), r'$\phi^{\rm ext}$', fontsize=20, horizontalalignment='center', verticalalignment='center')
    ax0.plot([0,  center[0]], [0, center[1]], linestyle='--', color='k', lw=1, zorder=5)
    ax0.plot([0,  2], [0, 0], linestyle='--', color='k', lw=1, zorder=5)
    ax0.annotate('',
            xy=(1.5*np.cos(phi), 1.5*np.sin(phi)),
            xytext=(1.5, 0),
            arrowprops=arrow_dict2,
            color='k',
            zorder=4)
    ax0.text(2.0*np.cos(phi/2), 2.0*np.sin(phi/2), r'$\phi^{\rm v}$', fontsize=20, horizontalalignment='center', verticalalignment='center')


    center = np.array([0, 0])
    direct = 0
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
    ax0.add_patch(perm1)
    ax0.add_patch(perm2)
    ax0.add_patch(para)
    ##vectors
    theta_1 = direct + np.pi/8
    theta_2 = direct + np.pi/8
    ax0.quiver(pos_1[0], pos_1[1], 0.08*np.cos(theta_1), 0.08*np.sin(theta_1), pivot='mid', scale=1.5, width=0.5e-2, headwidth=3.0, headlength=4, headaxislength=4, color='black', zorder=2)
    ax0.quiver(pos_2[0], pos_2[1], 0.08*np.cos(theta_2), 0.08*np.sin(theta_2), pivot='mid', scale=1.5, width=0.5e-2, headwidth=3.0, headlength=4, headaxislength=4, color='black', zorder=2)
    
    ##frames
    ax0.plot([pos_1[0], pos_2[0]], [pos_1[1], pos_2[1]], 'k-', lw=3, zorder=0)
    ax0.plot([pos_2[0], pos_3[0]], [pos_2[1], pos_3[1]], 'k-', lw=3, zorder=0)
    ax0.plot([pos_3[0], pos_1[0]], [pos_3[1], pos_1[1]], 'k-', lw=3, zorder=0)
    
    


    """
    ax1
    """
    theta = np.loadtxt('../phases/fig3_theta1out.txt')
    angle = np.loadtxt('../phases/fig3_result.txt', skiprows=2)
    ax1.set_xlabel(r'$t^*$')
    ax1.set_ylabel(r'$\phi^{\rm head}$')
    ax1.set_xlim(0, 10)
    ax1.set_ylim(-0.1, 1*np.pi/4)
    xticks = np.arange(0, 11.0, 2.0)
    xticklabels = [str(n) for n in xticks]
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(xticklabels)
    ax1.set_yticks([0, np.pi/8, np.pi/6, np.pi/4])
    ax1.set_yticklabels([r'$0$', r'$\pi/8$', r'$\phi^{\rm ext}$', r'$\pi/4$'])
    ax1.plot(theta[:, 0], angle[:, 4], color="red", label=r'$\theta$')
    ax1.hlines(np.pi/6, -1, 13, colors='k', ls='--')


    for ax in [ax2, ax3]:
        ax.set_xlabel(r'$\phi^{\rm ext}$', fontsize=20)
        ax.set_ylabel(r'$\phi^{\rm v}$', fontsize=20)
        ax.set_ylim(-np.pi-0.7, np.pi/2+0.7)
        ax.set_xticks([0, np.pi/2, np.pi])
        ax.set_xticklabels([r'$0$', r'$\pi/2$', r'$\pi$'], fontsize=20)
        ax.set_yticks([-np.pi, -np.pi/2, 0, np.pi/2])
        ax.set_yticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$'], fontsize=20)
    for ax in [ax2_mini, ax3_mini]:
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        ax.set_xticks([-1, 0, 1])
        ax.set_xticklabels([r'$-1.0$', r'$0.0$', r'$1.0$'], fontsize=15)
        ax.set_yticks([-1, 0, 1])
        ax.set_yticklabels([r'$-1.0$', r'$0.0$', r'$1.0$'], fontsize=15)
        ax.set_xlabel(r'$x/\ell$', labelpad=-3, fontsize=15)
        ax.set_ylabel(r'$y/\ell$', labelpad=-8, fontsize=15)
        ax.set_aspect('equal')
    #ax[1].quiver(np.zeros(len(ext_angle)), np.zeros(len(ext_angle)), pos_x/length, pos_y/length, angles='xy', scale_units='xy', scale=1)
    step = len(ext_angle)
    n = 50
    step /= n
    print(len(pos_x[::int(step)]))
    ax2.plot(ext_angle, swimmer_angle-np.pi/2, marker='.', color='C0')
    ax2_mini.quiver(np.zeros(n), np.zeros(n), pos_y[::int(step)]/length[::int(step)], -pos_x[::int(step)]/length[::int(step)], angles='xy', scale_units='xy', scale=1, color='C0')

    data = np.loadtxt("../diagonal_phases/phases_a0.3.txt", skiprows=2)
    ext_angle = data[:,6] * (np.pi/180)
    pos_x = data[:,4]
    pos_y = data[:,5]
    length = np.sqrt(pos_x **2 + pos_y **2)
    swimmer_angle = np.arctan2(pos_y, pos_x)
    ax3.plot(ext_angle, swimmer_angle-np.pi/2, marker='.', color='C0')
    ax3_mini.quiver(np.zeros(n), np.zeros(n), pos_y[::int(step)]/length[::int(step)], -pos_x[::int(step)]/length[::int(step)], angles='xy', scale_units='xy', scale=1, color='C0')

    fig.savefig('papers/figure_3.png')
    fig.savefig('papers/figure_3.eps')
    #plt.show()

if __name__ == '__main__':
    main()
