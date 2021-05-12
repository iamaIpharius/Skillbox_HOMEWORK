message = input('Введите сообщение: ')

temp = ''
result = ''
for word in message:
  if not word.isalpha():
    temp = temp[::-1]
    result += temp
    result += word
    temp = ''
  else:
    temp += word
print(result)
