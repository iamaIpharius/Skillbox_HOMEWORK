import random
N = int(input('Введите число максимальное: '))

hidden_number = str(random.randint(1, N))

not_solved = True
no_help = True

num_set_yes = {str(i) for i in range(1, N + 1)}


while not_solved or no_help:
    numbers = input('Нужное число есть среди вот этих чисел: ')
    if numbers.lower() == 'help':
        print('Артём мог загадать следующие числа: ', num_set_yes)
        no_help = False
        break
    num_set_maybe = set(numbers)
    if hidden_number in num_set_maybe:
        if len(num_set_maybe) == 1:
            print('Угадал!')
            not_solved = False
            break
        else:
            print('Ответ Артёма: Да')
            num_set_yes &= num_set_maybe
    elif hidden_number not in num_set_maybe:
        print('Ответ Артёма: Нет')
        num_set_yes -= num_set_maybe