import matplotlib.pyplot as plt
import numpy as np


def parabola_plot(a=1, b=1, c=0):
    x = np.arange(-10, 10, 1)
    y = a*x**2 + b*x + c
    plt.plot(x, y, color='purple', label='parabola', marker='.', ms=5)
    plt.xlabel('Coord: X')
    plt.ylabel('Coord: Y')
    plt.legend()

    plt.grid()
    plt.axis('equal') # отключение масштабирования
    plt.savefig('x**2.png')


if __name__ == '__main__':
    parabola_plot()
