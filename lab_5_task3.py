import time
import random

N = random.randint(0, 10)
M = random.randint(0, 10)

for i in range(0, M):
    print(i)
    time.sleep(1)
    for j in range(0, N):
        print(j)
        time.sleep(1)