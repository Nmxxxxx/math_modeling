import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import initial_data_for_2 as si


plt.style.use('dark_background')
# Определяем переменую величину
frames = 360
t = np.linspace(0, 10**(-6), frames)

# Определяем функцию для диф.уравнений

def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4,
     x5, v_x5, y5, v_y5,
     x6, v_x6, y6, v_y6) = s
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx1_dt = v_x1
    dvx1_dt =  (k * si.q_large * si.q1 * x1 / (x1**2 + y1**2) **1.5 ) / m
    dy1_dt = v_y1
    dvy1_dt =  (k * si.q_large * si.q1 * y1 / (x1**2 + y1**2) **1.5) / m
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx2_dt = v_x2
    dvx2_dt =  (-k * si.q_large * si.q1 * x2 / (x2**2 + y2**2) **1.5 ) / m
    dy2_dt = v_y2
    dvy2_dt =  (k * si.q_large * si.q1 * y2 / (x2**2 + y2**2) **1.5) / m
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx3_dt = v_x3
    dvx3_dt =  (k * si.q_large * si.q1 * x3 / (x3**2 + y3**2) **1.5 ) / m
    dy3_dt = v_y3
    dvy3_dt =  (k * si.q_large * si.q1 * y3 / (x3**2 + y3**2) **1.5) / m
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx4_dt = v_x4
    dvx4_dt =  (-k * si.q_large * si.q1 * x4 / (x4**2 + y4**2) **1.5 ) / m
    dy4_dt = v_y4
    dvy4_dt =  (k * si.q_large * si.q1 * y4 / (x4**2 + y4**2) **1.5) / m
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx5_dt = v_x5
    dvx5_dt =  (-k * si.q_large * si.q1 * x5 / (x5**2 + y5**2) **1.5 ) / m
    dy5_dt = v_y5
    dvy5_dt =  (k * si.q_large * si.q1 * y5 / (x5**2 + y5**2) **1.5) / m
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx6_dt = v_x6
    dvx6_dt =  (k * si.q_large * si.q1 * x6 / (x6**2 + y6**2) **1.5 ) / m
    dy6_dt = v_y6
    dvy6_dt =  (k * si.q_large * si.q1 * y6 / (x6**2 + y6**2) **1.5) / m

    return (dx1_dt, dvx1_dt, dy1_dt, dvy1_dt, 
            dx2_dt, dvx2_dt, dy2_dt, dvy2_dt,
            dx3_dt, dvx3_dt, dy3_dt, dvy3_dt,
            dx4_dt, dvx4_dt, dy4_dt, dvy4_dt,
            dx5_dt, dvx5_dt, dy5_dt, dvy5_dt,
            dx6_dt, dvx6_dt, dy6_dt, dvy6_dt,)

k = 9 * 10**(9)
m = 9.1093837 * 10**(-31)

s0 = (si.x10, si.v_x10, si.y10, si.v_y10,
      si.x20, si.v_x20, si.y20, si.v_y20,
      si.x30, si.v_x30, si.y30, si.v_y30,
      si.x40, si.v_x40, si.y40, si.v_y40,
      si.x50, si.v_x50, si.y50, si.v_y50,
      si.x60, si.v_x60, si.y60, si.v_y60)
sol = odeint(move_func, s0, t)
print(sol)
# Решение диф. Уравнения
def solve_func(i, key):
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]

        x2 = sol[i, 4]
        y2 = sol[i, 6]

        x3 = sol[i, 8]
        y3 = sol[i, 10]

        x4 = sol[i, 12]
        y4 = sol[i, 14]

        x5 = sol[i, 16]
        y5 = sol[i, 18]

        x6 = sol[i, 20]
        y6 = sol[i, 22]
    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]

        x2 = sol[:i, 4]
        y2 = sol[:i, 6]

        x3 = sol[:i, 8]
        y3 = sol[:i, 10]

        x4 = sol[:i, 12]
        y4 = sol[:i, 14]

        x5 = sol[:i, 16]
        y5 = sol[:i, 18]

        x6 = sol[:i, 20]
        y6 = sol[:i, 22]
        
    return ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6))

# Строим график

fig, ax = plt.subplots()
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')

ball2, = plt.plot([], [], 'o', color='r')
ball_line2, = plt.plot([], [], '-', color='r')

ball3, = plt.plot([], [], 'o', color='purple')
ball_line3, = plt.plot([], [], '-', color='purple')

ball4, = plt.plot([], [], 'o', color='green')
ball_line4, = plt.plot([], [], '-', color='green')

ball5, = plt.plot([], [], 'o', color='white')
ball_line5, = plt.plot([], [], '-', color='white')

ball6, = plt.plot([], [], 'o', color='brown')
ball_line6, = plt.plot([], [], '-', color='brown')
plt.plot([0], [0], 'o', color='orange', ms=15)

def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])
    ball_line1.set_data(solve_func(i, 'line')[0])

    ball2.set_data(solve_func(i, 'point')[1])
    ball_line2.set_data(solve_func(i, 'line')[1])

    ball3.set_data(solve_func(i, 'point')[2])
    ball_line3.set_data(solve_func(i, 'line')[2])

    ball4.set_data(solve_func(i, 'point')[3])
    ball_line4.set_data(solve_func(i, 'line')[3])

    ball5.set_data(solve_func(i, 'point')[4])
    ball_line5.set_data(solve_func(i, 'line')[4])

    ball6.set_data(solve_func(i, 'point')[5])
    ball_line6.set_data(solve_func(i, 'line')[5])

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

plt.axis('equal')
edge = 0.5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('lab_12_task_dopad_2.gif')