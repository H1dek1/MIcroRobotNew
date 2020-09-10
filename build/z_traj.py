#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.loadtxt('../result/zout.txt')

fig, ax = plt.subplots(1, 1, figsize=(6.4, 4.5))
ax.set_xlabel('$t*$')
ax.set_ylabel('$y$')
xticks = np.arange(0, 2.5, 0.5)
ax.set_xticks(xticks)
xticklabels = [str(n) for n in xticks]
ax.set_xticklabels(xticklabels, fontsize=10)
#ax.set_yticks([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
#ax.set_yticklabels(['0', '$\pi$', '$2\pi$', '$3\pi$', '$4\pi$'], fontsize=10)
ax.plot(data[:, 0], data[:, 1])
ax.grid()
fig.savefig('z_traj.png')
plt.show()
