import matplotlib.pyplot as plt
import numpy as np
import random

def ellipse(R=3, a = random.randint(1, 25), b = random.randint(1,25)):
    alpha = np.linspace(-2*np.pi, 2*np.pi, 1000)
    print(a, b)
    x = a * np.cos(alpha)
    y = b * np.sin(alpha)

    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('ellipse_with_parametric.png')


if __name__ == '__main__':
    ellipse()
