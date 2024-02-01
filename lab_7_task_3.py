import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import math

colors = ['red', 'blue', 'purple', 'green']

def Butterfly(angle_vel, time):

    t = angle_vel * np.pi / 180 * time
    x = np.sin(t) * (np.e**np.cos(t) - 2*np.cos(4*t) + np.sin(t/12)**5)
    y = np.cos(t) * (np.e**np.cos(t) - 2*np.cos(4*t) + np.sin(t/12)**5)
    # x = 16*np.sin(t)**3
    # y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
    return x, y
#angle_vel = изменение угла
def animate(i):
    color = random.choice(colors)
    circle_razer.set_data(Butterfly(angle_vel=np.linspace(0, 2*np.pi, 100), time=i))
    circle_razer.set_color(color)

if __name__ == '__main__':
    fig, ax = plt.subplots()

    circle_razer, = plt.plot([], [], '-',  label='Butterfly')

    
    plt.axis('equal')
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)

    ani.save('Butterfly_and_heart.gif', fps=30)