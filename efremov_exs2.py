#Задание 2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure()

R = 20

def crcl(x_centre=0, y_centre=0, Radius=10):
    x = []
    y = []
    alpha = np.linspace(0, 2 * np.pi, 200)
    for i in alpha:
     x.append(x_centre + Radius * np.cos(i))
     y.append(y_centre + Radius * np.sin(i))
    return x, y

a, b, c = 3, 3, 16

alpha = np.linspace(0, 2 * np.pi, 100)
x_coord = 3/4 * R * np.cos(alpha)
y_coord = 3/4 * R * np.sin(alpha)

x_coord_mn = R * np.cos(alpha)
y_coord_mn = R * np.sin(alpha)

x_coord_ast = R * np.cos(alpha)**3
y_coord_ast = R * np.sin(alpha)**3
plt.plot(x_coord_mn, y_coord_mn, 'r')
#plt.plot(x_coord_ast, y_coord_ast, 'g')
anim_list = []

for i in range(0, 100, 1):
    x, y = crcl(x_coord[i], y_coord[i], R/4)
    anim_odj, = plt.plot(x, y, 'bo', ms=0.5)
    anim_odj1, = plt.plot(x_coord_ast[i], y_coord_ast[i], 'bo', ms=10)
    anim_odj2, = plt.plot(x_coord_ast[:i], y_coord_ast[:i], 'b-')
    anim_list.append([anim_odj, anim_odj1, anim_odj2])
    
    
plt.axis('equal')
ani = ArtistAnimation(fig, anim_list, interval=50)
ani.save('ani_2.gif')