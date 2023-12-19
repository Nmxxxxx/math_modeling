import matplotlib.pyplot as plt

import numpy as np

# логарифмическая спираль
def log_spiral(a):
    log_spir = np.linspace(0, 8*np.pi, 1000)
    radius = np.exp(a * log_spir)

    x = radius * np.sin(log_spir)
    y = radius * np.cos(log_spir)
    plt.plot(x,y)
    plt.axis('equal') # отключение масштабирования
    plt.savefig('log_spiral.png')

# архимедова спираль
def arximed_spiral(a):
    arx_spir = np.linspace(0, 8*np.pi, 1000)
    radius = a * arx_spir
    x = radius * np.cos(arx_spir)
    y = radius * np.sin(arx_spir)
    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('arximed_spiral.png')

# спираль жезл
def spiral_zhezl(k):
    spiral = np.linspace(0.01, 8*np.pi, 100)
    phi = (1 + np.sqrt(5)) / 2 
    r = k / np.sqrt(phi)
    x = r * np.cos(spiral)
    y = r * np.sin(spiral)
    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('spiral_zhezl.png')


#роза
def rosa(k):
    phi = np.linspace(0, 2*np.pi, 1000)

    r = np.sin(k * phi)
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('rosa.png')





if __name__ == '__main__':
    # log_spiral(0.1)
    # arximed_spiral(1)
    # spiral_zhezl(1)
    rosa(6)