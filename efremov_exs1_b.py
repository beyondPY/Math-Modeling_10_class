#Задание 2
import numpy as np
from math import pi
import matplotlib.pyplot as plt

t = np.arange(-2 * pi, 2 * pi, 0.1)
R = 5
plt.xlim(-5, 5)
plt.ylim(-5, 5)

x = R * np.sin(t)**3
y = R * np.cos(t)**3

plt.plot(x, y)
plt.show()