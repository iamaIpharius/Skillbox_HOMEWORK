from typing import List

first_list = []
second_list = []

for _ in range(3):
    first_list.append(int(input('Введите число в 1 список: ')))

for _ in range(7):
    second_list.append(int(input('Введите число во 2 список: ')))

first_list.extend(second_list)
unique_numbers_list = list(set(first_list))

print('Новый первый список с уникальными элементами:', unique_numbers_list)