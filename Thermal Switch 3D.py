import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
from collections import OrderedDict
from mpl_toolkits import mplot3d
from matplotlib import cm

#Numerical Values
pi = math.pi
dT = 85
Ea = 10000
Es = 30000
alphaa = 12.5 * 10**(-6)
alphas = 6.6 * 10**(-6)
ts = 1/16
ws = 1/8
L = 4

ta = np.linspace(0.04,0.05,500)
wa = (dT*(alphaa-alphas)-(pi**2)*(ta**2)/3/(L**2))*((6*(L**2)*Es*ts*ws)/((pi**2)*Ea*(ta**3)))
ylim = ta
area = ta*wa

colors = -area


ax = plt.axes(projection='3d')
ax.set_ylim(0,0.7)
ax.set_xlim(0.04,0.05)
ax.set_zlim(0,0.04)
ax.set_ylabel("wₐ (in)")
ax.set_xlabel("tₐ (in)")
ax.set_zlabel('Area, (in²)')
ax.scatter3D(ta,wa,area, c=colors, cmap='RdYlGn')


plt.show()


exit()