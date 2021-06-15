def sort_dict(tup):
    return tup[2]


first_t_file = open('first_tour.txt', 'r')
k = 0
second_t_list = []
k_2 = 0

for index, val in enumerate(first_t_file):
    if index == 0:
        k = int(val)
    elif val != '\n':
        val_list = val.split()
        if int(val_list[2]) > k:
            k_2 += 1
            second_t_list.append((val_list[0], val_list[1], int(val_list[2])))

print(second_t_list)
sorted_dic = sorted(second_t_list, key=sort_dict, reverse=True)
print(sorted_dic)
second_t_file = open('second_tour.txt', 'w')
second_t_file.write(str(k_2) + '\n')
for index, player in enumerate(sorted_dic, 1):
    second_t_file.write(str(index) + ') ')
    second_t_file.write(player[1][0] + '. ')
    second_t_file.write(player[0] + ' ' + str(player[2]) + '\n')

first_t_file.close()
second_t_file.close()
