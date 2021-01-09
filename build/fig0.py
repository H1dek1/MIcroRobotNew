#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import scipy
from scipy import ndimage

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 25
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['text.latex.preamble']=[r'\usepackage{amsmath}']

fig = plt.figure(figsize=(13, 9), tight_layout=True)
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
ax0.set_xlim([-2.0, 4.5])
ax0.set_ylim([-0.7, 2.5])
ax0.set_xlabel(r'$x/\ell$')
ax0.set_ylabel(r'$y/\ell$')
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
para = patches.Circle(xy=(pos_3[0], pos_3[1]), radius=ratio * 0.15, fc='orange')
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

#ax0.plot([pos_1[0], pos_1[0]+0.8*np.cos(direct)],  [pos_1[1], pos_1[1]+0.8*np.sin(direct)], linestyle='--', color='k', lw=1, zorder=5)
#ax0.plot([pos_1[0], pos_1[0]+0.8*np.cos(theta_1)], [pos_1[1], pos_1[1]+0.8*np.sin(theta_1)], linestyle='--', color='k', lw=1, zorder=5)
#
#ax0.plot([pos_2[0], pos_2[0]+0.8*np.cos(direct)],  [pos_2[1], pos_2[1]+0.8*np.sin(direct)], linestyle='--', color='k', lw=1, zorder=5)
#ax0.plot([pos_2[0], pos_2[0]+0.8*np.cos(theta_2)], [pos_2[1], pos_2[1]+0.8*np.sin(theta_2)], linestyle='--', color='k', lw=1, zorder=5)

ext_x = -1.0
ext_y =  0.0
ext_u = 0.8*np.cos(np.pi/6)
ext_v = 0.8*np.sin(np.pi/6)
ax0.plot([ext_x, ext_x+1.0], [ext_y, ext_y], linestyle='--', color='k', lw=1, zorder=5)
ax0.plot([ext_x, ext_x+1.0*np.cos(np.pi/6)], [ext_y, ext_y+1.0*np.sin(np.pi/6)], linestyle='--', color='k', lw=1, zorder=5)
#ax0.quiver(ext_x, ext_y, ext_u, ext_v, pivot='mid', scale=5, width=1.0e-2, headwidth=3, headlength=5, headaxislength=4, color='black', zorder=2)
arrow_dict4 = dict(arrowstyle = '<->, head_width=0.10, head_length=0.4', color='k', linestyle='-', shrinkA=0, shrinkB=0, lw=2.0e+0)
ax0.annotate('',
        xy=(ext_x+ext_u/2, ext_y+ext_v/2),
        xytext=(ext_x-ext_u/2, ext_y-ext_v/2),
        arrowprops=arrow_dict4,
        color='k',
        zorder=4)
##measures
R = 0.6*ratio
arrow_dict0 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=0.3', color='k', linestyle='--', shrinkA=0, shrinkB=0)
arrow_dict1 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=0.3', color='k', linestyle='--', shrinkA=0, shrinkB=0)
arrow_dict2 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=-0.25', color='k', linestyle='--', shrinkA=0, shrinkB=0)
arrow_dict3 = dict(arrowstyle = '->, head_width=0.2, head_length=0.3', connectionstyle='arc3, rad=0.25', color='k', linestyle='--', shrinkA=0, shrinkB=0)
#ax0.annotate('',
#        xy=(pos_1[0] + R*np.cos(theta_1), pos_1[1] + R*np.sin(theta_1)),
#        xytext=(pos_1[0] + R*np.cos(direct), pos_1[1] + R*np.sin(direct)),
#        arrowprops=arrow_dict1,
#        color='k',
#        zorder=4)
#ax0.annotate('',
#        xy=(pos_2[0] + R*np.cos(theta_2), pos_2[1] + R*np.sin(theta_2)),
#        xytext=(pos_2[0] + R*np.cos(direct), pos_2[1] + R*np.sin(direct)),
#        arrowprops=arrow_dict2,
#        color='k',
#        zorder=4)
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
ax0.text(ext_x-0.2, ext_y+0.4, r'$B^{\rm ext}$', fontsize=20, horizontalalignment='left', verticalalignment='top')
ax0.text(ext_x+1.2*np.cos(np.pi/12), ext_y+1.2*np.sin(np.pi/12), r'$\phi^{\rm ext}$', fontsize=20, horizontalalignment='center', verticalalignment='center')
#ax0.text(pos_1[0]+0.9*np.cos(theta_1-np.pi/8), pos_1[1]+0.9*np.sin(theta_1-np.pi/8), r'$\theta_1$', fontsize=20, horizontalalignment='center', verticalalignment='center')
#ax0.text(pos_2[0]+0.9*np.cos(theta_2+np.pi/6), pos_2[1]+0.9*np.sin(theta_2+np.pi/6), r'$\theta_2$', fontsize=20, horizontalalignment='center', verticalalignment='center')
ax0.text(center[0]+1.9*np.cos(direct/2), center[1]+1.9*np.sin(direct/2), r'$\phi^{\rm head}$', fontsize=20, horizontalalignment='center', verticalalignment='center')
ax0.text(0, 2.1, r'left permanent magnetic particle',               fontsize=15, horizontalalignment='left', verticalalignment='center')
ax0.text(0, 2.1-0.3, r'$\left(\cos\theta_1, \sin\theta_1 \right)$', fontsize=15, horizontalalignment='left', verticalalignment='center')
ax0.text(1.05, 0, r'right permanent magnetic particle',              fontsize=15, horizontalalignment='left', verticalalignment='center')
ax0.text(1.05, 0-0.3, r'$\left(\cos\theta_2, \sin\theta_2 \right)$', fontsize=15, horizontalalignment='left', verticalalignment='center')


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
LX = 1.60
LY = 1.0
gridwidth = 0.1
ratio = 1.0
ax1.set_xlabel(r'$x/\ell$')
ax1.set_ylabel(r'$y/\ell$')
ax1.set_xlim([-LX, LX])
ax1.set_ylim([-LY, LY])
ax1.set_aspect('equal')
#ax1.axis('off')
#ax1.xaxis.set_visible(False)

ax1.set_yticks([-1, 0, 1])
pos_1 = [ratio * -0.5, 0]
pos_2 = [ratio * 0.5, 0 ]
perm1 = patches.Circle(xy=(pos_1[0], pos_1[1]), radius=ratio * 0.3, ls='-', ec='gray', fc='gray', fill=True)
perm2 = patches.Circle(xy=(pos_2[0], pos_2[1]), radius=ratio * 0.3, ls='-', ec='gray', fc='gray', fill=True)
ax1.add_patch(perm1)
ax1.add_patch(perm2)
left_arc  = patches.Arc(xy=(ratio * -0.5, 0), lw=4.0, width=0.40, height=0.40, angle=0.0, theta1=-240, theta2=60)
right_arc = patches.Arc(xy=(ratio * 0.5, 0 ), lw=4.0, width=0.40, height=0.40, angle=0.0, theta1=-240, theta2=60)
ax1.add_patch(left_arc)
ax1.add_patch(right_arc)
arrow_dict = dict(arrowstyle = '->, head_width=0.3, head_length=0.5', color='k', linestyle='-', shrinkA=0, shrinkB=0, lw=3.0e+0)
ax1.annotate('',
        xy=(-0.5+0.2*np.cos(np.pi/3)+0.05*np.cos(np.pi/3+np.pi/2-np.pi/30), 0.2*np.sin(np.pi/3)+0.05*np.sin(np.pi/3+np.pi/2-np.pi/30)),
        xytext=(-0.5+0.2*np.cos(np.pi/3), 0.2*np.sin(np.pi/3)),
        arrowprops=arrow_dict,
        color='k',
        zorder=4)
ax1.annotate('',
        xy=(0.5+0.2*np.cos(2*np.pi/3)+0.05*np.cos(2*np.pi/3-np.pi/2+np.pi/30), 0.2*np.sin(2*np.pi/3)+0.05*np.sin(2*np.pi/3-np.pi/2+np.pi/30)),
        xytext=(0.5+0.2*np.cos(2*np.pi/3), 0.2*np.sin(2*np.pi/3)),
        arrowprops=arrow_dict,
        color='k',
        zorder=4)
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
ax1.quiver(pos_1[0], pos_1[1], 0., 0.8, color='red', angles='xy', scale_units='xy', scale=1.0, zorder=2, headwidth=4, headlength=6, headaxislength=5)
ax1.quiver(pos_2[0], pos_2[1], 0., 0.8, color='red', angles='xy', scale_units='xy', scale=1.0, zorder=2, headwidth=4, headlength=6, headaxislength=5)


"""
ax2
"""
img = plt.imread('microrobot_real2.png')
#img = ndimage.rotate(img, -2)
ax2.imshow(img)
ax2.axis('off')
#ax2.set_xlim(1200, 2600)
#ax2.set_ylim(750, 2030)


"""
ax3
"""
width = 858
height = 460
origin_x = width/2
origin_y = height/2
ax3.set_xlim(origin_x-430, origin_x+430)
ax3.set_ylim(origin_y+250, origin_y-300)
ax3.set_aspect('equal')
img3 = plt.imread('chlamidomonas3.jpg')
ax3.imshow(img3, zorder=0)
ax3.axis('off')

center_x = origin_x
center_y = origin_y + 80
body = patches.Circle(xy=(center_x, center_y), radius=40, fc='black', fill=True, zorder=1)
left_hand  = patches.Circle(xy=(center_x-320, 13), radius=15, fc='black', fill=True, zorder=1)
right_hand = patches.Circle(xy=(center_x+320, 13), radius=15, fc='black', fill=True, zorder=1)

RADI = 100
beam = 340
ang = np.pi/4.5
circle_x = 110 + RADI*np.cos(3*np.pi/8)
circle_y = 6   + RADI*np.sin(3*np.pi/8)
#left_circle  = patches.Circle(xy=(origin_x-circle_x, circle_y), radius=RADI, ec='black', fill=False, zorder=1)
#right_circle = patches.Circle(xy=(origin_x+circle_x, circle_y), radius=RADI, ec='black', fill=False, zorder=1)
left_circle  = patches.Circle(xy=(center_x-beam*np.cos(ang), center_y-beam*np.sin(ang)), radius=RADI, ec='black', fill=False, zorder=1)
right_circle = patches.Circle(xy=(center_x+beam*np.cos(ang), center_y-beam*np.sin(ang)), radius=RADI, ec='black', fill=False, zorder=1)
ax3.add_patch(body)
ax3.add_patch(left_hand)
ax3.add_patch(right_hand)
ax3.add_patch(left_circle)
ax3.add_patch(right_circle)
ax3.plot([center_x-beam*np.cos(ang), center_x+beam*np.cos(ang)], [center_y-beam*np.sin(ang), center_y-beam*np.sin(ang)], lw=1.5, color='black')
ax3.plot([center_x-beam*np.cos(ang), center_x                 ], [center_y-beam*np.sin(ang), center_y                 ], lw=1.5, color='black')
ax3.plot([center_x                 , center_x+beam*np.cos(ang)], [center_y                 , center_y-beam*np.sin(ang)], lw=1.5, color='black')

# arrows
left_arc  = patches.Arc(xy=(center_x-beam*np.cos(ang),center_y-beam*np.sin(ang)), lw=3.0, width=300, height=300, angle=0.0, theta1=135, theta2=225)
right_arc = patches.Arc(xy=(center_x+beam*np.cos(ang),center_y-beam*np.sin(ang)), lw=3.0, width=300, height=300, angle=0.0, theta1=-45, theta2=45)
ax3.add_patch(left_arc)
ax3.add_patch(right_arc)
#ax3.quiver(center_x-beam*np.cos(ang)+300*np.cos(5*np.pi/4), center_y-beam*np.sin(ang)+300*np.sin(5*np.pi/4), 400, -400, color='red', angles='xy', scale_units='xy', scale=1.0, zorder=5)
#ax3.quiver(center_x-beam*np.cos(ang)+150*np.cos(5*np.pi/4), center_y-beam*np.sin(ang)-150*np.sin(5*np.pi/4), 10, 10, headlength=100, headaxislength=90, headwidth=60, color='k', angles='xy', scale_units='xy', scale=0.5, zorder=5)
arrow_dict = dict(arrowstyle = '->, head_width=0.2, head_length=0.5', color='k', linestyle='-', shrinkA=0, shrinkB=0, lw=2.0e+0)
ax3.annotate('',
        xy=(center_x-beam*np.cos(ang)+150*np.cos(5*np.pi/4)+10, center_y-beam*np.sin(ang)-150*np.sin(5*np.pi/4)+10),
        xytext=(center_x-beam*np.cos(ang)+150*np.cos(5*np.pi/4), center_y-beam*np.sin(ang)-150*np.sin(5*np.pi/4)),
        arrowprops=arrow_dict,
        color='k',
        zorder=4)
ax3.annotate('',
        xy=(center_x+beam*np.cos(ang)+150*np.cos(np.pi/4)-10, center_y-beam*np.sin(ang)+150*np.sin(np.pi/4)+10),
        xytext=(center_x+beam*np.cos(ang)+150*np.cos(np.pi/4), center_y-beam*np.sin(ang)+150*np.sin(np.pi/4)),
        arrowprops=arrow_dict,
        color='k',
        zorder=4)
#ax1.quiver(pos_2[0], pos_2[1], 0., 0.8, color='red', angles='xy', scale_units='xy', scale=1.0, zorder=2)

plt.show()
fig.savefig('papers/figure_0.png')
fig.savefig('papers/figure_0.eps')
