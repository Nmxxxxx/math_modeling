import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation




def animate(i):
    cycloida.set_data(cycloid(R=0.5,angle_vel=np.linspace(0, 2*np.pi, 1000), time=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()

    cycloida, = plt.plot([], [], '-', color='purple', label='Циклоида')

    edge = 6
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(0, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)

    ani.save('cycloida.gif', fps=30)
