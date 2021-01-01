#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

def main():
    data = np.loadtxt("../diagonal_phases/phases_a0.4.txt", skiprows=2)
    ext_angle = data[:,6] * (np.pi/180)
    pos_x = data[:,4]
    pos_y = data[:,5]
    length = np.sqrt(pos_x **2 + pos_y **2)
    swimmer_angle = np.arctan2(pos_y, pos_x)

    fig, ax = plt.subplots(2, 2, figsize=(16, 9))
    mini_ax = fig.add_axes([0.2, 0.2, 0.5, 0.3])
    for i in range(2):
        ax[i, 0].set_xlabel(r'$\phi_B$', fontsize=25)
        ax[i, 0].set_ylabel(r'$\phi_S$', fontsize=25)
        ax[i, 0].set_ylim(-np.pi-0.7, np.pi/2+0.7)
        ax[i, 0].set_xticks([0, np.pi/2, np.pi])
        ax[i, 0].set_xticklabels([r'$0$', r'$\pi/2$', r'$\pi$'], fontsize=20)
        ax[i, 0].set_yticks([-np.pi, -np.pi/2, 0, np.pi/2])
        ax[i, 0].set_yticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$'], fontsize=20)
        ax[i, 1].set_xlim(-1.2, 1.2)
        ax[i, 1].set_ylim(-1.2, 1.2)
        ax[i, 1].set_xticks([-1, 0, 1])
        ax[i, 1].set_xticklabels([r'$-1.0$', r'$0.0$', r'$1.0$'], fontsize=20)
        ax[i, 1].set_yticks([-1, 0, 1])
        ax[i, 1].set_yticklabels([r'$-1.0$', r'$0.0$', r'$1.0$'], fontsize=20)
        ax[i, 1].set_xlabel(r'$x/l$', fontsize=25)
        ax[i, 1].set_ylabel(r'$y/l$', fontsize=25)
        ax[i, 1].set_aspect('equal')
    #ax[1].quiver(np.zeros(len(ext_angle)), np.zeros(len(ext_angle)), pos_x/length, pos_y/length, angles='xy', scale_units='xy', scale=1)
    step = len(ext_angle)
    n = 50
    step /= n
    print(len(pos_x[::int(step)]))
    ax[0, 0].plot(ext_angle, swimmer_angle-np.pi/2, marker='.', color='C0')
    ax[0, 1].quiver(np.zeros(n), np.zeros(n), pos_x[::int(step)]/length[::int(step)], pos_y[::int(step)]/length[::int(step)], angles='xy', scale_units='xy', scale=1, color='C0')

    data = np.loadtxt("../diagonal_phases/phases_a0.3.txt", skiprows=2)
    ext_angle = data[:,6] * (np.pi/180)
    pos_x = data[:,4]
    pos_y = data[:,5]
    length = np.sqrt(pos_x **2 + pos_y **2)
    swimmer_angle = np.arctan2(pos_y, pos_x)
    ax[1, 0].plot(ext_angle, swimmer_angle-np.pi/2, marker='.', color='C0')
    ax[1, 1].quiver(np.zeros(n), np.zeros(n), pos_x[::int(step)]/length[::int(step)], pos_y[::int(step)]/length[::int(step)], angles='xy', scale_units='xy', scale=1,color='C0')

    ax[0, 0].text(-0.5, np.pi/2+1, '(a)', fontsize=25)
    ax[0, 1].text(-1.5, 1.31, '(b)', fontsize=25)
    fig.tight_layout()
    fig.savefig('phase_diagonal.png')
    fig.savefig('phase_diagonal.eps')
    plt.show()

if __name__ == '__main__':
    main()
