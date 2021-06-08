def min_lenght(first_obj, second_obj):
    return min(len(first_obj), len(second_obj))

def my_zip(first_obj, second_obj):
    one = enumerate(first_obj)
    two = enumerate(second_obj)
    gen = ((next(one)[1], next(two)[1]) for _ in range(min_lenght(first_obj, second_obj)))
    result_list = list(gen)
    return result_list



string = {1:2, 3:4, 5:6}
tup_nums = (10, 20, 30, 40)


print(my_zip(string, tup_nums))