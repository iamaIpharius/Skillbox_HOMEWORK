start_string = input('Введите строку: ')
result = ''
i = 0
while i < len(start_string):
  result += start_string[i]
  lenght = start_string.count(start_string[i])
  result += str(lenght)
  i += lenght
print(result)
