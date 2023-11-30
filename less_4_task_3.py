import numpy as np
from const import g

def EnergyOpredelyator3000(m, h, v):
    E = m * g * h
    return E

m = int(input('Enter massa: '))
h = int(input('Enter height: '))
v = int(input('Enter speed: '))

en = EnergyOpredelyator3000(m, h, v)
print(en)