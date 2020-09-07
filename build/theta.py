#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.loadtxt('../result/theta1out.txt')

fig, ax = plt.subplots(1, 1)
ax.set_xlabel('$t*$')
ax.set_ylabel('$\\theta_1$')
ax.set_yticks([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
ax.set_yticklabels(['0', '$\pi$', '$2\pi$', '$3\pi$', '$4\pi$'])
ax.plot(data[:, 0], data[:, 1])
plt.show()
