import matplotlib.pyplot as plt
import numpy as np
N = 100

def hiperbola(x_min, x_max,x_min2, x_max2, N):
    x = np.linspace(x_min, x_max, N)
    k = 10
    y = k / x

    plt.plot(x, y, color='black')
    x2 = np.linspace(x_min2, x_max2, N)
    y = k / x2
    plt.plot(x2, y, color= 'black')
    # plt.axis('equal') # отключение масштабирования
    plt.savefig('task_2.png')

x_min = -10
x_max = -1
x_min2 = 1
x_max2 = 10

if __name__ == '__main__':
    hiperbola(x_min, x_max, x_min2, x_max2, N)