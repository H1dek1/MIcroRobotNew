#!/usr/bin/env python3
import time
import numpy as np
from tqdm import tqdm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

ALPHA = 1.0e+2
GAMMA = 1.0e-1
N = 200
center_angle = np.pi/2

x1 = np.linspace(-4*np.pi, 4*np.pi, N)
x2 = np.linspace(-4*np.pi, 4*np.pi, N)
x1 -= np.pi/2
x2 -= np.pi/2
X1, X2 = np.meshgrid(x1, x2)
phi = np.arange(0, 4*np.pi, np.pi/10)
Bext_y = np.cos(phi)

fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(2, 1, 1, projection='3d')
ax2 = fig.add_subplot(2, 1, 2)

def ext_potential(theta1, theta2, ext_x, ext_y):
    ext_field = np.array([ext_x, ext_y])
    moment_1 = np.array([np.cos(theta1), np.sin(theta1)]).T
    moment_2 = np.array([np.cos(theta2), np.sin(theta2)]).T
    potential = -2 * ALPHA * moment_1.dot(ext_field)
    potential += -2 * ALPHA * moment_2.dot(ext_field)
    return potential

def init():
    ax1.set_zlim(-400, 400)
    ax1.set_xlabel("$\\theta_1$")
    ax1.set_ylabel("$\\theta_2$")
    ax1.view_init(elev=60, azim=-45)
    Y = ext_potential(X1, X2, 0, Bext_y[0])
    surf = ax1.plot_surface(X1, X2, Y, cmap='plasma', linewidth=0, rstride=1, cstride=1, antialiased=False)
    #fig.colorbar(surf)

start = time.time()
def update(i):
    if (i+1)%5 == 0:
        elapsed_time = time.time() - start
        timebyiter = elapsed_time / i
        remaining_time = (Bext_y.size - i) * timebyiter
        print("{}/{} remaining time : {}m {}s".format(i+1, Bext_y.size, int(remaining_time/60), int(remaining_time%60)))
    if i != 0:
        ax1.cla()
        ax2.cla()

    ax1.set_zlim(-400, 400)
    ax1.set_xlabel("$\\theta_1$")
    ax1.set_ylabel("$\\theta_2$")
    ax1.view_init(elev=60, azim=-45)
    Y = ext_potential(X1, X2, 0, Bext_y[i])
    surf = ax1.plot_surface(X1, X2, Y, cmap='plasma', linewidth=0, rstride=1, cstride=1, antialiased=False)

ani = animation.FuncAnimation(fig, update, init_func=init, interval=100, frames=Bext_y.size)
ani.save('rough2.mp4', writer='ffmpeg')

