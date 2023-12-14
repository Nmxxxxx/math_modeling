import matplotlib.pyplot as plt
import numpy as np
N = 100

def hiperbola(x_min, x_max, N):
    x = np.linspace(x_min,x_max, N)
    k = 10
    y = k / x
    for i in x:
        if i != 0 and i != 1:
            y = k / i
            y_sorted = []
            y_sorted.append(i)
            print(y_sorted)
        else:
            pass


    plt.plot(x, y, color='black')
    # plt.axis('equal') # отключение масштабирования
    plt.savefig('task_2.png')

x_min = -10
x_max = 10

if __name__ == '__main__':
    hiperbola(x_min, x_max , N)