import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('coordinates.txt', 'r') as file:
    try:
        with open('result.txt', 'w') as file_2:
            for index, line in enumerate(file):
                nums_list = line.split()
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                number = random.randint(0, 100)
                my_list = sorted([str(res1), str(res2), str(number)])
                file_2.write(' '.join(my_list))
                file_2.write('\n')
    except ValueError:
        print(f'Ошибка значения в строке {index}')
    except TypeError:
        print(f'Ошибка при записи в строке {index}')
    except ZeroDivisionError:
        print(f'Делить на ноль нельзя в строке {index}')
    else:
        print('Без ошибок!')