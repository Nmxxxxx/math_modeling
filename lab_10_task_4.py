import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def diff_func(f, x):
    y, w = f
    dy_dx = w
    dw_dx = -5*y -4*w
    return dy_dx, dw_dx


# initail data
y0 = 3
w = 0 # dy0_dx = w - это омега

f = y0, w

sol = odeint(diff_func, f, x)

plt.plot(x, sol[:, 0], 'black', label='какая-то фигня')
plt.plot(x, sol[:, 1], 'black', label='какая-то фигня2')
plt.legend()
plt.savefig('lab_10_task_3.png')