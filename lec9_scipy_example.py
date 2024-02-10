import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# Пределы изменения переменой величины
# В данной задаче переменной величиной является время
t= np.arange(0, 10**6, 100)

# Запись диф. уравнения

def radio_function(m, t):
    dmdt = - k * m
    return dmdt

# определение начальных условия и параметров
m_0 = 10
k = 1.61 * 10**(-6) # Постояная распада для Висмута

# Решение диференциального уравнения функцией odeint
m_t = odeint(radio_function, m_0, t)


plt.plot(t, m_t[:, 0], label = 'Распад для Висмута')
plt.title('Распад для Висмута')

plt.savefig('lec9_scipy_example.png')
