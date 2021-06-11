import os

def sort_dict(dic):
    max_score = 0
    for name, score in dic.items():
        if score > max_score:
            max_score = score
    return max_score

first_t_file = open('first_tour.txt', 'r')
k = 0
second_t_dict = dict()
k_2 = 0

for index, val in enumerate(first_t_file):
    if index == 0:
        k = int(val)
    elif val != '\n':
        val_list = val.split()
        if int(val_list[2]) > k:
            k_2 += 1
            second_t_dict[(val_list[0], val_list[1])] = int(val_list[2])




print(second_t_dict)