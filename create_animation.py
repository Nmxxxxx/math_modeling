import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots() # Создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации

xdata, ydata = [], [] # координаты объекта анимаций

ax.set_xlim(0, 2*np.pi) # пределы изменения переменой X
ax.set_ylim(-1, 1) # пределы изменения переменой Y

#функция подстановки координат в объект анимации
def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))

    anim_object.set_data(xdata, ydata) # передача координат


ani = FuncAnimation(fig, # стандартный вызов пространства
                    update, # вызов функции подстановки координат
                    frames=np.arange(0, 2*np.pi, 0.1), #
                    interval=100) #интервал между кадрами по умолчанию 200 милисекунд

ani.save('create_animation.gif')