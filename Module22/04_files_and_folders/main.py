import os

result_list = [0, 0, 0]


def find_weight(path):
    for i_elem in os.listdir(path):
        cur_path = os.path.join(path, i_elem)
        if os.path.isdir(cur_path):
            result_list[1] += 1
            find_weight(cur_path)

        if os.path.isfile(cur_path):
            result_list[0] += 1
            result_list[2] += os.path.getsize(cur_path)


my_path = os.path.join(input('Введите путь до католога: '))

find_weight(my_path)

print('Размер каталога (в Кб):', round(result_list[2] / 1024))
print('Количество подкаталогов:', result_list[1])
print('Количество файлов:', result_list[0])
