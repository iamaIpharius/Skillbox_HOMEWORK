import os


def gen_files_path(path=os.path.join('C:')):
    for i in os.listdir(path):
        cur_path = os.path.join(path, i)
        if os.path.isfile(cur_path):
            yield cur_path
        elif os.path.isdir(cur_path):
            for q in gen_files_path(cur_path):
                print(q)


os.path.join(os.path.abspath('.').split(os.path.sep)[0])

for q in gen_files_path():
    print(q)
