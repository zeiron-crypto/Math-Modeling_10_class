import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from scipy.integrate import odeint

t = np.arange(0, 30, 0.1)


def diff_func(s, t):
    phi, v_phi = s
    dphidt = v_phi
    dv_phidt =  (R**2*l*omega**2*np.sin(phi - omega*t) - R*g*l*np.sin(phi)) / R*l**2
    return dphidt, dv_phidt

l = 1
m = 9
R = 3
omega = 0.2
g = 9.8
v_phi0 = 0
phi0 = np.pi / 3
s0 = phi0,  v_phi0

sol = odeint(diff_func, s0, t)

x1 = R * np.sin(omega * t[:])
y1 = - R * np.cos(omega * t[:])

x2 = x1 + l * np.sin(sol[:, 0])
y2 = y1 - l * np.cos(sol[:, 0])


abodys = []
fig = plt.figure()

for i in range(0, len(t), 1):
    tx = [0, x1[i], x2[i]]
    ty = [0, y1[i], y2[i]]
    check, = plt.plot(tx, ty, '-o', color='b')
    abodys.append([check])

ani = ArtistAnimation(fig, abodys, interval=50)

plt.axis('equal')
ani.save('getto.gif')