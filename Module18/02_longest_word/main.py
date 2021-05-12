start_string = input('Введите строку с пробелами: ')
list_of_words = start_string.split()
largest_word = ''
for word in list_of_words:
  if len(word) > len(largest_word):
    largest_word = word
print(largest_word)
