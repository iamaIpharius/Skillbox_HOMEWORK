nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def unbend_list(my_list):
    result = []
    for i in my_list:
        if isinstance(i, list):
            result += unbend_list(i)
        else:
            result.append(i)
    return result


print(unbend_list(nice_list))