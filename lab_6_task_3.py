import matplotlib.pyplot as plt

import numpy as np

def circle_plotter(radius=10):
    x = 10
    N = 100
    h = 0
    k = 0
    a = 2
    b = 1
    ellipse = np.linspace(0, x, N)
    x_coord = h + a * np.cos(ellipse)
    y_coord = k + b * np.sin(ellipse)

    plt.plot(x_coord, y_coord)
    plt.axis('equal') # отключение масштабирования
    plt.savefig('ellipse.png')

if __name__ == '__main__':
    circle_plotter()