#!/bin/python

import numpy as np
from itertools import combinations
from matplotlib import pyplot as plt
from matplotlib import animation as ani
plt.style.use('dark_background')

def anim(i):
    global xdat,ydat, vx, vy
    xdat, ydat = get_dat(xdat,ydat)
    vx, vy = walls(xdat,ydat,vx,vy)
    vx, vy = coll(xdat, ydat)
    plot1.set_data(xdat, ydat)
    ax2.clear()
    plot2 = ax2.hist(vx**2+vy**2,bins=30,density=True)
    return plot1,


def init():
    xdat = lim*np.random.random(n) - lim/2
    ydat = lim*np.random.random(n) - lim/2
    return xdat,ydat


def get_dat(xdat, ydat):
    xdat = xdat + vx*h
    ydat = ydat + vy*h
    return xdat, ydat


def rand_coll(xdat, ydat):
    for (i,j) in combinations(range(n),2):
        if (xdat[i]-xdat[j])**2 + (ydat[i]-ydat[j])**2 <= 0.1:
            rat = np.random.random(4)
            rat /= np.sum(rat)
            vx[i], vy[i], vx[j], vy[j] = np.sqrt(rat*(vx[i]**2 + vy[i]**2 + vx[j]**2 + vy[j]**2))
    return vx, vy


def walls(xdat, ydat, vx, vy):
    wall = [-lim,lim]
    vx *= np.where(((xdat >= wall[1]) | (xdat <= wall[0])), -1, 1) 
    vy *= np.where(((ydat >= wall[1]) | (ydat <= wall[0])), -1, 1) 
    return vx, vy

    
fig, (ax1, ax2) = plt.subplots(1, 2)
lim = 50
ax1.set_xlim(-lim,lim)
ax1.set_ylim(-lim,lim)
n = 500
h = 0.1
xdat, ydat = init()
vx = 1000*np.random.random(n)-500
vy = 1000*np.random.random(n)-500
plot1, = ax1.plot(xdat,ydat, linestyle=' ', marker='o')
plot2 = ax2.hist(vx**2+vy**2,bins=20)

myani = ani.FuncAnimation(fig, anim, interval=1000*h)
plt.show()
