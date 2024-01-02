import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

def circle_raz(angle_vel, a, time):

    t = a * np.pi / 180 * time
    r = a * t
    x = r * np.cos(angle_vel)
    y = r * np.sin(angle_vel)
    return x, y
#angle_vel = изменение угла
def animate(i):

    circle_razer.set_data(circle_raz(angle_vel=np.linspace(0, 2*np.pi, 100), a=0.5, time=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()

    circle_razer, = plt.plot([], [], '-', color='r', label='Astroida')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)

    ani.save('cirlce_raz.gif', fps=30)