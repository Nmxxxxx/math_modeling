import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 1)

def raz_bac(n, t):
    dndt = k * n
    return dndt


n_0 = 10
k = 0.1

m_t = odeint(raz_bac, n_0, t)


plt.plot(t, m_t[:, 0], label = 'Размножение бактерий')
plt.title('Размножение бактерий')

plt.savefig('lab1_task1.png')
