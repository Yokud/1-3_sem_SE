# Проектно-технологическая практика
# Малышев Иван ИУ7-11Б

# Назначение программы:
# Программа создаёт текстовый файл OUTPUT.TXT и записывает в него
# программу для Машины Тьюринга: первая строка - количество состояний,
# вторая - номер начального состояния. Дальнейшие строки - это правила
# для Машины Тьюринга

# Описание переменных:
# N - Количество состояний
# S - Номер начального состояния
# Q - Список правил для Машины Тьюринга

N = 41
S = 1
Q = ['1 0 1 0 1',
     '1 1 1 1 1',
     '1 E 2 E -1',
     '2 0 3 E 1',
     '2 1 8 E 1',
     '2 E 13 E 1',
     '3 0 3 0 1',
     '3 1 3 1 1',
     '3 E 4 E 1',
     '4 0 4 0 1',
     '4 1 4 1 1',
     '4 E 5 0 1',
     '5 E 6 0 -1',
     '6 0 6 0 -1',
     '6 1 6 1 -1',
     '6 E 7 E -1',
     '7 0 7 0 -1',
     '7 1 7 1 -1',
     '7 E 2 0 -1',
     '8 0 8 0 1',
     '8 1 8 1 1',
     '8 E 9 E 1',
     '9 0 9 0 1',
     '9 1 9 1 1',
     '9 E 10 1 1',
     '10 E 11 0 -1',
     '11 0 11 0 -1',
     '11 1 11 1 -1',
     '11 E 12 E -1',
     '12 0 12 0 -1',
     '12 1 12 1 -1',
     '12 E 2 1 -1',
     '13 0 13 0 1',
     '13 1 13 1 1',
     '13 E 14 E -1',
     '14 0 15 E 1',
     '14 1 23 E 1',
     '15 0 15 0 1',
     '15 E 18 E 1',
     '16 0 16 0 -1',
     '16 E 32 0 -1',
     '17 0 18 0 1',
     '17 1 18 1 1',
     '17 E 18 E 1',
     '18 0 17 0 1',
     '18 1 19 0 1',
     '19 0 20 0 1',
     '19 1 20 1 1',
     '19 E 20 E 1',
     '20 0 17 1 1',
     '20 1 19 1 1',
     '20 E 21 1 -1',
     '21 0 38 0 -1',
     '21 1 38 1 -1',
     '21 E 22 E -1',
     '22 0 21 0 -1',
     '22 1 21 1 -1',
     '23 0 23 0 1',
     '23 E 24 E 1',
     '24 0 28 0 1',
     '24 1 30 0 1',
     '24 E 21 E -1',
     '25 0 29 0 1',
     '25 1 31 0 1',
     '25 E 29 E 1',
     '26 0 28 1 1',
     '26 1 30 1 1',
     '26 E 28 1 1',
     '27 0 29 1 1',
     '27 1 31 1 1',
     '27 E 29 1 1',
     '28 0 24 0 1',
     '28 1 24 1 1',
     '28 E 24 0 1',
     '29 0 24 1 1',
     '29 1 25 0 1',
     '29 E 24 1 1',
     '30 0 26 1 1',
     '30 1 27 0 1',
     '30 E 26 1 1',
     '31 0 27 0 1',
     '31 1 27 1 1',
     '31 E 27 0 1',
     '32 0 15 E 1',
     '32 1 23 E 1',
     '32 E 33 E 1',
     '33 0 33 0 1',
     '33 E 34 E 1',
     '34 0 35 0 1',
     '34 1 35 1 1',
     '34 E 37 E -1',
     '35 0 34 0 1',
     '35 1 34 1 1',
     '35 E 36 E -1',
     '36 0 37 0 -1',
     '36 1 37 1 -1',
     '37 0 36 0 -1',
     '37 1 40 1 -1 1',
     '38 0 39 0 -1',
     '38 1 39 1 -1',
     '39 0 38 0 -1',
     '39 1 38 1 -1',
     '39 E 16 E -1',
     '40 0 41 0 -1',
     '40 1 41 1 -1',
     '41 0 40 0 -1 0',
     '41 1 40 1 -1 1']

OUTPUT = open('OUTPUT.TXT', 'w')
OUTPUT.write(str(N))
OUTPUT.write('\n' + str(S))
for i in range(len(Q)):
    OUTPUT.write('\n' + Q[i])
OUTPUT.close()
