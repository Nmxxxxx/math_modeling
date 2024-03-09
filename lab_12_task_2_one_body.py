import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import initial_data_for_2 as si
import mplcyberpunk


plt.style.use('dark_background')
# Определяем переменую величину
frames = 360
t = np.linspace(0, 10**(-6), frames)

# Определяем функцию для диф.уравнений

def move_func(s, t):
    (x1, v_x1, y1, v_y1) = s
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx1_dt = v_x1
    dvx1_dt =  (k * si.q_large * si.q1 * x1 / (x1**2 + y1**2) **1.5 ) / m
    dy1_dt = v_y1
    dvy1_dt =  (k * si.q_large * si.q1 * y1 / (x1**2 + y1**2) **1.5) / m

    return (dx1_dt, dvx1_dt, dy1_dt, dvy1_dt)

k = 9 * 10**(9)
m = 9.1093837 * 10**(-31)

s0 = (si.x10, si.v_x10, si.y10, si.v_y10)
sol = odeint(move_func, s0, t)
print(sol)
# Решение диф. Уравнения
def solve_func(i, key):
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
    return (x1, y1)

# Строим график

fig, ax = plt.subplots()
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color = 'b')
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=

plt.plot([0], [0], 'o', color='orange', ms=10)

def animate(i):
    ball1.set_data(solve_func(i, 'point'))
    ball_line1.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

plt.axis('equal')
edge = 0.5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('lab_12_task__dop_2.gif')