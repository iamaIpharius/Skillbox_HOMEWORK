def calculating_math_func(data, data_dict={}):
    if data in data_dict:
        return data_dict[data]
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    data_dict[data] = result
    return result