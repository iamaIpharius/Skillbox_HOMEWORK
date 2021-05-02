word = input('Введите слово: ')
reverse_count = -1
status = True
for i in word:
    if i != word[reverse_count]:
        print('Это не палиндром')
        status = False
        break
    reverse_count -= 1
if status:
    print('Это палиндром')