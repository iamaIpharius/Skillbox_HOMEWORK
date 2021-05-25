string = 'abcd'
tup_nums = (10, 20, 30, 40)

gen = ((string[i], tup_nums[i]) for i in range(len(string)))
print(gen)
for i in gen:
    print(i)
