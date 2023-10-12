b1 = int(input('Введи начальное число: '))
q = int(input('Введи знаменатель: '))
colvo = int(input('Введи количество членов в прогрессии: '))


result = []

for el in range(0, colvo + 1):
    second_el = b1 * (q**el-1)
    result.append(second_el)


print(*result)