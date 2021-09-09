import os


def gen_files_path(path: str = os.path.join('C:')) -> str:
    for i in os.listdir(path):
        cur_path = os.path.join(path, i)
        if os.path.isfile(cur_path):
            yield cur_path
        elif os.path.isdir(cur_path):
            for q in gen_files_path(cur_path):
                yield q


my_path = os.path.join(input('Введите путь: '))

for q in gen_files_path(my_path):
    print(q)
