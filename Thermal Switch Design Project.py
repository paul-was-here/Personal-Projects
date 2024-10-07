# Code for plotting dimensions function for engr135 thermal switch design project
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
from collections import OrderedDict

#Constant values:
pi = math.pi
dT = 85
Ea = 10000
Es = 30000
alphaa = 12.5 * 10**(-6)
alphas = 6.6 * 10**(-6)
ts = 1/16
ws = 1/8
L = 4

#Functions:
def allValues():
    x = np.linspace(0.04,0.05,500)
    y = (dT*(alphaa-alphas)-(pi**2)*(x**2)/3/(L**2))*((6*(L**2)*Es*ts*ws)/((pi**2)*Ea*(x**3)))
    y2 = x
    return(x,y,y2)
def plotting(x,y,y2):
    plt.plot(x,y,label="wₐ(tₐ)")
    plt.plot(x,y2,label="wₐ > tₐ")
    ax = plt.gca()
    ax.set_ylim(0,0.7)
    ax.set_xlim(0.04,0.05)
    ax.set_ylabel("wₐ (in)")
    ax.set_xlabel("tₐ (in)")
    ax.fill_between(y,y2,100,interpolate='True',color='Orange',alpha=0.1)
    ax.legend()
    plt.show()

#Main:
ta,wa,ylim = allValues()
plotting(ta,wa,ylim)