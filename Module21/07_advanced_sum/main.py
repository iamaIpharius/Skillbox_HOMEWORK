def super_sum(*args):
    result = 0
    for i in args:
        if isinstance(i, list):
            for j in range(len(i)):
                result += super_sum(i[j])
        else:
            result += i
    return result

print(super_sum([[1, 2, [3]], [1], 3]))