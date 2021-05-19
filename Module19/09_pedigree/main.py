total_family = int(input('Сколько членов семьи? '))
family_dict = dict()
high_dict = dict()
high = -1

for i in range(1, total_family):
    pair_enter = input('Введите {0} пару: '.format(i)).split()
    family_dict[pair_enter[0]] = pair_enter[1]
prev = ''
for item in family_dict:
    parent = family_dict[item]
    kid = item
    if parent == prev:
        high_dict[kid] = high + 1

    else:
        high += 1
        high_dict[parent] = high
        high_dict[kid] = high + 1
        prev = parent

print(high_dict)