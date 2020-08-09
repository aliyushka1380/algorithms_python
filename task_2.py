"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

from functools import lru_cache
import timeit

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

print(timeit.timeit("recursive_reverse(500)", setup="from __main__ import recursive_reverse", number=100000))
print(recursive_reverse(500))


@lru_cache(maxsize=None)
def recursive_reverse2(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse2(number // 10)}'
print(timeit.timeit("recursive_reverse2(500)", setup="from __main__ import recursive_reverse2", number=100000))
print(recursive_reverse2(500))



