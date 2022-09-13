"""
Напишите программу, которая принимает на вход вещественное число и
показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
--------------------------
Напишите программу, которая принимает на вход число N и
выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
--------------------------
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и
выведите на экран их сумму.
Пример:
- Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}
--------------------------
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
--------------------------
*Реализуйте алгоритм перемешивания списка.
"""


from random import randint


def task1(num=None):
    try:
        if not isinstance(num, (int, float)):
            raise TypeError(
                'Аргументом функции должно быть число!'
            )
        num_str = str(abs(num)).replace('.', '')
        num_sum = 0
        for digit in num_str:
            num_sum += int(digit)
    except Exception as error:
        print(error)
    else:
        print(f'{num} -> {num_sum}')


def task2(num=None):
    try:
        if (not isinstance(num, int)) or (num <= 0):
            raise TypeError(
                'Аргументом функции должно быть '
                'целое положительное!'
            )
        prod = 1
        result = []
        for i in range(1, num + 1):
            prod *= i
            result.append(prod)
    except Exception as error:
        print(error)
    else:
        print(result)


def task3(num=None):
    def num_format(num):
        return int(num) if not num % 1 else round(num, 2)

    try:
        if (not isinstance(num, int)) or (num <= 0):
            raise TypeError(
                'Аргументом функции должно быть '
                'целое положительное!'
            )
        result = {n: num_format((1 + 1 / n) ** n) for n in range(1, num + 1)}
    except Exception as error:
        print(error)
    else:
        print(result)


def task4(num=None):
    random_values = [randint(-num, num) for _ in range(num)]
    index_list = []
    try:
        f = open('file.txt', 'rt')
        for line in f:
            if line.strip().isdigit():
                index_list.append(int(line.strip()))
            else:
                mes = (
                    f'Значение "{line.strip()}" в файле - не целое число! '
                    'Исключено из обработки.'
                )
                print(mes)
        f.close()
        if index_list:
            for idx in index_list:
                result = 1
                result *= random_values[idx]
        else:
            result = None
        print('Список значений:', random_values)
        print('Позиции для перемножения:', tuple(index_list))
        print('Результат:', result)
    except ValueError as not_int_error:
        print(not_int_error)
    except Exception as error:
        print(error)


def task5(initial_list: list):
    list_len = len(initial_list)
    print('Начальный список:', initial_list)
    list_mixed = initial_list.copy()
    try:
        for i in range(list_len):
            random_index = randint(0, list_len - 1)
            tmp_val = list_mixed[i]
            list_mixed[i] = list_mixed[random_index]
            list_mixed[random_index] = tmp_val
    except Exception as error:
        print(error)
    else:
        print('Перемешанный список:', list_mixed)


if __name__ == '__main__':
    print()
    print('ЗАДАНИЕ 1:')
    task1(6872)
    task1(0.56)
    task1(-3.5)
    task1('0.56')

    print()
    print('ЗАДАНИЕ 2:')
    task2(4)
    task2(-3)

    print()
    print('ЗАДАНИЕ 3:')
    task3(6)

    print()
    print('ЗАДАНИЕ 4:')
    task4(6)

    print()
    print('ЗАДАНИЕ 5:')
    task5([1, 2, 3, 4, 5, 6, 7])
