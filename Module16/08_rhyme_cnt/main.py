n = int(input('Введите количество человек: '))
k = int(input('Введите число в считалке: '))

current_human_index = 0
human_list = list(range(1, n + 1))



while len(human_list) > 1:
    print('Текущий круг людей:', human_list)
    print('Начало счета с номера', human_list[current_human_index])

    for i in range(k):
        print('Участник', human_list[current_human_index])
        if i == k - 1:
            break
        current_human_index += 1
        if current_human_index > len(human_list) - 1:
            current_human_index = 0




    print('Выбывает номер', human_list[current_human_index])
    human_list.remove(human_list[current_human_index])
    if current_human_index > len(human_list) - 1:
        current_human_index = 0
print('Остался участник', human_list[current_human_index])