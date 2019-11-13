#Задание 2.2
import numpy as np
from math import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
crcl, = plt.plot([], [], marker='o')

R = 5

def move(R, alpha, time):
    alpha = alpha*time
    x = R * np.sin(alpha)**3
    y = R * np.cos(alpha)**3
    return x, y

edge = 15
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def anim(i):
    crcl.set_data(move(R=5, alpha=1, time=i))
    
ani = animation.FuncAnimation(fig,
                              anim,
                              frames=np.arange(-2 * pi, 2 * pi, 0.1),
                              interval=40)

t = np.arange(-2 * pi, 2 * pi, 0.1)

x = R * np.sin(t)**3
y = R * np.cos(t)**3

ax.plot(x, y)

ani.save('ani2.gif')