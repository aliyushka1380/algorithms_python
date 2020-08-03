"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time

def check_list(n):

    start_val = time.time()

    numbers1 = []
    for i in range(n):
        numbers1.append(i)
        numbers1.index(i)

    end_val = time.time()

    return numbers1, end_val - start_val


def check_dict(n):
    start_val = time.time()

    goods = dict()
    for i in range(n):
        goods[i] = i
        goods.get(i)

    end_val = time.time()

    return goods, end_val - start_val

"""
for i in range(3):
    print(f'Операция заняла {check_list(10000)[1]} сек')
for i in range(3):
    print(f'Операция заняла {check_dict(10000)[1]} сек')
"""

print(f'Словари обрабатываются быстрее: {check_dict(10000)[1]} сек против {check_list(10000)[1]} сек' if check_dict(10000)[1] < check_list(10000)[1] else f'Списки обрабатываются быстрее: {check_list(10000)[1]} сек против {check_dict(10000)[1]} сек')
