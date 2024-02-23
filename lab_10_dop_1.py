import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def diff_func(f, t):
    x, y, z = f
    dx_dt = 3*x - y + z
    dy_dt = x + y + z
    dz_dt = 4*x - y + 4*z
    return dx_dt, dy_dt, dz_dt


# initail data
x0 = -71
y0 = 1
z0 = -3 # dy0_dx = w - это омега

f = x0, y0, z0

sol = odeint(diff_func, f, t)

plt.plot(t, sol[:, 0], 'black',linewidth = 2, label='какая-то фигня')
plt.plot(t, sol[:, 1], 'red', label='какая-то фигня2')
plt.plot(t, sol[:, 2], 'blue', label='какая-то фигня2')
plt.legend()
plt.savefig('lab_10_dop_1.png')