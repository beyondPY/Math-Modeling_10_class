#Задание 2.1
import numpy as np
from math import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
crcl, = plt.plot([], [], marker='o')

R = 5

def move(R, alpha, time):
    alpha = alpha*time
    x = R * (alpha - np.sin(alpha))
    y = R * (1 - np.cos(alpha))
    return x, y

edge = 40
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def anim(i):
    crcl.set_data(move(R=5, alpha=1, time=i))
    
ani = animation.FuncAnimation(fig,
                              anim,
                              frames=np.arange(-2 * pi, 2 * pi, 0.1),
                              interval=40)

t = np.arange(-2 * pi, 2 * pi, 0.1)

x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))

ax.plot(x, y)

ani.save('ani.gif')