import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Определяем переменую величину
frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, vx, y, vy = z

    # dx_dt = vx
    dx_dt = vx
    dvx_dt = -Fp/m
    # dy_dt = vy
    dy_dt = vy
    dvy_dt = -m*g


    return dx_dt, dvx_dt, dy_dt, dvy_dt

g = 9.8
v0 = 15
alpha = 30 * np.pi / 180
u = 0.2
Fp = 5
m = 0.5

x0 = 0
vx0 = v0 * np.cos(alpha)
y0 = 0
vy0 = v0 * np.sin(alpha)

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
ball_line, = plt.plot([], [], '-', color='r')

# i - это переменая frames
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 30
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save('lab_11_task_2.gif')