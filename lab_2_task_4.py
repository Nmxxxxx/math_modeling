n = int(input('Введи натуральное число: '))
fib1 = 1
fib2 = 1
result = [fib1, fib2]

for a in range(2 , n + 1):
    fib1, fib2 = fib2, fib1 + fib2
    result.append(fib2)
    

print(*result)