word = input('Введите слово: ')
uniq_letters = []

for i in word:
    letter_count = 0
    for q in word:
        if q == i:
            letter_count += 1
    if letter_count == 1:
        uniq_letters.append(i)
print('Уникальных букв:', len(uniq_letters))