#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

def main():
    data = np.loadtxt("../result/phases.txt", skiprows=2)
    ext_angle = data[:,6] * (np.pi/180)
    pos_x = data[:,4]
    pos_y = data[:,5]
    length = np.sqrt(pos_x **2 + pos_y **2)
    swimmer_angle = np.arctan2(pos_y, pos_x)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].set_xlabel(r'$\phi_B$', fontsize=25)
    ax[0].set_ylabel(r'$\phi_S$', fontsize=25)
    ax[0].set_xticks([0, np.pi/2, np.pi])
    ax[0].set_xticklabels(['$0$', r'$\pi/2$', r'$\pi$'], fontsize=25)
    ax[0].set_yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    #ax[0].set_yticklabels(['$0$', r'$\pi/2$', r'$\pi$'], fontsize=25)
    ax[0].plot(ext_angle, swimmer_angle-np.pi/2, marker='.')
    ax[1].set_xlim(-1.2, 1.2)
    ax[1].set_ylim(-1.2, 1.2)
    ax[1].set_xlabel(r'$x/l$', fontsize=25)
    ax[1].set_ylabel(r'$y/l$', fontsize=25)
    ax[1].set_aspect('equal')
    #ax[1].quiver(np.zeros(len(ext_angle)), np.zeros(len(ext_angle)), pos_x/length, pos_y/length, angles='xy', scale_units='xy', scale=1)
    step = len(ext_angle)
    n = 10
    step /= n
    print(len(pos_x[::int(step)]))
    ax[1].quiver(np.zeros(n), np.zeros(n), pos_x[::int(step)]/length[::int(step)], pos_y[::int(step)]/length[::int(step)], angles='xy', scale_units='xy', scale=1)
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
