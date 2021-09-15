list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break

def find_gen(first_l: list, second_l: list, find: int) -> tuple:
    for i in first_l:
        for q in second_l:
            if i * q == find:
                print(f'Числа {i} и {q} в результате попарного перемножения дают {find}')
                return
            yield i, q


for i in find_gen(list_1, list_2, to_find):
    print(i)
