#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.size'] = 25
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

fig = plt.figure(figsize=(15, 9), tight_layout=True)
#fig.subplots_adjust(hspace=0.4, wspace=0.0)
gs = fig.add_gridspec(2, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax3 = fig.add_subplot(gs[0, 1])
ax0 = fig.add_subplot(gs[1, 0])
ax2 = fig.add_subplot(gs[1, 1])

"""
ax0
"""
# visual set
ratio = 1.0
ax0.set_xlim([-2.5, 4.5])
ax0.set_ylim([-0.7, 2.5])
ax0.set_xlabel(r'$x/l$')
ax0.set_ylabel(r'$y/l$')
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
ax0.quiver(pos_1[0], pos_1[1], 0.12*np.cos(theta_1), 0.12*np.sin(theta_1), pivot='mid', scale=1.5, width=0.7e-2, headwidth=3, headlength=5, headaxislength=4, color='black', zorder=2)
ax0.quiver(pos_2[0], pos_2[1], 0.12*np.cos(theta_2), 0.12*np.sin(theta_2), pivot='mid', scale=1.5, width=0.7e-2, headwidth=3, headlength=5, headaxislength=4, color='black', zorder=2)

##frames
ax0.plot([pos_1[0], pos_2[0]], [pos_1[1], pos_2[1]], 'k-', lw=3, zorder=3)
ax0.plot([pos_2[0], pos_3[0]], [pos_2[1], pos_3[1]], 'k-', lw=3, zorder=3)
ax0.plot([pos_3[0], pos_1[0]], [pos_3[1], pos_1[1]], 'k-', lw=3, zorder=3)


ax0.plot([center[0],  center[0]+1.6*np.cos(direct)], [center[1], center[1]+1.6*np.sin(direct)], linestyle='--', color='k', lw=1, zorder=5)
ax0.plot([center[0],  center[0]+1.6],                [center[1], center[1]], linestyle='--', color='k', lw=1, zorder=5)

ax0.plot([pos_1[0], pos_1[0]+0.8*np.cos(direct)],  [pos_1[1], pos_1[1]+0.8*np.sin(direct)], linestyle='--', color='k', lw=1, zorder=5)
ax0.plot([pos_1[0], pos_1[0]+0.8*np.cos(theta_1)], [pos_1[1], pos_1[1]+0.8*np.sin(theta_1)], linestyle='--', color='k', lw=1, zorder=5)

ax0.plot([pos_2[0], pos_2[0]+0.8*np.cos(direct)],  [pos_2[1], pos_2[1]+0.8*np.sin(direct)], linestyle='--', color='k', lw=1, zorder=5)
ax0.plot([pos_2[0], pos_2[0]+0.8*np.cos(theta_2)], [pos_2[1], pos_2[1]+0.8*np.sin(theta_2)], linestyle='--', color='k', lw=1, zorder=5)

ext_x = -1.5
ext_y =  0.0
ext_u = 0.8*np.cos(np.pi/6)
ext_v = 0.8*np.sin(np.pi/6)
ax0.plot([ext_x, ext_x+1.0], [ext_y, ext_y], linestyle='--', color='k', lw=1, zorder=5)
ax0.plot([ext_x, ext_x+1.0*np.cos(np.pi/6)], [ext_y, ext_y+1.0*np.sin(np.pi/6)], linestyle='--', color='k', lw=1, zorder=5)
ax0.quiver(ext_x, ext_y, ext_u, ext_v, pivot='mid', scale=5, width=1.0e-2, headwidth=3, headlength=5, headaxislength=4, color='black', zorder=2)
##measures
R = 0.6*ratio
arrow_dict0 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=0.3', color='k', linestyle='--', shrinkA=0, shrinkB=0)
arrow_dict1 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=0.3', color='k', linestyle='--', shrinkA=0, shrinkB=0)
arrow_dict2 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=-0.25', color='k', linestyle='--', shrinkA=0, shrinkB=0)
arrow_dict3 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=0.25', color='k', linestyle='--', shrinkA=0, shrinkB=0)
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
        xy=(    center[0] + 1.4*np.cos(direct), center[1] + 1.4*np.sin(direct)),
        xytext=(center[0] + 1.4*np.cos(0),      center[1] + 1.4*np.sin(0)),
        arrowprops=arrow_dict3,
        color='k',
        zorder=4)
ax0.annotate('',
        xy=(    ext_x + 0.8*np.cos(np.pi/6), ext_y + 0.8*np.sin(np.pi/6)),
        xytext=(ext_x + 0.8*np.cos(0),       ext_y + 0.8*np.sin(0)),
        arrowprops=arrow_dict3,
        color='k',
        zorder=4)
ax0.text(ext_x-0.2, ext_y+0.4, r'$\mathbf{B}^{ext}$', fontsize=20, horizontalalignment='center', verticalalignment='center')
ax0.text(ext_x+1.2*np.cos(np.pi/12), ext_y+1.2*np.sin(np.pi/12), r'$\phi^{ext}$', fontsize=20, horizontalalignment='center', verticalalignment='center')
ax0.text(pos_1[0]+0.9*np.cos(theta_1-np.pi/8), pos_1[1]+0.9*np.sin(theta_1-np.pi/8), r'$\theta_1$', fontsize=20, horizontalalignment='center', verticalalignment='center')
ax0.text(pos_2[0]+0.9*np.cos(theta_2+np.pi/6), pos_2[1]+0.9*np.sin(theta_2+np.pi/6), r'$\theta_2$', fontsize=20, horizontalalignment='center', verticalalignment='center')
ax0.text(center[0]+1.9*np.cos(direct/2), center[1]+1.9*np.sin(direct/2), r'$\phi^{head}$', fontsize=20, horizontalalignment='center', verticalalignment='center')


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
LX = 2.0
LY = 1.0
gridwidth = 0.1
ratio = 1.0
ax1.set_xlabel(r'$x/l$')
ax1.set_ylabel(r'$y/l$')
ax1.set_xlim([-LX, LX])
ax1.set_ylim([-LY, LY])
ax1.set_aspect('equal')
#ax1.axis('off')
#ax1.xaxis.set_visible(False)

ax1.set_yticks([-1, 0, 1])
pos_1 = [ratio * -0.5, 0]
pos_2 = [ratio * 0.5, 0]
perm1 = patches.Circle(xy=(pos_1[0], pos_1[1]), radius=ratio * 0.3, ls='-', ec='gray', fc='gray', fill=True)
perm2 = patches.Circle(xy=(pos_2[0], pos_2[1]), radius=ratio * 0.3, ls='-', ec='gray', fc='gray', fill=True)
ax1.add_patch(perm1)
ax1.add_patch(perm2)
x_arr = np.arange(-LX, LX, gridwidth)
y_arr = np.arange(-LY, LY, gridwidth)
X, Y = np.meshgrid(x_arr, y_arr)
U = np.zeros((len(y_arr), len(x_arr)))
V = np.zeros((len(y_arr), len(x_arr)))
for i in range(len(y_arr)):
    for j in range(len(x_arr)):
        R1_x = X[i][j] - pos_1[0]
        R1_y = Y[i][j] - pos_1[1]
        R2_x = X[i][j] - pos_2[0]
        R2_y = Y[i][j] - pos_2[1]
        R1 = np.sqrt(R1_x**2 + R1_y**2)
        R2 = np.sqrt(R2_x**2 + R2_y**2)
        T_1 =  0.03
        T_2 = -0.03
        U[i][j] = 0.0
        V[i][j] = 0.0
        if R1 > 0.3*ratio:
            U[i][j] += -R1_y / (R1**3) * T_1
            V[i][j] +=  R1_x / (R1**3) * T_1

        if R2 > 0.3*ratio:
            U[i][j] += -R2_y / (R2**3) * T_2
            V[i][j] +=  R2_x / (R2**3) * T_2
        U[i][j] *= ratio
        V[i][j] *= ratio


ax1.quiver(X, Y, U, V, color='C0', angles='xy', scale_units='xy', scale=1.0)
ax1.quiver(pos_1[0], pos_1[1], 0., 0.8, color='red', angles='xy', scale_units='xy', scale=1.0, zorder=2)
ax1.quiver(pos_2[0], pos_2[1], 0., 0.8, color='red', angles='xy', scale_units='xy', scale=1.0, zorder=2)


"""
ax2
"""
img = plt.imread('microrobot_real.jpeg')
ax2.imshow(img)
ax2.axis('off')

"""
ax3
"""
width = 535
height = 332
origin_x = width/2
origin_y = height/2
ax3.set_xlim(origin_x-400, origin_x+400)
ax3.set_ylim(origin_y+200, origin_y-250)
ax3.set_aspect('equal')
img3 = plt.imread('chlamidomonas2.jpg')
ax3.imshow(img3, zorder=0)
#ax3.axis('off')

center_x = origin_x
center_y = origin_y + 80
body = patches.Circle(xy=(center_x, center_y), radius=40, fc='black', fill=True, zorder=1)
left_hand  = patches.Circle(xy=(center_x-200, 10), radius=15, fc='black', fill=True, zorder=1)
right_hand = patches.Circle(xy=(center_x+200, 10), radius=15, fc='black', fill=True, zorder=1)

RADI = 80
circle_x = 110 + RADI*np.cos(3*np.pi/8)
circle_y = 6   + RADI*np.sin(3*np.pi/8)
#left_circle  = patches.Circle(xy=(origin_x-circle_x, circle_y), radius=RADI, ec='black', fill=False, zorder=1)
#right_circle = patches.Circle(xy=(origin_x+circle_x, circle_y), radius=RADI, ec='black', fill=False, zorder=1)
left_circle  = patches.Circle(xy=(center_x-250*np.cos(np.pi/3), center_y-250*np.sin(np.pi/3)), radius=RADI, ec='black', fill=False, zorder=1)
right_circle = patches.Circle(xy=(center_x+250*np.cos(np.pi/3), center_y-250*np.sin(np.pi/3)), radius=RADI, ec='black', fill=False, zorder=1)
ax3.add_patch(body)
ax3.add_patch(left_hand)
ax3.add_patch(right_hand)
ax3.add_patch(left_circle)
ax3.add_patch(right_circle)
ax3.plot([center_x-250*np.cos(np.pi/3), center_x+250*np.cos(np.pi/3)], [center_y-250*np.sin(np.pi/3), center_y-250*np.sin(np.pi/3)], lw=1.5, color='black')
ax3.plot([center_x-250*np.cos(np.pi/3), center_x                    ], [center_y-250*np.sin(np.pi/3), center_y                    ], lw=1.5, color='black')
ax3.plot([center_x                    , center_x+250*np.cos(np.pi/3)], [center_y                    , center_y-250*np.sin(np.pi/3)], lw=1.5, color='black')

plt.show()
fig.savefig('papers/figure_0.png')
fig.savefig('papers/figure_0.eps')
