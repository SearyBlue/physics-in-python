#!/bin/python

import numpy as np
import math
import matplotlib
from itertools import combinations
from matplotlib import pyplot as plt
from matplotlib import animation as ani
plt.style.use('ggplot')
# matplotlib.use("Agg")
Writer = ani.writers['ffmpeg']
writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)


def anim(i):
    global xdat, ydat, vx, vy
    get_dat()
    walls()
    newt_coll()
    plot1.set_data(xdat, ydat)
    ax2.clear()
    plot2 = ax2.hist(vx**2+vy**2,bins=bins, histtype='stepfilled', color='blue')
    return plot1,



def init(n,lim):
    xdat = 2*(lim-1)*(np.random.random(n) - 0.5)
    ydat = 2*(lim-1)*(np.random.random(n) - 0.5)
    vx = 5000*(np.random.random(n) - 0.5)
    vy = 5000*(np.random.random(n) - 0.5)
    return xdat,ydat,vx,vy


def get_dat():
    global xdat,ydat,vx,vy
    xdat = xdat + vx*h
    ydat = ydat + vy*h
    return xdat, ydat


def newt_coll():
    global xdat,ydat,vx,vy
    for (i,j) in combinations(range(n),2):
        if (xdat[i]-xdat[j])**2 + (ydat[i]-ydat[j])**2 <= 0.5:
            ui = np.sqrt(vx[i]**2 + vy[i]**2) 
            uj = np.sqrt(vx[j]**2 + vy[j]**2) 
            ti = np.arctan(vy[i]/vx[i])
            tj = np.arctan(vy[j]/vx[j])
            f = np.arctan((ydat[i]-ydat[j])/(xdat[i]-xdat[j]))
            vx[i] = uj*math.cos(tj-f)*math.cos(f) - ui*math.sin(ti - f)*math.sin(f)
            vy[i] = uj*math.cos(tj-f)*math.sin(f) + ui*math.sin(ti - f)*math.cos(f)
            vx[j] = ui*math.cos(ti-f)*math.cos(f) - uj*math.sin(tj - f)*math.sin(f)
            vy[j] = ui*math.cos(ti-f)*math.sin(f) + uj*math.sin(tj - f)*math.cos(f)
    return vx, vy


def rand_coll(xdat, ydat):
    for (i,j) in combinations(range(n),2):
        if (xdat[i]-xdat[j])**2 + (ydat[i]-ydat[j])**2 <= 0.1:
            rat = np.random.random(4)
            rat /= np.sum(rat)
            vx[i], vy[i], vx[j], vy[j] = np.sqrt(rat*(vx[i]**2 + vy[i]**2 + vx[j]**2 + vy[j]**2))
    return vx, vy


def walls():
    global xdat,ydat,vx,vy
    xdat_ = xdat - 2*np.sign(xdat - lim)*np.where(np.abs(xdat) >= lim, np.abs(xdat) - lim, 0)
    ydat_ = ydat - 2*np.sign(ydat - lim)*np.where(np.abs(ydat) >= lim, np.abs(ydat) - lim, 0)
    vx *= np.where((np.abs(xdat) >= lim), -1, 1)
    vy *= np.where((np.abs(ydat) >= lim), -1, 1)
    xdat = xdat_
    ydat = ydat_
    
def main1():
    global xdat,ydat,vx,vy,h,lim,n,plot1,plot2,ax1,ax2,bins
    fig, (ax1, ax2) = plt.subplots(1, 2)
    lim = 40
    ax1.set_xlim(-lim,lim)
    ax1.set_ylim(-lim,lim)
    n = 50
    h = 0.001
    bins = 50
    xdat, ydat, vx, vy = init(n, lim)
    plot1, = ax1.plot(xdat,ydat, linestyle=' ', marker='o')
    plot2 = ax2.hist(vx**2+vy**2,bins=bins, histtype='stepfilled', color='blue')
    fig.set_size_inches(20, 11, forward=True)
    plt.margins(tight=True)
    myani = ani.FuncAnimation(fig, anim, interval=1, repeat=True)
    #myani.save('im.mkv', writer=writer)
    plt.show()

def main2():
    lim = 40
    n = 10
    h = 0.0001
    xdat, ydat, vx, vy = init(n,lim)
    while True:
        xdat, ydat = get_dat(xdat,ydat, h ,vx, vy)
        vx, vy = walls(xdat,ydat,vx,vy,lim)
        vx, vy = newt_coll(xdat, ydat, vx, vy, n)
        print ('\t'.join(map(str, xdat)))
        print ('\t'.join(map(str, ydat)))
        print ('\t'.join(map(str, vx)))
        print ('\t'.join(map(str, vy)))


main1()

