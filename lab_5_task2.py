name = input('Введи имя и фамилию на латинице: ')
nameredakted = '_'.join(name)
nameredakted2 = nameredakted.upper()
print(nameredakted2)
a = []
for i in nameredakted2:
    a.append(ord(i))

print(a)

# --- - -- -- - - 2_-- -- - - - -_-- --

nameredakted3 = '_'.join(name)
nameredakted4 = nameredakted.lower()
print(nameredakted4)
b = []
for i in nameredakted4:
    a.append(ord(i))

print(a)
