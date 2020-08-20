"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random


def merger_sort(lst_left, lst_right):
    res = []
    i = 0
    j = 0
    while i < len(lst_left) and j < len(lst_right):
        if lst_left[i] <= lst_right[j]:
            res.append(lst_left[i])
            i += 1
        else:
            res.append(lst_right[j])
            j += 1
    res += lst_left[i:] + lst_right[j:]
    return res


def merge_sort(lst_paste):
    if len(lst_paste) <= 1:
        return lst_paste
    else:
        lst_lft = lst_paste[:len(lst_paste) // 2]
        lst_rgh = lst_paste[len(lst_paste) // 2:]
    return merger_sort(merge_sort(lst_lft), merge_sort(lst_rgh))


list_el = [random.uniform(0, 50) for i in range(1, 10)]

print(f'Исходный массив: {list_el}')
print(f'Отсортированный массив: {merge_sort(list_el)}')