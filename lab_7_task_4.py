import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def circle_move(x0, y0, C, D, n, time, angle_vel):
    
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0
    y[0] = y0
    
    for j in range(1, n):
        # t = angle_vel * np.pi / 180 * time
        x[j] = x[j-1] **2 - y[j-1]**2 + C
        y[j] = 2*x[j-1] * y[j-1] + D

    return x,y

def animate(i):
    asd.set_data(circle_move(x0=1,y0=1,C = 0.3, D = 0.33,n = 1000, time=i))

if __name__ == '__main__':

    fig, ax = plt.subplots()
    asd, = plt.plot([], [], color='r', label='fractal')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)


    ani = FuncAnimation(fig, animate, frames=300, interval=30)

    ani.save('fractal.gif')
