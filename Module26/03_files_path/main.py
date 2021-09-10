import os
from collections.abc import Iterable


def find_path(to_find: str, start: str = os.path.join('C:')) -> None:
    for i in os.listdir(start):
        current = os.path.join(start, i)
        if i == to_find and os.path.isdir(current):
            for q in gen_files_path(current):
                print(q)
        elif os.path.isdir(current):
            find_path(to_find, current)


def gen_files_path(path: str) -> str:
    for i in os.listdir(path):
        cur_path = os.path.join(path, i)
        if os.path.isfile(cur_path):
            yield cur_path
        elif os.path.isdir(cur_path):
            for q in gen_files_path(cur_path):
                yield q


my_path = os.path.abspath(input('Введите директорию, где будем искать: '))
find = input('Какой каталог ищем? ')

find_path(find, my_path)
