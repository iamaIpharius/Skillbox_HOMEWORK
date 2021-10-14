print(list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))), range(2, 1001))))

simple_list = []

for x in range(2, 1001):
    flag = True
    for y in range(2, x):
        if x % y == 0:
            flag = False
            break
    if flag:
        simple_list.append(x)

print(simple_list)
