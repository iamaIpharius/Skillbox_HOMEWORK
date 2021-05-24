import random

ran_list = [random.randint(1, 10) for _ in range(10)]
print(ran_list)
# первый вариант
new_list = []
for i in range(0, len(ran_list), 2):
    tup = ran_list[i], ran_list[i + 1]
    new_list.append(tup)
# второй вариант
first_list = [ran_list[i] for i in range(0, len(ran_list), 2)]
second_list = [ran_list[i + 1] for i in range(0, len(ran_list), 2)]
result_list = []
result = zip(first_list, second_list)
for i in result:
    result_list.append(i)

print(new_list)
print(result_list)

