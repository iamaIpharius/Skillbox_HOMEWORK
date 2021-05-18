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
print(synon_dict)
word = input('Введите слово: ').lower()
flag = True
while flag:
    if word in synon_dict:
        print('Синоним:', synon_dict[word])
        flag = False
    elif word in synon_dict.values():
        for word_dict in synon_dict:
            if synon_dict[word_dict] == word:
                print('Синоним:', word_dict)
                flag = False
    else:
        print('Такого слова в словаре нет.')
        word = input('Введите слово: ')
