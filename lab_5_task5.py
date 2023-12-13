fio = input()

lower_symbol = [ord(i.lower()) for i in fio]

lower_ascii_sum = sum(lower_symbol)


upper_symbol = [ord(j.upper()) for j in fio]

upper_ascii_sum = sum(upper_symbol)

result = lower_ascii_sum + upper_ascii_sum
print(result)