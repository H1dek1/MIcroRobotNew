#!/usr/bin/env python3
import numpy as np
from tqdm import tqdm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

def main():
    data = np.loadtxt("../result/result.txt", skiprows=2)
    DT = 0.01
    AbyL = 0.3
    
    ext_x        = data[:, 0]
    ext_y        = data[:, 1]
    center_x     = data[:, 2]
    center_y     = data[:, 3]
    center_angle = data[:, 4]
    theta_1      = data[:, 5]
    theta_2      = data[:, 6]

    perm1_x = center_x - 0.5*np.cos(center_angle)
    perm1_y = center_y - 0.5*np.sin(center_angle)
    perm1_u = 2 * AbyL * np.cos(theta_1)
    perm1_v = 2 * AbyL * np.sin(theta_1)

    perm2_x = center_x + 0.5*np.cos(center_angle)
    perm2_y = center_y + 0.5*np.sin(center_angle)
    perm2_u = 2 * AbyL * np.cos(theta_2)
    perm2_v = 2 * AbyL * np.sin(theta_2)

    para_x = center_x - 0.5*np.sqrt(3)*np.sin(center_angle)
    para_y = center_y + 0.5*np.sqrt(3)*np.cos(center_angle)
    para_u = data[:, 7] / 10 * (2*AbyL)
    para_v = data[:, 8] / 10 * (2*AbyL)
    
    fig, axes = plt.subplots(1, 2, figsize=(10, 8))
    matplotlibSetting(fig, axes)
    ims = []
    
    for step in tqdm(range(ext_x.size)):
        im_0 = axes[0].quiver(-2, -0.5, ext_x[step], ext_y[step], color='black', angles='xy', scale_units='xy', scale=2, width=5.0e-3)

        perm1 = patches.Circle(xy=(perm1_x[step], perm1_y[step]), radius=AbyL, fc='gray', ec='gray', fill=False)
        im_1_patch = axes[0].add_patch(perm1)
        im_1 = axes[0].quiver(perm1_x[step], perm1_y[step], perm1_u[step], perm1_v[step], color='gray', angles='xy', scale_units='xy', scale=1, pivot='mid', width=5.0e-3)

        perm2 = patches.Circle(xy=(perm2_x[step], perm2_y[step]), radius=AbyL, fc='gray', ec='gray', fill=False)
        im_2_patch = axes[0].add_patch(perm2)
        im_2 = axes[0].quiver(perm2_x[step], perm2_y[step], perm2_u[step], perm2_v[step], color='gray', angles='xy', scale_units='xy', scale=1, pivot='mid', width=5.0e-3)

        para = patches.Circle(xy=(para_x[step], para_y[step]), radius=AbyL, fc='orange', ec='orange', fill=False)
        im_3_patch = axes[0].add_patch(para)
        im_3 = axes[0].quiver(para_x[step], para_y[step], para_u[step], para_v[step], color='orange', angles='xy', scale_units='xy', scale=1, pivot='mid', width=5.0e-3)
        ims.append(
                [im_1_patch]+[im_2_patch]+[im_3_patch] \
                +[im_0]+[im_1]+[im_2]+[im_3] \
                )
    
    ani = animation.ArtistAnimation(fig, ims, interval=(DT*5)*1.0e+3)
    print('Saving animation ...')
    ani.save('../test.mp4', writer='ffmpeg')

def matplotlibSetting(fig, axes):
    axes[0].set_xlabel('$x/l$', fontsize=15)
    axes[0].set_ylabel('$y/l$', fontsize=15)
    axes[0].set_xlim(-3, 3)
    axes[0].set_ylim(-1, 4)
    axes[0].set_aspect('equal')

if __name__ == '__main__':
    main()
