with open('people.txt', 'r') as text_file:
    letter_count = 0
    for index, line in enumerate(text_file):
        try:
            if len(line) < 4:

                for letter in line:
                    if letter.isalpha():
                        letter_count += 1
                with open('errors.txt', 'a', encoding='utf-8') as log_file:
                    log_file.write(f'Длина менее 3 символов в {index} строке\n')
                raise IndexError
            for letter in line:
                if letter.isalpha():
                    letter_count += 1
        except IndexError:
            print(f'Длина менее 3 символов в {index} строке')

print(letter_count)
print(text_file.closed)
print(log_file.closed)