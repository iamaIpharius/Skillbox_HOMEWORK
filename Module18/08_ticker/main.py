first_str = input('Введите первую строку: ')
second_str = input('Введите вторую строку: ')
shift = 0
for i in range(len(first_str)):
  if first_str == second_str:
    print('Первая строка получается из второй со сдвигом', shift)
    break
  else:
    temp = first_str[:1]
    first_str = first_str[1:len(first_str)-1]
    first_str.join(temp)
    shift += 1
if first_str != second_str:
  print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
