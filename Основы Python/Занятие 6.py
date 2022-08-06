import math as m

figura = input('Введите тип фигуры:')
if figura == 'Круг':
    radius = int(input('Введите радиус:'))
    area = m.pi * m.pow(radius, 2)
    print('Площадь круга:', area)
elif figura == 'Треугольник':
    a = int(input('Введите длину 1 стороны:'))
    b = int(input('Введите длину 2 стороны:'))
    c = int(input('Введите длину 3 стороны:'))
    p = (a + b + c) / 2
    area = m.sqrt((p * (p - a) * (p - b) * (p - c)))
    print('Площадь треугольника:', area)
elif figura == 'Прямоугольник':
    a = int(input('Введите длину 1 стороны:'))
    b = int(input('Введите длину 2 стороны:'))
    area = a * b
    print('Площадь прямоугольника:', area)
else:
    print('Ошибка')
