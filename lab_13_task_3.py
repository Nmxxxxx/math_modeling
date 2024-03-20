import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


# Определяем переменую величину
frames = 365
second_in_year = 365 * 24 * 60 * 60
years = 0.5

t = np.linspace(0, years*second_in_year, frames)

# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3) = s
    
    # Динамика для первого тела
    dxdt1 = v_x1
    dv_xdt1 = (- G * m2 * (x1 - x2)/ ((x1-x2)**2 + (y1- y2)**2)**1.5
               - G * m3 * (x1 - x3)/ ((x1-x3)**2 + (y1- y3)**2)**1.5
               + k * q1 * q2 / m1 * (x1 - x2) / ((x1-x2)**2 + (y1- y2)**2)**1.5
               + k * q1 * q3 / m1 * (x1 - x3) / ((x1-x3)**2 + (y1 - y3)**2)**1.5              
               )
    dydt1 = v_y1
    dv_ydt1 = (- G * m2 * (y1 - y2)/ ((x1-x2)**2 + (y1- y2)**2)**1.5
               - G * m2 * (y1 - y3)/ ((x1-x3)**2 + (y1- y3)**2)**1.5
               + k * q1 * q2 / m1 * (y1 - y2) / ((x1-x2)**2 + (y1- y2)**2)**1.5
               + k * q1 * q3 / m1 * (y1 - y3) / ((x1-x3)**2 + (y1 - y3)**2)**1.5              
               )
    
    # Динамика для второго тела
    dxdt2 = v_x2
    dv_xdt2 = (- G * m1 * (x2 - x1)/ ((x2-x1)**2 + (y2- y1)**2)**1.5
               - G * m3 * (x2 - x3)/ ((x2-x3)**2 + (y2- y3)**2)**1.5
               + k * q2 * q1 / m2 * (x2 - x1) / ((x2-x1)**2 + (y2- y1)**2)**1.5
               + k * q2 * q3 / m2 * (x2 - x3) / ((x2-x3)**2 + (y2 - y3)**2)**1.5              
               )
    dydt2 = v_y2
    dv_ydt2 = (- G * m1 * (y2 - y1)/ ((x2-x1)**2 + (y2- y1)**2)**1.5
               - G * m3 * (y2 - y3)/ ((x2-x3)**2 + (y2- y3)**2)**1.5
               + k * q2 * q1 / m2 * (y2 - y1) / ((x2-x1)**2 + (y2- y1)**2)**1.5
               + k * q2 * q3 / m2 * (y2 - y3) / ((x2-x3)**2 + (y2 - y3)**2)**1.5              
               )
    # Динамика для третьего тела
    dxdt3 = v_x3
    dv_xdt3 = (- G * m1 * (x3 - x1)/ ((x3-x1)**2 + (y3- y1)**2)**1.5
               - G * m2 * (x3 - x2)/ ((x3-x2)**2 + (y3- y2)**2)**1.5
               + k * q3 * q1 / m3 * (x3 - x1) / ((x3-x1)**2 + (y3- y1)**2)**1.5
               + k * q3 * q2 / m3 * (x3 - x2) / ((x3-x2)**2 + (y3 - y2)**2)**1.5              
               )
    dydt3 = v_y3
    dv_ydt3 = (- G * m1 * (y3 - y1)/ ((x3-x1)**2 + (y3- y1)**2)**1.5
               - G * m2 * (y3 - y2)/ ((x3-x2)**2 + (y3- y2)**2)**1.5
               + k * q3 * q1 / m3 * (y3 - y1) / ((x3-x1)**2 + (y3- y1)**2)**1.5
               + k * q3 * q2 / m3 * (y3 - y2) / ((x3-x2)**2 + (y3 - y2)**2)**1.5              
               )
    
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3)

# Определяем начальные значения и параметры

colors = ['red', 'green', 'purple']

# x10 = 150 * 10**9
# v_x10 = 0
# y10 = 0
# v_y10 = 30000

# x20 = 200 * 10**9
# v_x20 = 1
# y20 = 0
# v_y20 = - 30000


# x30 = 250 *  10**9
# v_x30 = 30000
# y30 = 100
# v_y30 = 0


# x10 = 150 * 10**9
# v_x10 = 0
# y10 = 0
# v_y10 = 30000

# x20 = 200 * 10**9
# v_x20 = 1
# y20 = 0
# v_y20 = - 30000


# x30 = 250 *  10**9
# v_x30 = 30000
# y30 = 100
# v_y30 = 30000


x10 = 150 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 30000

x20 = 200 * 10**9
v_x20 = 1
y20 = 0
v_y20 = - 30000


x30 = 250 *  10**9
v_x30 = 30000
y30 = 100
v_y30 = 0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30)

m1 =  1
q1 = 10**(-20)

m2 = 1
q2 = 10**(-20)

m3 = 1
q3 =  10**(-20)

G = 6.67 * 10** (-11)
k = 8.98755 * 10**9

#Решаем систему диф. уравнений
sol = odeint(move_func , s0, t)

# Строим решение 

fig, ax = plt.subplots()

balls = []
balls_lines = []

for i in range(3):
    balls.append(plt.plot([], [], 'o', color = random.choice(colors)))
    balls_lines.append(plt.plot([], [], '-', color = 'r'))

def animate(i):
    for j in range(3):
        balls[j][0].set_data(sol[i, 4*j], sol[i, 4*j+2])
        balls_lines[j][0].set_data(sol[:i, 4*j], sol[:i, 4*j+2])


ani = FuncAnimation(fig, animate, frames=frames, interval = 30)

plt.axis('equal')
edge = 4 * x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('lab_13_task_3.gif')