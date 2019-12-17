import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange (0,7, 0.01)

def diff(z, t):
    s, v = z
    ds_dt = v
    dv_dt = -9.8*np.sin(s/l)
    return ds_dt, dv_dt
s0 = 3
v0 = 2
l = 2
z0 = s0, v0
solve = odeint(diff, z0, t)
plt.plot(t, solve[:,0], "r", label="График")
plt.legend()
plt.show()
