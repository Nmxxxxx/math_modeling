import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def diff_func(f, t):
    x, y = f
    dx_dt = 3*x - 2*y + (np.e**(3*t))/(np.e**(t) + 1)
    dy_dt = x - (np.e**(3*t)/np.e**(t) + 1)
    return dx_dt, dy_dt

# initail data
x0 = 5
y0 = -7

f = x0, y0

sol = odeint(diff_func, f, t)

plt.plot(t, sol[:, 0], 'black', label='какая-то фигня')
plt.plot(t, sol[:, 1], 'black', label='какая-то фигня2')
plt.legend()
plt.savefig('lab_10_task_2.png')