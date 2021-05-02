n = int(input('Сколько элементов в списке? '))
start_list = []
for _ in range(n):
    start_list.append(int(input('Введите элемент')))

current_element = start_list[0]
for i in range(len(start_list)):
    for q in range(len(start_list)):
        if start_list[i] < start_list[q]:
            temp = start_list[q]
            start_list[q] = start_list[i]
            start_list[i] = temp
print(start_list)