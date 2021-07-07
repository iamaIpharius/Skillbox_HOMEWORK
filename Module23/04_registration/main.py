def checking(line):
    line_list = line.split()
    if len(line_list) != 3:
        raise ValueError
    name = line_list[0]
    email = line_list[1]
    age = line_list[2]

    if not name.isalpha():
        raise NameError
    elif not '@' in email or not '.' in email:
        raise SyntaxError
    elif not age.isdigit():
        raise ValueError
    elif not 10 < int(age) < 99:
        raise ValueError
    
    
    
    
    
with open('registrations.txt', 'r', encoding='utf-8') as file:
    bad_file = open('registrations_bad.txt', 'a', encoding='utf-8')
    good_file = open('registrations_good.txt', 'a', encoding='utf-8')
    for index, line in enumerate(file, 1):
        try:
            checking(line)
        except ValueError:
            print('НЕ присутствуют все три поля или Поле «Возраст» НЕ является числом от 10 до 99')
            bad_file.write(f'{line} ошибка ValueError\n\n\n')
        except NameError:
            print('Поле имени содержит НЕ только буквы')
            bad_file.write(f'{line} ошибка ValueError\n\n\n')
        except SyntaxError:
            print('Поле «Имейл» НЕ содержит @ и .(точку)')
            bad_file.write(f'{line} ошибка ValueError\n\n\n')
        else:
            print('Без ошибок')
            good_file.write(line)
    bad_file.close()
    good_file.close()