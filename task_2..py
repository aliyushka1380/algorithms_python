"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import defaultdict


class Cmplx:
    def __init__(self, num_dict):
        self.first_number = num_dict[0]
        self.second_number = num_dict[1]

    def __add__(self, other):
        return list(hex(int(''.join(self.first_number), 16) + int(''.join(self.second_number), 16)).upper())[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_number), 16) * int(''.join(self.second_number), 16)).upper())[2:]


hex_dict = defaultdict(list)
hex_dict[0].append(input("Введите 1-е шестнадцатиричное число: "))
hex_dict[1].append(input("Введите 2-е шестнадцатиричное число: "))

sums = Cmplx(hex_dict).__add__(other=0)
muls = Cmplx(hex_dict).__mul__(other=0)

print(sums, muls)