import random


result = 0
flag = True
while flag:
    try:
        num = int(input('Введите число: '))
        rnd = random.randint(1, 13)
        if rnd == 1:
            raise BaseException('Критическая ошибка!')
        with open('result.txt', 'a') as file:
            file.write(str(num))
            file.write('\n')
        result += num
        if result >= 777:
            print('Вы выиграли!')
            break
    except ValueError:
        print('Это не число')
    except BaseException:
        raise BaseException('Критическая ошибка!')

