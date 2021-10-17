import itertools

code_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for count, i in enumerate(itertools.product(code_numbers, repeat=4), 1):

    print(i, count, 'вариант')
