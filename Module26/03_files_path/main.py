import os
from collections.abc import Iterable


def find_path(to_find: str, start: str = os.path.join('C:'), flag=False) -> Iterable:
    for i in os.listdir(start):
        current_path = os.path.join(start, i)
        if os.path.isfile(current_path):
            yield current_path
        elif i == to_find and os.path.isdir(current_path):
            print('Директоряи найдена!')
            raise StopIteration
        elif os.path.isdir(current_path):
            yield from find_path(to_find, current_path, flag)




my_path = os.path.abspath(input('Введите директорию, где будем искать: '))
find = input('Какой каталог ищем? ')

for i in find_path(find, my_path):

    print(i)

