import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x,y


def animate(i):
    asd.set_data(circle_move(R=0.5, vx0=0.01,vy0=0.01,  time=i))

if __name__ == '__main__':

    fig, ax = plt.subplots()
    asd, = plt.plot([], [], '-', color='purple', label='Asd')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)


    ani = FuncAnimation(fig, animate, frames=300, interval=30)

    ani.save('nonstandart_ball.gif')
