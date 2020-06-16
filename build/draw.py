#!/usr/bin/env python3
import numpy as np
from tqdm import tqdm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

data = np.loadtxt("../result/result.txt", skiprows=2)

ext_x        = data[:, 0]
ext_y        = data[:, 1]
center_x     = data[:, 2]
center_y     = data[:, 3]
center_angle = data[:, 4]
theta_1      = data[:, 5]
theta_2      = data[:, 6]
para_norm    = data[:, 7]
para_angle   = data[:, 8]

fig, axes = plt.subplots(2, 1)
axes[0].set_xlim(-3, 3)
axes[0].set_ylim(-1, 1.5)
axes[0].set_aspect('equal')
ims = []

print(ext_x.size)
for step in tqdm(range(ext_x.size)):
    im_0 = axes[0].quiver(0, 0, ext_x[step], ext_y[step], color='black', angles='xy', scale_units='xy', scale=1, pivot='mid', width=5.0e-3)
    ims.append([im_0])

ani = animation.ArtistAnimation(fig, ims, interval=0.01*1.0e+3)
print('Saving animation ...')
ani.save('test.mp4', writer='ffmpeg')
