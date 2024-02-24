import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 3, 0.01)

def diff_func(f, t):
    y , w = f
    dy_dt = w
    d = np.sqrt(1-(w**2))
    dw_dt = d
    return dy_dt, dw_dt


# initail data
y0 = 1
w = 0
f = y0, w

sol = odeint(diff_func, f, t)

plt.plot(t, sol[:, 0], 'black', label='какая-то фигня')
plt.plot(t, sol[:, 1], 'red', label='какая-то фигня2')
plt.legend()
plt.savefig('lab_10_dop_3.png')