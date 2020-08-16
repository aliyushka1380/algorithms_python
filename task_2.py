"""
Задание 2.
Предложить варианты оптимизации и доказать (наглядно, кодом) их эффективность
"""

#Вариант 1. Сериализация с момощью модуля pickle - оптимизирует, но не сильно...

from memory_profiler import profile
import pickle
import random

def random_string():
    return "".join([chr(64 + random.randint(0, 25)) for _ in range(20)])

@profile
def create_file():
    x = [(random.random(),
          random_string(),
          random.randint(0,2 ** 64))
         for _ in range(10000)]

    pickle.dump(x, open('machin.pkl', 'wb'))

@profile
def load_file():
    y = pickle.load(open('machin.pkl', 'rb'))
    return y

if __name__=="__main__":
    create_file()
    load_file()

# Остальные нижеперечисленные варианты, описанные в интернете, не выявили сильной оптимизации:
"""Вариант 3. Сократите количество строк в коде. Пользуйтесь встроенными функциями Python
from memory_profiler import profile


old_list = [i for i in range(1,100000)]

@profile
def function_1():
    new_list = []
    for item in old_list:
        new_list.append(int(item))

    print(new_list)

@profile
def function_2():
    new_list = list(map(int, old_list))
    print (new_list)

if __name__ == "__main__":
    function_1()
    function_2()

#Вариант 4. Для сокращения строк пользуйтесь циклами и генераторами for
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. 
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

from memory_profiler import profile

@profile
def int_func1(word):
    words, result = [], []
    if len(word) > 0:
        for i in word.split():
            words.append(i[0].upper() + i[1:])
        result = ' '.join(words)
    return result



#  ------------------------------------------- вариант решения ---------------------------------------------------------
import uuid;
a = uuid.uuid4().hex.upper()[0:10000]

@profile
def int_func2(word):
    words, result = [], []
    if len(word) > 0:
        words = [i[0].upper() + i[1:] for i in word.split()]
        result = ' '.join(words)
    return result



if __name__ == "__main__":
    print(int_func1(a))
    print(int_func2(a))

"""