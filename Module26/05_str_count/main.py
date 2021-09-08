import os
from collections.abc import Iterable

def get_line(path: str = os.path.join('C:')) -> Iterable[int]:
    for i in os.listdir(path):
        cur_path = os.path.join(path, i)
        if os.path.isfile(cur_path) and cur_path.endswith('.py'):
            print(cur_path)
            with open(cur_path, 'r', encoding='utf-8') as py_file:
                for line in py_file:
                    if line.isspace() or '#' in line:
                        continue
                    else:
                        yield 1


        elif os.path.isdir(cur_path):
            for q in get_line(cur_path):
                yield q


my_path = os.path.join(input('Введие путь: '))
total_lines = 0
for q in get_line(my_path):
    total_lines += q

print(f'В найденных питоновских файлах {total_lines} строк кода без пустых и комментариев')
