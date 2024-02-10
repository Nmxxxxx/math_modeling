import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.01)

def invest(n, t):
    dndt = -k * n * t
    return dndt


n_0 = 1000
k = 0.08

m_t = odeint(invest, n_0, t)


plt.plot(t, m_t[:, 0], label = 'Invest')
plt.title('Invest')

plt.savefig('lab9_task2.png')
