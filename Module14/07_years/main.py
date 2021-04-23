first_year = int(input('Введите первый год: '))
last_year = int(input('Введите второй год: '))

print('Года от', first_year, 'до', last_year, 'с тремя одинаковыми цифрами:')
for i in range(first_year, last_year + 1):
    current_year = str(i)
    if current_year[0] == current_year[1] == current_year[2] or current_year[0] == current_year[2] == current_year[3] \
            or current_year[1] == current_year[2] == current_year[3] \
            or current_year[0] == current_year[1] == current_year[3]:
        print(i)
