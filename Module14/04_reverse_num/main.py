def reverse_count(count):
    count = str(count)
    first_part = ''
    second_part = ''
    temp = ''
    result = ''
    for i in count:
        if i == '.':
            first_part = temp
            temp = ''
            continue
        temp += i
    second_part = temp
    first_part_rev = first_part[::-1]

    second_part_rev = second_part[::-1]
    result = first_part_rev + '.' + second_part_rev
    return float(result)


n = float(input('Введите первое число: '))
k = float(input('Введите второе число: '))
n_rev = reverse_count(n)
k_rev = reverse_count(k)
print('Первое число наоборот:', n_rev)
print('Второе число наоборот:', k_rev)
print('Сумма', n_rev + k_rev)



