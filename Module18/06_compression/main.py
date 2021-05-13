start_string = input('Введите строку: ')
result = ''
count = 0
prev = start_string[0]
for letter in start_string:
  if letter == prev:
    count += 1
    prev = letter
  else:
    result += prev
    result += str(count)
    count = 1
print(result)