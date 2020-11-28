#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
# ex.) dejavusans, dejavuserif, cm, stix, stixsans, custom
plt.rcParams['font.size'] = 20
#print(plt.rcParams['mathtext.fontset'])
print(plt.rcParams['mathtext.default'])

fig, axes = plt.subplots(1, 3, figsize=(21, 6))
axes[0].set_xlabel(r'$\alpha$', fontsize=25)
axes[0].set_ylabel(r'$\beta$', fontsize=25)
axes[0].set_xscale('log')
axes[0].set_yscale('log')
axes[0].set_aspect('equal')
axes[0].set_xticks([0.1, 1, 10, 100, 1000])
#ax.set_xlim(0, 0.5)
#ax.set_ylim(0, 200)
#cm = plt.cm.get_cmap('Blues')
cm = plt.cm.get_cmap('cividis')
#-------------------
data = np.loadtxt('../phases/phases_g1.txt')
alpha = data[:,0]
beta = data[:,1]
gamma = data[:,2]

n_iter = data[:,3]
pos_x = data[:,4]
pos_y = np.round(data[:,5], decimals=4)
print(min(pos_y))
print(max(pos_y))
#-------------------
#mappable = ax.scatter(alpha, beta, c=pos_y, vmin=min(pos_y)-0.2, vmax=max(pos_y)+0.2, s=35, cmap=cm)
mappable0 = axes[0].scatter(alpha, beta, c=pos_y, vmin=min(pos_y), vmax=max(pos_y), s=35, cmap=cm)
"""
ax1
"""
axes[1].set_xlabel(r'$\alpha$', fontsize=25)
axes[1].set_ylabel(r'$\beta$', fontsize=25)
axes[1].set_xscale('log')
axes[1].set_yscale('log')
axes[1].set_aspect('equal')
axes[1].set_xticks([0.1, 1, 10, 100, 1000])
#ax.set_xlim(0, 0.5)
#ax.set_ylim(0, 200)
#cm = plt.cm.get_cmap('Blues')
cm = plt.cm.get_cmap('cividis')
#-------------------
data = np.loadtxt('../phases/phases_g1e-7.txt')
alpha = data[:,0]
beta = data[:,1]
gamma = data[:,2]

n_iter = data[:,3]
pos_x = data[:,4]
pos_y = np.round(data[:,5], decimals=4)
print(min(pos_y))
print(max(pos_y))
#-------------------
#mappable = ax.scatter(alpha, beta, c=pos_y, vmin=min(pos_y)-0.2, vmax=max(pos_y)+0.2, s=35, cmap=cm)
mappable1 = axes[1].scatter(alpha, beta, c=pos_y, vmin=min(pos_y), vmax=max(pos_y), s=35, cmap=cm)
fig.colorbar(mappable1, ax=axes[0], ticks=[0.0, 0.5, 1.0, 1.5])
fig.colorbar(mappable1, ax=axes[1], ticks=[0.0, 0.5, 1.0, 1.5])
fig.tight_layout()


"""
ax2
"""
alpha = 0.3
gamma = 0.3
def U(theta_, t_):
    return 4 - 2*(np.cos(theta_))**2 \
            + (-(4*alpha + 5*gamma)*np.cos(theta_) + 3*np.sqrt(3)*gamma*np.sin(theta_))*np.cos(2*np.pi*t_)

def dU(theta_, t_):
    return 4*np.sin(theta_)*np.cos(theta_) \
            + ( (4*alpha + 5*gamma)*np.sin(theta_) + 3*np.sqrt(3)*gamma*np.cos(theta_) ) * np.cos(2*np.pi*t_)

def pole_theta(t_, theta_0):
    # gradient descent
    epsilon = 1.0e-5
    eta = 1.0e-3
    while True:
    #for i in range(100):
        dU_dtheta = dU(theta_=theta_0, t_=t_)
        if abs(dU_dtheta) < epsilon: break
        theta_0 -= eta * dU_dtheta

    return theta_0

time = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
theta = np.arange(-np.pi, np.pi, np.pi/100)
    
axes[2].set_xlabel('$\\theta$', fontsize=20)
axes[2].set_ylabel('$U^{all*}$', fontsize=20)
axes[2].set_xlim(-np.pi, np.pi)
axes[2].set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
axes[2].set_xticklabels(['$-\\pi$', '$-\\pi/2$', '0', '$\\pi/2$', '$\\pi$'], fontsize=20)
axes[2].set_ylim(-5, 10)
y_values = [-5, 0, 5, 10]
axes[2].set_yticks(y_values)
axes[2].set_yticklabels([str(idx) for idx in y_values], fontsize=20)

i = 0
for t in time:
    print(t)
    potential = U(theta, t)
    pole = pole_theta(t, theta_0=0)
    local_min = U(pole, t)
    axes[2].plot(pole, local_min, color='C{}'.format(i), marker='.', markersize=20)
    axes[2].plot(theta, potential, color='C{}'.format(i), label='$t*={}$'.format(t))
    #ax.axvline(pole, ls='--', color='C{}'.format(i))
    print(pole)
    i += 1
axes[2].legend(fontsize=15)


#plt.subplots_adjust(left=0.12, right=1.0, bottom=0.1, top=0.9)
fig.savefig('../phases/test.eps')
fig.savefig('../phases/test.png')
plt.show()

