import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange (0,7, 0.01)

def diff(z,t):
    y, alpha = z
    dy_dt = alpha
    dalpha_dt = -np.sin(y)*alpha-2*y*t-5
    return dy_dt, dalpha_dt
y0 = 0.01
alpha = 0.05

z0 = y0, alpha0

solve = odeint(diff, z0, t)
plt.plot(solve[:,1], solve[:,0], "g", label="График")
plt.legend()
plt.show()