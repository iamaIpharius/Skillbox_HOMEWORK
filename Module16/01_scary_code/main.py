main_list = [1, 5, 3]
ad_list_1 = [1, 5, 1, 5]
ad_list_2 = [1, 3, 1, 5, 3, 3]

main_list.extend(ad_list_1)
print('Кол-во цифр 5 при первом объединении:', main_list.count(5))

for item in main_list:
    if item == 5:
        main_list.remove(item)
main_list.extend(ad_list_2)
print('Кол-во цифр 3 при втором объединении:', main_list.count(3))
print('Итоговый список:', main_list)