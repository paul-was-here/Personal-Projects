# Code for plotting dimensions function for engr135 thermal switch design project
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
from collections import OrderedDict

#Constant values
pi = math.pi
dT = 85
Ea = 10000
Es = 30000
alphaa = 12.5 * 10**(-6)
alphas = 6.6 * 10**(-6)
ts = 1/16
ws = 1/8
L = 4

#Functions and variables
ta = np.linspace(0.04,0.05,500)
wa = (dT*(alphaa-alphas)-(pi**2)*(ta**2)/3/(L**2))*((6*(L**2)*Es*ts*ws)/((pi**2)*Ea*(ta**3)))
ylim = ta

#Plotting
plt.plot(ta,wa, label="wₐ(tₐ)")
plt.plot(ta,ylim, label="wₐ > tₐ")
ax = plt.gca()
ax.set_ylim(0,0.7)
ax.set_xlim(0.04,0.05)
ax.set_ylabel("wₐ (in)")
ax.set_xlabel("tₐ (in)")
ax.fill_between(ta, ylim, 100, interpolate='True',color='Orange', alpha=0.1)
ax.legend()

plt.show()


exit()


#UNUSED CODE:

coords = list(zip(wa,ta))

def valueWithin15(value):
    return round(1/value) - 1/value <= 0.05

def filterFn(coord):
    return valueWithin15(coord[0]) and valueWithin15(coord[1])

sortedlist = list(filter(filterFn, coords))
for item in sortedlist:
    #print(str(item[0])+'\t|\t'+str(item[1]))
    if item[0] > 0 and item[1] > 0:
        print('1/'+str(round(1/item[0],1))+'\t|\t1/'+str(round(1/item[1],1)))
        xlabel = "1/"+str(round(1/round(1/item[0],2),2))
        ylabel = "1/"+str(round(1/round(1/item[1],2),2))
        plt.gca().annotate(("↙ "+xlabel+", "+ylabel), (item[0], item[1]))

