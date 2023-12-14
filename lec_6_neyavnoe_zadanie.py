import matplotlib.pyplot as plt

import numpy as np

def circle_plotter(radius=10):

    x = np.arange(-2*radius, 2*radius, 1)
    y = np.arange(-2*radius, 2*radius, 1)

    # переход к неявно заданым командам
    X,Y = np.meshgrid(x, y)

    fxy = X**2 + Y ** 2 - radius**2
    #Команда рисования
    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal') # отключение масштабирования
    plt.savefig('circle.png')

if __name__ == '__main__':
    circle_plotter()