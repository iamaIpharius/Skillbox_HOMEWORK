import os

text = input('Введите текст: ')

disk = input('Выберите диск для сохранения: ')
path = os.path.join(disk+':', os.path.sep)
flag = True
while flag:
    folder = input('Введите папку или файл: ')
    new_path = os.path.join(path, folder)
    path = new_path
    if '.txt' in folder:
        flag = False

if os.path.exists(os.path.dirname(path)):
    if os.path.exists(path):
        open_file = open(path, 'a')
        open_file.write(text)
        open_file.close()
    else:
        new_file = open(path, 'w')
        new_file.write(text)
        new_file.close()
else:
    print('Указанного пути не существует')
