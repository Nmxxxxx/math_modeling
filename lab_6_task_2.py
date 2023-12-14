import matplotlib.pyplot as plt
import numpy as np
N = 100

def hiperbola(x_min, x_max, N):
    x = np.linspace(x_min,x_max, N)
    k = 10
    y = k / x


    plt.plot(x, y, color='black')
    # plt.axis('equal') # отключение масштабирования
    plt.savefig('task_2.png')

x_min = -10
x_max = 10

if __name__ == '__main__':
    hiperbola(x_min, x_max , N)