import numpy as np
# Земля
x0_earth = 149 * 10**9
v_x0_earth = 0
y0_earth = 0
v_y0_earth = 30000


# Меркурий
x0_merc = 0
v_x0_merc = -47360
y0_merc = 0.387 * 149 * 10**9
v_y0_merc = 0

# Венера
x0_venus = 0
v_x0_venus = -35000
y0_venus = 0.723 * 149 * 10**9
v_y0_venus = 0


# Марс
x0_mars = 0
v_x0_mars = -24130
y0_mars = 1.52 * 149 * 10**9
v_y0_mars = 0

# faeton
e = 0.88994
x0_faeton = 0
v_x0_faeton = 20122 * np.sqrt((1+e)/(1-e))
print(v_x0_faeton)
y0_faeton = 0.2 * 149 * 10**9
v_y0_faeton = 0
