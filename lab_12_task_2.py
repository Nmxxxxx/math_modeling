import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import initial_data_for_2 as si
import mplcyberpunk


plt.style.use('dark_background')
# Определяем переменую величину
frames = 720
seconds_in_year = 365* 24 * 60 * 60
years = 1
t = np.linspace(0, 10**(-3), frames)

# Определяем функцию для диф.уравнений

def move_func(s, t):
    (si.x0_earth, si.v_x0_earth, si.y0_earth, si.v_y0_earth,
      si.x0_merc, si.v_x0_merc, si.y0_merc, si.v_y0_merc,
      si.x0_venus, si.v_x0_venus, si.y0_venus, si.v_y0_venus,
      si.x0_mars, si.v_x0_mars, si.y0_mars, si.v_y0_mars,
      si.x0_faeton, si.v_x0_faeton, si.y0_faeton, si.v_y0_faeton,
      si.x0_6, si.v_x0_6, si.y0_6, si.v_y0_6) = s
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx_dt_earth = si.v_x0_earth
    dv_xdt_earth =  (k * si.q_large * si.q1 * si.x0_earth / (si.x0_earth**2 + si.y0_earth**2) **1.5) / m
    dydt_earth = si.v_y0_earth
    dy_ydt_earth =  (k *si.q_large * si.q1 * si.y0_earth / (si.x0_earth**2 + si.y0_earth**2) **1.5) / m

# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx_dt_merc = si.v_x0_merc
    dv_xdt_merc =  (k *si.q_large * si.q2 * si.x0_merc/ (si.x0_merc**2 + si.y0_merc**2) **1.5) / m
    dydt_merc = si.v_y0_merc
    dy_ydt_merc =  (k *si.q_large * si.q2 * si.y0_merc / (si.x0_merc**2 + si.y0_merc**2) **1.5) / m
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx_dt_venus = si.v_x0_venus
    dv_xdt_venus =  (k *si.q_large * si.q3 * si.x0_venus / (si.x0_venus**2 + si.y0_venus**2) **1.5) / m
    dydt_venus = si.v_y0_venus
    dy_ydt_venus =  (k *si.q_large * si.q3 * si.y0_venus / (si.x0_venus**2 + si.y0_venus**2) **1.5) / m
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx_dt_mars = si.v_x0_mars
    dv_xdt_mars = (- k *si.q_large * si.q4 * si.x0_mars / (si.x0_mars**2 + si.y0_mars**2) **1.5) / m
    dydt_mars = si.v_y0_mars
    dy_ydt_mars = (- k *si.q_large * si.q4 * si.y0_mars / (si.x0_mars**2 + si.y0_mars**2) **1.5) / m

# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
    dx_dt_faeton = si.v_x0_faeton
    dv_xdt_faeton = (- k *si.q_large * si.q5 * si.x0_faeton / (si.x0_faeton**2 + si.y0_faeton**2) **1.5) / m
    dydt_faeton = si.v_y0_faeton
    dy_ydt_faeton = (- k *si.q_large * si.q5 * si.y0_faeton / (si.x0_faeton**2 + si.y0_faeton**2) **1.5) / m

    dx_dt_6 = si.v_x0_6
    dv_xdt_6 = (- k *si.q_large * si.q5 * si.x0_6  / (si.x0_6**2 + si.y0_6**2) **1.5) / m
    dydt_6 = si.v_y0_6
    dy_ydt_6 = (- k *si.q_large * si.q5 * si.y0_6  /  (si.x0_6**2 + si.y0_6**2) **1.5) / m

    return (dx_dt_earth,  dv_xdt_earth, dydt_earth, dy_ydt_earth,
            dx_dt_merc,   dv_xdt_merc,  dydt_merc, dy_ydt_merc,
            dx_dt_venus,  dv_xdt_venus, dydt_venus, dy_ydt_venus,
            dx_dt_mars,   dv_xdt_mars,  dydt_mars, dy_ydt_mars,
            dx_dt_faeton, dv_xdt_faeton, dydt_faeton, dy_ydt_faeton,
            dx_dt_6, dv_xdt_6, dydt_6, dy_ydt_6)

k = 9 * 10**(9)
m = 1.98 * 10**(30)

s0 = (si.x0_earth, si.v_x0_earth, si.y0_earth, si.v_y0_earth,
      si.x0_merc, si.v_x0_merc, si.y0_merc, si.v_y0_merc,
      si.x0_venus, si.v_x0_venus, si.y0_venus, si.v_y0_venus,
      si.x0_mars, si.v_x0_mars, si.y0_mars, si.v_y0_mars,
      si.x0_faeton, si.v_x0_faeton, si.y0_faeton, si.v_y0_faeton,
      si.x0_6, si.v_x0_6, si.y0_6, si.v_y0_6)
sol = odeint(move_func, s0, t)

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
    return ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6))

# Строим график

fig, ax = plt.subplots()
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color = 'b')
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=

ball2, = plt.plot([], [], 'o', color='r')
ball_line2, = plt.plot([], [], '-', color = 'r')
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
ball3, = plt.plot([], [], 'o', color='white')
ball_line3, = plt.plot([], [], '-', color = 'white')
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
ball4, = plt.plot([], [], 'o', color='r')
ball_line4, = plt.plot([], [], '-', color = 'r')
# -=---==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-==-==-=-=-=-=-=-=-=-=-=
ball5, = plt.plot([], [], 'o', color='grey')
ball_line5, = plt.plot([], [], '-', color = 'grey')

ball6, = plt.plot([], [], 'o', color='g')
ball_line6, = plt.plot([], [], '-', color = 'g')

plt.plot([0], [0], 'o', color='orange', ms=10)

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
ani.save('lab_12_task_2.gif')