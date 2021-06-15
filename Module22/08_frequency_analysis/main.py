alphabet = 'abcdefghijklmnopqrstuvwxyz'


def sort_list(elem):
    i = abs(alphabet.index(elem[0]) - 33)
    return elem[1] + i


def sum_of_letters(dic):
    result = 0
    for key, val in dic.items():
        result += val
    return result


text = open('text.txt', 'r')

text_dict = dict()

for string in text:
    string = string.lower()
    for letter in string:
        if letter in alphabet:
            if letter in text_dict:
                text_dict[letter] += 1
            else:
                text_dict[letter] = 1

print(text_dict)

text_lenght = sum_of_letters(text_dict)
print(text_lenght)
text_list = [(key, val) for key, val in text_dict.items()]
analysis = open('analysis.txt', 'w')
sorted_text_list = sorted(text_list, key=sort_list, reverse=True)
print(sorted_text_list)

for elem in sorted_text_list:
    analysis.write(elem[0] + ' ' + str(round(elem[1] / text_lenght, 3)) + '\n')


text.close()
analysis.close()
