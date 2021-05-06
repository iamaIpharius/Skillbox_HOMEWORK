def get_cypher_letter(letter, shift, alphabet):
    if letter in alphabet:
        return alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
    else:
        return letter

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
            'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
            'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

message = input('введите сообщение: ')
k = int(input('введите сдвиг: '))

result = [get_cypher_letter(letter_m, k, alphabet) for letter_m in message]
result_str = ''.join(result)


# result = ''
# current_letter = ''
# for letter_m in message:
#     for letter_a in alphabet:
#         if letter_a == letter_m:
#             index_k = (alphabet.index(letter_a) + k) % len(alphabet)
#             current_letter = alphabet[index_k]
#             break
#         else:
#             current_letter = letter_m
#     result += current_letter
print(result_str)