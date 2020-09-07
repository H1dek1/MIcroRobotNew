#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.loadtxt('../result/zout.txt')

fig, ax = plt.subplots(1, 1)
ax.set_xlabel('$t*$')
ax.set_ylabel('$y$')
ax.plot(data[:, 0], data[:, 1])
plt.show()
