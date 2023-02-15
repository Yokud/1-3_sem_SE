# Лабораторная работа: Интегралы

# Назначение программы:
# Вычислить площадь под графиком функции методом левых прямоугольников
# и методом Уэддла

# Описание переменных:
# eps - точность
# a, b - начальное и конечное значения промежутка для интегрирования
# n1, n2, h - числа интервалов и шаг 
# I - значение интеграла
# abs_p, otn_p - абсолютная и относительная погрешность
# s, s1, x, n - вспомогательные переменные

# Тестовый пример :
# y = 2*x
# a = 0, b = 1, n1 = 6, n2 = 12, eps = 0.01
#
# По методу Уэддла: 1.000; по методу левых прямоугольников:
# 0.5555556, 0.7638889
# Площадь под графиком по методу левых прямоугольников с
# точностью eps: 0.9689670
# Абсолютная погрешность: 0.4134115
# Относительная погрешность: 0.4266517


def F(x):
    return x*x

def Weddle(func, a, b, n):
    h = (b-a)/n
    I = 0
    count, ll = 0, a
    limit = n // 6
    if n % 6 == 0:
        while count < limit:
            I += 0.3*h*(func(ll)+func(ll+2*h)+5*func(ll+h)+6*func(ll+3*h)+func(ll+4*h)+\
                5*func(ll+5*h)+func(ll+6*h))
            ll += 6*h
            count += 1
    else:
        I = '--'
    return I

def Left_Rectangles(func, a, b, n):
    h = (b-a)/n
    x = a
    Sum = 0
    for i in range(n-1):
        Sum += func(x)
        x += h
    I = h*Sum
    return I

def main():
    # Печать таблицы       
    a, b = map(float, input('Введите начальное и конечное значения промежутка'\
               +' для интегрирования через пробел: ').split())
    s = 'Введите 2 значения числа интервалов через пробел(Для использования метод'\
        +'а Уэддла число должно быть кратно 6): '
    n1, n2 = map(int, input(s).split())
    eps = float(input('Введите точность: '))
    print('╓', '─'*14, '╥', '─'*13,  '╥', '─'*13, '╖', sep = '')
    print('║{:^14s}║{:>5s} = {:<5d}║{:>5s} = {:<5d}║'.format('Метод','n1',+\
                                                             n1,'n2', n2))
    print('╟', '─'*14, '╫', '─'*13,'╫', '─'*13,  '╢', sep = '')
    print('║{:^14s}║'.format('Метод Уэддла'), end = '')
    s1 = '{:^13.7g}║'
    if type(Weddle(F, a, b, n1)) == str:
        s1 = '{:^13s}║'
    print(s1.format(Weddle(F, a, b, n1)), end = '')
    s1 = '{:^13.7g}║'
    if type(Weddle(F, a, b, n2)) == str:
        s1 = '{:^13s}║'
    print(s1.format(Weddle(F, a, b, n2)))
    print('╟', '─'*14, '╫', '─'*13,'╫', '─'*13,  '╢', sep = '')
    print('║{:^14s}║{:^13.7g}║{:^13.7g}║'.format('Метод Л. Прям.',\
                                                 Left_Rectangles(F, a, b, n1),\
                                                 Left_Rectangles(F, a, b, n2)))
    print('╙', '─'*14, '╨', '─'*13, '╨', '─'*13, '╜', sep = '')


    # Вычисление интеграла функции с точностью eps и погрешностей
    if n1 % 6 == 0 and n2 % 6 == 0:
        if abs(Left_Rectangles(F, a, b, n1) - Left_Rectangles(F, a, b, n2)) >\
           abs(Weddle(F, a, b, n1) - Weddle(F, a, b, n2)):
            n = 2
            
            while abs(Left_Rectangles(F, a, b, n) - Left_Rectangles(F, a, b, 2*n)) > eps:
                n *= 2
                I = Left_Rectangles(F, a, b, n)
                #n *= 2
            print('Площадь под графиком по методу левых прямоугольников с'+\
                  ' точностью eps: {:.7g}'.format(I))
            abs_p = abs(I - Left_Rectangles(F, a, b, 2*n))
            otn_p = abs_p/I
            print('Абсолютная погрешность: {:.7g}'.format(abs_p))
            print('Относительная погрешность: {:.7g}'.format(otn_p))
        else:
            n = 2
            while abs(Weddle(F, a, b, n) - Weddle(F, a, b, 2*n)) > eps:
                n *= 2
                I = Weddle(F, a, b, n)
                #n *= 2
            print('Площадь под графиком по методу Уэддла с точностью eps: {:.7g}'\
                  .format(I))
            abs_p = abs(I - Weddle(F, a, b, 2*n))
            otn_p = abs_p/I
            print('Абсолютная погрешность: {:.7g}'.format(abs_p))
            print('Относительная погрешность: {:.7g}'.format(otn_p))
    else:
        n = 2
        while abs(Left_Rectangles(F, a, b, n) - Left_Rectangles(F, a, b, 2*n)) > eps:
            n *= 2
            I = Left_Rectangles(F, a, b, n)
            #n *= 2
        print('Площадь под графиком по методу левых прямоугольников с'+\
        ' точностью eps: {:.7g}'.format(I))
        abs_p = abs(I - Left_Rectangles(F, a, b, 2*n))
        otn_p = abs_p/I
        print('Абсолютная погрешность: {:.7g}'.format(abs_p))
        print('Относительная погрешность: {:.7g}'.format(otn_p))

main()
if __name__ == '__main__':
    main()
