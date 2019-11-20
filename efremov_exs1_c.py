#Задание 1.c
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure()

def crcl(x_centre=0, y_centre=0, R=10):
    x = []
    y = []
    alpha = np.linspace(0, 2 * np.pi, R*20)
    for i in alpha:
     x.append(x_centre + R * np.cos(i))
     y.append(y_centre + R * np.sin(i))
    return x, y

a, b, c = 3, 3, 16

x_coord = np.linspace(-5, 5, 100)
y_coord = np.zeros(100)

for i in range(0, 100, 1):
    y_coord[i] = a * x_coord[i]**2 + b * x_coord[i] + c

prb = plt.plot(x_coord, y_coord, color='r')
anim_list = []

for i in range(0, 100, 1):
    x, y = crcl(x_coord[i], y_coord[i], 10)
    anim_odj, = plt.plot(x, y, 'bo', ms=0.5)
    anim_list.append([anim_odj])
plt.axis('equal')
ani = ArtistAnimation(fig, anim_list, interval=50)
ani.save('ani_1c.gif')