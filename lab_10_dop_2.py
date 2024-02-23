import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 5, 0.01)

def diff_func(f, t):
    y, w = f
    dy_dx = w
    dy_dt = (3*y**2)/np.sqrt(t)
    return dy_dx, dy_dt


# initail data
y0 = 0
w = 1 # dy0_dx = w - это омега

f = y0, w

sol = odeint(diff_func, f, t)

plt.plot(t, sol[:, 0], 'black', label='какая-то фигня')
plt.plot(t, sol[:, 1], 'red', label='какая-то фигня2')
plt.legend()
plt.savefig('lab_10_dop_2.png')