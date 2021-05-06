n = int(input('Введите количество чисел: '))

list_of_nums = [int(input('Введите число: ')) for _ in range(n)]
for num in list_of_nums:
    if num == 0:
        list_of_nums.remove(0)
        list_of_nums.append(0)
list_of_nums = list_of_nums[:list_of_nums.index(0)]
print(list_of_nums)