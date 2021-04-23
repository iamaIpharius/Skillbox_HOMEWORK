def summary(n):
    sum = 0
    for i in range(len(str(n))):
        sum += n % 10
        n //= 10
    return sum


def quantity(n):
    counts = 0
    for i in range(len(str(n))):
        counts += 1
    return counts


N = int(input('Введите целое положительное число N: '))
n_sum = summary(N)
n_counts = quantity(N)

print('Сумма цифр равна', n_sum)
print('Кол-во цифр в числе:', n_counts)
print('Разность суммы и кол-ва цифр:', n_sum - n_counts)
