import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 100, 1)
def speed(v, t):
    dvdt = (f - g * v ** 2) / m
    return dvdt
v0 = 0
m = 100
g =0.5
f = 10
solve = odeint(speed, v0, t)
plt.plot(t, solve)
plt.show()
    