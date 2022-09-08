"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
---------------
Напишите программу для. проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
---------------
Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
эта точка (или на какой оси она находится).

Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 ->
----------------
Напишите программу, которая по заданному номеру четверти, показывает диапазон
возможных координат точек в этой четверти (x и y).
----------------
Напишите программу, которая принимает на вход координаты двух точек и
находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""


from math import sqrt


def task1(week_day=None):
    days_off = (6, 7,)
    try:
        if not isinstance(week_day, int):
            raise TypeError('Аргументом функции должен быть номер дня недели!')
        if (week_day < 0):
            raise ValueError('Номер дня недели не может быть отрицательным!')
        if int(week_day) in days_off:
            mes = 'да'
        else:
            mes = 'нет'
    except Exception as error:
        print(error)
    else:
        print(week_day, '->', mes)


def task2():
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                result = not (x or y or z) == (not x) and (not y) and (not z)
                mes = (
                    f'\u00ac({x} \u2228 {y} \u2228 {z}) = '
                    f'(\u00ac {x}) \u2227 (\u00ac {y}) \u2227 (\u00ac {z})'
                )
                print(mes, ':', result)


def task3(x=None, y=None):
    try:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Аргументами функции должны быть числа!')
        if (x > 0) and (y > 0):
            result = 1
        elif (x > 0) and (y < 0):
            result = 4
        elif (x < 0) and (y < 0):
            result = 3
        else:
            result = 2
    except Exception as error:
        print(error)
    else:
        print(f'x={x}; y={y}', ' -> ', result)


def task4(quater=None):
    quaters = {
        1: '[0 < x < +\u221e], [0 < y < +\u221e]',
        2: '[-\u221e < x < 0], [0 < y < -\u221e]',
        3: '[-\u221e < x < 0], [-\u221e < y < 0]',
        4: '[0 < x < +\u221e], [-\u221e < y < 0]'
    }
    values_range = quaters.get(quater)
    if values_range:
        print(
            f'Диапазон возможных координат точек '
            f'в четверти "{quater}" - {values_range}'
        )
    else:
        print('Укажите четверть декартовых координат: 1..4')


def dist2points(*args):
    if len(args) == 2:
        point1, point2 = args
        try:
            for val in (*point1, *point2):
                if not isinstance(val, (int, float)):
                    raise Exception('Координаты должны быть числами!')
            x1, y1 = point1
            x2, y2 = point2
            dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
            return_value = f'Расстояние между двумя точками равно {dist:.5}'
        except Exception as error:
            return_value = error
    else:
        return_value = (
            'Укажите координаты 2-х точек в виде: (x1, y1), (x2, y2)'
        )
    return return_value


if __name__ == '__main__':
    print()
    print('ЗАДАНИЕ 1:')
    task1(6)
    task1(7)
    task1(1)
    task1('Вс')
    task1()
    task1(-1)
    print()
    print('ЗАДАНИЕ 2:')
    task2()
    print()
    print('ЗАДАНИЕ 3:')
    task3(34, -30)
    task3(2, 4)
    task3(-34, -30)
    task3(-2, 4)
    task3()
    print()
    print('ЗАДАНИЕ 4:')
    task4(1)
    task4(2)
    task4(3)
    task4(4)
    task4(5)
    print()
    print('ЗАДАНИЕ 5:')
    print(dist2points())
    print(dist2points((7, 2), (-3, 7), (6, 9)))
    print(dist2points((7, 2), (-3, 7)))
