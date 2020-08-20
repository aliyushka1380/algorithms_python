"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию

Дмитрий, я реализовала, но судя по замерам, получилось дольше... В чем моя ошибка?
"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        #print(lst_obj)
        n += 1
    return lst_obj

def bubble_sort2(lst_obj):
    n = 1
    flag = True
    while flag:
        flag = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
        #print(lst_obj)

        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
#orig_list = [68, -62, -66, -39, -47, -25, 84, 32, 35, -90]
print(orig_list)
print(bubble_sort(orig_list))
print()
print(bubble_sort2(orig_list))


print("замеры 10")
orig_list = [random.randint(-100, 100) for _ in range(10)]

print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1))
print(timeit.timeit("bubble_sort2(orig_list)", \
    setup="from __main__ import bubble_sort2, orig_list", number=1))

print("замеры 100")
orig_list = [random.randint(-100, 100) for _ in range(100)]

print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1))
print(timeit.timeit("bubble_sort2(orig_list)", \
    setup="from __main__ import bubble_sort2, orig_list", number=1))

print("замеры 1000")
orig_list = [random.randint(-100, 100) for _ in range(1000)]

print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1))
print(timeit.timeit("bubble_sort2(orig_list)", \
    setup="from __main__ import bubble_sort2, orig_list", number=1))