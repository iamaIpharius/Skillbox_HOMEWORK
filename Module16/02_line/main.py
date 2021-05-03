first_class = list(range(160, 177, 2))
second_class = list(range(162, 181, 3))

all_children = []
all_children.extend(first_class)
all_children.extend(second_class)
all_children.sort()

print(all_children)