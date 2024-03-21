import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


# Определяем переменую величину
frames = 730
second_in_year = 365 * 24 * 60 * 60
years = 2

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
           
               )
    dydt1 = v_y1
    dv_ydt1 = (- G * m2 * (y1 - y2)/ ((x1-x2)**2 + (y1- y2)**2)**1.5
               - G * m3 * (y1 - y3)/ ((x1-x3)**2 + (y1- y3)**2)**1.5
          
               )
    
    # Динамика для второго тела
    dxdt2 = v_x2
    dv_xdt2 = (- G * m1 * (x2 - x1)/ ((x2-x1)**2 + (y2- y1)**2)**1.5
               - G * m3 * (x2 - x3)/ ((x2-x3)**2 + (y2- y3)**2)**1.5
           
               )
    dydt2 = v_y2
    dv_ydt2 = (- G * m1 * (y2 - y1)/ ((x2-x1)**2 + (y2- y1)**2)**1.5
               - G * m3 * (y2 - y3)/ ((x2-x3)**2 + (y2- y3)**2)**1.5
        
               )
    # Динамика для третьего тела
    dxdt3 = v_x3
    dv_xdt3 = (- G * m1 * (x3 - x1)/ ((x3-x1)**2 + (y3- y1)**2)**1.5
               - G * m2 * (x3 - x2)/ ((x3-x2)**2 + (y3- y2)**2)**1.5
        
               )
    dydt3 = v_y3
    dv_ydt3 = (- G * m1 * (y3 - y1)/ ((x3-x1)**2 + (y3- y1)**2)**1.5
               - G * m2 * (y3 - y2)/ ((x3-x2)**2 + (y3- y2)**2)**1.5          
               )
    
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3)

# Определяем начальные значения и параметры

colors = ['red', 'green', 'purple']
ae = 149 * 10**9
x10 = 0
v_x10 = 0
y10 = 0
v_y10 = -8638

x20 = 12.3 * ae
v_x20 = 0
y20 = 0
v_y20 = 6000


x30 = (12.3 + 0.67) * ae
v_x30 = 0
y30 = 0
v_y30 = -4000


s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30)

M_sun = 1.98847 * 10**(30)

m1 = 1.06 * M_sun
m2 = 0.96 * M_sun
m3 = 0.67 * M_sun

G = 6.67 * 10** (-11)


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
edge = (12.3+0.67) * ae * 1.5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('lab_13_task_1.gif')