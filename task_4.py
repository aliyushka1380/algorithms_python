"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

print(timeit.timeit("func_1()", setup="from __main__ import func_1", number=100000))
print(func_1())
print(timeit.timeit("func_2()", setup="from __main__ import func_2", number=100000))
print(func_2())

def func_5():
    a_set = set(array)

    most_common = None
    qty_most_common = 0

    for item in a_set:
        qty = array.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item

    return(f'Чаще всего встречается число {most_common}, ' \
            f'оно появилось в массиве {qty_most_common} раз(а)')
print(timeit.timeit("func_5()", setup="from __main__ import func_5", number=100000))
print(func_5())

""" 
Неудачные варианты:

def func_3():
    a = sorted([(i,array.count(i)) for i in set(array)],key=lambda t:t[1])[-1]
    return (f'Чаще всего встречается число {a[0]}, ' \
               f'оно появилось в массиве {a[1]} раз(а)')

print(timeit.timeit("func_3()", setup="from __main__ import func_3", number=100000))
print(func_3())

def func_4():
    num = array[0]
    max_frq = 1
    for i in range(len(array) - 1):
        frq = 1
        for k in range(i + 1, len(array)):
            if array[i] == array[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = array[i]
    return (f'Чаще всего встречается число {num}, ' \
            f'оно появилось в массиве {max_frq} раз(а)')

print(timeit.timeit("func_4()", setup="from __main__ import func_4", number=100000))
print(func_4())
"""