import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
amin_object, = plt.plot([],[], marker="o")
def Сikloida_m(r, t):
    x=r*np.cos(t)**3
    y=r*np.sin(t)**3
    return x,y
edge=4
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def animate(i):
    amin_object.set_data(Сikloida_m(r=1, t=i))

ani=FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, 0.1), interval=100)

ani.save("cikloida.gif")