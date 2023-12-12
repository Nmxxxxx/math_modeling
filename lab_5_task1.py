import random
N = int(input())
a = []
b = []
c = []
for i in range(N):
    a.append(random.randint(0,100))
    b.append(random.randint(0,100))
    c.append(random.randint(0,100))
max_el = max(a), max(b), max(c)
print(max(max_el))
summa = sum(a) + sum(b) + sum(c)
print(summa)