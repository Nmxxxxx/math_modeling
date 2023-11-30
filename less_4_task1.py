import numpy as np

data = np.arange(10)

def average_data(x):
    sum_of_data = x.sum()
    result = sum_of_data / len(x)
    return result

n = average_data(data)
print(n)