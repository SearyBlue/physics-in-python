#!/bin/python

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as ani


def anim(i):
    global xdat,ydat
    xdat, ydat = get_dat(xdat,ydat)
    plot.set_data(xdat, ydat)
    return plot,

def init():
    xdat = np.random.randint(n)
    ydat = np.random.randint(n)
    return xdat,ydat


def get_dat(xdat, ydat):
    global vy
    vy = vy - g*h
    ydat = ydat - h*vy
    return xdat, ydat


fig, ax = plt.subplots()
n = 2
g = 1
h = 0.01
xdat, ydat = init()
vy = np.zeros(n)
plot, = plt.plot(xdat,ydat)


myani = ani.FuncAnimation(fig, anim, interval=1000*h)
plt.show()
