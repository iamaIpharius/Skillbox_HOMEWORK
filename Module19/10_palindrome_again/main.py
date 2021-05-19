string = list(input('Введите строку: '))
pal_dict = dict()
for letter in string:
    if letter in pal_dict:
        pal_dict[letter] += 1
    else:
        pal_dict[letter] = 1

not_even = 0

for item in pal_dict:
    if pal_dict[item] % 2 != 0:
        not_even += 1
if not_even > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')

