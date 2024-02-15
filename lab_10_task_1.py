import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


x = np.arange(-5, 5, 0.01)

def diff_func(f, x):
    y, z = f

    dy_dx = (y**2) * z
    dz_dx = z/x - y*(z**2)

    return dy_dx, dz_dx
# initail data
y0 = 1
z0 = -3

f = y0, z0

sol = odeint(diff_func, f, x)

plt.plot(x, sol[:, 0], 'black', label='какая-то фигня')
plt.plot(x, sol[:, 1], 'black', label='какая-то фигня2')
plt.legend()
plt.savefig('lab_10_task_1.png')