#!/usr/bin/env python3
import time
import numpy as np
from tqdm import tqdm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

max_X = 4
max_Y = 2
ALPHA = 1.0e+2

def main(start):
    N = 200
    x1 = np.linspace(-4*np.pi, 4*np.pi, N)
    x2 = np.linspace(-4*np.pi, 4*np.pi, N)
    X1, X2 = np.meshgrid(x1, x2)

    data = np.loadtxt("../result/result.txt", skiprows=2)

    DT = 0.01
    AbyL = 0.3
    para_abs = 130
    
    ext_x         = data[:, 0]
    ext_y         = data[:, 1]
    center_x      = data[:, 2]
    center_y      = data[:, 3]
    center_angle  = data[:, 4]
    theta_1       = data[:, 5]
    theta_2       = data[:, 6]
    para_u        = data[:, 7]
    para_v        = data[:, 8]
    ext_potential = data[:, 9]

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
    
    para_max = np.sqrt(para_u**2 + para_v**2).max()
    para_u = data[:, 7] / para_max * (2*AbyL)
    para_v = data[:, 8] / para_max * (2*AbyL)
    
    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2, projection='3d')

    def ext_potential_surface(theta1, theta2, field_x, field_y):
        ext_field = np.array([field_x, field_y])
        moment_1 = np.array([-np.sin(theta1), np.cos(theta1)]).T
        moment_2 = np.array([-np.sin(-theta2), np.cos(-theta2)]).T
        potential = -2 * ALPHA * moment_1.dot(ext_field)
        potential += -2 * ALPHA * moment_2.dot(ext_field)
        return potential

    def init():
        matplotlibSetting(ax1)
        matplotlibSetting3D(ax2)
        ax1.quiver(-max_X+1, -max_Y+0.5, ext_x[0], ext_y[0], color='black', angles='xy', scale_units='xy', scale=2, width=5.0e-3)

        perm1 = patches.Circle(xy=(perm1_x[0], perm1_y[0]), radius=AbyL, fc='gray', ec='gray', fill=True, zorder=2)
        ax1.add_patch(perm1)
        ax1.quiver(perm1_x[0], perm1_y[0], perm1_u[0], perm1_v[0], color='black', angles='xy', scale_units='xy', scale=1, pivot='mid', width=4.0e-3, zorder=3)

        perm2 = patches.Circle(xy=(perm2_x[0], perm2_y[0]), radius=AbyL, fc='gray', ec='gray', fill=True, zorder=2)
        ax1.add_patch(perm2)
        ax1.quiver(perm2_x[0], perm2_y[0], perm2_u[0], perm2_v[0], color='black', angles='xy', scale_units='xy', scale=1, pivot='mid', width=4.0e-3, zorder=3)

        para = patches.Circle(xy=(para_x[0], para_y[0]), radius=AbyL, fc='orange', ec='orange', fill=True, zorder=2)
        ax1.add_patch(para)
        ax1.quiver(para_x[0], para_y[0], para_u[0], para_v[0], color='black', angles='xy', scale_units='xy', scale=1, pivot='mid', width=4.0e-3, zorder=3)
        ax1.plot([perm1_x[0], perm2_x[0]], [perm1_y[0], perm2_y[0]], '-', color='k', lw=4, zorder=1)
        ax1.plot([perm2_x[0], para_x[0]], [perm2_y[0], para_y[0]], '-', color='k', lw=4, zorder=1)
        ax1.plot([para_x[0], perm1_x[0]], [para_y[0], perm1_y[0]], '-', color='k', lw=4, zorder=1)

        Y = ext_potential_surface(X1, X2, ext_x[0], ext_y[0])
        surf = ax2.plot_surface(X1, X2, Y, cmap='gnuplot', linewidth=0, rstride=5, cstride=5, antialiased=False, zorder=1)
        ax2.plot([theta_1[0]], [-theta_2[0]], [ext_potential[0]], marker='o', color='red', markersize=15, zorder=2, alpha=0.4)


    def update(i):
        if (i+1)%10 == 0:
            elapsed_time = time.time() - start
            timebyiter = elapsed_time / i
            remaining_time = (ext_x.size - i) * timebyiter
            print('{}/{} remaining time : {}min. {}sec.'.format(i+1, ext_x.size, int(remaining_time/60), int(remaining_time%60)))
        if i != 0:
            ax1.cla()
            ax2.cla()

        matplotlibSetting(ax1)
        matplotlibSetting3D(ax2)
        ax1.quiver(-max_X+1, -max_Y+0.5, ext_x[i], ext_y[i], color='black', angles='xy', scale_units='xy', scale=2, width=5.0e-3)

        perm1 = patches.Circle(xy=(perm1_x[i], perm1_y[i]), radius=AbyL, fc='gray', ec='gray', fill=True, zorder=2)
        ax1.add_patch(perm1)
        ax1.quiver(perm1_x[i], perm1_y[i], perm1_u[i], perm1_v[i], color='black', angles='xy', scale_units='xy', scale=1, pivot='mid', width=4.0e-3, zorder=3)

        perm2 = patches.Circle(xy=(perm2_x[i], perm2_y[i]), radius=AbyL, fc='gray', ec='gray', fill=True, zorder=2)
        ax1.add_patch(perm2)
        ax1.quiver(perm2_x[i], perm2_y[i], perm2_u[i], perm2_v[i], color='black', angles='xy', scale_units='xy', scale=1, pivot='mid', width=4.0e-3, zorder=3)

        para = patches.Circle(xy=(para_x[i], para_y[i]), radius=AbyL, fc='orange', ec='orange', fill=True, zorder=2)
        ax1.add_patch(para)
        ax1.quiver(para_x[i], para_y[i], para_u[i], para_v[i], color='black', angles='xy', scale_units='xy', scale=1, pivot='mid', width=4.0e-3, zorder=3)
        ax1.plot([perm1_x[i], perm2_x[i]], [perm1_y[i], perm2_y[i]], '-', color='k', lw=4, zorder=1)
        ax1.plot([perm2_x[i], para_x[i]], [perm2_y[i], para_y[i]], '-', color='k', lw=4, zorder=1)
        ax1.plot([para_x[i], perm1_x[i]], [para_y[i], perm1_y[i]], '-', color='k', lw=4, zorder=1)


        Y = ext_potential_surface(X1, X2, ext_x[i], ext_y[i])
        surf = ax2.plot_surface(X1, X2, Y, cmap='gnuplot', linewidth=0, rstride=5, cstride=5, antialiased=False, zorder=1, alpha=0.4)
        ax2.plot([theta_1[i]], [-theta_2[i]], [ext_potential[i]], marker='o', color='red', markersize=15, zorder=2)
        if (i+1)%10 == 0:
            print(theta_1[i], theta_2[i])

    
    ani = animation.FuncAnimation(fig, update, init_func=init, interval=(DT*5)*1.0e+3, frames=ext_x.size)
    print('Drawing ...')
    ani.save('../test.mp4', writer='ffmpeg')

def matplotlibSetting(ax):
    ax.set_xlabel('$x/l$', fontsize=15)
    ax.set_ylabel('$y/l$', fontsize=15)
    ax.set_xlim(-max_X, max_X)
    ax.set_ylim(-max_Y, max_Y)
    ax.set_aspect('equal')

def matplotlibSetting3D(ax):
    ax.set_xlim(-4*np.pi, 4*np.pi)
    ax.set_ylim(-4*np.pi, 4*np.pi)
    ax.set_zlim(-400, 400)
    ax.set_xlabel('$\\theta_1$')
    ax.set_ylabel('$\\theta_2$')
    ax.view_init(elev=80, azim=-45)
    

if __name__ == '__main__':
    start = time.time()
    main(start)
    #print("\007")
