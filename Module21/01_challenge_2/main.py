def super_fun(num, start=1):
    print(start)
    if start == num:
        return
    start += 1
    super_fun(num, start)


super_fun(5)
