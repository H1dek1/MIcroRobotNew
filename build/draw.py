#!/usr/bin/env python3
import numpy as np
from tqdm import tqdm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

max_X = 4
max_Y = 2

def main():
    data = np.loadtxt("../result/result.txt", skiprows=2)

    DT = 0.01
    AbyL = 0.3
    para_abs = 130
    
    ext_x        = data[:, 0]
    ext_y        = data[:, 1]
    center_x     = data[:, 2]
    center_y     = data[:, 3]
    center_angle = data[:, 4]
    theta_1      = data[:, 5]
    theta_2      = data[:, 6]
    para_u       = data[:, 7]
    para_v       = data[:, 8]

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
    #para_u = data[:, 7] / 110 * (2*AbyL)
    #para_v = data[:, 8] / 110 * (2*AbyL)
    
    para_max = np.sqrt(para_u**2 + para_v**2).max()
    para_u = data[:, 7] / para_max * (2*AbyL)
    para_v = data[:, 8] / para_max * (2*AbyL)
    
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    matplotlibSetting(fig, axes)
    ims = []
    
    for step in tqdm(range(ext_x.size)):
    #for step in range(1):
        im_0 = axes[0].quiver(-max_X+1, -max_Y+0.5, ext_x[step], ext_y[step], color='black', angles='xy', scale_units='xy', scale=2, width=5.0e-3)

        perm1 = patches.Circle(xy=(perm1_x[step], perm1_y[step]), radius=AbyL, fc='gray', ec='gray', fill=True, zorder=2)
        im_1_patch = axes[0].add_patch(perm1)
        im_1 = axes[0].quiver(perm1_x[step], perm1_y[step], perm1_u[step], perm1_v[step], color='black', angles='xy', scale_units='xy', scale=1, pivot='mid', width=4.0e-3, zorder=3)

        perm2 = patches.Circle(xy=(perm2_x[step], perm2_y[step]), radius=AbyL, fc='gray', ec='gray', fill=True, zorder=2)
        im_2_patch = axes[0].add_patch(perm2)
        im_2 = axes[0].quiver(perm2_x[step], perm2_y[step], perm2_u[step], perm2_v[step], color='black', angles='xy', scale_units='xy', scale=1, pivot='mid', width=4.0e-3, zorder=3)

        para = patches.Circle(xy=(para_x[step], para_y[step]), radius=AbyL, fc='orange', ec='orange', fill=True, zorder=2)
        im_3_patch = axes[0].add_patch(para)
        im_3 = axes[0].quiver(para_x[step], para_y[step], para_u[step], para_v[step], color='black', angles='xy', scale_units='xy', scale=1, pivot='mid', width=4.0e-3, zorder=3)
        body1 = axes[0].plot([perm1_x[step], perm2_x[step]], [perm1_y[step], perm2_y[step]], '-', color='k', lw=4, zorder=1)
        body2 = axes[0].plot([perm2_x[step], para_x[step]], [perm2_y[step], para_y[step]], '-', color='k', lw=4, zorder=1)
        body3 = axes[0].plot([para_x[step], perm1_x[step]], [para_y[step], perm1_y[step]], '-', color='k', lw=4, zorder=1)


        #energy = axes[1].scatter3D(potential_x[step*ONE_STEP], potential_y[step*ONE_STEP], potential_val, marker='.', markersize=10, color='b')
        ims.append(
                [im_1_patch]+[im_2_patch]+[im_3_patch] \
                +[im_0]+[im_1]+[im_2]+[im_3] \
                +body1+body2+body3 \
        #        +energy
                )
    
    ani = animation.ArtistAnimation(fig, ims, interval=(DT*5)*1.0e+3)
    print('Saving animation ...')
    ani.save('../test.mp4', writer='ffmpeg')

def matplotlibSetting(fig, axes):
    axes[0].set_xlabel('$x/l$', fontsize=15)
    axes[0].set_ylabel('$y/l$', fontsize=15)
    axes[0].set_xlim(-max_X, max_X)
    axes[0].set_ylim(-max_Y, max_Y)
    axes[0].set_aspect('equal')

if __name__ == '__main__':
    main()
    print("\007")
