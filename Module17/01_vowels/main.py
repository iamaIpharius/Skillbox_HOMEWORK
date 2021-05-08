text = input('Введите текст: ')
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

vowels_list = [vowel for vowel in text if vowel in vowels]
print('Список гласных букв: ', vowels_list)
print('Длина списка:', len(vowels_list))