#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 25
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

def main():
    theta = np.loadtxt('../result/theta1out.txt')
    fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)
    #xticks = np.arange(0, 3.0, 0.5)
    #xticklabels = [str(n) for n in xticks]
    #ax.set_xticks(xticks)
    #ax.set_xticklabels(xticklabels, fontsize=25)
    ax.set_yticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
    ax.set_yticklabels([r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$'], fontsize=25)
    ax.set_xlabel(r'$t^*$')
    ax.set_ylabel(r'$\theta$')

    ax.plot(theta[:, 0]-1, theta[:, 1], color="C0", label=r'$\theta$')
    fig.savefig('temp.png')
    plt.show()

if __name__ =='__main__':
    main()
