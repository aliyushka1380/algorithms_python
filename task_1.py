"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО.
"""


"""
64-разрядная ОС
Python 3.7.6

Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы 
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
"""
# программа function_1 наиболее эффективна в использовании памяти.
from memory_profiler import profile

@profile
def function_1():
    print('Var 1')
    my_list = list(range(100000))

    for i in range(1, len(my_list), 2):
        my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1] # память не выделяется, только ссылки меняются местами

    print(my_list)

#  ------------------------------------------- вариант решения ---------------------------------------------------------

@profile
def function_2():
    print('Var 2')
    my_list = list(range(100000))
    my_list2 = []

    for i in range(1, len(my_list), 2):
        my_list2.append(my_list[i])       # Выделяет доп память
        my_list2.append(my_list[i - 1])   # Выделяет доп память

    print(my_list2)                       # Память освободилась от ссылки на my_list

"""
#  ------------------------------------------- вариант решения ---------------------------------------------------------

@profile
def function_3():
    print('Var 3')
    a = list(range(100000))
    i = 0
    #print(f'Оригинальный список {a}')
    while i + 1 < len(a):
        if i % 2 == 0:
            a.insert(i, a.pop(i + 1))
        i += 1
    print(f'Измененный список {a}')
"""

if __name__ == "__main__":
    function_1()
    function_2()
