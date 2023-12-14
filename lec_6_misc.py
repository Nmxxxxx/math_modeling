import matplotlib.pyplot as plt

x = [1, 4, 9, 16, 25]
y = [1, 2, 3, 4, 5]

plt.plot(x, y, color='black', label='√x', marker='>', ms=5)

# ----- Украшения ------
plt.xlabel('Coord: X')
plt.ylabel('Coord: Y')
plt.legend()
plt.title('√x')
plt.grid()

plt.savefig('√x aka misc.png')

