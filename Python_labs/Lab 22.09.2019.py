# Лабораторная работа: Треугольник

# Назначение программы:
# Программа предназначена для вычисления длин сторон треугольника ABC; длины
# высоты, проведённого из наименьшего угла; принадлежности ABC к 
# равнобедренным треугольникам; принадлежности точки T к ABC и вычисления
# расстояния от T до ближайшей стороны этого треугольника, если эта точка
# принадлежит ему

# Переменные:
# Xa, Ya - координаты точки A
# Xb, Yb - координаты точки B
# Xc, Yc - координаты точки C
# Xab, Yab - координаты вектора AB
# Xbc, Ybc - координаты вектора BC
# Xac, Yac - координаты вектора AC
# len_AB - длина стороны AB
# len_BC - длина стороны BC
# len_AC - длина стороны AC
# P - полупериметр треугольника ABC
# S - площадь треугольника ABC
# h - высота треугольника ABC, проведённая из наименьшего угла
# str1 - строка, отвечающая за принадлежность треугольника ABC к равнобедренным
# треугольникам
# Xt, Yt - координаты точки T
# Zn1, Zn2, Zn3 - значения, используемые для расчёта принадлежности точки T к
# треугольнику ABC
# d_AB - расстояние от точки T до стороны AB
# d_BC - расстояние от точки T до стороны BC
# d_AC - расстояние от точки T до стороны AC

# Тестовый пример:
# При Xa, Ya = 0 0; Xb, Yb = 1 2; Xc, Yc = 2 0; Xt, Yt = 1 1
# len_AB = 2.23606; len_BC = 2.23606; len_AC = 2.00000
# h = 2.00000
# Треугольник является равнобедренным
# Точка T лежит внутри треугольника
# Расстояние от точки T до ближайшей стороны треугольника: 0.44721

from math import sqrt
Xa, Ya = map(int, input('Введите координаты (x, y) точки A'\
                        +' через пробел: ').split())
Xb, Yb = map(int, input('Введите координаты (x, y) точки B'\
                        +' через пробел: ').split())
Xc, Yc = map(int, input('Введите координаты (x, y) точки C'\
                        +' через пробел: ').split())
Xab, Yab = Xb - Xa, Yb - Ya
Xbc, Ybc = Xc - Xb, Yc - Yb
Xac, Yac = Xc - Xa, Yc - Ya
len_AB = sqrt(Xab**2 + Yab**2)
len_BC = sqrt(Xbc**2 + Ybc**2)
len_AC = sqrt(Xac**2 + Yac**2)

if len_AB + len_BC > len_AC and len_BC + len_AC > len_AB and \
   len_AB + len_AC > len_BC: # Проверка входных данных
    print('Длина стороны AB: {:.5f}\nДлина стороны BC: {:.5f}\
      \nДлина стороны AC: {:.5f}'.format(len_AB, len_BC, len_AC))

    P = (len_AB + len_BC + len_AC)/2
    S = sqrt(P * (P - len_AB) * (P - len_BC) * (P - len_AC))
    h = 2*S/(min(len_AB, len_BC, len_AC))
    print('Длина высоты, проведённого из наименьшего угла: {:.5f}'.format(h))

    str1 = ' не '
    if len_AB == len_BC or len_AB == len_AC or len_BC == len_AC:
        str1 = ' '
    print('Треугольник'+str1+'является равнобедренным')

    Xt, Yt = map(int, input('Введите координаты (x, y) точки T'\
                            +' через пробел: ').split())
    Zn1 = (Xa - Xt)*Yab - Xab*(Ya - Yt)
    Zn2 = (Xb - Xt)*Ybc - Xbc*(Yb - Yt)
    Zn3 = (Xc - Xt)*(-Yac) - (-Xac)*(Yc - Yt)
    if (Zn1 >= 0 and Zn2 >= 0 and Zn3 >= 0) or\
       (Zn1 <= 0 and Zn2 <= 0 and Zn3 <= 0):
        print('Точка T лежит внутри треугольника')
        d_AB = abs(Yab*Xt - Xb*Yt + Xb*Ya - Yb*Xa) / len_AB
        d_BC = abs(Ybc*Xt - Xbc*Yt + Xc*Yb - Yc*Xb) / len_BC
        d_AC = abs((-Yac)*Xt - (-Xac)*Yt + Xa*Yc - Ya*Xc) / len_AC
        print('Расстояние от точки T до ближайшей стороны треугольника:',\
              round(min(d_AB, d_BC, d_AC), 5))
    else:
        print('Точка T не лежит внутри треугольника')
else:
    print('Такого треугольника не существует')