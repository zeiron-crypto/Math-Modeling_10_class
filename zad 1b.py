import numpy as np
import matplotlib.pyplot as plt
def Acikloida (r=30):
    t=np.arange(-2*np.pi, 2*np.pi, 0.1)
    x=r*np.cos(t)**3
    y=r*np.sin(t)**3
    plt.plot(x,y, label="Acikloida")
    plt.xlim(-10*np.pi, 10*np.pi)
    plt.ylim(-10*np.pi, 10*np.pi)
    plt.legend()
    plt.show()
Acikloida()
