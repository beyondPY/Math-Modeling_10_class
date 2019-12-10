import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 21, 2)
def invest(m, t):
    dmdt = -k * m * t
    return dmdt
m = 1000
k = 0.08
solve = odeint(invest, m, t)
plt.plot(t,solve)
plt.show()
    