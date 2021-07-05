

result = 0
with open('calc.txt', 'r', encoding='utf-8') as calc_file:
    for line in calc_file:
        try:
            line_list = line.split()
            a = int(line_list[0])
            b = int(line_list[2])
            oper = line_list[1]
            if oper == '+':
                temp = a + b
                result += temp
                print(temp)
            elif oper == '-':
                temp = a - b
                result += temp
                print(temp)
            elif oper == '*':
                temp = a * b
                result += temp
                print(temp)
            elif oper == '/':
                temp = a / b
                result += temp
                print(temp)
            elif oper == '%':
                temp = a % b
                result += temp
                print(temp)
            elif oper == '//':
                temp = a // b
                result += temp
                print(temp)
            else:
                raise SyntaxError
        except SyntaxError:
            print('ошибка в операторе')
        except ValueError:
            print('ошибка в операнде')
print('Результат:', result)