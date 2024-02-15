import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


x = np.arange(1, 3, 0.01)


#Функция для системы дифференциальных уравнений
def diff_func2(z, x): # z - изменяемая величина для системы
    y, omega = z

    # первое уравнение
    dy_dt = omega

    # второе уравнение 
    domega_dt = np.sin(y) * omega - 3*(x*y) - 5

    return dy_dt, domega_dt # возвращаем переменые по порядку

# начальные значения
y0 = 0.01             # |
omega0 = 0.05         # |
                      # v
z01 = y0, omega0   #  передаем по порядку


sol2 = odeint(diff_func2, z01, x)   
# print(sol2)
plt.plot(x, sol2[:, 0], 'purple', label='y(t)')
plt.plot(x, sol2[:, 1], 'b')
plt.legend()
plt.savefig('fig_1.png')