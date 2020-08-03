"""
Задание 4.
Реализуйте скрипт "Кеширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП

"""

from uuid import uuid4
import hashlib

salt = uuid4().hex
cache = {}
def get_page(url):
    if cache.get(url):
        print(f'Страница {url} в кэше есть')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache[url] = res
        print(cache)

A = str('www.556.ru')
get_page(A)

B = str('www.556.ru')
get_page(B)

C = str('www.555.ru')
get_page(C)