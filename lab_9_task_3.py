import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 1)

def a0(v, t):
    dndt = a_0 - Y*(v**2)
    return dndt


a_0 = 10
Y = 0.2
v0 = 0

m_t = odeint(a0, a_0, t)


plt.plot(t, m_t[:, 0], label = '1')
plt.title('Р2')

plt.savefig('lab1_task3.png')
