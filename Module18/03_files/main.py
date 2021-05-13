file_name = input('Введите название файла: ')
suffix = ('.txt', '.docx')
if file_name[0] in '@№$%^&*().':
  print('Ошибка: название начинается на один из специальных символов')
elif file_name.endswith(suffix):
  print('Файл назван верно.')
else:
  print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')