figura = input('Выбери фигуру: круг, прямоугольник,прямоугольник(синус), треугольник, прямоугольный треугольник: ')

def Svishislyator():
    if figura == 'круг':
        R = int(input('Введи радиус:'))
        return 3.14 * (R**2)
    elif figura == 'прямоугольник':
        a = int(input('Введи сторону:'))
        b = int(input('Введи 2 сторону:'))
        return a*b
    elif figura == 'прямоугольник(синус)':
        d = int(input('Введи диагональ:'))
        sin = float(input('Введи синус угла: '))
        return 0.5*d*sin
    elif figura == 'треугольник':
        osn = int(input('Введи основание: '))
        h = int(input('Введи высоту: '))
        return osn*h*0.5
    elif figura == 'прямоугольный треугольник':
        osn1 = int(input('Введи первый катет: '))
        osn2 = int(input('Введи второй катет: '))
        return (osn1 * osn2)/2

n = Svishislyator()
print(n)