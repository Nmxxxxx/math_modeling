# import numpy as np
# from scipy.integrate import odeint
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import random

# #Определяем переменую величину
# frames = 200
# t = np.linspace(0, 10, frames)

# def move_func(z, t):
#     x, vx, y, vy = z

#     dx_dt = k1*(A - x - y)
#     dvx_dt = vx
#     dy_dt =  k2*(A - x - y)
#     dvy_dt = vy


#     return dx_dt, dvx_dt, dy_dt, dvy_dt


# v0 = 15
# alpha = 30 * np.pi / 180
# k1 = 3
# k2 = 4
# A = 10

# x0 = 0
# vx0 = v0 * np.cos(alpha)
# y0 = 0
# vy0 = v0 * np.sin(alpha)

# z0 = x0, vx0, y0, vy0
# sol = odeint(move_func, z0, t)


# def solve_func(i, key):

#     if key == 'point':
#         x = sol[i, 0]
#         y = sol[i, 2]
#     else:
#         x = sol[:i, 0]
#         y = sol[:i, 2]
#     return x,y

# #Строим решение в виде графика и анимируем
# fig, ax = plt.subplots()
# ball, = plt.plot([], [], 'o', color='r')
# ball_line, = plt.plot([], [], '-', color='r')

# # i - это переменая frames
# def animate(i):
#     ball.set_data(solve_func(i, 'point'))
#     ball_line.set_data(solve_func(i, 'line'))

# ani = FuncAnimation(fig, animate, frames=frames, interval=30)

# edge = 30
# ax.set_xlim(0, edge)
# ax.set_ylim(0, edge)

# ani.save('lab_11_task_3.gif')


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

#Определяем переменую величину
frames = 200
t = np.linspace(0, 1000, frames)

def move_func(z, t):
    x, y = z

    dx_dt = k1*(A - x - y)
    dy_dt =  k2*(A - x - y)
    return dx_dt, dy_dt

v0 = 15
alpha = 30 * np.pi / 180
k1 = 3
k2 = 4
A = 10

x0 = 0
y0 = 0

z0 = x0, y0,
sol = odeint(move_func, z0, t)


# def solve_func(i, key):

#     if key == 'point':
#         x = sol[i, 0]
#         y = sol[i, 2]
#     else:
#         x = sol[:i, 0]
#         y = sol[:i, 2]
#     return x,y

#Строим решение в виде графика и анимируем
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')

# i - это переменая frames


plt.plot(t, sol[:, 0], 'black', label='какая-то фигня')
plt.plot(t, sol[:, 1], 'red', label='какая-то фигня2')
plt.legend()
plt.savefig('lab_10_dop_3.png')
