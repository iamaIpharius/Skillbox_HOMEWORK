import os

text_file = open('text.txt', 'r')
cipher_count = 0
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
cipher_file = open('cipher_text.txt', 'a')
for string in text_file:
    cipher_count += 1
    new_string = ''
    for letter_s in string:
        for index, letter_a in enumerate(alphabet):
            if letter_s == letter_a:
                new_string += alphabet[index + cipher_count]
                break
    new_string = new_string + '\n'
    cipher_file.write(new_string)
text_file.close()
cipher_file.close()

