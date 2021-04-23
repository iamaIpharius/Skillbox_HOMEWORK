def divider(count):
    result = 0

    for i in range(2, count + 1):
        if count % i == 0:
            result = i
            break
    return result


n = int(input('Введите число: '))

print('Наименьший делитель, отличный от единицы:', divider(n))