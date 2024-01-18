import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def interference_of_light_waves(angle_vel, a, time):

    t = a * np.pi / 180 * time
    r = a * t
    x = r * np.cos(angle_vel)
    y = r * np.sin(angle_vel)
    return x, y

def interference_of_light_waves_stable(angle_vel, r):

    x = r * np.cos(angle_vel)
    y = r * np.sin(angle_vel)
    return x, y



def animate(i):

    interference.set_data(interference_of_light_waves_stable(angle_vel=np.linspace(0, np.pi, 100), r=0.25))
    interference2.set_data(interference_of_light_waves(angle_vel=np.linspace(0, np.pi, 100), a=0.45, time=i))
    interference3.set_data(interference_of_light_waves(angle_vel=np.linspace(0, np.pi, 100), a=0.5, time=i))
    interference4.set_data(interference_of_light_waves(angle_vel=np.linspace(0, np.pi, 100), a=0.55, time=i))
    interference5.set_data(interference_of_light_waves(angle_vel=np.linspace(0, np.pi, 100), a=0.6, time=i))
    interference6.set_data(interference_of_light_waves(angle_vel=np.linspace(0, np.pi, 100), a=0.65, time=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()

    interference, = plt.plot([], [], '-', color='r', label='Interference Of Light waves')
    interference2, = plt.plot([], [], '-', color='r', label='Interference Of Light waves2')
    
    interference3, = plt.plot([], [], '-', color='r', label='Interference Of Light waves3')
    interference4, = plt.plot([], [], '-', color='r', label='Interference Of Light waves4')
    interference5, = plt.plot([], [], '-', color='r', label='Interference Of Light waves5')
    interference6, = plt.plot([], [], '-', color='r', label='Interference Of Light waves6')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)


    ani = FuncAnimation(fig, animate, frames=360, interval=30)

    ani.save('Interference_Of_Light_waves.gif', fps=30)