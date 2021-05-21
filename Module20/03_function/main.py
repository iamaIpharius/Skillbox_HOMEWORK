def get_part_of_tuple(tup, element):
    count_list = []
    for index, tup_element in enumerate(tup):
        if tup_element == element:
            count_list.append(index)
    if len(count_list) == 2:
        new_tup = tup[count_list[0]:count_list[1] + 1]
        return new_tup
    elif len(count_list) == 1:
        new_tup = tup[count_list[0]:]
        return new_tup
    else:
        new_tup = tuple()
        return new_tup


my_tuple = 1, 3, 5, 7, 9, 2, 4, 6, 8, 0, 'asda', 'a', 2, 3, 9999, 123412

print(get_part_of_tuple(my_tuple, 3))

