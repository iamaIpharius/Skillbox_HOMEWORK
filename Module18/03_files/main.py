file_name = input('Введите название файла: ')
if file_name[0] in '@№$%^&*().':
  print('Ошибка: название начинается на один из специальных символов')
elif file_name.endswith('.txt') or file_name.endswith('.docx'):
  print('Файл назван верно.')
else:
  print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')