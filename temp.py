import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

t = np.arange(0,100, 0.01)

def diff(z,t):
    x, vx, y, vy = z
    dxdt = vx
    dvxdt = (f2*np.cos(2*np.pi/180*60))+f3*np.cos(2*np.pi/180*30)+f4/m
    dydt = vy
    dvydt = (f1 + f3*np.cos(2*np.cos(2*np.pi/180*30)+f4))/m
    return dxdt, dvxdt, dydt, dvydt

f1 = 200
f2 = 100
f3 = 400
f4 = 500
x0 = 0
m = 400
y0=0
vx0 = 100
vy0 = 30
z0 = x0, y0, vx0, vy0

solve = odeint(diff, z0, t)
plt.plot(solve[:,0], solve[:, 2], "r", label="График")
plt.legend()
plt.show()