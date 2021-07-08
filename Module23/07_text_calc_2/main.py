def calculating(line):
    line_list = line.split()
    a = int(line_list[0])
    b = int(line_list[2])
    oper = line_list[1]
    if oper == '+':
        temp = a + b
        return temp
    elif oper == '-':
        temp = a - b
        return temp
    elif oper == '*':
        temp = a * b
        return temp
    elif oper == '/':
        temp = a / b
        return temp
    elif oper == '%':
        temp = a % b
        return temp
    elif oper == '//':
        temp = a // b
        return temp
    else:
        raise SyntaxError

result = 0
with open('calc.txt', 'r', encoding='utf-8') as calc_file:
    for line in calc_file:
        try:
            calc_result = calculating(line)
            print(calc_result)
            result += calc_result
        except SyntaxError:
            print('ошибка в операторе:', line)
            fix = input('Исправим ошибку? 1 - да, 0 - нет: ')
            if fix == '1':
                new_line = input('Введите строку заново: ')
                new_calc_result = calculating(new_line)
                print(new_calc_result)
                result += new_calc_result
        except ValueError:
            print('ошибка в операнде:', line)

            fix = input('Исправим ошибку? 1 - да, 0 - нет: ')
            if fix == '1':
                new_line = input('Введите строку заново')
                new_calc_result = calculating(new_line)
                print(new_calc_result)
                result += new_calc_result
print('Результат:', result)