def get_invert_dict(dictionary):
    uniq_freq = set(dictionary.values())
    uniq_let = set(dictionary.keys())
    new_dict = dict()
    for freq in uniq_freq:
        new_dict[freq] = []
        for item in uniq_let:
            if freq == dictionary[item]:
                new_dict[freq].append(item)
    return new_dict


text = input('Введите текст: ').lower()
text_dict = dict()
for letter in text:
    if letter in text_dict:
        text_dict[letter] += 1
    else:
        text_dict[letter] = 1
print('Оригинальный словарь частот: ')
for key in sorted(text_dict.keys()):
    print(key, ":", text_dict[key])

print('Инвертированный словарь частот: ')
invert_dict = get_invert_dict(text_dict)
for key in sorted(invert_dict.keys()):
    print(key, ":", invert_dict[key])
