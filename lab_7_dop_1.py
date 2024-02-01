import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def star4(t):
    global x
    x = 12 * np.cos(t) + 8*np.cos(1.5*t)
    global y
    y = 12 * np.sin(t) - 8 * np.sin(1.5*t)
    return x,y

def krytyashka(alpha, x ,y):
    X = x * np.cos(alpha) - y * np.sin(alpha)
    Y = y * np.cos(alpha) + x * np.sin(alpha)
    return X, Y

def animate(i):
    drawstar.set_data(star4(t = np.linspace(0, 4*np.pi, 100)))
    drawstar.set_data(krytyashka(alpha = i, x = x, y=y))

if __name__ == '__main__':
    fig, ax = plt.subplots()

    drawstar, = plt.plot([], [], '-', color='purple', label='Циклоида')

    edge = 25
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 100), interval=30)

    ani.save('star4.gif', fps=30)
