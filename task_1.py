"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему

Дмитрий, я ничего хорошего придумать не смогла.
Функция func_2 работала бы быстрее, если нужно было четные элементы помещать, а не индексы.
Функция func_3 иногда работает быстрее за счет выноса пустого списка за пределы функции (меньше операций)
"""

import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit.timeit("func_1([10, 11, 12, 13, 14, 15, 16, 17, 18])", setup="from __main__ import func_1", number=1000))
print(func_1([10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))



def func_2(nums):
    b = [nums.index(x) for x in nums if not x%2]
    return b

print(timeit.timeit("func_2([10, 11, 12, 13, 14, 15, 16, 17, 18])", setup="from __main__ import func_2", number=1000))
print(func_2([10, 11, 12, 13, 14, 15, 16, 17, 18]))


def func_3(nums, new_arr1):

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr1.append(i)
    return new_arr1

new_arr1 = []
print(timeit.timeit("func_3([10, 11, 12, 13, 14, 15, 16, 17, 18],[])", setup="from __main__ import func_3", number=1000))
print(func_3([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], new_arr1))

