"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
 - revers_3 эффективнее, O(1) - константа
"""

import cProfile, timeit

def revers(enter_num, revers_num=0):#O(2^n) - экспоненциальная
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):# O(len(...)) - линейная
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num): # O(1) - константа
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def main():
    enter_num = 12345678987654321
    revers(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)

cProfile.run('main()')
print(timeit.timeit("revers(12345678987654321)", setup="from __main__ import revers", number=100000))
print(timeit.timeit("revers_2(12345678987654321)", setup="from __main__ import revers_2", number=100000))
print(timeit.timeit("revers_3(12345678987654321)", setup="from __main__ import revers_3", number=100000))