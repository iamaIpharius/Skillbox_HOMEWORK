zen = open('zen.txt', 'r')

zen_list = [i for i in zen]
strings = 0
words = 0
letters = 0
let_dict = dict()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for string in zen_list:
    strings += 1
    new_string = string.split()
    for word in new_string:
        words += 1
        for letter in word:
            if letter.lower() in alphabet:
                letters += 1
                if letter in let_dict:
                    let_dict[letter] += 1
                else:
                    let_dict[letter] = 1
min_count = max(let_dict.values())
min_letter = ''

for letter, val in let_dict.items():
    if val < min_count:
        min_letter = letter
        min_count = val

print('строк:', strings)
print('слов:', words)
print('букв:', letters)
print('Буква', min_letter, 'встречается', min_count, 'раз')

zen.close()