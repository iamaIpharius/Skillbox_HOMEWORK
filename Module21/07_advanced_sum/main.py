def super_sum(*args):
    result = 0
    for arg in args:
        if isinstance(arg, list):
            for num_arg, sub_arg in enumerate(arg):
                result += super_sum(sub_arg)
        else:
            result += arg
    return result

print(super_sum([[1, 2, [3]], [1], 3]))
