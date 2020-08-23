"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
# Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter


class Node:

    def __init__(self, value, lft=None, rght=None):
        self.rght = rght
        self.lft = lft
        self.value = value


def my_code(base_node, codes=dict(), code=''):

    if base_node is None:
        return

    if isinstance(base_node.value, str):
        codes[base_node.value] = code
        return codes

    my_code(base_node.left, codes, code + '0')
    my_code(base_node.right, codes, code + '1')

    return codes


def my_tree(s):
    count = Counter(s)

    if len(count) <= 1:
        node = Node(None)

        if len(count) == 1:
            node.lft = Node([key for key in count][0])
            node.rght = Node(None)

        string_count = {node: 1}

    while len(count) != 1:
        node = Node(None)
        spam = count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])

        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])

        else:
            node.right = spam[1][0]

        del count[spam[0][0]]
        del count[spam[1][0]]
        count[node] = spam[0][1] + spam[1][1]

    return [key for key in count][0]


my_string = "beep boop beer!"

codes = my_code(my_tree(my_string))
print(f'Исходная строка: {my_string}\n')
print(f'Кодовая таблица: {codes}\n')
for i in my_string:
    print(codes[i], end=' ')
for i in my_string:
    print(f'{i}: {codes[i]}')



