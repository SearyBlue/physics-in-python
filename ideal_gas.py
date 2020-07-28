#!/bin/python

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as ani
plt.style.use('dark_background')

def anim(i):
    global xdat,ydat, vx, vy
    xdat, ydat = get_dat(xdat,ydat)
    vx, vy = walls(xdat,ydat,vx,vy)
    plot.set_data(xdat, ydat)
    return plot,


def init():
    xdat = lim*np.random.random(n) - lim/2
    ydat = lim*np.random.random(n) - lim/2
    return xdat,ydat


def get_dat(xdat, ydat):
    xdat = xdat + vx*h
    ydat = ydat + vy*h
    return xdat, ydat


def walls(xdat, ydat, vx, vy):
    wall = [-lim,lim]
    vx *= np.where(((xdat >= wall[1]) | (xdat <= wall[0])), -1, 1) 
    vy *= np.where(((ydat >= wall[1]) | (ydat <= wall[0])), -1, 1) 
    return vx, vy

    
fig, ax = plt.subplots()
lim = 20
ax.set_xlim(-lim,lim)
ax.set_ylim(-lim,lim)
n = 50
h = 0.001
xdat, ydat = init()
vx = 1000*np.random.random(n)-500
vy = 1000*np.random.random(n)-500
plot, = plt.plot(xdat,ydat, linestyle=' ', marker='o')


myani = ani.FuncAnimation(fig, anim, interval=1000*h, frames=200)
plt.show()
