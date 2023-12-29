import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def cycloid(R,  time, angle_vel):

    t = angle_vel * np.pi / 180 * time
    # t = np.arange(-2*np.pi, 2*np.pi, 1000)
    x = R * t - np.sin(t)
    y = R * 1 - np.cos(t)
    return x, y
#angle_vel = изменение угла
def animate(i):

    cycloida.set_data(cycloid(R=0.5,angle_vel=np.linspace(-2*np.pi, 2*np.pi, 1000), time=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()

    cycloida, = plt.plot([], [], '-', color='purple', label='Циклоида')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)

    ani.save('cycloida.gif', fps=30)