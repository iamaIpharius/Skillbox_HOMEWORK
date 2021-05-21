players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

answer = []
for id_of_item, item in players.items():
    temp_list = []
    for element in id_of_item:
        temp_list.append(element)
    for element in item:
        temp_list.append(element)
    answer.append(tuple(temp_list))
print(answer)
