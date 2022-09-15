"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
--------------------------
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
--------------------------
Задайте список из вещественных чисел. Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
--------------------------
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
--------------------------
Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.
"""


def task1(my_list: list):
    print(my_list)
    new_list = []
    i = 1
    while i <= len(my_list) - 1:
        if isinstance(my_list[i], (int, float)):
            new_list.append(my_list[i])
            i += 2
    if new_list:
        print('Исходный список:', my_list)
        print('На нечётных позициях элементы:', new_list)
        print('Сумма:', sum(new_list))


def task2(my_list: list):
    i = 0
    n = -1
    list_len = len(my_list)
    new_list = []
    while abs(n) < (list_len - 1):
        if i == list_len + n:
            new_list.append(my_list[i] ** 2)
        else:
            new_list.append(my_list[i] * my_list[n])
        i += 1
        n -= 1
    print(my_list, '=>', new_list)


def task2_1(my_list: list):
    list_len = len(my_list)
    if list_len != 0:
        new_list = [
            my_list[i-1] * my_list[-i] for i in range(1, (list_len // 2) + 1)
        ]
        if list_len % 2 != 0:
            new_list.append(my_list[list_len // 2] ** 2)
        print(my_list, '=>', new_list)


def task3(my_list: list):
    def rnd(n, k):
        return n*(10**k)//1/10**k

    new_list = [el % 1 for el in my_list if isinstance(el, (int, float))]
    diff = max(new_list) - min(new_list)
    print(my_list, '=>', rnd(diff, 2))


def task4(num: int):
    def dec2bin(num: int):
        num_int = num // 2
        num_rem = num % 2
        if num_int in (0, 1):
            return str(num_int) + str(num_rem)
        else:
            return dec2bin(num_int) + str(num_rem)
    print(num, '->', dec2bin(num))


def task5(n=0):
    def fib(n=0):
        if n < 2:
            return n
        return fib(n-2) + fib(n-1)

    def nfib(n=-1):
        memo = {-1: 1, -2: -1}
        if n not in memo:
            return int((-1) ** (n+1) * fib(-n))
        return memo[n]

    fib_list = [fib(i) for i in range(n+1)]
    nfib_list = [nfib(i) for i in range(-n, 0)]
    nfib_list.reverse()
    print('Фиббоначи:     ', fib_list)
    print('негаФиббоначи: ', nfib_list)


if __name__ == '__main__':
    print()
    print('ЗАДАНИЕ 1:')
    task1([2, 3, 5, 9, 3])

    print()
    print('ЗАДАНИЕ 2:')
    task2([2, 3, 4, 5, 6])
    task2([2, 3, 5, 6])
    task2([])
    task2_1([2, 3, 4, 5, 6])
    task2_1([2, 3, 5, 6])
    task2_1([])

    print()
    print('ЗАДАНИЕ 3:')
    task3([1.1, 1.2, 3.1, 5, 10.01])

    print()
    print('ЗАДАНИЕ 4:')
    task4(45)
    task4(3)
    task4(2)
    task4(1)
    task4(0)

    print()
    print('ЗАДАНИЕ 5:')
    task5(8)
