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
    #x1 = np.linspace(-4*np.pi, 4*np.pi, N)
    #x2 = np.linspace(-4*np.pi, 4*np.pi, N)
    #X1, X2 = np.meshgrid(x1, x2)

    data = np.loadtxt("../result/result.txt", skiprows=2)

    DT = 0.01
    AbyL = 0.3
    para_abs = 130
    
    #for ax1
    ext_x         = data[:, 0]
    ext_y         = data[:, 1]
    center_x      = data[:, 2]
    center_y      = data[:, 3]
    center_angle  = data[:, 4]
    theta_1       = data[:, 5]
    theta_2       = data[:, 6]
    para_u        = data[:, 7]
    para_v        = data[:, 8]

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


    #for ax2
    all_potential = data[:, 9]
    theta1_rel =   theta_1 - center_angle - np.pi/2
    theta2_rel = -(theta_2 - center_angle - np.pi/2)
    
    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2, projection='3d')

    def ext_potential_surface(theta1, theta2, field_x, field_y):
        ext_field = np.array([field_x, field_y])
        moment_1 = np.array([np.cos(theta1), np.sin(theta1)]).T
        moment_2 = np.array([np.cos(theta2), np.sin(theta2)]).T
        potential = -2 * ALPHA * moment_1.dot(ext_field)
        potential += -2 * ALPHA * moment_2.dot(ext_field)
        return potential

    def dipole_potential_surface(theta1, theta2, center_angle):
        return 3*np.cos((theta1+theta2)-2*center_angle) - np.cos(theta1-theta2)

    def para_ext_potential(theta1, theta2, center_angle, field_x, field_y):
        para_moment = GAMMA * np.array([field_x, field_y])
        moment = []
        moment.append(np.array([-np.sin(theta1), np.cos(theta1)]).T)
        moment.append(np.array([-np.sin(-theta2), np.cos(-theta2)]).T)
        #1 -> para
        unit_vec1 = np.array([
            np.cos(np.pi/3+center_angle),
            np.sin(np.pi/3+center_angle)
            ])
        


    def all_potential_surface(theta1, theta2, center_angle, field_x, field_y):
        all_potential = ext_potential_surface(theta1, theta2, field_x, field_y)
        all_potential += dipole_potential_surface(theta1, theta2, center_angle)
        #all_potential += para_ext_potential(theta1, theta2, center_angle, field_x, field_y)
        #all_potential += para_dipole_potential(theta1, theta2)

        return all_potential

    def init():
        """
        theta1 & theta2 range
        """
        x1 = np.linspace(-4*np.pi, 4*np.pi, N)
        x2 = np.linspace(-4*np.pi, 4*np.pi, N)
        X1, X2 = np.meshgrid(x1, x2)

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

        Y = all_potential_surface((X1+center_angle[0]+np.pi/2), (-X2+center_angle[0]+np.pi/2), center_angle[0], ext_x[0], ext_y[0])
        surf = ax2.plot_surface(X1, X2, Y, cmap='gnuplot', linewidth=0, rstride=5, cstride=5, antialiased=True, zorder=1)
        ax2.plot([theta1_rel[0]], [theta2_rel[0]], [all_potential[0]], marker='o', color='red', markersize=5, zorder=2, alpha=0.5)
        print(theta_1[0])
        print(theta_2[0])
        print(theta1_rel[0])
        print(theta2_rel[0])


    def update(i):
        """
        theta1 & theta2 range
        """
        x1 = np.linspace(-4*np.pi, 4*np.pi, N)
        x2 = np.linspace(-4*np.pi, 4*np.pi, N)
        X1, X2 = np.meshgrid(x1, x2)

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


        Y = all_potential_surface((X1+center_angle[0]+np.pi/2), (-X2+center_angle[0]+np.pi/2), center_angle[0], ext_x[i], ext_y[i])
        surf = ax2.plot_surface(X1, X2, Y, cmap='gnuplot', linewidth=0, rstride=5, cstride=5, antialiased=True, zorder=1, alpha=0.5)
        ax2.plot([theta1_rel[i]], [theta2_rel[i]], [all_potential[i]], marker='o', color='red', markersize=5, zorder=2)

    
    ani = animation.FuncAnimation(fig, update, init_func=init, interval=(DT*5)*1.0e+3, frames=ext_x.size)
    print('Drawing ...')
    ani.save('../test2.mp4', writer='ffmpeg')

def matplotlibSetting(ax):
    ax.set_xlabel('$x/l$', fontsize=15)
    ax.set_ylabel('$y/l$', fontsize=15)
    ax.set_xlim(-max_X, max_X)
    ax.set_ylim(-max_Y, max_Y)
    ax.set_aspect('equal')

def matplotlibSetting3D(ax):
    ax.set_xlim(-4*np.pi, 4*np.pi)
    ax.set_ylim(-4*np.pi, 4*np.pi)
    ax.set_zlim(-800, 800)
    ax.set_zticks([-800, -400, 0, 400, 800])
    ax.set_xlabel('$\\theta_1$')
    ax.set_ylabel('$\\theta_2$')
    ax.view_init(elev=80, azim=-45)
    

if __name__ == '__main__':
    start = time.time()
    main(start)
    #print("\007")
