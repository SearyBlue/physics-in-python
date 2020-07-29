#!/bin/python

import random
from matplotlib import pyplot as plt
from matplotlib import animation as ani


plt.style.use('ggplot')
fig, ax = plt.subplots()
xdat = [0]
ydat = [0]
plot, = plt.plot(xdat,ydat, ls="--", marker='o')
plt.annotate(len(xdat), (xdat[-1],ydat[-1]))
def anim(i):
    random.seed()
    global xdat,ydat
    xdat.append(xdat[-1] + random.randrange(-1,2,2))
    ydat.append(ydat[-1] + random.randrange(-1,2,2))
    ax.clear()
    plt.annotate(len(xdat), (xdat[-1],ydat[-1]))
    plt.plot(xdat,ydat, ls="--", marker='o')

myani = ani.FuncAnimation(fig, anim, frames=50000, interval=1000)
plt.show()
