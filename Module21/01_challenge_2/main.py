def super_fun(num, start=1, result=[]):
    if start < num:
        result.append(start)
        start += 1
        return super_fun(num, start, result)
    else:
        result.append(start)
        return result



print(super_fun(5))
