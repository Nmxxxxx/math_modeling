import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


def interference_of_light_waves_stable1(x0, r):
    angle=np.linspace(0, np.pi, 100)
    x = x0 + r * np.cos(angle)
    y = r * np.sin(angle)

    for j in range(len(y)):
        if y[j] > 3:
            y[j] = 3
    return x, y

def interference_of_light_waves_stable2(x0, y0, r):
    angle=np.linspace(0, np.pi, 100)
    x = x0 + r * np.cos(angle)
    y = r * np.sin(angle)
    return x, y
def interference_of_light_waves_stable3(x0 ,y0, r):
    angle=np.linspace(0, np.pi, 100)
    x = x0 + r * np.cos(angle)
    y = r * np.sin(angle)
    return x, y

x, y = [], []

def animate(radius):
    coords = interference_of_light_waves_stable1(0, 3, r=radius)
    x.append(coords[0])
    y.append(coords[1])
    interference.set_data(x, y)


    coords2 = interference_of_light_waves_stable2(2.5, 3, r=radius)
    x.append(coords2[0])
    y.append(coords2[1])
    interference2.set_data(x, y)

    coords3 = interference_of_light_waves_stable3(-2.5, 3, r=radius)
    x.append(coords2[0])
    y.append(coords2[1])
    interference3.set_data(x, y)


if __name__ == '__main__':
    fig, ax = plt.subplots()

    interference, = plt.plot([], [], '-', color='r', label='Interference Of Light waves')
    interference2, = plt.plot([], [], '-', color='black', label='Interference Of Light waves')
    interference3, = plt.plot([], [], '-', color='black', label='Interference Of Light waves')
    plt.axhline(y=3, color='purple')
    edge = 6
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(0, edge)


    ani = FuncAnimation(fig, animate, frames=np.linspace(0, 4, 20), interval=30)

    ani.save('Interference_Of_Light_waves_test.gif', fps=30)