import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def astroid(R, time, angle_vel):

    t = angle_vel * np.pi / 180 * time
    # t = np.arange(-2*np.pi, 2*np.pi, 1000)
    x = (R/4) * np.cos(t) ** 3
    y = (R/4) * np.sin(t) ** 3
    return x, y
#angle_vel = изменение угла
def animate(i):

    astroida.set_data(astroid(R=16, angle_vel=np.linspace(-2*np.pi, 2*np.pi, 100), time=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()

    astroida, = plt.plot([], [], '-', color='r', label='Astroida')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)

    ani.save('astroida.gif', fps=30)