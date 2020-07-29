#!/bin/python

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as ani


def anim(i):
    global xdat,ydat, vx, vy
    coll()
    get_dat()
    plot.set_data(xdat, ydat)
    print (vy, ydat)
    return plot,

def init(n,lim):
    xdat = np.linspace(-2*lim/3, 2*lim/3, n)
    ydat = lim*np.random.random(n)/2 + lim/2
    vy = np.zeros(n)
    return xdat,ydat,vy


def get_dat():
    global xdat,ydat, vx, vy
    vy = vy + g*h
    ydat = ydat + h*vy


def coll():
    global vy
    e = 0.95
    vy *= np.where(((ydat < 0.1) & (vy < 0)), -e, 1)   


fig, ax = plt.subplots()
lim = 50
ax.set_ylim(0,lim)
n = 100
g = -50000
h = 0.001
xdat, ydat, vy = init(n, lim)
plot, = plt.plot(xdat,ydat, ls=' ', marker='o')


myani = ani.FuncAnimation(fig, anim, interval=1000*h)
plt.show()
