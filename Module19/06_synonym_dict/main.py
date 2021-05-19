number_of_pairs = int(input('Сколько будет пар? '))
synon_dict = dict()
print('Введите пары слов через пробел: ')
for num in range(number_of_pairs):
    pair = input('{0} пара: '.format(num + 1)).lower().split()
    if pair[0] in synon_dict.keys() or pair[0] in synon_dict.values():
        print('Слово уже есть')
    elif pair[1] in synon_dict.keys() or pair[0] in synon_dict.values():
        print('Слово уже есть')
    else:
        synon_dict[pair[0]] = pair[1]
        synon_dict[pair[1]] = pair[0]

word = input('Введите слово: ').lower()
while True:
    if word in synon_dict:
        print('Синоним:', synon_dict[word])
        break
    else:
        print('Такого слова в словаре нет.')
        word = input('Введите слово: ').lower()
