N = int(input('Введите целое положительное число N: '))

n_sum = 0
n_counts = 0
N_str = str(N)


for i in range(len(N_str)):
    n_sum += N % 10
    n_counts += 1
    N //= 10

print('Сумма цифр равна', n_sum)
print('Кол-во цифр в числе:', n_counts)
print('Разность суммы и кол-ва цифр:', n_sum - n_counts)