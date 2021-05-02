N = int(input('Сколько элементов в списке? '))
K = int(input('Сдвиг: '))
old_list = []
for _ in range(N):
    old_list.append(input('Введите элемент: '))
print('Изначальный список:', old_list)
new_list = '.' * N
new_list = list(new_list)

for element in old_list:
    if K >= N:
        K = 0
    new_list[K] = element
    K += 1
print('Новый список', new_list)