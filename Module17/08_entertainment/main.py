import random

N = int(input('Введите количество палок: '))
K = int(input('Введите количество бросков: '))

wood_list = ['I']*N
print('I' * N)
for throw in range(K):
    print(throw + 1, 'бросок: ')
    L = random.randint(0, N)
    R = random.randint(L, N)
    print('Сбиты палки с номера', L, 'по номер', R)
    for i in range(L, R+1):
        wood_list[i-1] = '.'
result = ''.join(wood_list)
print(result)
