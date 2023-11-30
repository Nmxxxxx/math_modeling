import numpy as np

data = np.arange(1, 11)


def Ymnozhator3000(x):
    result = data.prod()
    print(x)
    return result

n = Ymnozhator3000(data)
print(n)