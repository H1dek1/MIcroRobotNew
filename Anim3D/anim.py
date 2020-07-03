#!/usr/bin/env python3
import numpy as np
from tqdm import tqdm
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

ALPHA = 1.0e+2
GAMMA = 1.0e-1

def main():
    N = 100
    center_angle = np.pi/2
    x1 = np.linspace(-2*np.pi, 2*np.pi, N)
    x2 = np.linspace(-2*np.pi, 2*np.pi, N)
    phi = np.linspace(0, 4*np.pi, 100)
    ext_y = np.cos(phi)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("Surface Plot")
    X1, X2 = np.meshgrid(x1, x2)
    Y_plot = ext_potential(X1, X2, 0, 1)
    surf = ax.plot_surface(X1-np.pi/2, X2-np.pi/2, Y_plot, cmap='binary', linewidth=0)
    fig.colorbar(surf)
    plt.show()
    #ims = []

    #for step in tqdm(range(ext_y.size)):
    #    Y_plot = ext_potential(X1, X2, 0, ext_y[step])
    #    surf = ax.plot_surface(X1-np.pi/2, X2-np.pi/2, Y_plot, cmap='binary', linewidth=0)
    #    #a = fig.colorbar(surf)
    #    ims.append(surf)
    ##fig.savefig('image.png')
    #ani = animation.ArtistAnimation(fig, ims, interval=100)
    #ani.save('anim.mp4', writer='ffmpeg')

def ext_potential(theta1, theta2, ext_x, ext_y):
    ext_field = np.array([ext_x, ext_y])
    moment_1 = np.array([np.cos(theta1), np.sin(theta1)]).T
    moment_2 = np.array([np.cos(theta2), np.sin(theta2)]).T
    potential = -2 * ALPHA * moment_1.dot(ext_field)
    potential += -2 * ALPHA * moment_2.dot(ext_field)
    return potential


if __name__ == '__main__':
    main()
