import numpy as np
import matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt

class Drawer:
    def __init__(self, 
            dt,
            a,
            alpha,
            beta,
            gamma):
        self.dt = dt
        self.a = a
        self.alpha = alpha 
        self.beta = beta
        self.gamma = gamma

    def preprocess(self, data):
        self.ext_x = data[:, 0]
        self.ext_y = data[:, 1]
        self.center_x = data[:, 2]
        self.center_y = data[:, 3]
        self.center_angle = data[:, 4]
        self.theta_1 = data[:, 5]
        self.theta_2 = data[:, 6]
        self.perm1_x = self.center_x - 0.5*np.cos(self.center_angle)
        self.perm1_y = self.center_y - 0.5*np.sin(self.center_angle)
        self.perm1_u = 2 * self.a * np.cos(self.theta_1)
        self.perm1_v = 2 * self.a * np.sin(self.theta_1)
        self.perm2_x = self.center_x + 0.5*np.cos(self.center_angle)
        self.perm2_y = self.center_y + 0.5*np.sin(self.center_angle)
        self.perm2_u = 2 * self.a * np.cos(self.theta_2)
        self.perm2_v = 2 * self.a * np.sin(self.theta_2)
        self.para_x = self.center_x - 0.5*np.sqrt(3)*np.sin(self.center_angle)
        self.para_y = self.center_y + 0.5*np.sqrt(3)*np.cos(self.center_angle)
        self.para_max = np.sqrt(data[:, 7]**2 + data[:, 8]**2).max()
        self.para_u = data[:, 7] / self.para_max * (2*self.a)
        self.para_v = data[:, 8] / self.para_max * (2*self.a)


    def draw_swimmer(self, data, ax, time, label_time):
        self.preprocess(data)
        steps = int(time / self.dt)
        ax.text(self.center_x[steps]+0.4, self.para_y[steps]+0.7, 
                r'$t^*={}$'.format(label_time),
                horizontalalignment='left',
                verticalalignment='center',
                fontsize=20)

        perm1 = patches.Circle(
                xy=(self.perm1_x[steps], self.perm1_y[steps]),
                radius=self.a,
                fc='gray',
                ec='gray',
                fill=True,
                zorder=0)
        perm2 = patches.Circle(
                xy=(self.perm2_x[steps], self.perm2_y[steps]),
                radius=self.a,
                fc='gray',
                ec='gray',
                fill=True,
                zorder=0)
        para = patches.Circle(
                xy=(self.para_x[steps], self.para_y[steps]),
                radius=self.a/2,
                fc='orange',
                ec='orange',
                fill=True,
                zorder=0)
        ax.add_patch(perm1)
        ax.add_patch(perm2)
        ax.add_patch(para)
        ax.quiver(
                self.perm1_x[steps], self.perm1_y[steps],
                self.perm1_u[steps], self.perm1_v[steps],
                color='black',
                angles='xy', scale_units='xy', scale=1,
                pivot='mid',
                width=1.0e-2,
                zorder=1)
        ax.quiver(
                self.perm2_x[steps], self.perm2_y[steps],
                self.perm2_u[steps], self.perm2_v[steps],
                color='black',
                angles='xy', scale_units='xy', scale=1,
                pivot='mid',
                width=1.0e-2,
                zorder=1)
        ax.quiver(
                self.para_x[steps], self.para_y[steps],
                self.para_u[steps], self.para_v[steps],
                color='black',
                angles='xy', scale_units='xy', scale=1,
                pivot='mid',
                width=1.0e-2,
                zorder=1)
        ax.plot([self.perm1_x[steps], self.perm2_x[steps]],
                [self.perm1_y[steps], self.perm2_y[steps]],
                'k-', lw=5, zorder=2)
        ax.plot([self.perm2_x[steps], self.para_x[steps]],
                [self.perm2_y[steps], self.para_y[steps]],
                'k-', lw=5, zorder=2)
        ax.plot([self.para_x[steps], self.perm1_x[steps]],
                [self.para_y[steps], self.perm1_y[steps]],
                'k-', lw=5, zorder=2)

    def draw_ext_field(self, data, ax, time):
        steps = int(time / self.dt)
        ax.quiver(
                -1, -1,
                self.ext_x[steps], self.ext_y[steps],
                color='black',
                angles='xy', scale_units='xy', scale=2,
                width=5.0e-3)

