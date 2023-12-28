import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def circle_move(R, angle_vel, time):
    alpha = angle_vel * np.pi / 180 * time
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y

def animate(i):
    ball.set_data(circle_move(R=2, angle_vel=10, time=i))


if __name__ == '__main__':

    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='purple', label='Ball')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)


    ani = FuncAnimation(fig, animate, frames=360, interval=30)

    ani.save('standart_ball.gif')