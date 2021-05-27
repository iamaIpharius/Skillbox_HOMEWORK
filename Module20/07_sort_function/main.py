import random
def get_sorted_tuple(tup):
    res_list = []
    for num in start_tuple:
        if not str(num).isdigit():
            return tup
        else:
            res_list.append(num)
    result = tuple(sorted(res_list))
    return result




ran_list = [random.randint(1, 10) for _ in range(10)]
start_tuple = tuple(ran_list)





print(start_tuple)
print(get_sorted_tuple(start_tuple))
