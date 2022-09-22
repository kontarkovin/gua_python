"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные
об их хобби. Известно, что при хранении данных используется принцип:
одна строка — один пользователь.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби.
*Сохранить словарь в файл users_hobby.txt.
Фрагмент файла с данными о пользователях (users.txt):
Иванов Иван Иванович Петров Петр Петрович Фрагмент файла с данными о хобби
(hobby.txt): скалолазание, охота горные лыжи
---------------------------------------------
Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N.
---------------------------------------------
Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.
---------------------------------------------
*Задана натуральная степень k. Сформировать случайным образом список
коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
степени k. Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
---------------------------------------------
**Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0
"""


from random import randint


def task1():
    try:
        f1 = open('users.txt', 'rt')
        f2 = open('hobby.txt', 'rt')
        fio_list = [fio.strip() for fio in f1]
        hobby_list = [hobby.strip() for hobby in f2]
        f1.close()
        f2.close()
        fio_dict = dict(zip(fio_list, hobby_list))
        print(fio_dict)
    except Exception as error:
        print('Ошибка:', error)


def task2(num=None):
    def is_prime_num(num):
        isprime = True
        if num == 2 or num == 3:
            return isprime
        if (num % 2 == 0) or (num < 2):
            return not isprime
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return not isprime
        return isprime

    if (not isinstance(num, int)) or (num < 1):
        print('Задайте натуральное число!')
    else:
        prime_list = [i for i in range(1, num + 1) if is_prime_num(i)]
        i = 1
        cur_num = num
        prime_mults = []
        while i <= len(prime_list):
            div = prime_list[i-1]
            while cur_num % div == 0:
                prime_mults.append(div)
                cur_num = cur_num // div
            else:
                i += 1
        print(f'Список простых множителей чиcла {num}:', prime_mults)


def task3(num_list: list):
    if not isinstance(num_list, list):
        print('Задайте последовательность чисел!')
    else:
        print('Исходная последовательност чисел:', num_list)
        result = sorted(list(set(num_list)))
        print('Неповторяющаяся последовательность чисел:', result)


if __name__ == '__main__':
    print()
    print('ЗАДАНИЕ 1:')
    task1()

    print()
    print('ЗАДАНИЕ 2:')
    task2(randint(1, 2000))

    print()
    print('ЗАДАНИЕ 3:')
    my_list = [1, 1, 5, 7, 1, 5, 7, 9, 6]
    task3(my_list)
