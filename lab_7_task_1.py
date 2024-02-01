import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def cycloid(R,  time, angle_vel):

    t = angle_vel * time

    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y

def circle_move(R, vx0, time):
    x0 = vx0 * time 
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = R + R*np.sin(alpha)
    return x,y

def dotka(R, angle_vel, time):
    t = angle_vel  * time
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y

x, y = [], []

def animate(i):
    coords = cycloid(R=0.5,angle_vel=1, time=i)
    x.append(coords[0])
    y.append(coords[1])
    cycloida.set_data(x, y)
    dota.set_data(dotka(R = 0.5, angle_vel=1, time = i))
    circle.set_data(circle_move(R=0.5, vx0=0.5, time=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()

    cycloida, = plt.plot([], [], '-', color='black', label='Циклоида')
    dota, = plt.plot([], [], 'o', color = 'red')
    circle, = plt.plot([], [], '-', color='green', label='circle')


    plt.axis('equal')
    ax.set_xlim(-2, 8)
    ax.set_ylim(-2, 4)

    ani = FuncAnimation(fig, animate, frames=np.linspace(0, 3*np.pi, 100), interval=30)

    ani.save('cycloida.gif', fps=30)