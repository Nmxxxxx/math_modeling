import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.01)

def diff_func(f, x):
    w, y = f
    dy_dx = w
    dw_dx = (w*x - 2*y)/(1-x)*(1+x)
    return dy_dx, dw_dx



# initail data
y = 3
w = 0
f = w, y
sol = odeint(diff_func, f, x)

plt.plot(x, sol[:, 0], 'black', label='какая-то фигня')
plt.plot(x, sol[:, 1], 'red', label='какая-то фигня2')
plt.legend()
plt.savefig('lab_10_dop_5.png')