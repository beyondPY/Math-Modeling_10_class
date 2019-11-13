#Задание 1
import numpy as np
from math import pi
import matplotlib.pyplot as plt

t = np.arange(-2 * pi, 2 * pi, 0.1)
R = 5
plt.xlim(-15, 15)
plt.ylim(-10, 15)

x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))

plt.plot(x, y)
plt.show()