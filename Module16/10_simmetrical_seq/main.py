n = int(input('Сколько цифр? '))
start_list = []
for i in range(n):
    print('Введите', i + 1, 'число:', end=' ')
    start_list.append(int(input()))
print('Последовательность', start_list)
new_list = start_list[::-1]

for _ in range(n):
    if new_list[0] == start_list[-1]:
        start_list = start_list[:-1]
    else:
        break
start_list.reverse()
print('Нужно приписать чисел:', len(start_list))
print('Сами числа:', start_list)