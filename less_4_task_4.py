import numpy as np

def parabola():
    data = np.linspace(0, 10, 5)
    return data **2

n = parabola()
print(n)