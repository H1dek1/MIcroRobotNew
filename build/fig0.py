#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.size'] = 25
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig = plt.figure(figsize=(20, 12), tight_layout=True)
#fig.subplots_adjust(hspace=0.4, wspace=0.0)
gs = fig.add_gridspec(2, 2)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[1, 0])
ax2 = fig.add_subplot(gs[0:2, 1])

"""
ax0
"""
# visual set
ratio = 1.0
ax0.set_xlim([-0.5, 5.0])
ax0.set_ylim([-0.5, 3.0])
ax0.set_aspect('equal')
#ax0.axis('off')

#center position and direction
center = np.array([2, 1])
direct = np.pi/6
#drawing
#pos_1 = [ratio * -0.5, 0]
#pos_2 = [ratio * 0.5, 0]
#pos_3 = [0, ratio * np.sqrt(3)/2]

pos_1 = center + [-0.5*np.sin(direct),  0.5*np.cos(direct)]
pos_2 = center + [ 0.5*np.sin(direct), -0.5*np.cos(direct)]
pos_3 = center + [np.sqrt(3)/2 * np.cos(direct), np.sqrt(3)/2 * np.sin(direct)]
##particle
perm1 = patches.Circle(xy=(pos_1[0], pos_1[1]), radius=ratio * 0.3, fc='gray')
perm2 = patches.Circle(xy=(pos_2[0], pos_2[1]), radius=ratio * 0.3, fc='gray')
para = patches.Circle(xy=(pos_3[0], pos_3[1]), radius=ratio * 0.3, fc='orange')
ax0.add_patch(perm1)
ax0.add_patch(perm2)
ax0.add_patch(para)
##vectors
theta_1 = direct + np.pi/4
theta_2 = direct - np.pi/3
ax0.quiver(pos_1[0], pos_1[1], 0.15*np.cos(theta_1), 0.15*np.sin(theta_1), pivot='mid', scale=1, width=1.0e-2, headwidth=3, headlength=4, headaxislength=3, color='black', zorder=2)
ax0.quiver(pos_2[0], pos_2[1], 0.15*np.cos(theta_2), 0.15*np.sin(theta_2),   pivot='mid', scale=1, width=1.0e-2, headwidth=3, headlength=4, headaxislength=3, color='black', zorder=2)

##frames
ax0.plot([pos_1[0], pos_2[0]], [pos_1[1], pos_2[1]], 'k-', lw=3, zorder=3)
ax0.plot([pos_2[0], pos_3[0]], [pos_2[1], pos_3[1]], 'k-', lw=3, zorder=3)
ax0.plot([pos_3[0], pos_1[0]], [pos_3[1], pos_1[1]], 'k-', lw=3, zorder=3)


ax0.plot([center[0], pos_3[0]+0.8*np.cos(direct)], [center[1], pos_3[1]+0.8*np.sin(direct)], linestyle='--', color='k', lw=1, zorder=5)
ax0.plot([pos_3[0],  pos_3[0]+0.8], [pos_3[1], pos_3[1]], linestyle='--', color='k', lw=1, zorder=5)

ax0.plot([pos_1[0], pos_1[0]+0.8*np.cos(direct)],  [pos_1[1], pos_1[1]+0.8*np.sin(direct)], linestyle='--', color='k', lw=1, zorder=5)
ax0.plot([pos_1[0], pos_1[0]+0.8*np.cos(theta_1)], [pos_1[1], pos_1[1]+0.8*np.sin(theta_1)], linestyle='--', color='k', lw=1, zorder=5)

ax0.plot([pos_2[0], pos_2[0]+0.8*np.cos(direct)],  [pos_2[1], pos_2[1]+0.8*np.sin(direct)], linestyle='--', color='k', lw=1, zorder=5)
ax0.plot([pos_2[0], pos_2[0]+0.8*np.cos(theta_2)], [pos_2[1], pos_2[1]+0.8*np.sin(theta_2)], linestyle='--', color='k', lw=1, zorder=5)
##measures
R = 0.6*ratio
arrow_dict1 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=0.3', color='k', linestyle='--', shrinkA=0, shrinkB=0)
arrow_dict2 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=-0.25', color='k', linestyle='--', shrinkA=0, shrinkB=0)
arrow_dict3 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=-0.25', color='k', linestyle='--', shrinkA=0, shrinkB=0)
ax0.annotate('',
        xy=(pos_1[0] + R*np.cos(theta_1), pos_1[1] + R*np.sin(theta_1)),
        xytext=(pos_1[0] + R*np.cos(direct), pos_1[1] + R*np.sin(direct)),
        arrowprops=arrow_dict1,
        color='k',
        zorder=4)
ax0.annotate('',
        xy=(pos_2[0] + R*np.cos(theta_2), pos_2[1] + R*np.sin(theta_2)),
        xytext=(pos_2[0] + R*np.cos(direct), pos_2[1] + R*np.sin(direct)),
        arrowprops=arrow_dict2,
        color='k',
        zorder=4)
ax0.annotate('',
        xy=(pos_3[0] + R*np.cos(0), pos_3[1] + R*np.sin(0)),
        xytext=(pos_3[0] + R*np.cos(direct), pos_3[1] + R*np.sin(direct)),
        arrowprops=arrow_dict2,
        color='k',
        zorder=4)
ax0.text(pos_1[0]+1*np.cos(theta_1-np.pi/8), pos_1[1]+1*np.sin(theta_1-np.pi/8), r'$\theta_1$', fontsize=20, horizontalalignment='center', verticalalignment='center')
ax0.text(pos_2[0]+1*np.cos(theta_2+np.pi/6), pos_2[1]+1*np.sin(theta_2+np.pi/6), r'$\theta_2$', fontsize=20, horizontalalignment='center', verticalalignment='center')
ax0.text(pos_3[0]+1*np.cos(direct/2), pos_3[1]+1*np.sin(direct/2), r'$\phi^{head}$', fontsize=20, horizontalalignment='center', verticalalignment='center')
#ax.plot([0, 0], [0, np.sqrt(3)/2], ls='dashed', color='k', lw=1, zorder=4)

#ax0.plot([pos_2[0], pos_2[0]], [pos_2[1], pos_2[1]-1.2], linestyle='--', color='k', lw=1, zorder=5)
#ax0.plot([pos_1[0], pos_1[0]], [pos_1[1], pos_1[1]-1.2], linestyle='--', color='k', lw=1, zorder=5)
#ax0.plot([pos_2[0]-ratio*0.3, pos_2[0]-ratio*0.3], [pos_2[1], pos_2[1]-1.0], linestyle='--', color='k', lw=1, zorder=5)
#
#arrow_dict3 = dict(arrowstyle = '<->, head_width=0.2, head_length=0.4', connectionstyle='arc3', color='k', shrinkA=0, shrinkB=0, linestyle='--')
#
#
#ax0.annotate('',
#        xy=(pos_1[0], pos_1[1]-1.1),
#        xytext=(pos_2[0], pos_2[1]-1.1),
#        arrowprops=arrow_dict3,
#        color='k',
#        zorder=4)
#ax0.text(0, pos_1[1]-1.1, '$l$', fontsize=25, horizontalalignment='center', verticalalignment='bottom')
#ax0.annotate('',
#        xy=(pos_2[0]-ratio*0.3, pos_1[1]-0.9),
#        xytext=(pos_2[0], pos_2[1]-0.9),
#        arrowprops=arrow_dict3,
#        color='k',
#        zorder=4)
#ax0.text((2*pos_2[0]-ratio*0.3)/2, pos_2[1]-0.9, '$a$', fontsize=25, horizontalalignment='center', verticalalignment='bottom')
"""
ax1
"""

"""
ax2
"""
img = plt.imread('microrobot_real.jpeg')
ax2.imshow(img)
ax2.axis('off')
plt.show()
