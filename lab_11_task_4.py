import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Определяем переменую величину
frames = 200
t = np.linspace(0, 5, frames)

#Определяем функцию для системы диф. уравнений

def move_func(z, t):
    x, vx, y, vy = z

    dx_dt = vx
    dvx_dt = 0
    dy_dt = vy
    dvy_dt = g - (k/m) * y

    return dx_dt, dvx_dt, dy_dt, dvy_dt


#Определяем начальные значения и параметры
g = 9.8
v = 0.1
alpha = 50 * np.pi / 180
k = 5
m = 1.5

x0 = 0
vx0 = 0
y0 = 10
vy0 = 5

z0 = x0, vx0, y0, vy0
sol = odeint(move_func, z0, t)


def solve_func(i, key):

    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x,y

#Строим решение в виде графика и анимируем
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='black')

# i - это переменая frames
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 5
ax.set_xlim(-edge, edge)
ax.set_ylim(-10, 10)

ani.save('lab_11_task_4.gif')