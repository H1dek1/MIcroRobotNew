#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
# ex.) dejavusans, dejavuserif, cm, stix, stixsans, custom
plt.rcParams['font.size'] = 20
#print(plt.rcParams['mathtext.fontset'])
print(plt.rcParams['mathtext.default'])

fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)
ax.set_xlabel(r'$\alpha$', fontsize=25)
ax.set_ylabel(r'$\beta$', fontsize=25)
ax.set_xscale('log')
ax.set_yscale('log')
cm = plt.cm.get_cmap('Blues')
#-------------------
data = np.loadtxt('../phases/phases_gamma0.1.txt')
alpha = data[:,0]
beta = data[:,1]
gamma = data[:,2]
n_iter = data[:,3]
pos_x = data[:,4]
pos_y = np.round(data[:,5], decimals=4)
print(min(pos_y))
print(max(pos_y))
#-------------------
#for i in range(len(pos_y)):
#    if pos_y[i] == 0.0:
#        mappable = ax.scatter(alpha[i], beta[i], c='lightgray', s=35)
#    else:
#        mappable = ax.scatter(alpha[i], beta[i], c=pos_y[i], vmin=min(pos_y)-0.2, vmax=max(pos_y)+0.0, s=35, cmap=cm)

mappable = ax.scatter(alpha, beta, c=pos_y, vmin=min(pos_y)-0.2, vmax=max(pos_y)+0.2, s=35, cmap=cm)
fig.colorbar(mappable, ax=ax)
plt.subplots_adjust(left=0.12, right=1.0, bottom=0.1, top=0.9)
fig.savefig('../phases/phase.eps')
fig.savefig('../phases/phase.png')
plt.show()
